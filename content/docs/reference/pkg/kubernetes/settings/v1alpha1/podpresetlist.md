
---
title: "PodPresetList"
block_external_search_index: true
---



PodPresetList is a list of PodPreset objects.


## Create a PodPresetList Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/settings.k8s.io/v1alpha1/#PodPresetList">PodPresetList</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/settings.k8s.io/v1alpha1/#PodPresetListArgs">PodPresetListArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">PodPresetList</span><span class="p">(resource_name, opts=None, </span>api_version=None<span class="p">, </span>items=None<span class="p">, </span>kind=None<span class="p">, </span>metadata=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPodPresetList<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings.k8s.io/v1alpha1?tab=doc#PodPresetListArgs">PodPresetListArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings.k8s.io/v1alpha1?tab=doc#PodPresetList">PodPresetList</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Settings.K8s.Io/V1alpha1.PodPresetList.html">PodPresetList</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Settings.k8s.io/v1alpha1.PodPresetListArgs.html">PodPresetListArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Settings.k8s.io/v1alpha1.<wbr>Inputs.<wbr>Pod<wbr>Preset<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>List<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">[]Pod<wbr>Preset<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">Pod<wbr>Preset[]</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">List[Pod<wbr>Preset]</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Dict[List<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## PodPresetList Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Settings.k8s.io/v1alpha1.<wbr>Outputs.<wbr>Pod<wbr>Preset&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Outputs.<wbr>List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">[]Pod<wbr>Preset<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">Pod<wbr>Preset[]?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpreset">List[Pod<wbr>Preset]</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of schema objects.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Dict[List<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

</dl>
{{% /choosable %}}












## Supporting Types

<h4>AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#AWSElasticBlockStoreVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#AWSElasticBlockStoreVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AWSElasticBlockStoreVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AWSElasticBlockStoreVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Azure<wbr>Disk<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#AzureDiskVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#AzureDiskVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureDiskVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureDiskVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Caching<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host Caching mode: None, Read Only, Read Write.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>URI</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Caching<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Host Caching mode: None, Read Only, Read Write.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name of the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>URI</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>caching<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host Caching mode: None, Read Only, Read Write.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>URI</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>caching<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host Caching mode: None, Read Only, Read Write.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>URI</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Azure<wbr>File<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#AzureFileVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#AzureFileVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureFileVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureFileVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of secret that contains Azure Storage Account Name and Key{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Share Name{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the name of secret that contains Azure Storage Account Name and Key{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Share Name{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of secret that contains Azure Storage Account Name and Key{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Share Name{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of secret that contains Azure Storage Account Name and Key{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Share Name{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>CSIVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CSIVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CSIVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CSIVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CSIVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies a read-only configuration for the volume. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies a read-only configuration for the volume. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies a read-only configuration for the volume. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies a read-only configuration for the volume. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ceph<wbr>FSVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CephFSVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CephFSVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CephFSVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CephFSVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Used as the mounted root, rather than the full Ceph tree, default is /{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: Used as the mounted root, rather than the full Ceph tree, default is /{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Used as the mounted root, rather than the full Ceph tree, default is /{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: Used as the mounted root, rather than the full Ceph tree, default is /{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cinder<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CinderVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CinderVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CinderVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CinderVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Optional: points to a secret object containing parameters used to connect to OpenStack.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}Optional: points to a secret object containing parameters used to connect to OpenStack.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}Optional: points to a secret object containing parameters used to connect to OpenStack.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}Optional: points to a secret object containing parameters used to connect to OpenStack.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Config<wbr>Map<wbr>Env<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ConfigMapEnvSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ConfigMapEnvSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapEnvSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapEnvSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Config<wbr>Map<wbr>Key<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ConfigMapKeySelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ConfigMapKeySelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapKeySelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapKeySelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key to select.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key to select.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key to select.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key to select.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Config<wbr>Map<wbr>Projection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ConfigMapProjection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ConfigMapProjection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapProjectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapProjectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path[]?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List[Key<wbr>To<wbr>Path]</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Config<wbr>Map<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ConfigMapVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ConfigMapVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ConfigMapVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path[]?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List[Key<wbr>To<wbr>Path]</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the ConfigMap or its keys must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Downward<wbr>APIProjection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DownwardAPIProjection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DownwardAPIProjection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIProjectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIProjectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Downward<wbr>APIVolume<wbr>File<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of DownwardAPIVolume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">Downward<wbr>APIVolume<wbr>File</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of DownwardAPIVolume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">Downward<wbr>APIVolume<wbr>File[]?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of DownwardAPIVolume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">List[Downward<wbr>APIVolume<wbr>File]</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of DownwardAPIVolume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Downward<wbr>APIVolume<wbr>File</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DownwardAPIVolumeFile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DownwardAPIVolumeFile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIVolumeFileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIVolumeFileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Object<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Resource<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Dict[Object<wbr>Field<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Dict[Resource<wbr>Field<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Downward<wbr>APIVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DownwardAPIVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DownwardAPIVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#DownwardAPIVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Downward<wbr>APIVolume<wbr>File<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of downward API volume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">Downward<wbr>APIVolume<wbr>File</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of downward API volume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">Downward<wbr>APIVolume<wbr>File[]?</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of downward API volume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumefile">List[Downward<wbr>APIVolume<wbr>File]</a></span>
    </dt>
    <dd>{{% md %}}Items is a list of downward API volume file{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Empty<wbr>Dir<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#EmptyDirVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#EmptyDirVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EmptyDirVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EmptyDirVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Medium</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Medium</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>medium</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>medium</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Env<wbr>From<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#EnvFromSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#EnvFromSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvFromSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvFromSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapenvsource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Config<wbr>Map<wbr>Env<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The ConfigMap to select from{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretenvsource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Env<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Secret to select from{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapenvsource">Config<wbr>Map<wbr>Env<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}The ConfigMap to select from{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretenvsource">Secret<wbr>Env<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}The Secret to select from{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapenvsource">Config<wbr>Map<wbr>Env<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}The ConfigMap to select from{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretenvsource">Secret<wbr>Env<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}The Secret to select from{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapenvsource">Dict[Config<wbr>Map<wbr>Env<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}The ConfigMap to select from{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretenvsource">Dict[Secret<wbr>Env<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}The Secret to select from{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Env<wbr>Var</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#EnvVar">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#EnvVar">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvVarArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvVarOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the environment variable. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvarsource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Env<wbr>Var<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Source for the environment variable's value. Cannot be used if value is not empty.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the environment variable. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvarsource">Env<wbr>Var<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Source for the environment variable's value. Cannot be used if value is not empty.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the environment variable. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvarsource">Env<wbr>Var<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Source for the environment variable's value. Cannot be used if value is not empty.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the environment variable. Must be a C_IDENTIFIER.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvarsource">Dict[Env<wbr>Var<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Source for the environment variable's value. Cannot be used if value is not empty.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Env<wbr>Var<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#EnvVarSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#EnvVarSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvVarSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EnvVarSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapkeyselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Config<wbr>Map<wbr>Key<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a ConfigMap.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Object<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Resource<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretkeyselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Key<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a secret in the pod's namespace{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapkeyselector">Config<wbr>Map<wbr>Key<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a ConfigMap.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretkeyselector">Secret<wbr>Key<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a secret in the pod's namespace{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapkeyselector">Config<wbr>Map<wbr>Key<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a ConfigMap.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretkeyselector">Secret<wbr>Key<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a secret in the pod's namespace{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapkeyselector">Dict[Config<wbr>Map<wbr>Key<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a ConfigMap.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Dict[Object<wbr>Field<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Dict[Resource<wbr>Field<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretkeyselector">Dict[Secret<wbr>Key<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a secret in the pod's namespace{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>FCVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#FCVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#FCVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FCVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FCVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: FC target lun number{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>WWNs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Optional: FC target worldwide names (WWNs){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wwids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: FC target lun number{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>WWNs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Optional: FC target worldwide names (WWNs){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wwids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: FC target lun number{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>WWNs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Optional: FC target worldwide names (WWNs){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wwids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: FC target lun number{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>WWNs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Optional: FC target worldwide names (WWNs){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wwids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flex<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#FlexVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#FlexVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlexVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlexVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Optional: Extra command options if any.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Optional: Extra command options if any.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>options</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Optional: Extra command options if any.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>options</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Optional: Extra command options if any.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flocker<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#FlockerVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#FlockerVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlockerVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlockerVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>UUID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UUID of the dataset. This is unique identifier of a Flocker dataset{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>UUID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UUID of the dataset. This is unique identifier of a Flocker dataset{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>UUID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UUID of the dataset. This is unique identifier of a Flocker dataset{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>UUID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UUID of the dataset. This is unique identifier of a Flocker dataset{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#GCEPersistentDiskVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#GCEPersistentDiskVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GCEPersistentDiskVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GCEPersistentDiskVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pd<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pd<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pd<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pd<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Git<wbr>Repo<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#GitRepoVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#GitRepoVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GitRepoVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GitRepoVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Repository URL{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Commit hash for the specified revision.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Repository URL{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Commit hash for the specified revision.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repository</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Repository URL{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Commit hash for the specified revision.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repository</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Repository URL{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Commit hash for the specified revision.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Glusterfs<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#GlusterfsVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#GlusterfsVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GlusterfsVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GlusterfsVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Host<wbr>Path<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#HostPathVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HostPathVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HostPathVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HostPathVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>ISCSIVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ISCSIVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ISCSIVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ISCSIVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ISCSIVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Chap<wbr>Auth<wbr>Discovery</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Discovery CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chap<wbr>Auth<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Session CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initiator<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iqn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Target iSCSI Qualified Name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Lun number.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portals</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CHAP Secret for iSCSI target and initiator authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Portal</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Chap<wbr>Auth<wbr>Discovery</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Discovery CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chap<wbr>Auth<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Session CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initiator<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iqn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Target iSCSI Qualified Name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Lun number.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portals</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}CHAP Secret for iSCSI target and initiator authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Portal</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>chap<wbr>Auth<wbr>Discovery</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Discovery CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chap<wbr>Auth<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Session CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initiator<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iqn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Target iSCSI Qualified Name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Lun number.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}CHAP Secret for iSCSI target and initiator authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Portal</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>chap<wbr>Auth<wbr>Discovery</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Discovery CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chap<wbr>Auth<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Session CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initiator<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iqn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Target iSCSI Qualified Name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Lun number.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portals</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}CHAP Secret for iSCSI target and initiator authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Portal</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Key<wbr>To<wbr>Path</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#KeyToPath">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#KeyToPath">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#KeyToPathArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#KeyToPathOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key to project.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key to project.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key to project.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key to project.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Label<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LabelSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LabelSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>Label<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">Label<wbr>Selector<wbr>Requirement</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">Label<wbr>Selector<wbr>Requirement[]?</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">List[Label<wbr>Selector<wbr>Requirement]</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Label<wbr>Selector<wbr>Requirement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LabelSelectorRequirement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LabelSelectorRequirement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorRequirementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorRequirementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>List<wbr>Meta</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ListMeta">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ListMeta">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ListMetaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ListMetaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Local<wbr>Object<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LocalObjectReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LocalObjectReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LocalObjectReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LocalObjectReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Managed<wbr>Fields<wbr>Entry</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ManagedFieldsEntry">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ManagedFieldsEntry">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ManagedFieldsEntryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ManagedFieldsEntryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>NFSVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#NFSVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#NFSVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NFSVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NFSVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Object<wbr>Field<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ObjectFieldSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectFieldSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ObjectFieldSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ObjectFieldSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of the schema the FieldPath is written in terms of, defaults to "v1".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path of the field to select in the specified API version.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Version of the schema the FieldPath is written in terms of, defaults to "v1".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path of the field to select in the specified API version.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of the schema the FieldPath is written in terms of, defaults to "v1".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path of the field to select in the specified API version.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Version of the schema the FieldPath is written in terms of, defaults to "v1".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path of the field to select in the specified API version.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Object<wbr>Meta</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ObjectMeta">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectMeta">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ObjectMetaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ObjectMetaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>Managed<wbr>Fields<wbr>Entry<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>Owner<wbr>Reference<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">Managed<wbr>Fields<wbr>Entry</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">Owner<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">Managed<wbr>Fields<wbr>Entry[]?</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">Owner<wbr>Reference[]?</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">List[Managed<wbr>Fields<wbr>Entry]</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">List[Owner<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Owner<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#OwnerReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#OwnerReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#OwnerReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#OwnerReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}API version of the referent.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}API version of the referent.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}API version of the referent.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}API version of the referent.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PersistentVolumeClaimVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PersistentVolumeClaimVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PersistentVolumeClaimVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PersistentVolumeClaimVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Will force the ReadOnly setting in VolumeMounts. Default false.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Will force the ReadOnly setting in VolumeMounts. Default false.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Will force the ReadOnly setting in VolumeMounts. Default false.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Will force the ReadOnly setting in VolumeMounts. Default false.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PhotonPersistentDiskVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PhotonPersistentDiskVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PhotonPersistentDiskVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PhotonPersistentDiskVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pd<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID that identifies Photon Controller persistent disk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pd<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID that identifies Photon Controller persistent disk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pd<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID that identifies Photon Controller persistent disk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pd<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID that identifies Photon Controller persistent disk{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Preset</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodPreset">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodPreset">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings/v1alpha1?tab=doc#PodPresetTypeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings/v1alpha1?tab=doc#PodPresetTypeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>Object<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpresetspec">Pulumi.<wbr>Kubernetes.<wbr>Settings.k8s.io/v1alpha1.<wbr>Inputs.<wbr>Pod<wbr>Preset<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpresetspec">*Pod<wbr>Preset<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpresetspec">Pod<wbr>Preset<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podpresetspec">Dict[Pod<wbr>Preset<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Preset<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodPresetSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodPresetSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings/v1alpha1?tab=doc#PodPresetSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/settings/v1alpha1?tab=doc#PodPresetSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Env<wbr>Var<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Env defines the collection of EnvVar to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Env<wbr>From<wbr>Source<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}EnvFrom defines the collection of EnvFromSource to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Inputs.<wbr>Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selector is a label query over a set of resources, in this case pods. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Volume<wbr>Mount<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}VolumeMounts defines the collection of VolumeMount to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Volume<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Volumes defines the collection of Volume to inject into the pod.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var</a></span>
    </dt>
    <dd>{{% md %}}Env defines the collection of EnvVar to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}EnvFrom defines the collection of EnvFromSource to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Selector is a label query over a set of resources, in this case pods. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount</a></span>
    </dt>
    <dd>{{% md %}}VolumeMounts defines the collection of VolumeMount to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">Volume</a></span>
    </dt>
    <dd>{{% md %}}Volumes defines the collection of Volume to inject into the pod.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var[]?</a></span>
    </dt>
    <dd>{{% md %}}Env defines the collection of EnvVar to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source[]?</a></span>
    </dt>
    <dd>{{% md %}}EnvFrom defines the collection of EnvFromSource to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Selector is a label query over a set of resources, in this case pods. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount[]?</a></span>
    </dt>
    <dd>{{% md %}}VolumeMounts defines the collection of VolumeMount to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">Volume[]?</a></span>
    </dt>
    <dd>{{% md %}}Volumes defines the collection of Volume to inject into the pod.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List[Env<wbr>Var]</a></span>
    </dt>
    <dd>{{% md %}}Env defines the collection of EnvVar to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List[Env<wbr>From<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}EnvFrom defines the collection of EnvFromSource to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Selector is a label query over a set of resources, in this case pods. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List[Volume<wbr>Mount]</a></span>
    </dt>
    <dd>{{% md %}}VolumeMounts defines the collection of VolumeMount to inject into containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">List[Volume]</a></span>
    </dt>
    <dd>{{% md %}}Volumes defines the collection of Volume to inject into the pod.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Portworx<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PortworxVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PortworxVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PortworxVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PortworxVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeID uniquely identifies a Portworx volume{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}VolumeID uniquely identifies a Portworx volume{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeID uniquely identifies a Portworx volume{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeID uniquely identifies a Portworx volume{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Projected<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ProjectedVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ProjectedVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ProjectedVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ProjectedVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeprojection">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Volume<wbr>Projection<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}list of volume projections{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeprojection">Volume<wbr>Projection</a></span>
    </dt>
    <dd>{{% md %}}list of volume projections{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeprojection">Volume<wbr>Projection[]?</a></span>
    </dt>
    <dd>{{% md %}}list of volume projections{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeprojection">List[Volume<wbr>Projection]</a></span>
    </dt>
    <dd>{{% md %}}list of volume projections{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Quobyte<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#QuobyteVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#QuobyteVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#QuobyteVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#QuobyteVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Group to map volume access to Default is no group{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Registry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User to map volume access to Defaults to serivceaccount user{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Volume is a string that references an already created Quobyte volume by name.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Group to map volume access to Default is no group{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Registry</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User to map volume access to Defaults to serivceaccount user{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Volume is a string that references an already created Quobyte volume by name.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Group to map volume access to Default is no group{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>registry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User to map volume access to Defaults to serivceaccount user{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Volume is a string that references an already created Quobyte volume by name.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Group to map volume access to Default is no group{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>registry</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User to map volume access to Defaults to serivceaccount user{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Volume is a string that references an already created Quobyte volume by name.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>RBDVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#RBDVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#RBDVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#RBDVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#RBDVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keyring</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keyring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keyring</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keyring</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Resource<wbr>Field<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ResourceFieldSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ResourceFieldSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ResourceFieldSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ResourceFieldSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container name: required for volumes, optional for env vars{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Divisor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the output format of the exposed resources, defaults to "1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required: resource to select{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Container name: required for volumes, optional for env vars{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Divisor</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the output format of the exposed resources, defaults to "1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required: resource to select{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container name: required for volumes, optional for env vars{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>divisor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the output format of the exposed resources, defaults to "1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required: resource to select{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Container name: required for volumes, optional for env vars{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>divisor</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the output format of the exposed resources, defaults to "1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required: resource to select{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Scale<wbr>IOVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ScaleIOVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ScaleIOVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ScaleIOVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ScaleIOVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The host address of the ScaleIO API Gateway.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protection<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the ScaleIO Protection Domain for the configured storage.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to enable/disable SSL communication with Gateway, default false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ScaleIO Storage Pool associated with the protection domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the storage system as configured in ScaleIO.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a volume already created in the ScaleIO system that is associated with this volume source.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The host address of the ScaleIO API Gateway.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protection<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the ScaleIO Protection Domain for the configured storage.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to enable/disable SSL communication with Gateway, default false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ScaleIO Storage Pool associated with the protection domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the storage system as configured in ScaleIO.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a volume already created in the ScaleIO system that is associated with this volume source.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The host address of the ScaleIO API Gateway.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protection<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the ScaleIO Protection Domain for the configured storage.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to enable/disable SSL communication with Gateway, default false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ScaleIO Storage Pool associated with the protection domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>system</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the storage system as configured in ScaleIO.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a volume already created in the ScaleIO system that is associated with this volume source.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The host address of the ScaleIO API Gateway.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protection<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the ScaleIO Protection Domain for the configured storage.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to enable/disable SSL communication with Gateway, default false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ScaleIO Storage Pool associated with the protection domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>system</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the storage system as configured in ScaleIO.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a volume already created in the ScaleIO system that is associated with this volume source.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Secret<wbr>Env<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecretEnvSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecretEnvSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretEnvSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretEnvSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Secret<wbr>Key<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecretKeySelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecretKeySelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretKeySelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretKeySelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the secret to select from.  Must be a valid secret key.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key of the secret to select from.  Must be a valid secret key.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the secret to select from.  Must be a valid secret key.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key of the secret to select from.  Must be a valid secret key.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Secret<wbr>Projection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecretProjection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecretProjection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretProjectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretProjectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path[]?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List[Key<wbr>To<wbr>Path]</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its key must be defined{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Secret<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecretVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecretVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its keys must be defined{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its keys must be defined{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">Key<wbr>To<wbr>Path[]?</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its keys must be defined{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#keytopath">List[Key<wbr>To<wbr>Path]</a></span>
    </dt>
    <dd>{{% md %}}If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify whether the Secret or its keys must be defined{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Service<wbr>Account<wbr>Token<wbr>Projection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ServiceAccountTokenProjection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ServiceAccountTokenProjection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ServiceAccountTokenProjectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ServiceAccountTokenProjectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path is the path relative to the mount point of the file to project the token into.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path is the path relative to the mount point of the file to project the token into.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path is the path relative to the mount point of the file to project the token into.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path is the path relative to the mount point of the file to project the token into.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Storage<wbr>OSVolume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#StorageOSVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#StorageOSVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#StorageOSVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#StorageOSVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Volume">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Volume">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Elastic<wbr>Block<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#awselasticblockstorevolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Azure<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurefilevolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Azure<wbr>File<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfsvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Ceph<wbr>FSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cindervolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Cinder<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Config<wbr>Map<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ConfigMap represents a configMap that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csivolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>CSIVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Downward<wbr>APIVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DownwardAPI represents downward API about the pod that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Empty<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#emptydirvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Empty<wbr>Dir<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fcvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>FCVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flex<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Flex<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Flocker<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Git<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gitrepovolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Git<wbr>Repo<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfsvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Glusterfs<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Host<wbr>Path<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsivolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>ISCSIVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>NFSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumeclaimvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Photon<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portworx<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#portworxvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Portworx<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PortworxVolume represents a portworx volume attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Projected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectedvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Projected<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Items for all in one resources secrets, configmaps, and downward API{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Quobyte<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>RBDVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiovolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Scale<wbr>IOVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageosvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Storage<wbr>OSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aws<wbr>Elastic<wbr>Block<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#awselasticblockstorevolumesource">AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Azure<wbr>Disk<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurefilevolumesource">Azure<wbr>File<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfsvolumesource">Ceph<wbr>FSVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cindervolumesource">Cinder<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapvolumesource">Config<wbr>Map<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}ConfigMap represents a configMap that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csivolumesource">CSIVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumesource">Downward<wbr>APIVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}DownwardAPI represents downward API about the pod that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Empty<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#emptydirvolumesource">Empty<wbr>Dir<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fcvolumesource">FCVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flex<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexvolumesource">Flex<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Flocker<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Git<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gitrepovolumesource">Git<wbr>Repo<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfsvolumesource">Glusterfs<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Host<wbr>Path<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsivolumesource">ISCSIVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">NFSVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumeclaimvolumesource">Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Photon<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portworx<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#portworxvolumesource">Portworx<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}PortworxVolume represents a portworx volume attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Projected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectedvolumesource">Projected<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Items for all in one resources secrets, configmaps, and downward API{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Quobyte<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdvolumesource">RBDVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiovolumesource">Scale<wbr>IOVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretvolumesource">Secret<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageosvolumesource">Storage<wbr>OSVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aws<wbr>Elastic<wbr>Block<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#awselasticblockstorevolumesource">AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Azure<wbr>Disk<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurefilevolumesource">Azure<wbr>File<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfsvolumesource">Ceph<wbr>FSVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cindervolumesource">Cinder<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapvolumesource">Config<wbr>Map<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}ConfigMap represents a configMap that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csivolumesource">CSIVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumesource">Downward<wbr>APIVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}DownwardAPI represents downward API about the pod that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>empty<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#emptydirvolumesource">Empty<wbr>Dir<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fcvolumesource">FCVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flex<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexvolumesource">Flex<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Flocker<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>git<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gitrepovolumesource">Git<wbr>Repo<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfsvolumesource">Glusterfs<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Host<wbr>Path<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsivolumesource">ISCSIVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">NFSVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumeclaimvolumesource">Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>photon<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portworx<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#portworxvolumesource">Portworx<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}PortworxVolume represents a portworx volume attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>projected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectedvolumesource">Projected<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Items for all in one resources secrets, configmaps, and downward API{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Quobyte<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdvolumesource">RBDVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiovolumesource">Scale<wbr>IOVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretvolumesource">Secret<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageosvolumesource">Storage<wbr>OSVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aws<wbr>Elastic<wbr>Block<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#awselasticblockstorevolumesource">Dict[AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Dict[Azure<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurefilevolumesource">Dict[Azure<wbr>File<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfsvolumesource">Dict[Ceph<wbr>FSVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cindervolumesource">Dict[Cinder<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapvolumesource">Dict[Config<wbr>Map<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}ConfigMap represents a configMap that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csivolumesource">Dict[CSIVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumesource">Dict[Downward<wbr>APIVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}DownwardAPI represents downward API about the pod that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>empty<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#emptydirvolumesource">Dict[Empty<wbr>Dir<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fcvolumesource">Dict[FCVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flex<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexvolumesource">Dict[Flex<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Dict[Flocker<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">Dict[GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>git<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gitrepovolumesource">Dict[Git<wbr>Repo<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfsvolumesource">Dict[Glusterfs<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Dict[Host<wbr>Path<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsivolumesource">Dict[ISCSIVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">Dict[NFSVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumeclaimvolumesource">Dict[Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>photon<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Dict[Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portworx<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#portworxvolumesource">Dict[Portworx<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}PortworxVolume represents a portworx volume attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>projected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectedvolumesource">Dict[Projected<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Items for all in one resources secrets, configmaps, and downward API{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Dict[Quobyte<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdvolumesource">Dict[RBDVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiovolumesource">Dict[Scale<wbr>IOVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretvolumesource">Dict[Secret<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageosvolumesource">Dict[Storage<wbr>OSVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Dict[Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Mount</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeMount">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeMount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeMountArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeMountOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path within the container at which the volume should be mounted.  Must not contain ':'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Propagation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This must match the Name of a Volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sub<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sub<wbr>Path<wbr>Expr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path within the container at which the volume should be mounted.  Must not contain ':'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Propagation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}This must match the Name of a Volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sub<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sub<wbr>Path<wbr>Expr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path within the container at which the volume should be mounted.  Must not contain ':'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Propagation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This must match the Name of a Volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sub<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sub<wbr>Path<wbr>Expr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path within the container at which the volume should be mounted.  Must not contain ':'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Propagation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This must match the Name of a Volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sub<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sub<wbr>Path<wbr>Expr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Projection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeProjection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeProjection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeProjectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeProjectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapprojection">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Config<wbr>Map<wbr>Projection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the configMap data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapiprojection">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Downward<wbr>APIProjection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the downwardAPI data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretprojection">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Projection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the secret data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#serviceaccounttokenprojection">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Service<wbr>Account<wbr>Token<wbr>Projection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the serviceAccountToken data to project{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapprojection">Config<wbr>Map<wbr>Projection</a></span>
    </dt>
    <dd>{{% md %}}information about the configMap data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapiprojection">Downward<wbr>APIProjection</a></span>
    </dt>
    <dd>{{% md %}}information about the downwardAPI data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretprojection">Secret<wbr>Projection</a></span>
    </dt>
    <dd>{{% md %}}information about the secret data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#serviceaccounttokenprojection">Service<wbr>Account<wbr>Token<wbr>Projection</a></span>
    </dt>
    <dd>{{% md %}}information about the serviceAccountToken data to project{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapprojection">Config<wbr>Map<wbr>Projection?</a></span>
    </dt>
    <dd>{{% md %}}information about the configMap data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapiprojection">Downward<wbr>APIProjection?</a></span>
    </dt>
    <dd>{{% md %}}information about the downwardAPI data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretprojection">Secret<wbr>Projection?</a></span>
    </dt>
    <dd>{{% md %}}information about the secret data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#serviceaccounttokenprojection">Service<wbr>Account<wbr>Token<wbr>Projection?</a></span>
    </dt>
    <dd>{{% md %}}information about the serviceAccountToken data to project{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapprojection">Dict[Config<wbr>Map<wbr>Projection]</a></span>
    </dt>
    <dd>{{% md %}}information about the configMap data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapiprojection">Dict[Downward<wbr>APIProjection]</a></span>
    </dt>
    <dd>{{% md %}}information about the downwardAPI data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretprojection">Dict[Secret<wbr>Projection]</a></span>
    </dt>
    <dd>{{% md %}}information about the secret data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#serviceaccounttokenprojection">Dict[Service<wbr>Account<wbr>Token<wbr>Projection]</a></span>
    </dt>
    <dd>{{% md %}}information about the serviceAccountToken data to project{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VsphereVirtualDiskVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VsphereVirtualDiskVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VsphereVirtualDiskVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VsphereVirtualDiskVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path that identifies vSphere volume vmdk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path that identifies vSphere volume vmdk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path that identifies vSphere volume vmdk{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>ID</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path that identifies vSphere volume vmdk{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-kubernetes">https://github.com/pulumi/pulumi-kubernetes</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

