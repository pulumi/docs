
---
title: "GetAccount"
block_external_search_index: true
---

Use this data source to access information about an existing CosmosDB (formally DocumentDB) Account.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/cosmosdb_account.html.markdown.





## Using GetAccount

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAccount<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GetAccountArgs">GetAccountArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GetAccountResult">GetAccountResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_account(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAccount<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#LookupAccountArgs">LookupAccountArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#LookupAccountResult">LookupAccountResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetAccount </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Cosmosdb.GetAccountResult.html">GetAccountResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.CosmosDB.Inputs.GetAccountArgs.html">GetAccountArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group in which the CosmosDB Account resides.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group in which the CosmosDB Account resides.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group in which the CosmosDB Account resides.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group in which the CosmosDB Account resides.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetAccount Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountcapability">List&lt;Pulumi.<wbr>Azure.<wbr>Cosmos<wbr>DB.<wbr>Outputs.<wbr>Get<wbr>Account<wbr>Capability&gt;</a></span>
    </dt>
    <dd>{{% md %}}Capabilities enabled on this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Consistency<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountconsistencypolicy">List&lt;Pulumi.<wbr>Azure.<wbr>Cosmos<wbr>DB.<wbr>Outputs.<wbr>Get<wbr>Account<wbr>Consistency<wbr>Policy&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Automatic<wbr>Failover</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If automatic failover is enabled for this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Multiple<wbr>Write<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If multi-master is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint used to connect to the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Geo<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountgeolocation">List&lt;Pulumi.<wbr>Azure.<wbr>Cosmos<wbr>DB.<wbr>Outputs.<wbr>Get<wbr>Account<wbr>Geo<wbr>Location&gt;</a></span>
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
        <span>Ip<wbr>Range<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current IP Filter for this CosmosDB account
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Virtual<wbr>Network<wbr>Filter<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If virtual network filtering is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kind of the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Offer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Offer Type to used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary read-only master Key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Read<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of read endpoints available for this CosmosDB account.
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
        <span>Secondary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary read-only master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountvirtualnetworkrule">List&lt;Pulumi.<wbr>Azure.<wbr>Cosmos<wbr>DB.<wbr>Outputs.<wbr>Get<wbr>Account<wbr>Virtual<wbr>Network<wbr>Rule&gt;</a></span>
    </dt>
    <dd>{{% md %}}Subnets that are allowed to access this CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Write<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of write endpoints available for this CosmosDB account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountcapability">[]Get<wbr>Account<wbr>Capability</a></span>
    </dt>
    <dd>{{% md %}}Capabilities enabled on this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Consistency<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountconsistencypolicy">[]Get<wbr>Account<wbr>Consistency<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Automatic<wbr>Failover</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If automatic failover is enabled for this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Multiple<wbr>Write<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If multi-master is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint used to connect to the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Geo<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountgeolocation">[]Get<wbr>Account<wbr>Geo<wbr>Location</a></span>
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
        <span>Ip<wbr>Range<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current IP Filter for this CosmosDB account
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Is<wbr>Virtual<wbr>Network<wbr>Filter<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If virtual network filtering is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kind of the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Offer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Offer Type to used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary read-only master Key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Read<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of read endpoints available for this CosmosDB account.
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
        <span>Secondary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary read-only master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountvirtualnetworkrule">[]Get<wbr>Account<wbr>Virtual<wbr>Network<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Subnets that are allowed to access this CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Write<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of write endpoints available for this CosmosDB account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountcapability">Get<wbr>Account<wbr>Capability[]</a></span>
    </dt>
    <dd>{{% md %}}Capabilities enabled on this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>consistency<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountconsistencypolicy">Get<wbr>Account<wbr>Consistency<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Automatic<wbr>Failover</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If automatic failover is enabled for this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Multiple<wbr>Write<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If multi-master is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint used to connect to the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>geo<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountgeolocation">Get<wbr>Account<wbr>Geo<wbr>Location[]</a></span>
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
        <span>ip<wbr>Range<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current IP Filter for this CosmosDB account
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is<wbr>Virtual<wbr>Network<wbr>Filter<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If virtual network filtering is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kind of the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>offer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Offer Type to used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary read-only master Key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>read<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of read endpoints available for this CosmosDB account.
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
        <span>secondary<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary<wbr>Readonly<wbr>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary read-only master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual<wbr>Network<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountvirtualnetworkrule">Get<wbr>Account<wbr>Virtual<wbr>Network<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}Subnets that are allowed to access this CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>write<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of write endpoints available for this CosmosDB account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountcapability">List[Get<wbr>Account<wbr>Capability]</a></span>
    </dt>
    <dd>{{% md %}}Capabilities enabled on this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>consistency_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountconsistencypolicy">List[Get<wbr>Account<wbr>Consistency<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>automatic_<wbr>failover</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If automatic failover is enabled for this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>multiple_<wbr>write_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If multi-master is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The endpoint used to connect to the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>geo_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountgeolocation">List[Get<wbr>Account<wbr>Geo<wbr>Location]</a></span>
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
        <span>ip_<wbr>range_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current IP Filter for this CosmosDB account
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>is_<wbr>virtual_<wbr>network_<wbr>filter_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If virtual network filtering is enabled for this Cosmos DB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kind of the CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>offer_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Offer Type to used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary_<wbr>master_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary_<wbr>readonly_<wbr>master_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary read-only master Key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>read_<wbr>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of read endpoints available for this CosmosDB account.
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
        <span>secondary_<wbr>master_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secondary master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary_<wbr>readonly_<wbr>master_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secondary read-only master key for the CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual_<wbr>network_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountvirtualnetworkrule">List[Get<wbr>Account<wbr>Virtual<wbr>Network<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Subnets that are allowed to access this CosmosDB account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>write_<wbr>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of write endpoints available for this CosmosDB account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Account<wbr>Capability</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAccountCapability">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#GetAccountCapability">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Specifies the name of the CosmosDB Account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Account<wbr>Consistency<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAccountConsistencyPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#GetAccountConsistencyPolicy">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Consistency<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consistency Level used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Interval<wbr>In<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Staleness<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of stale requests tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Consistency<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consistency Level used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Interval<wbr>In<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Staleness<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of stale requests tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>consistency<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consistency Level used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Interval<wbr>In<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Staleness<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of stale requests tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>consistency<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Consistency Level used by this CosmosDB Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Interval<wbr>In<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Staleness<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of stale requests tolerated when the consistency level is Bounded Staleness.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Account<wbr>Geo<wbr>Location</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAccountGeoLocation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#GetAccountGeoLocation">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Failover<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the virtual network subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Failover<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the virtual network subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>failover<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the virtual network subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>failover<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the virtual network subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Azure region hosting replicated data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Account<wbr>Virtual<wbr>Network<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAccountVirtualNetworkRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/cosmosdb?tab=doc#GetAccountVirtualNetworkRule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the virtual network subnet.
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
    <dd>{{% md %}}The ID of the virtual network subnet.
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
    <dd>{{% md %}}The ID of the virtual network subnet.
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
    <dd>{{% md %}}The ID of the virtual network subnet.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







