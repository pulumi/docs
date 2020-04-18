
---
title: "GetIpRanges"
block_external_search_index: true
---



Use this data source to retrieve information about Datadog's IP addresses.
{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as datadog from "@pulumi/datadog";

const test = datadog.getIpRanges();
```

{{% /example %}}
{{% /examples %}}





## Using GetIpRanges

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getIpRanges<span class="p">(</span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/datadog/#GetIpRangesResult">GetIpRangesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_ip_ranges(</span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupIpRanges<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-datadog/sdk/v2/go/datadog/?tab=doc#LookupIpRangesResult">LookupIpRangesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetIpRanges </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Datadog/Pulumi.Datadog.GetIpRangesResult.html">GetIpRangesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}




## GetIpRanges Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Agents<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Agents<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Apm<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Apm<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

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
        <span>Logs<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logs<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Process<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Process<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Synthetics<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Synthetics<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhooks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhooks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Agents<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Agents<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Apm<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Apm<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

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
        <span>Logs<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logs<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Process<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Process<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Synthetics<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Synthetics<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhooks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhooks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>agents<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>agents<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>apm<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>apm<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

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
        <span>logs<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logs<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>process<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>process<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>synthetics<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>synthetics<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhooks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhooks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>agents_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>agents_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the agent endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the api endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>apm_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>apm_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the apm endpoint.
{{% /md %}}</dd>

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
        <span>logs_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logs_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the logs endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>process_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>process_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the process endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>synthetics_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>synthetics_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the synthetics endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhooks_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv4 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhooks_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An Array of IPv6 addresses in CIDR format specifying the A records for the webhooks endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







