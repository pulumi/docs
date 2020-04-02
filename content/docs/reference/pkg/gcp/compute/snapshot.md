
---
title: "Snapshot"
block_external_search_index: true
---

Represents a Persistent Disk Snapshot resource.

Use snapshots to back up data from your persistent disks. Snapshots are
different from public images and custom images, which are used primarily
to create instances or configure instance templates. Snapshots are useful
for periodic backup of the data on your persistent disks. You can create
snapshots from persistent disks even while they are attached to running
instances.

Snapshots are incremental, so you can create regular snapshots on a
persistent disk faster and at a much lower cost than if you regularly
created a full image of the disk.


To get more information about Snapshot, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/snapshots)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/compute/docs/disks/create-snapshots)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown.



## Create a Snapshot Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Snapshot">Snapshot</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#SnapshotArgs">SnapshotArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Snapshot</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>snapshot_encryption_key=None<span class="p">, </span>source_disk=None<span class="p">, </span>source_disk_encryption_key=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSnapshot<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotArgs">SnapshotArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#Snapshot">Snapshot</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Snapshot.html">Snapshot</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.SnapshotArgs.html">SnapshotArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
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
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">*Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">*Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
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
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
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
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Dict[Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>disk_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Dict[Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Snapshot Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">*Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">*Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Dict[Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>disk_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Dict[Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>disk_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Snapshot Resource

Get an existing Snapshot resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#SnapshotState">SnapshotState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Snapshot">Snapshot</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>creation_timestamp=None<span class="p">, </span>description=None<span class="p">, </span>disk_size_gb=None<span class="p">, </span>label_fingerprint=None<span class="p">, </span>labels=None<span class="p">, </span>licenses=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, </span>snapshot_encryption_key=None<span class="p">, </span>snapshot_id=None<span class="p">, </span>source_disk=None<span class="p">, </span>source_disk_encryption_key=None<span class="p">, </span>source_disk_link=None<span class="p">, </span>storage_bytes=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSnapshot<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotState">SnapshotState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#Snapshot">Snapshot</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Snapshot.html">Snapshot</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.SnapshotState.html">SnapshotState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">*Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">*Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Disk<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the snapshot, specified in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fingerprint used for optimistic locking of this resource. Used internally during updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Labels to apply to this Snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>licenses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsnapshotencryptionkey">Dict[Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the disk used to create this snapshot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>disk_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#snapshotsourcediskencryptionkey">Dict[Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a
customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>disk_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A size of the the storage used by the snapshot. As snapshots share storage, this number is expected to change with
snapshot creation/deletion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the zone where the disk is hosted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Snapshot<wbr>Snapshot<wbr>Encryption<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#SnapshotSnapshotEncryptionKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#SnapshotSnapshotEncryptionKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotSnapshotEncryptionKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotSnapshotEncryptionKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Raw<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Raw<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>raw<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>raw<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Snapshot<wbr>Source<wbr>Disk<wbr>Encryption<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#SnapshotSourceDiskEncryptionKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#SnapshotSourceDiskEncryptionKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotSourceDiskEncryptionKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#SnapshotSourceDiskEncryptionKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Raw<wbr>Key</span>
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
        <span>Raw<wbr>Key</span>
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
        <span>raw<wbr>Key</span>
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
        <span>raw<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
