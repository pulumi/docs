
---
title: "GetService"
block_external_search_index: true
---

Use this data source to access information about an existing API Management Service.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management.html.markdown.





## Using GetService

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getService<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#GetServiceArgs">GetServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#GetServiceResult">GetServiceResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_service(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#LookupServiceArgs">LookupServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#LookupServiceResult">LookupServiceResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetService </span><span class="p">{</span><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Apimanagement.GetServiceResult.html">GetServiceResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.ApiManagement.Inputs.GetServiceArgs.html">GetServiceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">}</span></code></pre></div>
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
    <dd>{{% md %}}The name of the API Management service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which the API Management Service exists.
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
    <dd>{{% md %}}The name of the API Management service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which the API Management Service exists.
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
    <dd>{{% md %}}The name of the API Management service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which the API Management Service exists.
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
    <dd>{{% md %}}The name of the API Management service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which the API Management Service exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetService Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getserviceadditionallocation">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Outputs.<wbr>Get<wbr>Service<wbr>Additional<wbr>Location&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_location` blocks as defined below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the API Management Service's Gateway.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfiguration">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Outputs.<wbr>Get<wbr>Service<wbr>Hostname<wbr>Configuration&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `hostname_configuration` block as defined below.
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
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Api<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the Management API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the plan's pricing tier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Sender<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email address from which the notification will be sent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Portal<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the Publisher Portal.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publisher<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email of Publisher/Company of the API Management Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publisher<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Publisher/Company of the API Management Service.
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
        <span>Scm<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SCM (Source Code Management) endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getserviceadditionallocation">[]Get<wbr>Service<wbr>Additional<wbr>Location</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_location` blocks as defined below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the API Management Service's Gateway.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfiguration">[]Get<wbr>Service<wbr>Hostname<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A `hostname_configuration` block as defined below.
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
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Api<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the Management API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the plan's pricing tier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Sender<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email address from which the notification will be sent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Portal<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the Publisher Portal.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publisher<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email of Publisher/Company of the API Management Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publisher<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Publisher/Company of the API Management Service.
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
        <span>Scm<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SCM (Source Code Management) endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getserviceadditionallocation">Get<wbr>Service<wbr>Additional<wbr>Location[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_location` blocks as defined below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the API Management Service's Gateway.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfiguration">Get<wbr>Service<wbr>Hostname<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}A `hostname_configuration` block as defined below.
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
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Api<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL for the Management API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the plan's pricing tier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification<wbr>Sender<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email address from which the notification will be sent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>portal<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the Publisher Portal.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publisher<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The email of Publisher/Company of the API Management Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publisher<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Publisher/Company of the API Management Service.
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
        <span>scm<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SCM (Source Code Management) endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getserviceadditionallocation">List[Get<wbr>Service<wbr>Additional<wbr>Location]</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_location` blocks as defined below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway_<wbr>regional_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL for the API Management Service's Gateway.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfiguration">List[Get<wbr>Service<wbr>Hostname<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A `hostname_configuration` block as defined below.
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
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>api_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL for the Management API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the plan's pricing tier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification_<wbr>sender_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The email address from which the notification will be sent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>portal_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL of the Publisher Portal.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publisher_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The email of Publisher/Company of the API Management Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publisher_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Publisher/Company of the API Management Service.
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
        <span>scm_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SCM (Source Code Management) endpoint.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags assigned to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

#### Get&lt;wbr&gt;Service&lt;wbr&gt;Additional&lt;wbr&gt;Location
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceAdditionalLocation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceAdditionalLocation">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>gateway<wbr>Regional<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>gateway_<wbr>regional_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Gateway URL of the API Management service in the Region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location name of the additional region among Azure Data center regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Service&lt;wbr&gt;Hostname&lt;wbr&gt;Configuration
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceHostnameConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceHostnameConfiguration">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Managements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationmanagement">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Inputs.<wbr>Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Management<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `management` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Portals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationportal">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Inputs.<wbr>Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Portal<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `portal` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationproxy">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Inputs.<wbr>Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Proxy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `proxy` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationscm">List&lt;Pulumi.<wbr>Azure.<wbr>Api<wbr>Management.<wbr>Inputs.<wbr>Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Scm<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `scm` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Managements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationmanagement">[]Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}One or more `management` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Portals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationportal">[]Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Portal</a></span>
    </dt>
    <dd>{{% md %}}One or more `portal` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationproxy">[]Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Proxy</a></span>
    </dt>
    <dd>{{% md %}}One or more `proxy` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationscm">[]Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Scm</a></span>
    </dt>
    <dd>{{% md %}}One or more `scm` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>managements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationmanagement">Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Management[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `management` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>portals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationportal">Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Portal[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `portal` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationproxy">Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Proxy[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `proxy` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationscm">Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Scm[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `scm` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>managements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationmanagement">List[Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Management]</a></span>
    </dt>
    <dd>{{% md %}}One or more `management` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>portals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationportal">List[Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Portal]</a></span>
    </dt>
    <dd>{{% md %}}One or more `portal` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationproxy">List[Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Proxy]</a></span>
    </dt>
    <dd>{{% md %}}One or more `proxy` blocks as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getservicehostnameconfigurationscm">List[Get<wbr>Service<wbr>Hostname<wbr>Configuration<wbr>Scm]</a></span>
    </dt>
    <dd>{{% md %}}One or more `scm` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Service&lt;wbr&gt;Hostname&lt;wbr&gt;Configuration&lt;wbr&gt;Management
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceHostnameConfigurationManagement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceHostnameConfigurationManagement">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key_<wbr>vault_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Service&lt;wbr&gt;Hostname&lt;wbr&gt;Configuration&lt;wbr&gt;Portal
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceHostnameConfigurationPortal">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceHostnameConfigurationPortal">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key_<wbr>vault_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Service&lt;wbr&gt;Hostname&lt;wbr&gt;Configuration&lt;wbr&gt;Proxy
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceHostnameConfigurationProxy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceHostnameConfigurationProxy">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Ssl<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the default SSL Binding?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Ssl<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the default SSL Binding?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Ssl<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is this the default SSL Binding?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Ssl<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the default SSL Binding?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key_<wbr>vault_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Service&lt;wbr&gt;Hostname&lt;wbr&gt;Configuration&lt;wbr&gt;Scm
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetServiceHostnameConfigurationScm">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#GetServiceHostnameConfigurationScm">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Hostname used for the SCM URL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key_<wbr>vault_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault Secret which contains the SSL Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>negotiate<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Client Certificate Negotiation enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







