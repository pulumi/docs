
---
title: "GetElasticIp"
block_external_search_index: true
---



`aws.ec2.Eip` provides details about a specific Elastic IP.

{{% examples %}}
## Example Usage

{{% example %}}
### Search By Allocation ID (VPC only)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const byAllocationId = pulumi.output(aws.getElasticIp({
    id: "eipalloc-12345678",
}, { async: true }));
```

{{% /example %}}
{{% example %}}
### Search By Filters (EC2-Classic or VPC)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const byFilter = pulumi.output(aws.getElasticIp({
    filters: [{
        name: "tag:Name",
        values: ["exampleNameTagValue"],
    }],
}, { async: true }));
```

{{% /example %}}
{{% example %}}
### Search By Public IP (EC2-Classic or VPC)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const byPublicIp = pulumi.output(aws.getElasticIp({
    publicIp: "1.2.3.4",
}, { async: true }));
```

{{% /example %}}
{{% example %}}
### Search By Tags (EC2-Classic or VPC)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const byTags = pulumi.output(aws.getElasticIp({
    tags: {
        Name: "exampleNameTagValue",
    },
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetElasticIp

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getElasticIp<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/#GetElasticIpArgs">GetElasticIpArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/#GetElasticIpResult">GetElasticIpResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_elastic_ip(</span>filters=None<span class="p">, </span>id=None<span class="p">, </span>public_ip=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupElasticIp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetElasticIpArgs">GetElasticIpArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#LookupElasticIpResult">LookupElasticIpResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetElasticIp </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetElasticIpResult.html">GetElasticIpResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetElasticIpArgs.html">GetElasticIpArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">List&lt;Get<wbr>Elastic<wbr>Ip<wbr>Filter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `public_ip`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the specific EIP to retrieve.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Elastic IP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">[]Get<wbr>Elastic<wbr>Ip<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `public_ip`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The public IP of the specific EIP to retrieve.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Elastic IP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">Get<wbr>Elastic<wbr>Ip<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `public_ip`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The public IP of the specific EIP to retrieve.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Elastic IP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">List[Get<wbr>Elastic<wbr>Ip<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `public_ip`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public IP of the specific EIP to retrieve.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Elastic IP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetElasticIp Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Association<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID representing the association of the address with an instance in a VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">List&lt;Get<wbr>Elastic<wbr>Ip<wbr>Filter&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance that the address is associated with (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the AWS account that owns the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Private DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private IP address associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public IP address of Elastic IP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ipv4Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of an address pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Key-value map of tags associated with Elastic IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Association<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID representing the association of the address with an instance in a VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">[]Get<wbr>Elastic<wbr>Ip<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance that the address is associated with (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the AWS account that owns the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Private DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private IP address associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public IP address of Elastic IP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ipv4Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of an address pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value map of tags associated with Elastic IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>association<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID representing the association of the address with an instance in a VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">Get<wbr>Elastic<wbr>Ip<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance that the address is associated with (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the AWS account that owns the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Private DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private IP address associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Public IP address of Elastic IP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ipv4Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of an address pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Key-value map of tags associated with Elastic IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>association_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID representing the association of the address with an instance in a VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getelasticipfilter">List[Get<wbr>Elastic<wbr>Ip<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the instance that the address is associated with (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the AWS account that owns the network interface.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Private DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The private IP address associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>dns</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Public DNS associated with the Elastic IP address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Public IP address of Elastic IP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ipv4_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an address pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value map of tags associated with Elastic IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Elastic<wbr>Ip<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetElasticIpFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetElasticIpFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetElasticIpFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetElasticIpFilter">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







