
---
title: "GetPolicy"
block_external_search_index: true
---

Use this data source to access information about an existing Storage Management Policy.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_management_policy.html.markdown.





## Using GetPolicy

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getPolicy<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/storage/#GetPolicyArgs">GetPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/storage/#GetPolicyResult">GetPolicyResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_policy(</span>storage_account_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#LookupPolicyArgs">LookupPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#LookupPolicyResult">LookupPolicyResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetPolicy </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Storage.GetPolicyResult.html">GetPolicyResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Storage.GetPolicyArgs.html">GetPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account to retrieve the management policy for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account to retrieve the management policy for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account to retrieve the management policy for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account to retrieve the management policy for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetPolicy Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

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
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrule">List&lt;Get<wbr>Policy<wbr>Rule&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `rule` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

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
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrule">[]Get<wbr>Policy<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A `rule` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

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
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrule">Get<wbr>Policy<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}A `rule` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrule">List[Get<wbr>Policy<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A `rule` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>account_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Policy<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetPolicyRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetPolicyRule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleaction">List&lt;Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An `actions` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean to specify whether the rule is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrulefilter">List&lt;Get<wbr>Policy<wbr>Rule<wbr>Filter<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `filter` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleaction">[]Get<wbr>Policy<wbr>Rule<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}An `actions` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean to specify whether the rule is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrulefilter">[]Get<wbr>Policy<wbr>Rule<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}A `filter` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleaction">Get<wbr>Policy<wbr>Rule<wbr>Action[]</a></span>
    </dt>
    <dd>{{% md %}}An `actions` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Boolean to specify whether the rule is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrulefilter">Get<wbr>Policy<wbr>Rule<wbr>Filter[]</a></span>
    </dt>
    <dd>{{% md %}}A `filter` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleaction">List[Get<wbr>Policy<wbr>Rule<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}An `actions` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean to specify whether the rule is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyrulefilter">List[Get<wbr>Policy<wbr>Rule<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}A `filter` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Rule<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetPolicyRuleAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetPolicyRuleAction">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Base<wbr>Blobs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionbaseblob">List&lt;Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Base<wbr>Blob<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `base_blob` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshots</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionsnapshot">List&lt;Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Snapshot<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `snapshot` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Base<wbr>Blobs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionbaseblob">[]Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Base<wbr>Blob</a></span>
    </dt>
    <dd>{{% md %}}A `base_blob` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshots</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionsnapshot">[]Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Snapshot</a></span>
    </dt>
    <dd>{{% md %}}A `snapshot` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>base<wbr>Blobs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionbaseblob">Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Base<wbr>Blob[]</a></span>
    </dt>
    <dd>{{% md %}}A `base_blob` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshots</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionsnapshot">Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Snapshot[]</a></span>
    </dt>
    <dd>{{% md %}}A `snapshot` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>base<wbr>Blobs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionbaseblob">List[Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Base<wbr>Blob]</a></span>
    </dt>
    <dd>{{% md %}}A `base_blob` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshots</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicyruleactionsnapshot">List[Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Snapshot]</a></span>
    </dt>
    <dd>{{% md %}}A `snapshot` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Base<wbr>Blob</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetPolicyRuleActionBaseBlob">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetPolicyRuleActionBaseBlob">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to delete the blob.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier<wbr>To<wbr>Archive<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier<wbr>To<wbr>Cool<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to delete the blob.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier<wbr>To<wbr>Archive<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier<wbr>To<wbr>Cool<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to delete the blob.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier<wbr>To<wbr>Archive<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier<wbr>To<wbr>Cool<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to delete the blob.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier<wbr>To<wbr>Archive<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier<wbr>To<wbr>Cool<wbr>After<wbr>Days<wbr>Since<wbr>Modification<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Rule<wbr>Action<wbr>Snapshot</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetPolicyRuleActionSnapshot">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetPolicyRuleActionSnapshot">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>After<wbr>Days<wbr>Since<wbr>Creation<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after create to delete the snaphot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>After<wbr>Days<wbr>Since<wbr>Creation<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The age in days after create to delete the snaphot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>After<wbr>Days<wbr>Since<wbr>Creation<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The age in days after create to delete the snaphot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>After<wbr>Days<wbr>Since<wbr>Creation<wbr>Greater<wbr>Than</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The age in days after create to delete the snaphot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Rule<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetPolicyRuleFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetPolicyRuleFilter">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}An array of predefined values. Only `blockBlob` is supported.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}An array of strings for prefixes to be matched.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of predefined values. Only `blockBlob` is supported.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of strings for prefixes to be matched.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}An array of predefined values. Only `blockBlob` is supported.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}An array of strings for prefixes to be matched.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of predefined values. Only `blockBlob` is supported.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of strings for prefixes to be matched.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







