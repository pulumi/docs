
---
title: "DeploymentList"
block_external_search_index: true
---



DeploymentList is a list of Deployments.


## Create a DeploymentList Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/apps/v1/#DeploymentList">DeploymentList</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/apps/v1/#DeploymentListArgs">DeploymentListArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DeploymentList</span><span class="p">(resource_name, opts=None, </span>items=None<span class="p">, </span>metadata=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDeploymentList<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentListArgs">DeploymentListArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentList">DeploymentList</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Apps.V1.DeploymentList.html">DeploymentList</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Apps.V1.DeploymentListArgs.html">DeploymentListArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">List&lt;Deployment<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">[]Deployment<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">Deployment[]</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">List[Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Dict[List<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DeploymentList Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">List&lt;Deployment&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">[]Deployment<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">Deployment[]?</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>items</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deployment">List[Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Items is the list of Deployments.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Dict[List<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata.{{% /md %}}</dd>

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
        <span>fs_<wbr>type</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Affinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Affinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#AffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeaffinity">Node<wbr>Affinity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes node affinity scheduling rules for the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinity">Pod<wbr>Affinity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Anti<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podantiaffinity">Pod<wbr>Anti<wbr>Affinity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeaffinity">Node<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}Describes node affinity scheduling rules for the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinity">Pod<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Anti<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podantiaffinity">Pod<wbr>Anti<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeaffinity">Node<wbr>Affinity?</a></span>
    </dt>
    <dd>{{% md %}}Describes node affinity scheduling rules for the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinity">Pod<wbr>Affinity?</a></span>
    </dt>
    <dd>{{% md %}}Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Anti<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podantiaffinity">Pod<wbr>Anti<wbr>Affinity?</a></span>
    </dt>
    <dd>{{% md %}}Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeaffinity">Dict[Node<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}Describes node affinity scheduling rules for the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinity">Dict[Pod<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod_<wbr>anti_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podantiaffinity">Dict[Pod<wbr>Anti<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).{{% /md %}}</dd>

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
        <span>caching_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host Caching mode: None, Read Only, Read Write.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI the data disk in the blob storage{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of secret that contains Azure Storage Account Name and Key{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>name</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>publish_<wbr>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies a read-only configuration for the volume. Defaults to false (read/write).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Capabilities</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Capabilities">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Capabilities">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CapabilitiesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#CapabilitiesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Add</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Added capabilities{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Drop</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Removed capabilities{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Add</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Added capabilities{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Drop</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Removed capabilities{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Added capabilities{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>drop</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Removed capabilities{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Added capabilities{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>drop</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Removed capabilities{{% /md %}}</dd>

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
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}Optional: points to a secret object containing parameters used to connect to OpenStack.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>id</span>
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
        <span class="property-type"><a href="#keytopath">List&lt;Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
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
        <span class="property-type"><a href="#keytopath">List&lt;Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
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





<h4>Container</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Container">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Container">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ContainerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List&lt;Env<wbr>Var<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List&lt;Env<wbr>From<wbr>Source<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Actions that the management system should take in response to container lifecycle events. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">List&lt;Container<wbr>Port<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is a beta feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">List&lt;Volume<wbr>Device<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List&lt;Volume<wbr>Mount<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle</a></span>
    </dt>
    <dd>{{% md %}}Actions that the management system should take in response to container lifecycle events. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">Container<wbr>Port</a></span>
    </dt>
    <dd>{{% md %}}List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements</a></span>
    </dt>
    <dd>{{% md %}}Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context</a></span>
    </dt>
    <dd>{{% md %}}Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is a beta feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">Volume<wbr>Device</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var[]?</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source[]?</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle?</a></span>
    </dt>
    <dd>{{% md %}}Actions that the management system should take in response to container lifecycle events. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">Container<wbr>Port[]?</a></span>
    </dt>
    <dd>{{% md %}}List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements?</a></span>
    </dt>
    <dd>{{% md %}}Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context?</a></span>
    </dt>
    <dd>{{% md %}}Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is a beta feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">Volume<wbr>Device[]?</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount[]?</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List[Env<wbr>Var]</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List[Env<wbr>From<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Dict[Lifecycle]</a></span>
    </dt>
    <dd>{{% md %}}Actions that the management system should take in response to container lifecycle events. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">List[Container<wbr>Port]</a></span>
    </dt>
    <dd>{{% md %}}List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Dict[Resource<wbr>Requirements]</a></span>
    </dt>
    <dd>{{% md %}}Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Dict[Security<wbr>Context]</a></span>
    </dt>
    <dd>{{% md %}}Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is a beta feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">List[Volume<wbr>Device]</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List[Volume<wbr>Mount]</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Container<wbr>Port</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ContainerPort">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ContainerPort">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ContainerPortArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ContainerPortOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>IP</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What host IP to bind the external port to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>IP</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}What host IP to bind the external port to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>IP</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}What host IP to bind the external port to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}What host IP to bind the external port to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Deployment</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Deployment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Deployment">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentTypeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentTypeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentspec">Deployment<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the Deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstatus">Deployment<wbr>Status<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Most recently observed status of the Deployment.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentspec">*Deployment<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the Deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstatus">*Deployment<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}Most recently observed status of the Deployment.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentspec">Deployment<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the Deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstatus">Deployment<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}Most recently observed status of the Deployment.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard object metadata.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentspec">Dict[Deployment<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the Deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstatus">Dict[Deployment<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}Most recently observed status of the Deployment.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Deployment<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DeploymentCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DeploymentCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentConditionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Last time the condition transitioned from one status to another.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The last time this condition was updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human readable message indicating details about the transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the condition, one of True, False, Unknown.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of deployment condition.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Last time the condition transitioned from one status to another.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The last time this condition was updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human readable message indicating details about the transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Status of the condition, one of True, False, Unknown.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of deployment condition.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Last time the condition transitioned from one status to another.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The last time this condition was updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human readable message indicating details about the transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the condition, one of True, False, Unknown.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of deployment condition.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Last time the condition transitioned from one status to another.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The last time this condition was updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human readable message indicating details about the transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of the condition, one of True, False, Unknown.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of deployment condition.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Deployment<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DeploymentSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DeploymentSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ready<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paused</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates that the deployment is paused.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Progress<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstrategy">Deployment<wbr>Strategy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The deployment strategy to use to replace existing pods with new ones.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podtemplatespec">Pod<wbr>Template<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Template describes the pods that will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ready<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paused</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the deployment is paused.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Progress<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstrategy">*Deployment<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The deployment strategy to use to replace existing pods with new ones.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podtemplatespec">Pod<wbr>Template<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Template describes the pods that will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Ready<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paused</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates that the deployment is paused.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>progress<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstrategy">Deployment<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}The deployment strategy to use to replace existing pods with new ones.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podtemplatespec">Pod<wbr>Template<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}Template describes the pods that will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>ready_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paused</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the deployment is paused.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>progress_<wbr>deadline_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision_<wbr>history_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentstrategy">Dict[Deployment<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}The deployment strategy to use to replace existing pods with new ones.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podtemplatespec">Dict[Pod<wbr>Template<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}Template describes the pods that will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Deployment<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DeploymentStatus">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DeploymentStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentStatusArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Available<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Collision<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentcondition">List&lt;Deployment<wbr>Condition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Represents the latest available observations of a deployment's current state.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The generation observed by the deployment controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ready<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total number of ready pods targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment (their labels match the selector).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unavailable<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Updated<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment that have the desired template spec.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Available<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Collision<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentcondition">[]Deployment<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}Represents the latest available observations of a deployment's current state.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The generation observed by the deployment controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ready<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total number of ready pods targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment (their labels match the selector).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unavailable<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Updated<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment that have the desired template spec.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>collision<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentcondition">Deployment<wbr>Condition[]?</a></span>
    </dt>
    <dd>{{% md %}}Represents the latest available observations of a deployment's current state.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The generation observed by the deployment controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ready<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total number of ready pods targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment (their labels match the selector).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unavailable<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>updated<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment that have the desired template spec.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>collision_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#deploymentcondition">List[Deployment<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}Represents the latest available observations of a deployment's current state.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>observed_<wbr>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The generation observed by the deployment controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ready_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total number of ready pods targeted by this deployment.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment (their labels match the selector).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unavailable_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>updated_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total number of non-terminated pods targeted by this deployment that have the desired template spec.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Deployment<wbr>Strategy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#DeploymentStrategy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#DeploymentStrategy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentStrategyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#DeploymentStrategyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rollingupdatedeployment">Rolling<wbr>Update<wbr>Deployment<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rollingupdatedeployment">*Rolling<wbr>Update<wbr>Deployment</a></span>
    </dt>
    <dd>{{% md %}}Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rollingupdatedeployment">Rolling<wbr>Update<wbr>Deployment?</a></span>
    </dt>
    <dd>{{% md %}}Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>rolling_<wbr>update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rollingupdatedeployment">Dict[Rolling<wbr>Update<wbr>Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.{{% /md %}}</dd>

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
        <span class="property-type"><a href="#downwardapivolumefile">List&lt;Downward<wbr>APIVolume<wbr>File<wbr>Args&gt;?</a></span>
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
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#downwardapivolumefile">List&lt;Downward<wbr>APIVolume<wbr>File<wbr>Args&gt;?</a></span>
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
        <span class="property-type"><a href="#configmapenvsource">Config<wbr>Map<wbr>Env<wbr>Source<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#secretenvsource">Secret<wbr>Env<wbr>Source<wbr>Args?</a></span>
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
        <span>secret_<wbr>ref</span>
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
        <span class="property-type"><a href="#envvarsource">Env<wbr>Var<wbr>Source<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#configmapkeyselector">Config<wbr>Map<wbr>Key<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a key of a ConfigMap.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectfieldselector">Object<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Field<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcefieldselector">Resource<wbr>Field<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Key<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretkeyselector">Secret<wbr>Key<wbr>Selector<wbr>Args?</a></span>
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





<h4>Ephemeral<wbr>Container</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#EphemeralContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#EphemeralContainer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EphemeralContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#EphemeralContainerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List&lt;Env<wbr>Var<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List&lt;Env<wbr>From<wbr>Source<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Lifecycle is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">List&lt;Container<wbr>Port<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Ports are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">List&lt;Volume<wbr>Device<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List&lt;Volume<wbr>Mount<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle</a></span>
    </dt>
    <dd>{{% md %}}Lifecycle is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">Container<wbr>Port</a></span>
    </dt>
    <dd>{{% md %}}Ports are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements</a></span>
    </dt>
    <dd>{{% md %}}Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">Volume<wbr>Device</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">Env<wbr>Var[]?</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">Env<wbr>From<wbr>Source[]?</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Lifecycle?</a></span>
    </dt>
    <dd>{{% md %}}Lifecycle is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">Container<wbr>Port[]?</a></span>
    </dt>
    <dd>{{% md %}}Ports are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Resource<wbr>Requirements?</a></span>
    </dt>
    <dd>{{% md %}}Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Security<wbr>Context?</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Probe?</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">Volume<wbr>Device[]?</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">Volume<wbr>Mount[]?</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envvar">List[Env<wbr>Var]</a></span>
    </dt>
    <dd>{{% md %}}List of environment variables to set in the container. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#envfromsource">List[Env<wbr>From<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Pull<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#lifecycle">Dict[Lifecycle]</a></span>
    </dt>
    <dd>{{% md %}}Lifecycle is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#containerport">List[Container<wbr>Port]</a></span>
    </dt>
    <dd>{{% md %}}Ports are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcerequirements">Dict[Resource<wbr>Requirements]</a></span>
    </dt>
    <dd>{{% md %}}Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#securitycontext">Dict[Security<wbr>Context]</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext is not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>startup<wbr>Probe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#probe">Dict[Probe]</a></span>
    </dt>
    <dd>{{% md %}}Probes are not allowed for ephemeral containers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stdin<wbr>Once</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Message<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumedevice">List[Volume<wbr>Device]</a></span>
    </dt>
    <dd>{{% md %}}volumeDevices is the list of block devices to be used by the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>mounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volumemount">List[Volume<wbr>Mount]</a></span>
    </dt>
    <dd>{{% md %}}Pod volumes to mount into the container's filesystem. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>working<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Exec<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ExecAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ExecAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ExecActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ExecActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Command</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>command</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.{{% /md %}}</dd>

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
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Optional: FC target worldwide names (WWNs){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wwids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span>fs_<wbr>type</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>ww_<wbr>ns</span>
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
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>fs_<wbr>type</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
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
        <span>dataset_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset_<wbr>uuid</span>
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
        <span>fs_<wbr>type</span>
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
        <span>pd_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>HTTPGet<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#HTTPGetAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HTTPGetAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HTTPGetActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HTTPGetActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpheader">List&lt;HTTPHeader<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Custom headers to set in the request. HTTP allows repeated headers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to access on the HTTP server.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">Union&lt;double, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scheme to use for connecting to the host. Defaults to HTTP.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpheader">HTTPHeader</a></span>
    </dt>
    <dd>{{% md %}}Custom headers to set in the request. HTTP allows repeated headers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path to access on the HTTP server.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Scheme to use for connecting to the host. Defaults to HTTP.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpheader">HTTPHeader[]?</a></span>
    </dt>
    <dd>{{% md %}}Custom headers to set in the request. HTTP allows repeated headers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to access on the HTTP server.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number | string</span>
    </dt>
    <dd>{{% md %}}Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scheme to use for connecting to the host. Defaults to HTTP.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpheader">List[HTTPHeader]</a></span>
    </dt>
    <dd>{{% md %}}Custom headers to set in the request. HTTP allows repeated headers.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path to access on the HTTP server.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scheme to use for connecting to the host. Defaults to HTTP.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>HTTPHeader</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#HTTPHeader">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HTTPHeader">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HTTPHeaderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HTTPHeaderOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The header field name{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The header field value{{% /md %}}</dd>

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
    <dd>{{% md %}}The header field name{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The header field value{{% /md %}}</dd>

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
    <dd>{{% md %}}The header field name{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The header field value{{% /md %}}</dd>

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
    <dd>{{% md %}}The header field name{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The header field value{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Handler</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Handler">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Handler">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HandlerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HandlerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Dict[Exec<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">Dict[HTTPGet<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">Dict[TCPSocket<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Host<wbr>Alias</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#HostAlias">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HostAlias">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HostAliasArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#HostAliasOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Hostnames for the above IP address.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the host file entry.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Hostnames for the above IP address.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address of the host file entry.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Hostnames for the above IP address.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the host file entry.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Hostnames for the above IP address.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the host file entry.{{% /md %}}</dd>

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
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>chap_<wbr>auth_<wbr>discovery</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Discovery CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chap_<wbr>auth_<wbr>session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether support iSCSI Session CHAP authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initiator_<wbr>name</span>
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
        <span>iscsi_<wbr>interface</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}CHAP Secret for iSCSI target and initiator authentication{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>portal</span>
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
        <span class="property-type"><a href="#labelselectorrequirement">List&lt;Label<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
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
        <span>match_<wbr>expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">List[Label<wbr>Selector<wbr>Requirement]</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>labels</span>
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
        <span class="property-type">List&lt;string&gt;?</span>
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





<h4>Lifecycle</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Lifecycle">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Lifecycle">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LifecycleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#LifecycleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pre<wbr>Stop</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler</a></span>
    </dt>
    <dd>{{% md %}}PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pre<wbr>Stop</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler</a></span>
    </dt>
    <dd>{{% md %}}PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>post<wbr>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler?</a></span>
    </dt>
    <dd>{{% md %}}PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pre<wbr>Stop</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Handler?</a></span>
    </dt>
    <dd>{{% md %}}PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>post<wbr>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Dict[Handler]</a></span>
    </dt>
    <dd>{{% md %}}PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pre<wbr>Stop</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#handler">Dict[Handler]</a></span>
    </dt>
    <dd>{{% md %}}PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks{{% /md %}}</dd>

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
        <span>continue_</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remaining_<wbr>item_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
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
        <span>Fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;?</span>
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
        <span>read_<wbr>only</span>
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





<h4>Node<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#NodeAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#NodeAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#NodeAffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#preferredschedulingterm">List&lt;Preferred<wbr>Scheduling<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Node<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#preferredschedulingterm">Preferred<wbr>Scheduling<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Node<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#preferredschedulingterm">Preferred<wbr>Scheduling<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Node<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#preferredschedulingterm">List[Preferred<wbr>Scheduling<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselector">Dict[Node<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.{{% /md %}}</dd>

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
        <span class="property-type"><a href="#nodeselectorterm">List&lt;Node<wbr>Selector<wbr>Term<wbr>Args&gt;?</a></span>
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
        <span>node_<wbr>selector_<wbr>terms</span>
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
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span class="property-type"><a href="#nodeselectorrequirement">List&lt;Node<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of node selector requirements by node's labels.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorrequirement">List&lt;Node<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
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
        <span>match_<wbr>expressions</span>
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
        <span>field_<wbr>path</span>
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
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
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
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">List&lt;Managed<wbr>Fields<wbr>Entry<wbr>Args&gt;?</a></span>
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
        <span class="property-type"><a href="#ownerreference">List&lt;Owner<wbr>Reference<wbr>Args&gt;?</a></span>
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
        <span>cluster_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>grace_<wbr>period_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>timestamp</span>
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
        <span>generate_<wbr>name</span>
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
        <span>managed_<wbr>fields</span>
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
        <span>owner_<wbr>references</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">List[Owner<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
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
        <span>read_<wbr>only</span>
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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pd_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID that identifies Photon Controller persistent disk{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">List&lt;Weighted<wbr>Pod<wbr>Affinity<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">List&lt;Pod<wbr>Affinity<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">Weighted<wbr>Pod<wbr>Affinity<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">Weighted<wbr>Pod<wbr>Affinity<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">List[Weighted<wbr>Pod<wbr>Affinity<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">List[Pod<wbr>Affinity<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Affinity<wbr>Term</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodAffinityTerm">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodAffinityTerm">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAffinityTermArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAffinityTermOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A label query over a set of resources, in this case pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}A label query over a set of resources, in this case pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}A label query over a set of resources, in this case pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}A label query over a set of resources, in this case pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Anti<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodAntiAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodAntiAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAntiAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodAntiAffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">List&lt;Weighted<wbr>Pod<wbr>Affinity<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">List&lt;Pod<wbr>Affinity<wbr>Term<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">Weighted<wbr>Pod<wbr>Affinity<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">Weighted<wbr>Pod<wbr>Affinity<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required<wbr>During<wbr>Scheduling<wbr>Ignored<wbr>During<wbr>Execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term[]?</a></span>
    </dt>
    <dd>{{% md %}}If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#weightedpodaffinityterm">List[Weighted<wbr>Pod<wbr>Affinity<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>required_<wbr>during_<wbr>scheduling_<wbr>ignored_<wbr>during_<wbr>execution</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">List[Pod<wbr>Affinity<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>DNSConfig</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodDNSConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodDNSConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodDNSConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodDNSConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfigoption">List&lt;Pod<wbr>DNSConfig<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfigoption">Pod<wbr>DNSConfig<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfigoption">Pod<wbr>DNSConfig<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfigoption">List[Pod<wbr>DNSConfig<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>DNSConfig<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodDNSConfigOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodDNSConfigOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodDNSConfigOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodDNSConfigOptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Required.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Readiness<wbr>Gate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodReadinessGate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodReadinessGate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodReadinessGateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodReadinessGateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ConditionType refers to a condition in the pod's condition list with matching type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ConditionType refers to a condition in the pod's condition list with matching type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ConditionType refers to a condition in the pod's condition list with matching type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ConditionType refers to a condition in the pod's condition list with matching type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Security<wbr>Context</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodSecurityContext">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodSecurityContext">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodSecurityContextArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodSecurityContextOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Group<wbr>Change<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified defaults to "Always".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplemental<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;int&gt;?</span>
    </dt>
    <dd>{{% md %}}A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sysctls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sysctl">List&lt;Sysctl<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fs<wbr>Group<wbr>Change<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified defaults to "Always".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplemental<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]int</span>
    </dt>
    <dd>{{% md %}}A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sysctls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sysctl">Sysctl</a></span>
    </dt>
    <dd>{{% md %}}Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs<wbr>Group<wbr>Change<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified defaults to "Always".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplemental<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">number[]?</span>
    </dt>
    <dd>{{% md %}}A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sysctls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sysctl">Sysctl[]?</a></span>
    </dt>
    <dd>{{% md %}}Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fs_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fs_<wbr>group_<wbr>change_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified defaults to "Always".{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>non_<wbr>root</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>se_<wbr>linux_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">Dict[SELinux<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplemental_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[Integer]</span>
    </dt>
    <dd>{{% md %}}A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sysctls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sysctl">List[Sysctl]</a></span>
    </dt>
    <dd>{{% md %}}Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Dict[Windows<wbr>Security<wbr>Context<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#affinity">Affinity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's scheduling constraints{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automount<wbr>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">List&lt;Container<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfig">Pod<wbr>DNSConfig<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Service<wbr>Links</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ephemeral<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ephemeralcontainer">List&lt;Ephemeral<wbr>Container<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostalias">List&lt;Host<wbr>Alias<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>IPC</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Use the host's ipc namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>PID</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Use the host's pid namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">List&lt;Local<wbr>Object<wbr>Reference<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Init<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">List&lt;Container<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overhead</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemption<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Gates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podreadinessgate">List&lt;Pod<wbr>Readiness<wbr>Gate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restart<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduler<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsecuritycontext">Pod<wbr>Security<wbr>Context<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Process<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subdomain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tolerations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toleration">List&lt;Toleration<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's tolerations.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Spread<wbr>Constraints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#topologyspreadconstraint">List&lt;Topology<wbr>Spread<wbr>Constraint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is only honored by clusters that enable the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">List&lt;Volume<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#affinity">Affinity</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's scheduling constraints{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automount<wbr>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">Container</a></span>
    </dt>
    <dd>{{% md %}}List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfig">Pod<wbr>DNSConfig</a></span>
    </dt>
    <dd>{{% md %}}Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Service<wbr>Links</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ephemeral<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ephemeralcontainer">Ephemeral<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostalias">Host<wbr>Alias</a></span>
    </dt>
    <dd>{{% md %}}HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>IPC</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Use the host's ipc namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>PID</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Use the host's pid namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Pull<wbr>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Init<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">Container</a></span>
    </dt>
    <dd>{{% md %}}List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overhead</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemption<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Gates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podreadinessgate">Pod<wbr>Readiness<wbr>Gate</a></span>
    </dt>
    <dd>{{% md %}}If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restart<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduler<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsecuritycontext">Pod<wbr>Security<wbr>Context</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Process<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subdomain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Termination<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tolerations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toleration">Toleration</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's tolerations.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Spread<wbr>Constraints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#topologyspreadconstraint">Topology<wbr>Spread<wbr>Constraint</a></span>
    </dt>
    <dd>{{% md %}}TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is only honored by clusters that enable the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">Volume</a></span>
    </dt>
    <dd>{{% md %}}List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#affinity">Affinity?</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's scheduling constraints{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automount<wbr>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">Container[]?</a></span>
    </dt>
    <dd>{{% md %}}List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfig">Pod<wbr>DNSConfig?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Service<wbr>Links</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ephemeral<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ephemeralcontainer">Ephemeral<wbr>Container[]?</a></span>
    </dt>
    <dd>{{% md %}}List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostalias">Host<wbr>Alias[]?</a></span>
    </dt>
    <dd>{{% md %}}HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>IPC</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Use the host's ipc namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>PID</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Use the host's pid namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Pull<wbr>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference[]?</a></span>
    </dt>
    <dd>{{% md %}}ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>init<wbr>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">Container[]?</a></span>
    </dt>
    <dd>{{% md %}}List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overhead</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemption<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Gates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podreadinessgate">Pod<wbr>Readiness<wbr>Gate[]?</a></span>
    </dt>
    <dd>{{% md %}}If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restart<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Class<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduler<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsecuritycontext">Pod<wbr>Security<wbr>Context?</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Process<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subdomain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tolerations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toleration">Toleration[]?</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's tolerations.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology<wbr>Spread<wbr>Constraints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#topologyspreadconstraint">Topology<wbr>Spread<wbr>Constraint[]?</a></span>
    </dt>
    <dd>{{% md %}}TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is only honored by clusters that enable the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">Volume[]?</a></span>
    </dt>
    <dd>{{% md %}}List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>deadline_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#affinity">Dict[Affinity]</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's scheduling constraints{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automount_<wbr>service_<wbr>account_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">List[Container]</a></span>
    </dt>
    <dd>{{% md %}}List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#poddnsconfig">Dict[Pod<wbr>DNSConfig]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>service_<wbr>links</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ephemeral_<wbr>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ephemeralcontainer">List[Ephemeral<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostalias">List[Host<wbr>Alias]</a></span>
    </dt>
    <dd>{{% md %}}HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>ipc</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Use the host's ipc namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>pid</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Use the host's pid namespace. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image_<wbr>pull_<wbr>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">List[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>init_<wbr>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#container">List[Container]</a></span>
    </dt>
    <dd>{{% md %}}List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overhead</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemption_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority_<wbr>class_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness_<wbr>gates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podreadinessgate">List[Pod<wbr>Readiness<wbr>Gate]</a></span>
    </dt>
    <dd>{{% md %}}If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restart_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>class_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduler_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsecuritycontext">Dict[Pod<wbr>Security<wbr>Context]</a></span>
    </dt>
    <dd>{{% md %}}SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>process_<wbr>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subdomain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>termination_<wbr>grace_<wbr>period_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tolerations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toleration">List[Toleration]</a></span>
    </dt>
    <dd>{{% md %}}If specified, the pod's tolerations.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology_<wbr>spread_<wbr>constraints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#topologyspreadconstraint">List[Topology<wbr>Spread<wbr>Constraint]</a></span>
    </dt>
    <dd>{{% md %}}TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is only honored by clusters that enable the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#volume">List[Volume]</a></span>
    </dt>
    <dd>{{% md %}}List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pod<wbr>Template<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodTemplateSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodTemplateSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodTemplateSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PodTemplateSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podspec">Pod<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podspec">Pod<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podspec">Pod<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podspec">Dict[Pod<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeID uniquely identifies a Portworx volume{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Preferred<wbr>Scheduling<wbr>Term</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PreferredSchedulingTerm">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PreferredSchedulingTerm">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PreferredSchedulingTermArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#PreferredSchedulingTermOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Node<wbr>Selector<wbr>Term<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A node selector term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Node<wbr>Selector<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}A node selector term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Node<wbr>Selector<wbr>Term?</a></span>
    </dt>
    <dd>{{% md %}}A node selector term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeselectorterm">Dict[Node<wbr>Selector<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}A node selector term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Probe</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Probe">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Probe">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ProbeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ProbeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Delay<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Delay<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Exec<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">HTTPGet<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Delay<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">TCPSocket<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#execaction">Dict[Exec<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}One and only one of the following should be specified. Exec specifies the action to take.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Get</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#httpgetaction">Dict[HTTPGet<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}HTTPGet specifies the http request to perform.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Delay<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tcpsocketaction">Dict[TCPSocket<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes{{% /md %}}</dd>

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
        <span class="property-type"><a href="#volumeprojection">List&lt;Volume<wbr>Projection<wbr>Args&gt;?</a></span>
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
        <span>read_<wbr>only</span>
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
        <span class="property-type">List&lt;string&gt;?</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>fs_<wbr>type</span>
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
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
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





<h4>Resource<wbr>Requirements</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ResourceRequirements">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ResourceRequirements">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ResourceRequirementsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#ResourceRequirementsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Rolling<wbr>Update<wbr>Deployment</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#RollingUpdateDeployment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#RollingUpdateDeployment">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#RollingUpdateDeploymentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/apps/v1?tab=doc#RollingUpdateDeploymentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">Union&lt;double, string&gt;?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">Union&lt;double, string&gt;?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">number | string</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">number | string</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>SELinux<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SELinuxOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SELinuxOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SELinuxOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SELinuxOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Level is SELinux level label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role is a SELinux role label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type is a SELinux type label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User is a SELinux user label that applies to the container.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Level is SELinux level label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Role is a SELinux role label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type is a SELinux type label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User is a SELinux user label that applies to the container.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Level is SELinux level label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role is a SELinux role label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type is a SELinux type label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User is a SELinux user label that applies to the container.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Level is SELinux level label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role is a SELinux role label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type is a SELinux type label that applies to the container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User is a SELinux user label that applies to the container.{{% /md %}}</dd>

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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>fs_<wbr>type</span>
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
        <span>protection_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the ScaleIO Protection Domain for the configured storage.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to enable/disable SSL communication with Gateway, default false{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>pool</span>
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
        <span>volume_<wbr>name</span>
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
        <span class="property-type"><a href="#keytopath">List&lt;Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
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
        <span class="property-type"><a href="#keytopath">List&lt;Key<wbr>To<wbr>Path<wbr>Args&gt;?</a></span>
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
        <span>secret_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Security<wbr>Context</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#SecurityContext">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#SecurityContext">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecurityContextArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SecurityContextOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Privilege<wbr>Escalation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#capabilities">Capabilities<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Privileged</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proc<wbr>Mount</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only<wbr>Root<wbr>Filesystem</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether this container has a read-only root filesystem. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Privilege<wbr>Escalation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#capabilities">Capabilities</a></span>
    </dt>
    <dd>{{% md %}}The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Privileged</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proc<wbr>Mount</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Read<wbr>Only<wbr>Root<wbr>Filesystem</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether this container has a read-only root filesystem. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Privilege<wbr>Escalation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#capabilities">Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>privileged</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proc<wbr>Mount</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read<wbr>Only<wbr>Root<wbr>Filesystem</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether this container has a read-only root filesystem. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>Non<wbr>Root</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>se<wbr>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">SELinux<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Windows<wbr>Security<wbr>Context<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>privilege_<wbr>escalation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#capabilities">Dict[Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>privileged</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proc<wbr>Mount</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only_<wbr>root_<wbr>filesystem</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether this container has a read-only root filesystem. Default is false.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>non_<wbr>root</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>user</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>se_<wbr>linux_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#selinuxoptions">Dict[SELinux<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowssecuritycontextoptions">Dict[Windows<wbr>Security<wbr>Context<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

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
        <span>expiration_<wbr>seconds</span>
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
        <span class="property-type"><a href="#localobjectreference">Local<wbr>Object<wbr>Reference<wbr>Args?</a></span>
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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>read_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#localobjectreference">Dict[Local<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Sysctl</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Sysctl">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Sysctl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SysctlArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#SysctlOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of a property to set{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Value of a property to set{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of a property to set{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Value of a property to set{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of a property to set{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Value of a property to set{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of a property to set{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value of a property to set{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>TCPSocket<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#TCPSocketAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#TCPSocketAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TCPSocketActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TCPSocketActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Host name to connect to, defaults to the pod IP.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">Union&lt;double, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional: Host name to connect to, defaults to the pod IP.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional: Host name to connect to, defaults to the pod IP.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number | string</span>
    </dt>
    <dd>{{% md %}}Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional: Host name to connect to, defaults to the pod IP.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Toleration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Toleration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#Toleration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TolerationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TolerationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Toleration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Toleration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>toleration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>toleration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Topology<wbr>Spread<wbr>Constraint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#TopologySpreadConstraint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#TopologySpreadConstraint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TopologySpreadConstraintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#TopologySpreadConstraintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Skew</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>When<wbr>Unsatisfiable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as "Unsatisfiable" if and only if placing incoming pod on any topology violates "MaxSkew". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Skew</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>When<wbr>Unsatisfiable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as "Unsatisfiable" if and only if placing incoming pod on any topology violates "MaxSkew". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Skew</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>when<wbr>Unsatisfiable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as "Unsatisfiable" if and only if placing incoming pod on any topology violates "MaxSkew". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Skew</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topology<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>when<wbr>Unsatisfiable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as "Unsatisfiable" if and only if placing incoming pod on any topology violates "MaxSkew". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.{{% /md %}}</dd>

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
        <span class="property-type"><a href="#awselasticblockstorevolumesource">AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Azure<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurefilevolumesource">Azure<wbr>File<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AzureFile represents an Azure File Service mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cephfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cephfsvolumesource">Ceph<wbr>FSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CephFS represents a Ceph FS mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cinder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cindervolumesource">Cinder<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configmapvolumesource">Config<wbr>Map<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ConfigMap represents a configMap that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#csivolumesource">CSIVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapivolumesource">Downward<wbr>APIVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DownwardAPI represents downward API about the pod that should populate this volume{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Empty<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#emptydirvolumesource">Empty<wbr>Dir<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fcvolumesource">FCVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flex<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexvolumesource">Flex<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Flocker</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flockervolumesource">Flocker<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gcepersistentdiskvolumesource">GCEPersistent<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Git<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gitrepovolumesource">Git<wbr>Repo<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Glusterfs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#glusterfsvolumesource">Glusterfs<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hostpathvolumesource">Host<wbr>Path<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#iscsivolumesource">ISCSIVolume<wbr>Source<wbr>Args?</a></span>
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
        <span class="property-type"><a href="#nfsvolumesource">NFSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistent<wbr>Volume<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#persistentvolumeclaimvolumesource">Persistent<wbr>Volume<wbr>Claim<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Photon<wbr>Persistent<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portworx<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#portworxvolumesource">Portworx<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}PortworxVolume represents a portworx volume attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Projected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectedvolumesource">Projected<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Items for all in one resources secrets, configmaps, and downward API{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quobyte</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#quobytevolumesource">Quobyte<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Quobyte represents a Quobyte mount on the host that shares a pod's lifetime{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rbd</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#rbdvolumesource">RBDVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>IO</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scaleiovolumesource">Scale<wbr>IOVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretvolumesource">Secret<wbr>Volume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storageos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#storageosvolumesource">Storage<wbr>OSVolume<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source<wbr>Args?</a></span>
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
        <span>aws_<wbr>elastic_<wbr>block_<wbr>store</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#awselasticblockstorevolumesource">Dict[AWSElastic<wbr>Block<wbr>Store<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#azurediskvolumesource">Dict[Azure<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>file</span>
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
        <span>config_<wbr>map</span>
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
        <span>flex_<wbr>volume</span>
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
        <span>gce_<wbr>persistent_<wbr>disk</span>
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
        <span>host_<wbr>path</span>
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
        <span>photon_<wbr>persistent_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#photonpersistentdiskvolumesource">Dict[Photon<wbr>Persistent<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portworx_<wbr>volume</span>
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
        <span>scale_<wbr>io</span>
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
        <span>vsphere_<wbr>volume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vspherevirtualdiskvolumesource">Dict[Vsphere<wbr>Virtual<wbr>Disk<wbr>Volume<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Volume<wbr>Device</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#VolumeDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#VolumeDevice">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#VolumeDeviceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}devicePath is the path inside of the container that the device will be mapped to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name must match the name of a persistentVolumeClaim in the pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}devicePath is the path inside of the container that the device will be mapped to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}name must match the name of a persistentVolumeClaim in the pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}devicePath is the path inside of the container that the device will be mapped to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name must match the name of a persistentVolumeClaim in the pod{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}devicePath is the path inside of the container that the device will be mapped to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name must match the name of a persistentVolumeClaim in the pod{{% /md %}}</dd>

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
        <span>read_<wbr>only</span>
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
        <span class="property-type"><a href="#configmapprojection">Config<wbr>Map<wbr>Projection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the configMap data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Downward<wbr>API</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#downwardapiprojection">Downward<wbr>APIProjection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the downwardAPI data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#secretprojection">Secret<wbr>Projection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}information about the secret data to project{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#serviceaccounttokenprojection">Service<wbr>Account<wbr>Token<wbr>Projection<wbr>Args?</a></span>
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
        <span>config_<wbr>map</span>
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
        <span>fs_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>policy_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Storage Policy Based Management (SPBM) profile name.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volume_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path that identifies vSphere volume vmdk{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Weighted<wbr>Pod<wbr>Affinity<wbr>Term</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#WeightedPodAffinityTerm">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#WeightedPodAffinityTerm">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#WeightedPodAffinityTermArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#WeightedPodAffinityTermOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Affinity<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Required. A pod affinity term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}weight associated with matching the corresponding podAffinityTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Affinity<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term</a></span>
    </dt>
    <dd>{{% md %}}Required. A pod affinity term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}weight associated with matching the corresponding podAffinityTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Affinity<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Pod<wbr>Affinity<wbr>Term?</a></span>
    </dt>
    <dd>{{% md %}}Required. A pod affinity term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}weight associated with matching the corresponding podAffinityTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Affinity<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podaffinityterm">Dict[Pod<wbr>Affinity<wbr>Term]</a></span>
    </dt>
    <dd>{{% md %}}Required. A pod affinity term, associated with the corresponding weight.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}weight associated with matching the corresponding podAffinityTerm, in the range 1-100.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Security<wbr>Context<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#WindowsSecurityContextOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#WindowsSecurityContextOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#WindowsSecurityContextOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/core/v1?tab=doc#WindowsSecurityContextOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Gmsa<wbr>Credential<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gmsa<wbr>Credential<wbr>Spec<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpecName is the name of the GMSA credential spec to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Gmsa<wbr>Credential<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gmsa<wbr>Credential<wbr>Spec<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpecName is the name of the GMSA credential spec to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>As<wbr>User<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>gmsa<wbr>Credential<wbr>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gmsa<wbr>Credential<wbr>Spec<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpecName is the name of the GMSA credential spec to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>As<wbr>User<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>gmsa_<wbr>credential_<wbr>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gmsa_<wbr>credential_<wbr>spec_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}GMSACredentialSpecName is the name of the GMSA credential spec to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>as_<wbr>user_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-kubernetes">https://github.com/pulumi/pulumi-kubernetes</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

