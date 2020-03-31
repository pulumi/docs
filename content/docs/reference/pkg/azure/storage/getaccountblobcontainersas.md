
---
title: "GetAccountBlobContainerSAS"
block_external_search_index: true
---

Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Storage Account Blob Container.

Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account Blob Container.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account_blob_container_sas.html.markdown.





## Using GetAccountBlobContainerSAS

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAccountBlobContainerSAS<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/storage/#GetAccountBlobContainerSASArgs">GetAccountBlobContainerSASArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/storage/#GetAccountBlobContainerSASResult">GetAccountBlobContainerSASResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_account_blob_container_sas(</span>cache_control=None<span class="p">, </span>connection_string=None<span class="p">, </span>container_name=None<span class="p">, </span>content_disposition=None<span class="p">, </span>content_encoding=None<span class="p">, </span>content_language=None<span class="p">, </span>content_type=None<span class="p">, </span>expiry=None<span class="p">, </span>https_only=None<span class="p">, </span>ip_address=None<span class="p">, </span>permissions=None<span class="p">, </span>start=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAccountBlobContainerSAS<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#LookupAccountBlobContainerSASArgs">LookupAccountBlobContainerSASArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#LookupAccountBlobContainerSASResult">LookupAccountBlobContainerSASResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetAccountBlobContainerSAS </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Storage.GetAccountBlobContainerSASResult.html">GetAccountBlobContainerSASResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Storage.Inputs.GetAccountBlobContainerSASArgs.html">GetAccountBlobContainerSASArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Cache-Control` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of an `azure.storage.Account` resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Disposition` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Encoding` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Language` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Type` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Single ipv4 address or range (connected with a dash) of ipv4 addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `permissions` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `Cache-Control` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of an `azure.storage.Account` resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `Content-Disposition` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `Content-Encoding` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `Content-Language` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `Content-Type` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Single ipv4 address or range (connected with a dash) of ipv4 addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</a></span>
    </dt>
    <dd>{{% md %}}A `permissions` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Cache-Control` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of an `azure.storage.Account` resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Disposition` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Encoding` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Language` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `Content-Type` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Single ipv4 address or range (connected with a dash) of ipv4 addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</a></span>
    </dt>
    <dd>{{% md %}}A `permissions` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `Cache-Control` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of an `azure.storage.Account` resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>container_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `Content-Disposition` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `Content-Encoding` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `Content-Language` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `Content-Type` response header that is sent when this SAS token is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Single ipv4 address or range (connected with a dash) of ipv4 addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Dict[Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions]</a></span>
    </dt>
    <dd>{{% md %}}A `permissions` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetAccountBlobContainerSAS Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
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
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sas</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The computed Blob Container Shared Access Signature (SAS).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start</span>
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
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
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
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sas</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The computed Blob Container Shared Access Signature (SAS).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start</span>
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
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
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
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sas</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The computed Blob Container Shared Access Signature (SAS).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start</span>
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
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>container_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiry</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
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
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getaccountblobcontainersaspermissions">Dict[Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sas</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The computed Blob Container Shared Access Signature (SAS).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Account<wbr>Blob<wbr>Container<wbr>SASPermissions</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#GetAccountBlobContainerSASPermissions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAccountBlobContainerSASPermissions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetAccountBlobContainerSASPermissionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/storage?tab=doc#GetAccountBlobContainerSASPermissions">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Add</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Add permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Create permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Delete permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>List</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should List permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Read</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Read permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Write</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Write permissions be enabled for this SAS?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Add</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Add permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Create permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Delete permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>List</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should List permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Read</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Read permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Write</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Write permissions be enabled for this SAS?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>add</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should Add permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>create</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should Create permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should Delete permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>list</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should List permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>read</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should Read permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>write</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should Write permissions be enabled for this SAS?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>add</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Add permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Create permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Delete permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>list</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should List permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>read</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Read permissions be enabled for this SAS?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>write</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Write permissions be enabled for this SAS?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







