
---
title: "NasDatastore"
block_external_search_index: true
---



The `vsphere..NasDatastore` resource can be used to create and manage NAS
datastores on an ESXi host or a set of hosts. The resource supports mounting
NFS v3 and v4.1 shares to be used as datastores.

> **NOTE:** Unlike [`vsphere..VmfsDatastore`][resource-vmfs-datastore], a NAS
datastore is only mounted on the hosts you choose to mount it on. To mount on
multiple hosts, you must specify each host that you want to add in the
`host_system_ids` argument.

[resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html

> This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/nas_datastore.html.markdown.



## Create a NasDatastore Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#NasDatastore">NasDatastore</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#NasDatastoreArgs">NasDatastoreArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NasDatastore</span><span class="p">(resource_name, opts=None, </span>access_mode=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datastore_cluster_id=None<span class="p">, </span>folder=None<span class="p">, </span>host_system_ids=None<span class="p">, </span>name=None<span class="p">, </span>remote_hosts=None<span class="p">, </span>remote_path=None<span class="p">, </span>security_type=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNasDatastore<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#NasDatastoreArgs">NasDatastoreArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#NasDatastore">NasDatastore</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..NasDatastore.html">NasDatastore</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.NasDatastoreArgs.html">NasDatastoreArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>system_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote_<wbr>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## NasDatastore Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>free_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host_<wbr>system_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintenance_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multiple_<wbr>host_<wbr>access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remote_<wbr>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remote_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uncommitted_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing NasDatastore Resource

Get an existing NasDatastore resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#NasDatastoreState">NasDatastoreState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#NasDatastore">NasDatastore</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>access_mode=None<span class="p">, </span>accessible=None<span class="p">, </span>capacity=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datastore_cluster_id=None<span class="p">, </span>folder=None<span class="p">, </span>free_space=None<span class="p">, </span>host_system_ids=None<span class="p">, </span>maintenance_mode=None<span class="p">, </span>multiple_host_access=None<span class="p">, </span>name=None<span class="p">, </span>protocol_endpoint=None<span class="p">, </span>remote_hosts=None<span class="p">, </span>remote_path=None<span class="p">, </span>security_type=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>uncommitted_space=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNasDatastore<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#NasDatastoreState">NasDatastoreState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#NasDatastore">NasDatastore</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..NasDatastore.html">NasDatastore</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..NasDatastoreState.html">NasDatastoreState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>free<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>System<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multiple<wbr>Host<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uncommitted<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum capacity of the datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute 
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the datastore folder to put the datastore in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>free_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Available space of this datastore, in megabytes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>system_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current maintenance mode state of the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multiple_<wbr>host_<wbr>access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, more than one host in the datacenter has
been configured with access to the datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the datastore. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote_<wbr>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The remote path of the mount point. Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uncommitted_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique locator for the datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vsphere">https://github.com/pulumi/pulumi-vsphere</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

