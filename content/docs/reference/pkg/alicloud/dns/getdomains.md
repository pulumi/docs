
---
title: "GetDomains"
block_external_search_index: true
---



This data source provides a list of DNS Domains in an Alibaba Cloud account according to the specified filters.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

const domainsDs = pulumi.output(alicloud.dns.getDomains({
    domainNameRegex: "^hegu",
    outputFile: "domains.txt",
}, { async: true }));

export const firstDomainId = domainsDs.domains[0].domainId;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_domains.html.markdown.





## Using GetDomains

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getDomains<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/dns/#GetDomainsArgs">GetDomainsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/dns/#GetDomainsResult">GetDomainsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_domains(</span>ali_domain=None<span class="p">, </span>domain_name_regex=None<span class="p">, </span>group_name_regex=None<span class="p">, </span>ids=None<span class="p">, </span>instance_id=None<span class="p">, </span>output_file=None<span class="p">, </span>resource_group_id=None<span class="p">, </span>version_code=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupDomains<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#LookupDomainsArgs">LookupDomainsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#LookupDomainsResult">LookupDomainsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetDomains </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Dns.GetDomainsResult.html">GetDomainsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Dns.GetDomainsArgs.html">GetDomainsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the domain name. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the group name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
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
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the domain name. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the group name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
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
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the domain name. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the group name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
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
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ali_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain_<wbr>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the domain name. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group_<wbr>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by the group name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
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
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetDomains Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the domain is an Alibaba Cloud domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsdomain">List&lt;Get<wbr>Domains<wbr>Domain&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of domains. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Group<wbr>Name<wbr>Regex</span>
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
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of domain names.
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
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether the domain is an Alibaba Cloud domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsdomain">[]Get<wbr>Domains<wbr>Domain</a></span>
    </dt>
    <dd>{{% md %}}A list of domains. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Group<wbr>Name<wbr>Regex</span>
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
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of domain names.
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
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the domain is an Alibaba Cloud domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain<wbr>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsdomain">Get<wbr>Domains<wbr>Domain[]</a></span>
    </dt>
    <dd>{{% md %}}A list of domains. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>group<wbr>Name<wbr>Regex</span>
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
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of domain names.
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
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ali_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether the domain is an Alibaba Cloud domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain_<wbr>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsdomain">List[Get<wbr>Domains<wbr>Domain]</a></span>
    </dt>
    <dd>{{% md %}}A list of domains. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>group_<wbr>name_<wbr>regex</span>
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
    <dd>{{% md %}}A list of domain IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of domain names.
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
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the dns belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code of the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Domains<wbr>Domain</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetDomainsDomain">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/dns?tab=doc#GetDomainsDomain">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}DNS list of the domain in the analysis system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Puny<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Punycode of the Chinese domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}DNS list of the domain in the analysis system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Puny<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Punycode of the Chinese domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}DNS list of the domain in the analysis system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>puny<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Punycode of the Chinese domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ali<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the domain is from Alibaba Cloud or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dns_<wbr>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}DNS list of the domain in the analysis system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Id of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of group that contains the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis product ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>puny<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Punycode of the Chinese domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud analysis version code.
* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







