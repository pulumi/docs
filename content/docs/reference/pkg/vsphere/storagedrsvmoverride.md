
---
title: "StorageDrsVmOverride"
block_external_search_index: true
---



The `vsphere..StorageDrsVmOverride` resource can be used to add a Storage DRS
override to a datastore cluster for a specific virtual machine. With this
resource, one can enable or disable Storage DRS, and control the automation
level and disk affinity for a single virtual machine without affecting the rest
of the datastore cluster.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

{{% examples %}}
## Example Usage
{{% example %}}

The example below builds on the [Storage DRS
example][tf-vsphere-vm-storage-drs-example] in the `vsphere..VirtualMachine`
resource. However, rather than use the output of the
[`vsphere..DatastoreCluster` data
source][tf-vsphere-datastore-cluster-data-source] for the location of the
virtual machine, we instead get what is assumed to be a member datastore using
the [`vsphere..getDatastore` data source][tf-vsphere-datastore-data-source] and put
the virtual machine there instead. We then use the
`vsphere..StorageDrsVmOverride` resource to ensure that Storage DRS does not
apply to this virtual machine, and hence the VM will never be migrated off of
the datastore.

[tf-vsphere-vm-storage-drs-example]: /docs/providers/vsphere/r/virtual_machine.html#using-storage-drs
[tf-vsphere-datastore-cluster-data-source]: /docs/providers/vsphere/d/datastore_cluster.html
[tf-vsphere-datastore-data-source]: /docs/providers/vsphere/d/datastore.html

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as vsphere from "@pulumi/vsphere";

const dc = vsphere.getDatacenter({
    name: "dc1",
});
const datastoreCluster = vsphere.getDatastoreCluster({
    datacenterId: dc.id,
    name: "datastore-cluster1",
});
const memberDatastore = vsphere.getDatastore({
    datacenterId: dc.id,
    name: "datastore-cluster1-member1",
});
const pool = vsphere.getResourcePool({
    datacenterId: dc.id,
    name: "cluster1/Resources",
});
const network = vsphere.getNetwork({
    datacenterId: dc.id,
    name: "public",
});
const vm = new vsphere.VirtualMachine("vm", {
    datastoreId: memberDatastore.id,
    disks: [{
        label: "disk0",
        size: 20,
    }],
    guestId: "other3xLinux64Guest",
    memory: 1024,
    networkInterfaces: [{
        networkId: network.id,
    }],
    numCpus: 2,
    resourcePoolId: pool.id,
});
const drsVmOverride = new vsphere.StorageDrsVmOverride("drs_vm_override", {
    datastoreClusterId: datastoreCluster.id,
    sdrsEnabled: "false",
    virtualMachineId: vm.id,
});
```

{{% /example %}}
{{% /examples %}}



## Create a StorageDrsVmOverride Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#StorageDrsVmOverride">StorageDrsVmOverride</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#StorageDrsVmOverrideArgs">StorageDrsVmOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">StorageDrsVmOverride</span><span class="p">(resource_name, opts=None, </span>datastore_cluster_id=None<span class="p">, </span>sdrs_automation_level=None<span class="p">, </span>sdrs_enabled=None<span class="p">, </span>sdrs_intra_vm_affinity=None<span class="p">, </span>virtual_machine_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewStorageDrsVmOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#StorageDrsVmOverrideArgs">StorageDrsVmOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#StorageDrsVmOverride">StorageDrsVmOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.StorageDrsVmOverride.html">StorageDrsVmOverride</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.StorageDrsVmOverrideArgs.html">StorageDrsVmOverrideArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>automation_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>intra_<wbr>vm_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing StorageDrsVmOverride Resource

Get an existing StorageDrsVmOverride resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#StorageDrsVmOverrideState">StorageDrsVmOverrideState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#StorageDrsVmOverride">StorageDrsVmOverride</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>datastore_cluster_id=None<span class="p">, </span>sdrs_automation_level=None<span class="p">, </span>sdrs_enabled=None<span class="p">, </span>sdrs_intra_vm_affinity=None<span class="p">, </span>virtual_machine_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetStorageDrsVmOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#StorageDrsVmOverrideState">StorageDrsVmOverrideState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#StorageDrsVmOverride">StorageDrsVmOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.StorageDrsVmOverride.html">StorageDrsVmOverride</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..StorageDrsVmOverrideState.html">StorageDrsVmOverrideState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Automation<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs<wbr>Intra<wbr>Vm<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>automation_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sdrs_<wbr>intra_<wbr>vm_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vsphere">https://github.com/pulumi/pulumi-vsphere</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`vsphere` Terraform Provider](https://github.com/terraform-providers/terraform-provider-vsphere).</dd>
</dl>

