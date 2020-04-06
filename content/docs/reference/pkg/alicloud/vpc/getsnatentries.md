
---
title: "GetSnatEntries"
block_external_search_index: true
---



This data source provides a list of Snat Entries owned by an Alibaba Cloud account.

> **NOTE:** Available in 1.37.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/snat_entries.html.markdown.





## Using GetSnatEntries

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSnatEntries<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#GetSnatEntriesArgs">GetSnatEntriesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#GetSnatEntriesResult">GetSnatEntriesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_snat_entries(</span>ids=None<span class="p">, </span>output_file=None<span class="p">, </span>snat_ip=None<span class="p">, </span>snat_table_id=None<span class="p">, </span>source_cidr=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSnatEntries<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#LookupSnatEntriesArgs">LookupSnatEntriesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#LookupSnatEntriesResult">LookupSnatEntriesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSnatEntries </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.GetSnatEntriesResult.html">GetSnatEntriesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.GetSnatEntriesArgs.html">GetSnatEntriesArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snat_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snat_<wbr>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSnatEntries Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Entries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsnatentriesentry">List&lt;Get<wbr>Snat<wbr>Entries<wbr>Entry&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries. Each element contains the following attributes:
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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}(Optional) A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Entries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsnatentriesentry">[]Get<wbr>Snat<wbr>Entries<wbr>Entry</a></span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries. Each element contains the following attributes:
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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(Optional) A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>entries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsnatentriesentry">Get<wbr>Snat<wbr>Entries<wbr>Entry[]</a></span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries. Each element contains the following attributes:
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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(Optional) A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snat<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>entries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsnatentriesentry">List[Get<wbr>Snat<wbr>Entries<wbr>Entry]</a></span>
    </dt>
    <dd>{{% md %}}A list of Snat Entries. Each element contains the following attributes:
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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(Optional) A list of Snat Entries IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snat_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snat_<wbr>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Snat<wbr>Entries<wbr>Entry</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetSnatEntriesEntry">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#GetSnatEntriesEntry">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snat<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snat_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public IP of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source CIDR block of the Snat Entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the Snat Entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







