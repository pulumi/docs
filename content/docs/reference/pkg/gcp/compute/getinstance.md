
---
title: "GetInstance"
block_external_search_index: true
---



Get information about a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).


{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const appserver = gcp.compute.getInstance({
    name: "primary-application-server",
    zone: "us-central1-a",
});
```

{{% /example %}}
{{% /examples %}}





## Using GetInstance

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getInstance<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#GetInstanceArgs">GetInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#GetInstanceResult">GetInstanceResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_instance(</span>name=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, </span>zone=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#LookupInstanceArgs">LookupInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#LookupInstanceResult">LookupInstanceResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetInstance </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.GetInstanceResult.html">GetInstanceResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.GetInstanceArgs.html">GetInstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If `self_link` is provided, this value is ignored.  If neither `self_link`
nor `project` are provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The self link of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The zone of the instance. If `self_link` is provided, this
value is ignored.  If neither `self_link` nor `zone` are provided, the
provider zone is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If `self_link` is provided, this value is ignored.  If neither `self_link`
nor `project` are provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The self link of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The zone of the instance. If `self_link` is provided, this
value is ignored.  If neither `self_link` nor `zone` are provided, the
provider zone is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If `self_link` is provided, this value is ignored.  If neither `self_link`
nor `project` are provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The self link of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The zone of the instance. If `self_link` is provided, this
value is ignored.  If neither `self_link` nor `zone` are provided, the
provider zone is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If `self_link` is provided, this value is ignored.  If neither `self_link`
nor `project` are provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The self link of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The zone of the instance. If `self_link` is provided, this
value is ignored.  If neither `self_link` nor `zone` are provided, the
provider zone is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetInstance Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceattacheddisk">List&lt;Get<wbr>Instance<wbr>Attached<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdisk">List&lt;Get<wbr>Instance<wbr>Boot<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether deletion protection is enabled on this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A brief description of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceguestaccelerator">List&lt;Get<wbr>Instance<wbr>Guest<wbr>Accelerator&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs made available within the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum CPU platform specified for the VM instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterface">List&lt;Get<wbr>Instance<wbr>Network<wbr>Interface&gt;</a></span>
    </dt>
    <dd>{{% md %}}The networks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Schedulings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescheduling">List&lt;Get<wbr>Instance<wbr>Scheduling&gt;</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy being used by the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescratchdisk">List&lt;Get<wbr>Instance<wbr>Scratch<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}The scratch disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceserviceaccount">List&lt;Get<wbr>Instance<wbr>Service<wbr>Account&gt;</a></span>
    </dt>
    <dd>{{% md %}}The service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceshieldedinstanceconfig">List&lt;Get<wbr>Instance<wbr>Shielded<wbr>Instance<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}The shielded vm config being used by the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of tags attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceattacheddisk">[]Get<wbr>Instance<wbr>Attached<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}List of disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdisk">[]Get<wbr>Instance<wbr>Boot<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether deletion protection is enabled on this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A brief description of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceguestaccelerator">[]Get<wbr>Instance<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs made available within the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum CPU platform specified for the VM instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterface">[]Get<wbr>Instance<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}The networks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Schedulings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescheduling">[]Get<wbr>Instance<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy being used by the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescratchdisk">[]Get<wbr>Instance<wbr>Scratch<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}The scratch disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceserviceaccount">[]Get<wbr>Instance<wbr>Service<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}The service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shielded<wbr>Instance<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceshieldedinstanceconfig">[]Get<wbr>Instance<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The shielded vm config being used by the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The list of tags attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow<wbr>Stopping<wbr>For<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attached<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceattacheddisk">Get<wbr>Instance<wbr>Attached<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}List of disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdisk">Get<wbr>Instance<wbr>Boot<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can<wbr>Ip<wbr>Forward</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deletion<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether deletion protection is enabled on this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A brief description of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Display</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceguestaccelerator">Get<wbr>Instance<wbr>Guest<wbr>Accelerator[]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs made available within the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata<wbr>Startup<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum CPU platform specified for the VM instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterface">Get<wbr>Instance<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}The networks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>schedulings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescheduling">Get<wbr>Instance<wbr>Scheduling[]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy being used by the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scratch<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescratchdisk">Get<wbr>Instance<wbr>Scratch<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}The scratch disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceserviceaccount">Get<wbr>Instance<wbr>Service<wbr>Account[]</a></span>
    </dt>
    <dd>{{% md %}}The service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded<wbr>Instance<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceshieldedinstanceconfig">Get<wbr>Instance<wbr>Shielded<wbr>Instance<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}The shielded vm config being used by the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The list of tags attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow_<wbr>stopping_<wbr>for_<wbr>update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attached_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceattacheddisk">List[Get<wbr>Instance<wbr>Attached<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}List of disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdisk">List[Get<wbr>Instance<wbr>Boot<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}The boot disk for the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can_<wbr>ip_<wbr>forward</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The CPU platform used by this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deletion_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether deletion protection is enabled on this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A brief description of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>display</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceguestaccelerator">List[Get<wbr>Instance<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The server-assigned unique identifier of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the labels.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The machine type to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata key/value pairs made available within the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata_<wbr>startup_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The minimum CPU platform specified for the VM instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterface">List[Get<wbr>Instance<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}The networks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>schedulings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescheduling">List[Get<wbr>Instance<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}The scheduling strategy being used by the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scratch_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancescratchdisk">List[Get<wbr>Instance<wbr>Scratch<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}The scratch disks attached to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceserviceaccount">List[Get<wbr>Instance<wbr>Service<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}The service account to attach to the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shielded_<wbr>instance_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceshieldedinstanceconfig">List[Get<wbr>Instance<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The shielded vm config being used by the instance. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The list of tags attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The unique fingerprint of the tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Instance<wbr>Attached<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceAttachedDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceAttachedDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Boot<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceBootDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceBootDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance is deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdiskinitializeparam">List&lt;Get<wbr>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Param<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Parameters with which a disk was created alongside the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance is deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdiskinitializeparam">[]Get<wbr>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Param</a></span>
    </dt>
    <dd>{{% md %}}Parameters with which a disk was created alongside the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance is deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdiskinitializeparam">Get<wbr>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Param[]</a></span>
    </dt>
    <dd>{{% md %}}Parameters with which a disk was created alongside the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the disk will be auto-deleted when the instance is deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name with which the attached disk is accessible
under `/dev/disk/by-id/`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Encryption<wbr>Key<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>initialize<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancebootdiskinitializeparam">List[Get<wbr>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Param]</a></span>
    </dt>
    <dd>{{% md %}}Parameters with which a disk was created alongside the instance.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Read/write mode for the disk. One of `"READ_ONLY"` or `"READ_WRITE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the disk attached to this instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Boot<wbr>Disk<wbr>Initialize<wbr>Param</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceBootDiskInitializeParam">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceBootDiskInitializeParam">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The image from which this disk was initialised.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The image from which this disk was initialised.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The image from which this disk was initialised.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The image from which this disk was initialised.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the image in gigabytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The accelerator type resource exposed to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfaceaccessconfig">List&lt;Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfacealiasiprange">List&lt;Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of alias IP ranges for this network interface. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The private IP address assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfaceaccessconfig">[]Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfacealiasiprange">[]Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}An array of alias IP ranges for this network interface. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The private IP address assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfaceaccessconfig">Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfacealiasiprange">Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range[]</a></span>
    </dt>
    <dd>{{% md %}}An array of alias IP ranges for this network interface. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The private IP address assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfaceaccessconfig">List[Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Access configurations, i.e. IPs via which this
instance can be accessed via the Internet. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>alias<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstancenetworkinterfacealiasiprange">List[Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}An array of alias IP ranges for this network interface. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance. One of `name` or `self_link` must be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The private IP address assigned to the instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the subnetwork attached to this interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project in which the subnetwork belongs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Access<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceNetworkInterfaceAccessConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceNetworkInterfaceAccessConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address that is be 1:1 mapped to the instance's
network ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance. One of `PREMIUM` or `STANDARD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address that is be 1:1 mapped to the instance's
network ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance. One of `PREMIUM` or `STANDARD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address that is be 1:1 mapped to the instance's
network ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance. One of `PREMIUM` or `STANDARD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>nat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP address that is be 1:1 mapped to the instance's
network ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [networking tier][network-tier] used for configuring this instance. One of `PREMIUM` or `STANDARD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Ptr<wbr>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The DNS domain name for the public PTR record.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Network<wbr>Interface<wbr>Alias<wbr>Ip<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceNetworkInterfaceAliasIpRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceNetworkInterfaceAliasIpRange">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Cidr<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ip_<wbr>cidr_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP CIDR range represented by this alias IP range.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnetwork<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The subnetwork secondary range name specifying
the secondary range from which to allocate the IP CIDR range for this alias IP
range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Scheduling</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceScheduling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceScheduling">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceschedulingnodeaffinity">List&lt;Get<wbr>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>On<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. One of `MIGRATE` or `TERMINATE`, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the instance is preemptible.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceschedulingnodeaffinity">[]Get<wbr>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>On<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. One of `MIGRATE` or `TERMINATE`, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the instance is preemptible.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceschedulingnodeaffinity">Get<wbr>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>on<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. One of `MIGRATE` or `TERMINATE`, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the instance is preemptible.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>automatic<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node<wbr>Affinities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceschedulingnodeaffinity">List[Get<wbr>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>on<wbr>Host<wbr>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Describes maintenance behavior for the
instance. One of `MIGRATE` or `TERMINATE`, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the instance is preemptible.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Scheduling<wbr>Node<wbr>Affinity</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceSchedulingNodeAffinity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceSchedulingNodeAffinity">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
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
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
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
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
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
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Scratch<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceScratchDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceScratchDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The disk interface used for attaching this disk. One of `SCSI` or `NVME`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The disk interface used for attaching this disk. One of `SCSI` or `NVME`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The disk interface used for attaching this disk. One of `SCSI` or `NVME`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The disk interface used for attaching this disk. One of `SCSI` or `NVME`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Service<wbr>Account</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceServiceAccount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceServiceAccount">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The service account e-mail address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of service scopes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account e-mail address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of service scopes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account e-mail address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of service scopes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The service account e-mail address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of service scopes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Instance<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetInstanceShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#GetInstanceShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Vtpm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







