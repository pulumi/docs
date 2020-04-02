
---
title: "InstanceTemplate"
block_external_search_index: true
---

Manages a VM instance template resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instance-templates)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instanceTemplates).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_template.html.markdown.



## Create a InstanceTemplate Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceTemplate">InstanceTemplate</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceTemplateArgs">InstanceTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">InstanceTemplate</span><span class="p">(resource_name, opts=None, </span>can_ip_forward=None<span class="p">, </span>description=None<span class="p">, </span>disks=None<span class="p">, </span>enable_display=None<span class="p">, </span>guest_accelerators=None<span class="p">, </span>instance_description=None<span class="p">, </span>labels=None<span class="p">, </span>machine_type=None<span class="p">, </span>metadata=None<span class="p">, </span>metadata_startup_script=None<span class="p">, </span>min_cpu_platform=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>scheduling=None<span class="p">, </span>service_account=None<span class="p">, </span>shielded_instance_config=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstanceTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateArgs">InstanceTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplate">InstanceTemplate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InstanceTemplate.html">InstanceTemplate</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InstanceTemplateArgs.html">InstanceTemplateArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List&lt;Instance<wbr>Template<wbr>Disk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List&lt;Instance<wbr>Template<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List&lt;Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">[]Instance<wbr>Template<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">[]Instance<wbr>Template<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">[]Instance<wbr>Template<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">*Instance<wbr>Template<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateserviceaccount">*Instance<wbr>Template<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">*Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">Instance<wbr>Template<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">Instance<wbr>Template<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">Instance<wbr>Template<wbr>Network<wbr>Interface[]?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description of this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List[Instance<wbr>Template<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List[Instance<wbr>Template<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata_<wbr>startup_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List[Instance<wbr>Template<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Dict[Instance<wbr>Template<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateserviceaccount">Dict[Instance<wbr>Template<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Dict[Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## InstanceTemplate Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List&lt;Instance<wbr>Template<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List&lt;Instance<wbr>Template<wbr>Guest<wbr>Accelerator&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List&lt;Instance<wbr>Template<wbr>Network<wbr>Interface&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">[]Instance<wbr>Template<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">[]Instance<wbr>Template<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">[]Instance<wbr>Template<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">*Instance<wbr>Template<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">Instance<wbr>Template<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">Instance<wbr>Template<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">Instance<wbr>Template<wbr>Network<wbr>Interface[]?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List[Instance<wbr>Template<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List[Instance<wbr>Template<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List[Instance<wbr>Template<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Dict[Instance<wbr>Template<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Dict[Instance<wbr>Template<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Dict[Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing InstanceTemplate Resource

Get an existing InstanceTemplate resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceTemplateState">InstanceTemplateState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InstanceTemplate">InstanceTemplate</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>can_ip_forward=None<span class="p">, </span>description=None<span class="p">, </span>disks=None<span class="p">, </span>enable_display=None<span class="p">, </span>guest_accelerators=None<span class="p">, </span>instance_description=None<span class="p">, </span>labels=None<span class="p">, </span>machine_type=None<span class="p">, </span>metadata=None<span class="p">, </span>metadata_fingerprint=None<span class="p">, </span>metadata_startup_script=None<span class="p">, </span>min_cpu_platform=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>scheduling=None<span class="p">, </span>self_link=None<span class="p">, </span>service_account=None<span class="p">, </span>shielded_instance_config=None<span class="p">, </span>tags=None<span class="p">, </span>tags_fingerprint=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInstanceTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateState">InstanceTemplateState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplate">InstanceTemplate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InstanceTemplate.html">InstanceTemplate</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InstanceTemplateState.html">InstanceTemplateState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List&lt;Instance<wbr>Template<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List&lt;Instance<wbr>Template<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List&lt;Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">[]Instance<wbr>Template<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">[]Instance<wbr>Template<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">[]Instance<wbr>Template<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">*Instance<wbr>Template<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">*Instance<wbr>Template<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">*Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">Instance<wbr>Template<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">Instance<wbr>Template<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">Instance<wbr>Template<wbr>Network<wbr>Interface[]?</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Instance<wbr>Template<wbr>Scheduling?</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Instance<wbr>Template<wbr>Service<wbr>Account?</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.
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
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatedisk">List[Instance<wbr>Template<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: `allow_stopping_for_update` must be set to true in order to update this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateguestaccelerator">List[Instance<wbr>Template<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A brief description to use for instances
created from this template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
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
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs to make available from
within instances created from this template.
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
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterface">List[Instance<wbr>Template<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.
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
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatescheduling">Dict[Instance<wbr>Template<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy to use. More details about
this configuration option are detailed below.
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
        <span class="property-type"><a href="#instancetemplateserviceaccount">Dict[Instance<wbr>Template<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}Service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateshieldedinstanceconfig">Dict[Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
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
    <dd>{{% md %}}Tags to attach to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Instance<wbr>Template<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not the disk should be auto-deleted.
This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates that this is a boot disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique device name that is reflected into the
/dev/  tree of a Linux operating system running within the instance. If not
specified, the server chooses a default device name to apply to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatediskdiskencryptionkey">Instance<wbr>Template<wbr>Disk<wbr>Disk<wbr>Encryption<wbr>Key<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Encrypts or decrypts a disk using a customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the disk. When not provided, this defaults
to the name of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not
specified, it will inherit the size of its base image. For SCRATCH disks,
the size must be exactly 375GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCE disk type. Can be either `"pd-ssd"`,
`"local-ssd"`, or `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the disk interface to use for attaching
this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name (**not self_link**)
of the disk (such as those managed by `gcp.compute.Disk`) to attach.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image from which to
initialize this disk. This can be one of: the image's `self_link`,
`projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`.
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
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the disk should be auto-deleted.
This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates that this is a boot disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique device name that is reflected into the
/dev/  tree of a Linux operating system running within the instance. If not
specified, the server chooses a default device name to apply to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatediskdiskencryptionkey">*Instance<wbr>Template<wbr>Disk<wbr>Disk<wbr>Encryption<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}Encrypts or decrypts a disk using a customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the disk. When not provided, this defaults
to the name of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not
specified, it will inherit the size of its base image. For SCRATCH disks,
the size must be exactly 375GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCE disk type. Can be either `"pd-ssd"`,
`"local-ssd"`, or `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the disk interface to use for attaching
this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name (**not self_link**)
of the disk (such as those managed by `gcp.compute.Disk`) to attach.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The image from which to
initialize this disk. This can be one of: the image's `self_link`,
`projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`.
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
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not the disk should be auto-deleted.
This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates that this is a boot disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique device name that is reflected into the
/dev/  tree of a Linux operating system running within the instance. If not
specified, the server chooses a default device name to apply to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatediskdiskencryptionkey">Instance<wbr>Template<wbr>Disk<wbr>Disk<wbr>Encryption<wbr>Key?</a></span>
    </dt>
    <dd>{{% md %}}Encrypts or decrypts a disk using a customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the disk. When not provided, this defaults
to the name of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not
specified, it will inherit the size of its base image. For SCRATCH disks,
the size must be exactly 375GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCE disk type. Can be either `"pd-ssd"`,
`"local-ssd"`, or `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the disk interface to use for attaching
this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name (**not self_link**)
of the disk (such as those managed by `gcp.compute.Disk`) to attach.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image from which to
initialize this disk. This can be one of: the image's `self_link`,
`projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`.
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
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the disk should be auto-deleted.
This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that this is a boot disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique device name that is reflected into the
/dev/  tree of a Linux operating system running within the instance. If not
specified, the server chooses a default device name to apply to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>encryption_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatediskdiskencryptionkey">Dict[Instance<wbr>Template<wbr>Disk<wbr>Disk<wbr>Encryption<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}Encrypts or decrypts a disk using a customer-supplied encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the disk. When not provided, this defaults
to the name of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes. If not
specified, it will inherit the size of its base image. For SCRATCH disks,
the size must be exactly 375GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCE disk type. Can be either `"pd-ssd"`,
`"local-ssd"`, or `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the disk interface to use for attaching
this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to instances
created from this template,
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name (**not self_link**)
of the disk (such as those managed by `gcp.compute.Disk`) to attach.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The image from which to
initialize this disk. This can be one of: the image's `self_link`,
`projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`.
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





<h4>Instance<wbr>Template<wbr>Disk<wbr>Disk<wbr>Encryption<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateDiskDiskEncryptionKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateDiskDiskEncryptionKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateDiskDiskEncryptionKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateDiskDiskEncryptionKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The self link of the encryption key that is stored in Google Cloud KMS
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The self link of the encryption key that is stored in Google Cloud KMS
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The self link of the encryption key that is stored in Google Cloud KMS
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The self link of the encryption key that is stored in Google Cloud KMS
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Template<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateGuestAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateGuestAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateGuestAcceleratorOutput">output</a> API doc for this type.
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





<h4>Instance<wbr>Template<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfaceaccessconfig">List&lt;Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Access<wbr>Config<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet (this means that ssh provisioners will
not work unless you can send traffic to the instance's
network (e.g. via tunnel or because it is running on another cloud instance
on that network). This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfacealiasiprange">List&lt;Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range<wbr>Args&gt;?</a></span>
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
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Use `network` attribute for Legacy or Auto subnetted networks and
`subnetwork` for custom subnetted networks.
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
    <dd>{{% md %}}the name of the subnetwork to attach this interface
to. The subnetwork must exist in the same `region` this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the subnetwork belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfaceaccessconfig">[]Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet (this means that ssh provisioners will
not work unless you can send traffic to the instance's
network (e.g. via tunnel or because it is running on another cloud instance
on that network). This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfacealiasiprange">[]Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</a></span>
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
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Use `network` attribute for Legacy or Auto subnetted networks and
`subnetwork` for custom subnetted networks.
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
    <dd>{{% md %}}the name of the subnetwork to attach this interface
to. The subnetwork must exist in the same `region` this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the subnetwork belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfaceaccessconfig">Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Access<wbr>Config[]?</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet (this means that ssh provisioners will
not work unless you can send traffic to the instance's
network (e.g. via tunnel or because it is running on another cloud instance
on that network). This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfacealiasiprange">Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range[]?</a></span>
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
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Use `network` attribute for Legacy or Auto subnetted networks and
`subnetwork` for custom subnetted networks.
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
    <dd>{{% md %}}the name of the subnetwork to attach this interface
to. The subnetwork must exist in the same `region` this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the subnetwork belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfaceaccessconfig">List[Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Access<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Omit to ensure that the instance
is not accessible from the Internet (this means that ssh provisioners will
not work unless you can send traffic to the instance's
network (e.g. via tunnel or because it is running on another cloud instance
on that network). This block can be repeated multiple times. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplatenetworkinterfacealiasiprange">List[Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range]</a></span>
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
    <dd>{{% md %}}The name of the instance template. If you leave
this blank, the provider will auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this interface to.
Use `network` attribute for Legacy or Auto subnetted networks and
`subnetwork` for custom subnetted networks.
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
    <dd>{{% md %}}the name of the subnetwork to attach this interface
to. The subnetwork must exist in the same `region` this instance will be
created in. Either `network` or `subnetwork` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the subnetwork belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateNetworkInterfaceAccessConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateNetworkInterfaceAccessConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceAccessConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceAccessConfigOutput">output</a> API doc for this type.
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
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring
this instance template. This field can take the following values: PREMIUM or
STANDARD. If this field is not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
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
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring
this instance template. This field can take the following values: PREMIUM or
STANDARD. If this field is not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
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
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring
this instance template. This field can take the following values: PREMIUM or
STANDARD. If this field is not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
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
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring
this instance template. This field can take the following values: PREMIUM or
STANDARD. If this field is not specified, it is assumed to be PREMIUM.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Template<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateNetworkInterfaceAliasIpRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateNetworkInterfaceAliasIpRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceAliasIpRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateNetworkInterfaceAliasIpRangeOutput">output</a> API doc for this type.
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
system or used by other network interfaces. At the time of writing only a
netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API
error.
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
system or used by other network interfaces. At the time of writing only a
netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API
error.
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
system or used by other network interfaces. At the time of writing only a
netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API
error.
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
system or used by other network interfaces. At the time of writing only a
netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API
error.
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





<h4>Instance<wbr>Template<wbr>Scheduling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateScheduling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateScheduling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateSchedulingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateSchedulingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether the instance should be
automatically restarted if it is terminated by Compute Engine (not
terminated by a user). This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateschedulingnodeaffinity">List&lt;Instance<wbr>Template<wbr>Scheduling<wbr>Node<wbr>Affinity<wbr>Args&gt;?</a></span>
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
    <dd>{{% md %}}Defines the maintenance behavior for this
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allows instance to be preempted. This defaults to
false. Read more on this
[here](https://cloud.google.com/compute/docs/instances/preemptible).
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
    <dd>{{% md %}}Specifies whether the instance should be
automatically restarted if it is terminated by Compute Engine (not
terminated by a user). This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateschedulingnodeaffinity">[]Instance<wbr>Template<wbr>Scheduling<wbr>Node<wbr>Affinity</a></span>
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
    <dd>{{% md %}}Defines the maintenance behavior for this
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allows instance to be preempted. This defaults to
false. Read more on this
[here](https://cloud.google.com/compute/docs/instances/preemptible).
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
    <dd>{{% md %}}Specifies whether the instance should be
automatically restarted if it is terminated by Compute Engine (not
terminated by a user). This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateschedulingnodeaffinity">Instance<wbr>Template<wbr>Scheduling<wbr>Node<wbr>Affinity[]?</a></span>
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
    <dd>{{% md %}}Defines the maintenance behavior for this
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allows instance to be preempted. This defaults to
false. Read more on this
[here](https://cloud.google.com/compute/docs/instances/preemptible).
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
    <dd>{{% md %}}Specifies whether the instance should be
automatically restarted if it is terminated by Compute Engine (not
terminated by a user). This defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instancetemplateschedulingnodeaffinity">List[Instance<wbr>Template<wbr>Scheduling<wbr>Node<wbr>Affinity]</a></span>
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
    <dd>{{% md %}}Defines the maintenance behavior for this
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allows instance to be preempted. This defaults to
false. Read more on this
[here](https://cloud.google.com/compute/docs/instances/preemptible).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Template<wbr>Scheduling<wbr>Node<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateSchedulingNodeAffinity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateSchedulingNodeAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateSchedulingNodeAffinityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateSchedulingNodeAffinityOutput">output</a> API doc for this type.
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





<h4>Instance<wbr>Template<wbr>Service<wbr>Account</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateServiceAccount">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateServiceAccount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateServiceAccountArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateServiceAccountOutput">output</a> API doc for this type.
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
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Instance<wbr>Template<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#InstanceTemplateShieldedInstanceConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InstanceTemplateShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateShieldedInstanceConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#InstanceTemplateShieldedInstanceConfigOutput">output</a> API doc for this type.
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








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
