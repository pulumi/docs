
---
title: "Volume"
block_external_search_index: true
---



Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

> This content is derived from https://github.com/terraform-providers/terraform-provider-digitalocean/blob/master/website/docs/r/volume.html.markdown.



## Create a Volume Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/digitalocean/#Volume">Volume</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/digitalocean/#VolumeArgs">VolumeArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Volume</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>filesystem_type=None<span class="p">, </span>initial_filesystem_label=None<span class="p">, </span>initial_filesystem_type=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>size=None<span class="p">, </span>snapshot_id=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVolume<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean/?tab=doc#VolumeArgs">VolumeArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean/?tab=doc#Volume">Volume</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Digitalocean/Pulumi.Digitalocean..Volume.html">Volume</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Digitalocean/Pulumi.Digitalocean.VolumeArgs.html">VolumeArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">FilesystemType?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">Region</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>filesystem_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Volume Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<int></span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]int</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">number[]</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">FilesystemType?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">Region</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>droplet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[Integer]</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filesystem_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>initial_<wbr>filesystem_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial_<wbr>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Volume Resource

Get an existing Volume resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/digitalocean/#VolumeState">VolumeState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/digitalocean/#Volume">Volume</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>droplet_ids=None<span class="p">, </span>filesystem_label=None<span class="p">, </span>filesystem_type=None<span class="p">, </span>initial_filesystem_label=None<span class="p">, </span>initial_filesystem_type=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>size=None<span class="p">, </span>snapshot_id=None<span class="p">, </span>tags=None<span class="p">, </span>urn=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVolume<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean/?tab=doc#VolumeState">VolumeState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean/?tab=doc#Volume">Volume</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Digitalocean/Pulumi.Digitalocean..Volume.html">Volume</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Digitalocean/Pulumi.Digitalocean..VolumeState.html">VolumeState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<int>?</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]int</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>droplet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">number[]?</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Filesystem<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Filesystem<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">FilesystemType?</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">Region?</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>droplet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[Integer]</span>
    </dt>
    <dd>{{% md %}}A list of associated droplet ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filesystem_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>filesystem_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem label for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>filesystem_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region that the block storage volume will be created in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the block storage volume in GiB. If updated, can only be expanded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the tags to be applied to this Volume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>urn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The uniform resource name for the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-digitalocean">https://github.com/pulumi/pulumi-digitalocean</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

