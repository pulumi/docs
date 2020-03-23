
---
title: "Instance"
block_external_search_index: true
---

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).


## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const defaultInstance = new gcp.compute.Instance("default", {
    bootDisk: {
        initializeParams: {
            image: "debian-cloud/debian-9",
        },
    },
    machineType: "n1-standard-1",
    metadata: {
        foo: "bar",
    },
    metadataStartupScript: "echo hi > /test.txt",
    networkInterfaces: [{
        accessConfigs: [{}],
        network: "default",
    }],
    // Local SSD disk
    scratchDisks: [{
        interface: "SCSI",
    }],
    serviceAccount: {
        scopes: [
            "userinfo-email",
            "compute-ro",
            "storage-ro",
        ],
    },
    tags: [
        "foo",
        "bar",
    ],
    zone: "us-central1-a",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance.html.markdown.



## Create a Instance Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Instance">Instance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Instance</span><span class="p">(resource_name, opts=None, </span>allow_stopping_for_update=None<span class="p">, </span>attached_disks=None<span class="p">, </span>boot_disk=None<span class="p">, </span>can_ip_forward=None<span class="p">, </span>deletion_protection=None<span class="p">, </span>description=None<span class="p">, </span>desired_status=None<span class="p">, </span>enable_display=None<span class="p">, </span>guest_accelerators=None<span class="p">, </span>hostname=None<span class="p">, </span>labels=None<span class="p">, </span>machine_type=None<span class="p">, </span>metadata=None<span class="p">, </span>metadata_startup_script=None<span class="p">, </span>min_cpu_platform=None<span class="p">, </span>name=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>project=None<span class="p">, </span>scheduling=None<span class="p">, </span>scratch_disks=None<span class="p">, </span>service_account=None<span class="p">, </span>shielded_instance_config=None<span class="p">, </span>tags=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Instance.html">Instance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Inputs.InstanceArgs.html">InstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List&lt;Instance<wbr>Attached<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List&lt;Instance<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List&lt;Instance<wbr>Network<wbr>Interface<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List&lt;Instance<wbr>Scratch<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">[]Instance<wbr>Attached<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">[]Instance<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">[]Instance<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">*Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">[]Instance<wbr>Scratch<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">*Instance<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">*Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">Instance<wbr>Attached<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">Instance<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">Instance<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">Instance<wbr>Scratch<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>stopping_<wbr>for_<wbr>update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List[Instance<wbr>Attached<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>boot_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Dict[Instance<wbr>Boot<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List[Instance<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata_<wbr>startup_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List[Instance<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Dict[Instance<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scratch_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List[Instance<wbr>Scratch<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Dict[Instance<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Dict[Instance<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Instance Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List&lt;Instance<wbr>Attached<wbr>Disk&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List&lt;Instance<wbr>Guest<wbr>Accelerator&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List&lt;Instance<wbr>Network<wbr>Interface&gt;</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List&lt;Instance<wbr>Scratch<wbr>Disk&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">[]Instance<wbr>Attached<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">[]Instance<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">[]Instance<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">[]Instance<wbr>Scratch<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">*Instance<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">Instance<wbr>Attached<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">Instance<wbr>Guest<wbr>Accelerator[]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">Instance<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">Instance<wbr>Scratch<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow_<wbr>stopping_<wbr>for_<wbr>update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attached_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List[Instance<wbr>Attached<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Dict[Instance<wbr>Boot<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deletion_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List[Instance<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata_<wbr>startup_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List[Instance<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Dict[Instance<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scratch_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List[Instance<wbr>Scratch<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Dict[Instance<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Dict[Instance<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Instance Resource

Get an existing Instance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Instance">Instance</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allow_stopping_for_update=None<span class="p">, </span>attached_disks=None<span class="p">, </span>boot_disk=None<span class="p">, </span>can_ip_forward=None<span class="p">, </span>cpu_platform=None<span class="p">, </span>current_status=None<span class="p">, </span>deletion_protection=None<span class="p">, </span>description=None<span class="p">, </span>desired_status=None<span class="p">, </span>enable_display=None<span class="p">, </span>guest_accelerators=None<span class="p">, </span>hostname=None<span class="p">, </span>instance_id=None<span class="p">, </span>label_fingerprint=None<span class="p">, </span>labels=None<span class="p">, </span>machine_type=None<span class="p">, </span>metadata=None<span class="p">, </span>metadata_fingerprint=None<span class="p">, </span>metadata_startup_script=None<span class="p">, </span>min_cpu_platform=None<span class="p">, </span>name=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>project=None<span class="p">, </span>scheduling=None<span class="p">, </span>scratch_disks=None<span class="p">, </span>self_link=None<span class="p">, </span>service_account=None<span class="p">, </span>shielded_instance_config=None<span class="p">, </span>tags=None<span class="p">, </span>tags_fingerprint=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Instance.html">Instance</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InstanceState.html">InstanceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List&lt;Instance<wbr>Attached<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List&lt;Instance<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List&lt;Instance<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List&lt;Instance<wbr>Scratch<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">[]Instance<wbr>Attached<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">*Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">[]Instance<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">[]Instance<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">*Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">[]Instance<wbr>Scratch<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">*Instance<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">*Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">Instance<wbr>Attached<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Instance<wbr>Boot<wbr>Disk?</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">Instance<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">Instance<wbr>Network<wbr>Interface[]?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Instance<wbr>Scheduling?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">Instance<wbr>Scratch<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Instance<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Instance<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>stopping_<wbr>for_<wbr>update</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, allows this prvider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attached_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceattacheddisk">List[Instance<wbr>Attached<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdisk">Dict[Instance<wbr>Boot<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `pulumi destroy`), or the instance cannot be deleted and the provider run will not complete successfully.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceguestaccelerator">List[Instance<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with `on_host_maintenance` option set to TERMINATE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `a-z`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata_<wbr>startup_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `pulumi stack` commands, depending on your use case.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterface">List[Instance<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescheduling">Dict[Instance<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scratch_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancescratchdisk">List[Instance<wbr>Scratch<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.
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
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceserviceaccount">Dict[Instance<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance.
Structure is documented below.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceshieldedinstanceconfig">Dict[Instance<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
**Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone that the machine should be created in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Instance<wbr>Attached<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceAttachedDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceAttachedDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceAttachedDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceAttachedDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Boot<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceBootDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceBootDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceBootDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceBootDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdiskinitializeparams">Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Params<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Parameters for a new disk that will be created
alongside the new instance. Either `initialize_params` or `source` must be set.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdiskinitializeparams">*Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Params</a></span>
    </dt>
    <dd>{{% md %}}Parameters for a new disk that will be created
alongside the new instance. Either `initialize_params` or `source` must be set.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdiskinitializeparams">Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Params?</a></span>
    </dt>
    <dd>{{% md %}}Parameters for a new disk that will be created
alongside the new instance. Either `initialize_params` or `source` must be set.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancebootdiskinitializeparams">Dict[Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Params]</a></span>
    </dt>
    <dd>{{% md %}}Parameters for a new disk that will be created
alongside the new instance. Either `initialize_params` or `source` must be set.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk to attach to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Params</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceBootDiskInitializeParams">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceBootDiskInitializeParams">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceBootDiskInitializeParamsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceBootDiskInitializeParamsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[gcp.compute.Image data source](https://www.terraform.io/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[gcp.compute.Image data source](https://www.terraform.io/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[gcp.compute.Image data source](https://www.terraform.io/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[gcp.compute.Image data source](https://www.terraform.io/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A map of key/value label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceGuestAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceGuestAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceGuestAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfaceaccessconfig">List&lt;Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet. If omitted, ssh will not
work unless this provider can send traffic to the instance's network (e.g. via
tunnel or because it is running on another cloud instance on that network).
This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfacealiasiprange">List&lt;Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An
array of alias IP ranges for this network interface. Can only be specified for network
interfaces on subnet-mode networks. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The private IP address to assign to the instance. If
empty, the address will be automatically assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
If the `subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `subnetwork` is a name and this
field is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfaceaccessconfig">[]Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet. If omitted, ssh will not
work unless this provider can send traffic to the instance's network (e.g. via
tunnel or because it is running on another cloud instance on that network).
This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfacealiasiprange">[]Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}An
array of alias IP ranges for this network interface. Can only be specified for network
interfaces on subnet-mode networks. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The private IP address to assign to the instance. If
empty, the address will be automatically assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
If the `subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `subnetwork` is a name and this
field is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfaceaccessconfig">Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config[]?</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet. If omitted, ssh will not
work unless this provider can send traffic to the instance's network (e.g. via
tunnel or because it is running on another cloud instance on that network).
This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfacealiasiprange">Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}An
array of alias IP ranges for this network interface. Can only be specified for network
interfaces on subnet-mode networks. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The private IP address to assign to the instance. If
empty, the address will be automatically assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
If the `subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `subnetwork` is a name and this
field is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfaceaccessconfig">List[Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet. If omitted, ssh will not
work unless this provider can send traffic to the instance's network (e.g. via
tunnel or because it is running on another cloud instance on that network).
This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancenetworkinterfacealiasiprange">List[Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}An
array of alias IP ranges for this network interface. Can only be specified for network
interfaces on subnet-mode networks. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The private IP address to assign to the instance. If
empty, the address will be automatically assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
If the `subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `subnetwork` is a name and this
field is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceNetworkInterfaceAccessConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceNetworkInterfaceAccessConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceAccessConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceAccessConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceNetworkInterfaceAliasIpRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceNetworkInterfaceAliasIpRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceAliasIpRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceNetworkInterfaceAliasIpRangeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ip_<wbr>cidr_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range. This IP CIDR range
must belong to the specified subnetwork and cannot contain IP addresses reserved by
system or used by other network interfaces. This range may be a single IP address
(e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range. If left unspecified, the primary range of the subnetwork will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Scheduling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceScheduling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceScheduling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceSchedulingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceSchedulingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceschedulingnodeaffinity">List&lt;Instance<wbr>Scheduling<wbr>Node<wbr>Affinity<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies node affinities or anti-affinities
to determine which sole-tenant nodes your instances and managed instance
groups will use as host systems. Read more on sole-tenant node creation
[here](https://cloud.google.com/compute/docs/nodes/create-nodes).
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance is preemptible.
If this field is set to true, then `automatic_restart` must be
set to false.  Defaults to false.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceschedulingnodeaffinity">[]Instance<wbr>Scheduling<wbr>Node<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}Specifies node affinities or anti-affinities
to determine which sole-tenant nodes your instances and managed instance
groups will use as host systems. Read more on sole-tenant node creation
[here](https://cloud.google.com/compute/docs/nodes/create-nodes).
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance is preemptible.
If this field is set to true, then `automatic_restart` must be
set to false.  Defaults to false.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceschedulingnodeaffinity">Instance<wbr>Scheduling<wbr>Node<wbr>Affinity[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies node affinities or anti-affinities
to determine which sole-tenant nodes your instances and managed instance
groups will use as host systems. Read more on sole-tenant node creation
[here](https://cloud.google.com/compute/docs/nodes/create-nodes).
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance is preemptible.
If this field is set to true, then `automatic_restart` must be
set to false.  Defaults to false.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceschedulingnodeaffinity">List[Instance<wbr>Scheduling<wbr>Node<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}Specifies node affinities or anti-affinities
to determine which sole-tenant nodes your instances and managed instance
groups will use as host systems. Read more on sole-tenant node creation
[here](https://cloud.google.com/compute/docs/nodes/create-nodes).
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the instance is preemptible.
If this field is set to true, then `automatic_restart` must be
set to false.  Defaults to false.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceSchedulingNodeAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceSchedulingNodeAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceSchedulingNodeAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceSchedulingNodeAffinityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key for the node affinity label.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operator. Can be `IN` for node-affinities
or `NOT_IN` for anti-affinities.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key for the node affinity label.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operator. Can be `IN` for node-affinities
or `NOT_IN` for anti-affinities.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key for the node affinity label.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operator. Can be `IN` for node-affinities
or `NOT_IN` for anti-affinities.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key for the node affinity label.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The operator. Can be `IN` for node-affinities
or `NOT_IN` for anti-affinities.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Scratch<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceScratchDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceScratchDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceScratchDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceScratchDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The disk interface to use for attaching this disk; either SCSI or NVME.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The disk interface to use for attaching this disk; either SCSI or NVME.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The disk interface to use for attaching this disk; either SCSI or NVME.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The disk interface to use for attaching this disk; either SCSI or NVME.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Service<wbr>Account</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceServiceAccount">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceServiceAccount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceServiceAccountArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceServiceAccountOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: `allow_stopping_for_update` must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceShieldedInstanceConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceShieldedInstanceConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceShieldedInstanceConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}-- Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}-- Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}-- Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}-- Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}-- Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}-- Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}-- Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}-- Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}-- Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}-- Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}-- Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}-- Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







