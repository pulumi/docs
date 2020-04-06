
---
title: "GetRecords"
block_external_search_index: true
---



This data source provides a list of DNS Domain Records in an Alibaba Cloud account according to the specified filters.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_records.html.markdown.





## Using GetRecords

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getRecords<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/dns/#GetRecordsArgs">GetRecordsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/dns/#GetRecordsResult">GetRecordsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_records(</span>domain_name=None<span class="p">, </span>host_record_regex=None<span class="p">, </span>ids=None<span class="p">, </span>is_locked=None<span class="p">, </span>line=None<span class="p">, </span>output_file=None<span class="p">, </span>status=None<span class="p">, </span>type=None<span class="p">, </span>value_regex=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupRecords<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#LookupRecordsArgs">LookupRecordsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#LookupRecordsResult">LookupRecordsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetRecords </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Dns.GetRecordsResult.html">GetRecordsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Dns.GetRecordsArgs.html">GetRecordsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host record regex. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of record IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the record is locked or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
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
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host record value regex. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Host record regex. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of record IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the record is locked or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
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
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Host record value regex. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host record regex. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of record IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the record is locked or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
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
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host record value regex. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>record_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host record regex. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of record IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is_<wbr>locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the record is locked or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
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
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host record value regex. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetRecords Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain the record belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}A list of record IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ISP line of the record. 
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
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrecordsrecord">List&lt;Get<wbr>Records<wbr>Record&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of records. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of entire URLs. Each item format as `<host_record>.<domain_name>`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain the record belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}A list of record IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ISP line of the record. 
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
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrecordsrecord">[]Get<wbr>Records<wbr>Record</a></span>
    </dt>
    <dd>{{% md %}}A list of records. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Status of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of entire URLs. Each item format as `<host_record>.<domain_name>`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain the record belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host<wbr>Record<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}A list of record IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is<wbr>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ISP line of the record. 
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
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrecordsrecord">Get<wbr>Records<wbr>Record[]</a></span>
    </dt>
    <dd>{{% md %}}A list of records. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of entire URLs. Each item format as `<host_record>.<domain_name>`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the domain the record belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host_<wbr>record_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}A list of record IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is_<wbr>locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ISP line of the record. 
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
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrecordsrecord">List[Get<wbr>Records<wbr>Record]</a></span>
    </dt>
    <dd>{{% md %}}A list of records. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of entire URLs. Each item format as `<host_record>.<domain_name>`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Records<wbr>Record</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetRecordsRecord">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#GetRecordsRecord">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether the record is locked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Priority of the `MX` record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record value of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether the record is locked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Priority of the `MX` record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record value of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Indicates whether the record is locked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Priority of the `MX` record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host record value of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The domain name associated to the records.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>record</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host record of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>line</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ISP line. Valid items are `default`, `telecom`, `unicom`, `mobile`, `oversea`, `edu`, `drpeng`, `btvn`, .etc. For checking all resolution lines enumeration please visit [Alibaba Cloud DNS doc](https://www.alibabacloud.com/help/doc-detail/34339.htm) 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>locked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether the record is locked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority of the `MX` record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Record status. Valid items are `ENABLE` and `DISABLE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Record type. Valid items are `A`, `NS`, `MX`, `TXT`, `CNAME`, `SRV`, `AAAA`, `REDIRECT_URL`, `FORWORD_URL` .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host record value of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







