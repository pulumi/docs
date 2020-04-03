
---
title: "VolumeAttachment"
block_external_search_index: true
---



VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

VolumeAttachment objects are non-namespaced.


## Create a VolumeAttachment Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/storage.k8s.io/v1beta1/#VolumeAttachment">VolumeAttachment</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/storage.k8s.io/v1beta1/#VolumeAttachmentArgs">VolumeAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VolumeAttachment</span><span class="p">(resource_name, opts=None, </span>api_version=None<span class="p">, </span>kind=None<span class="p">, </span>metadata=None<span class="p">, </span>spec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVolumeAttachment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage.k8s.io/v1beta1?tab=doc#VolumeAttachmentArgs">VolumeAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage.k8s.io/v1beta1?tab=doc#VolumeAttachment">VolumeAttachment</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Storage.K8s.Io/V1beta1.VolumeAttachment.html">VolumeAttachment</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Storage.k8s.io/v1beta1.VolumeAttachmentArgs.html">VolumeAttachmentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Inputs.<wbr>Volume<wbr>Attachment<wbr>Spec<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

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
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Volume<wbr>Attachment<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

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
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Volume<wbr>Attachment<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

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
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Dict[Volume<wbr>Attachment<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## VolumeAttachment Output Properties

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
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Pulumi.<wbr>Kubernetes.<wbr>Meta.<wbr>V1.<wbr>Outputs.<wbr>Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Outputs.<wbr>Volume<wbr>Attachment<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentstatus">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Outputs.<wbr>Volume<wbr>Attachment<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.{{% /md %}}</dd>

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
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">*Volume<wbr>Attachment<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentstatus">*Volume<wbr>Attachment<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.{{% /md %}}</dd>

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
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Volume<wbr>Attachment<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentstatus">Volume<wbr>Attachment<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.{{% /md %}}</dd>

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
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentspec">Dict[Volume<wbr>Attachment<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentstatus">Dict[Volume<wbr>Attachment<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.{{% /md %}}</dd>

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





<h4>Azure<wbr>File<wbr>Persistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#AzureFilePersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#AzureFilePersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureFilePersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AzureFilePersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span>Secret<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod{{% /md %}}</dd>

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
        <span>Secret<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod{{% /md %}}</dd>

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
        <span>secret<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod{{% /md %}}</dd>

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
        <span>secret<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Share Name{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>CSIPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CSIPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CSIPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CSIPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CSIPersistentVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Expand<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Stage<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Attributes of the volume to publish.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Handle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Expand<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Stage<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Attributes of the volume to publish.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Handle</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Expand<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Stage<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Attributes of the volume to publish.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Handle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Expand<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Driver is the name of the driver to use for this volume. Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Publish<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Stage<wbr>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Attributes of the volume to publish.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Handle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ceph<wbr>FSPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CephFSPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CephFSPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CephFSPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CephFSPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Cinder<wbr>Persistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CinderPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CinderPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CinderPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CinderPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Flex<wbr>Persistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#FlexPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#FlexPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlexPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#FlexPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Glusterfs<wbr>Persistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#GlusterfsPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#GlusterfsPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GlusterfsPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#GlusterfsPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span>Endpoints<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

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
        <span>Endpoints<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

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
        <span>endpoints<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

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
        <span>endpoints<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

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





<h4>ISCSIPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ISCSIPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ISCSIPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ISCSIPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ISCSIPersistentVolumeSourceOutput">output</a> API doc for this type.
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
    <dd>{{% md %}}iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
    <dd>{{% md %}}iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
    <dd>{{% md %}}iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
    <dd>{{% md %}}iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Local<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LocalVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LocalVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LocalVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LocalVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).{{% /md %}}</dd>

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
    <dd>{{% md %}}Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).{{% /md %}}</dd>

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
    <dd>{{% md %}}Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).{{% /md %}}</dd>

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
    <dd>{{% md %}}Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).{{% /md %}}</dd>

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





<h4>Node<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#NodeSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#NodeSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Selector<wbr>Terms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Node<wbr>Selector<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Required. A list of node selector terms. The terms are ORed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Selector<wbr>Terms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Node<wbr>Selector<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}Required. A list of node selector terms. The terms are ORed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Selector<wbr>Terms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Node<wbr>Selector<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}Required. A list of node selector terms. The terms are ORed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Selector<wbr>Terms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">List[Node<wbr>Selector<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}Required. A list of node selector terms. The terms are ORed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Selector<wbr>Requirement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#NodeSelectorRequirement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#NodeSelectorRequirement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorRequirementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorRequirementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

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
    <dd>{{% md %}}The label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

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
    <dd>{{% md %}}The label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

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
    <dd>{{% md %}}The label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Selector<wbr>Term</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#NodeSelectorTerm">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#NodeSelectorTerm">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorTermArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeSelectorTermOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Node<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">List&lt;Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Node<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's fields.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">Node<wbr>Selector<wbr>Requirement</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">Node<wbr>Selector<wbr>Requirement</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's fields.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">Node<wbr>Selector<wbr>Requirement[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">Node<wbr>Selector<wbr>Requirement[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's fields.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">List[Node<wbr>Selector<wbr>Requirement]</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">List[Node<wbr>Selector<wbr>Requirement]</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's fields.{{% /md %}}</dd>

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





<h4>Object<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ObjectReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ObjectReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ObjectReferenceOutput">output</a> API doc for this type.
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
        <span>Field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids{{% /md %}}</dd>

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
        <span>Field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids{{% /md %}}</dd>

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
        <span>field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids{{% /md %}}</dd>

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
        <span>field<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids{{% /md %}}</dd>

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





<h4>Persistent<wbr>Volume<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PersistentVolumeSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PersistentVolumeSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PersistentVolumeSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PersistentVolumeSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Modes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes{{% /md %}}</dd>

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
        <span class="property-type"><a href="#azurefilepersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Azure<wbr>File<wbr>Persistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfspersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Ceph<wbr>FSPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cinderpersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Cinder<wbr>Persistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csipersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>CSIPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CSI represents storage that is handled by an external CSI driver (Beta feature).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#flexpersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Flex<wbr>Persistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Flocker<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfspersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Glusterfs<wbr>Persistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Host<wbr>Path<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsipersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>ISCSIPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Local<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Local represents directly-attached storage with node affinity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>NFSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumenodeaffinity">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Volume<wbr>Node<wbr>Affinity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Reclaim<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming{{% /md %}}</dd>

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
        <span>Quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Quobyte<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdpersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>RBDPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiopersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Scale<wbr>IOPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageospersistentvolumesource">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Storage<wbr>OSPersistent<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.{{% /md %}}</dd>

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
        <span>Access<wbr>Modes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes{{% /md %}}</dd>

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
        <span class="property-type"><a href="#azurefilepersistentvolumesource">Azure<wbr>File<wbr>Persistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfspersistentvolumesource">Ceph<wbr>FSPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cinderpersistentvolumesource">Cinder<wbr>Persistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectreference">Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csipersistentvolumesource">CSIPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}CSI represents storage that is handled by an external CSI driver (Beta feature).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#flexpersistentvolumesource">Flex<wbr>Persistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Flocker<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfspersistentvolumesource">Glusterfs<wbr>Persistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Host<wbr>Path<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsipersistentvolumesource">ISCSIPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localvolumesource">Local<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Local represents directly-attached storage with node affinity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">NFSVolume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumenodeaffinity">Volume<wbr>Node<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Reclaim<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming{{% /md %}}</dd>

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
        <span>Quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Quobyte<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdpersistentvolumesource">RBDPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiopersistentvolumesource">Scale<wbr>IOPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageospersistentvolumesource">Storage<wbr>OSPersistent<wbr>Volume<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.{{% /md %}}</dd>

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
        <span>access<wbr>Modes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes{{% /md %}}</dd>

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
        <span class="property-type"><a href="#azurefilepersistentvolumesource">Azure<wbr>File<wbr>Persistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfspersistentvolumesource">Ceph<wbr>FSPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cinderpersistentvolumesource">Cinder<wbr>Persistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectreference">Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csipersistentvolumesource">CSIPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}CSI represents storage that is handled by an external CSI driver (Beta feature).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#flexpersistentvolumesource">Flex<wbr>Persistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Flocker<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfspersistentvolumesource">Glusterfs<wbr>Persistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Host<wbr>Path<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsipersistentvolumesource">ISCSIPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localvolumesource">Local<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Local represents directly-attached storage with node affinity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">NFSVolume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumenodeaffinity">Volume<wbr>Node<wbr>Affinity?</a></span>
    </dt>
    <dd>{{% md %}}NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Reclaim<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming{{% /md %}}</dd>

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
        <span>quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Quobyte<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdpersistentvolumesource">RBDPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiopersistentvolumesource">Scale<wbr>IOPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageospersistentvolumesource">Storage<wbr>OSPersistent<wbr>Volume<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.{{% /md %}}</dd>

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
        <span>access<wbr>Modes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes{{% /md %}}</dd>

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
        <span class="property-type"><a href="#azurefilepersistentvolumesource">Dict[Azure<wbr>File<wbr>Persistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfspersistentvolumesource">Dict[Ceph<wbr>FSPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cinderpersistentvolumesource">Dict[Cinder<wbr>Persistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectreference">Dict[Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csipersistentvolumesource">Dict[CSIPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}CSI represents storage that is handled by an external CSI driver (Beta feature).{{% /md %}}</dd>

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
        <span class="property-type"><a href="#flexpersistentvolumesource">Dict[Flex<wbr>Persistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Dict[Flocker<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">Dict[GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfspersistentvolumesource">Dict[Glusterfs<wbr>Persistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Dict[Host<wbr>Path<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsipersistentvolumesource">Dict[ISCSIPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localvolumesource">Dict[Local<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Local represents directly-attached storage with node affinity{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nfsvolumesource">Dict[NFSVolume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumenodeaffinity">Dict[Volume<wbr>Node<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Reclaim<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming{{% /md %}}</dd>

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
        <span>quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Dict[Quobyte<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdpersistentvolumesource">Dict[RBDPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiopersistentvolumesource">Dict[Scale<wbr>IOPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageospersistentvolumesource">Dict[Storage<wbr>OSPersistent<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Dict[Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

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





<h4>RBDPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#RBDPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#RBDPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#RBDPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#RBDPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Scale<wbr>IOPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ScaleIOPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ScaleIOPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ScaleIOPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ScaleIOPersistentVolumeSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Secret<wbr>Reference<wbr>Args?</a></span>
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
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference</a></span>
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
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Secret<wbr>Reference?</a></span>
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
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"{{% /md %}}</dd>

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
        <span class="property-type"><a href="#secretreference">Dict[Secret<wbr>Reference]</a></span>
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





<h4>Secret<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecretReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecretReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecretReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name is unique within a namespace to reference a secret resource.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within which the secret name must be unique.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name is unique within a namespace to reference a secret resource.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within which the secret name must be unique.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name is unique within a namespace to reference a secret resource.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within which the secret name must be unique.{{% /md %}}</dd>

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
    <dd>{{% md %}}Name is unique within a namespace to reference a secret resource.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within which the secret name must be unique.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Storage<wbr>OSPersistent<wbr>Volume<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#StorageOSPersistentVolumeSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#StorageOSPersistentVolumeSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#StorageOSPersistentVolumeSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#StorageOSPersistentVolumeSourceOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#objectreference">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#objectreference">Object<wbr>Reference</a></span>
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
        <span class="property-type"><a href="#objectreference">Object<wbr>Reference?</a></span>
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
        <span class="property-type"><a href="#objectreference">Dict[Object<wbr>Reference]</a></span>
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





<h4>Volume<wbr>Attachment<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeAttachmentSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeAttachmentSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeAttachmentSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeAttachmentSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Inline<wbr>Volume<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumespec">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Persistent<wbr>Volume<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the persistent volume to attach.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Inline<wbr>Volume<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumespec">Persistent<wbr>Volume<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the persistent volume to attach.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>inline<wbr>Volume<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumespec">Persistent<wbr>Volume<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the persistent volume to attach.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>inline<wbr>Volume<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumespec">Dict[Persistent<wbr>Volume<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistent<wbr>Volume<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the persistent volume to attach.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Attachment<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeAttachmentSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeAttachmentSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeAttachmentSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeAttachmentSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attacher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The node that the volume should be attached to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentsource">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Inputs.<wbr>Volume<wbr>Attachment<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Source represents the volume that should be attached.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attacher</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The node that the volume should be attached to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentsource">*Volume<wbr>Attachment<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}Source represents the volume that should be attached.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attacher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The node that the volume should be attached to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentsource">Volume<wbr>Attachment<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}Source represents the volume that should be attached.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attacher</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The node that the volume should be attached to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeattachmentsource">Dict[Volume<wbr>Attachment<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}Source represents the volume that should be attached.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Attachment<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeAttachmentStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeAttachmentStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Inputs.<wbr>Volume<wbr>Error<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attachment<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Pulumi.<wbr>Kubernetes.<wbr>Storage.k8s.io/v1beta1.<wbr>Inputs.<wbr>Volume<wbr>Error<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">*Volume<wbr>Error</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attachment<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">*Volume<wbr>Error</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Volume<wbr>Error?</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attachment<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Volume<wbr>Error?</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Dict[Volume<wbr>Error]</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attachment<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detach<wbr>Error</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumeerror">Dict[Volume<wbr>Error]</a></span>
    </dt>
    <dd>{{% md %}}The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Error</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeError">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/storage/v1beta1?tab=doc#VolumeErrorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time the error was encountered.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time the error was encountered.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time the error was encountered.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time the error was encountered.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Node<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeNodeAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeNodeAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeNodeAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeNodeAffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Pulumi.<wbr>Kubernetes.<wbr>Core.<wbr>V1.<wbr>Inputs.<wbr>Node<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Required specifies hard node constraints that must be met.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Node<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Required specifies hard node constraints that must be met.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Node<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Required specifies hard node constraints that must be met.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Dict[Node<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Required specifies hard node constraints that must be met.{{% /md %}}</dd>

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

