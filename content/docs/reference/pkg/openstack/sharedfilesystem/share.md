
---
title: "Share"
block_external_search_index: true
---



Use this resource to configure a share.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const network1 = new openstack.networking.Network("network_1", {
    adminStateUp: true,
});
const subnet1 = new openstack.networking.Subnet("subnet_1", {
    cidr: "192.168.199.0/24",
    ipVersion: 4,
    networkId: network1.id,
});
const sharenetwork1 = new openstack.sharedfilesystem.ShareNetwork("sharenetwork_1", {
    description: "test share network with security services",
    neutronNetId: network1.id,
    neutronSubnetId: subnet1.id,
});
const share1 = new openstack.sharedfilesystem.Share("share_1", {
    description: "test share description",
    shareNetworkId: sharenetwork1.id,
    shareProto: "NFS",
    size: 1,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_share_v2.html.markdown.



## Create a Share Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/sharedfilesystem/#Share">Share</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/sharedfilesystem/#ShareArgs">ShareArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Share</span><span class="p">(resource_name, opts=None, </span>availability_zone=None<span class="p">, </span>description=None<span class="p">, </span>is_public=None<span class="p">, </span>metadata=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>share_network_id=None<span class="p">, </span>share_proto=None<span class="p">, </span>share_type=None<span class="p">, </span>size=None<span class="p">, </span>snapshot_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewShare<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/sharedfilesystem?tab=doc#ShareArgs">ShareArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/sharedfilesystem?tab=doc#Share">Share</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Sharedfilesystem.Share.html">Share</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.SharedFileSystem.ShareArgs.html">ShareArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is_<wbr>public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>share_<wbr>proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Share Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">List&lt;Share<wbr>Export<wbr>Location&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">[]Share<wbr>Export<wbr>Location</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>all<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">Share<wbr>Export<wbr>Location[]</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>all_<wbr>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>export_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">List[Share<wbr>Export<wbr>Location]</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>has_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is_<wbr>public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replication_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share_<wbr>proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share_<wbr>server_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>share_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Share Resource

Get an existing Share resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/sharedfilesystem/#ShareState">ShareState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/sharedfilesystem/#Share">Share</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>all_metadata=None<span class="p">, </span>availability_zone=None<span class="p">, </span>description=None<span class="p">, </span>export_locations=None<span class="p">, </span>has_replicas=None<span class="p">, </span>host=None<span class="p">, </span>is_public=None<span class="p">, </span>metadata=None<span class="p">, </span>name=None<span class="p">, </span>project_id=None<span class="p">, </span>region=None<span class="p">, </span>replication_type=None<span class="p">, </span>share_network_id=None<span class="p">, </span>share_proto=None<span class="p">, </span>share_server_id=None<span class="p">, </span>share_type=None<span class="p">, </span>size=None<span class="p">, </span>snapshot_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetShare<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/sharedfilesystem?tab=doc#ShareState">ShareState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/sharedfilesystem?tab=doc#Share">Share</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Sharedfilesystem.Share.html">Share</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Sharedfilesystem.ShareState.html">ShareState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>All<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">List&lt;Share<wbr>Export<wbr>Location<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">[]Share<wbr>Export<wbr>Location</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>export<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">Share<wbr>Export<wbr>Location[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>has<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all_<wbr>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the share, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share availability zone. Changing this creates a
new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the share.
Changing this updates the description of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>export_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#shareexportlocation">List[Share<wbr>Export<wbr>Location]</a></span>
    </dt>
    <dd>{{% md %}}A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>has_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether a share has replicas or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share host name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is_<wbr>public</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}One or more metadata key and value pairs as a dictionary of
strings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the share. Changing this updates the name
of the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the Share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replication_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share replication type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of a share network where the share server exists
or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
the share_network_id value from the snapshot is used. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>server_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the share server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>share_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The share type name. If you omit this parameter, the default
share type is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the share's base snapshot. Changing this creates
a new share.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Share<wbr>Export<wbr>Location</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#ShareExportLocation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/sharedfilesystem?tab=doc#ShareExportLocationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred</span>
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
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred</span>
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
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred</span>
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
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

