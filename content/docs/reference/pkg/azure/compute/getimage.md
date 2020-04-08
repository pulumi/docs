
---
title: "GetImage"
block_external_search_index: true
---



Use this data source to access information about an existing Image.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/image.html.markdown.





## Using GetImage

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getImage<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#GetImageArgs">GetImageArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#GetImageResult">GetImageResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_image(</span>name=None<span class="p">, </span>name_regex=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>sort_descending=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupImage<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LookupImageArgs">LookupImageArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LookupImageResult">LookupImageResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetImage </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.GetImageResult.html">GetImageResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.GetImageArgs.html">GetImageArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Regex pattern of the image to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where this Image exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Regex pattern of the image to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where this Image exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Regex pattern of the image to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where this Image exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Image.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Regex pattern of the image to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where this Image exists.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort_<wbr>descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetImage Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimagedatadisk">List&lt;Get<wbr>Image<wbr>Data<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}a collection of `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Azure Location where this Image exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the Image.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimageosdisk">List&lt;Get<wbr>Image<wbr>Os<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}a `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}a mapping of tags to assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Resilient</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}is zone resiliency enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimagedatadisk">[]Get<wbr>Image<wbr>Data<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}a collection of `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Azure Location where this Image exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the name of the Image.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimageosdisk">[]Get<wbr>Image<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}a `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}a mapping of tags to assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Resilient</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}is zone resiliency enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimagedatadisk">Get<wbr>Image<wbr>Data<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}a collection of `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Azure Location where this Image exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the Image.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimageosdisk">Get<wbr>Image<wbr>Os<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}a `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort<wbr>Descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}a mapping of tags to assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Resilient</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}is zone resiliency enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>data_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimagedatadisk">List[Get<wbr>Image<wbr>Data<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}a collection of `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the Azure Location where this Image exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of the Image.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getimageosdisk">List[Get<wbr>Image<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}a `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort_<wbr>descending</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}a mapping of tags to assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>resilient</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}is zone resiliency enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Image<wbr>Data<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetImageDataDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#GetImageDataDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the logical unit number of the data disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the logical unit number of the data disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}the logical unit number of the data disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}the logical unit number of the data disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed_<wbr>disk_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Image<wbr>Os<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetImageOsDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#GetImageOsDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the State of the OS used in the Image, such as `Generalized`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the type of Operating System used on the OS Disk. such as `Linux` or `Windows`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the State of the OS used in the Image, such as `Generalized`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the type of Operating System used on the OS Disk. such as `Linux` or `Windows`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the State of the OS used in the Image, such as `Generalized`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the type of Operating System used on the OS Disk. such as `Linux` or `Windows`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the URI in Azure storage of the blob used to create the image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the caching mode for the Data Disk, such as `ReadWrite`, `ReadOnly`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed_<wbr>disk_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the ID of the Managed Disk used as the Data Disk Image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the State of the OS used in the Image, such as `Generalized`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the type of Operating System used on the OS Disk. such as `Linux` or `Windows`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}the size of this Data Disk in GB.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







