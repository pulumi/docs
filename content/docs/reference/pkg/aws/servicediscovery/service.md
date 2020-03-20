
---
title: "Service"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Service Discovery Service resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleVpc = new aws.ec2.Vpc("example", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
});
const examplePrivateDnsNamespace = new aws.servicediscovery.PrivateDnsNamespace("example", {
    description: "example",
    vpc: exampleVpc.id,
});
const exampleService = new aws.servicediscovery.Service("example", {
    dnsConfig: {
        dnsRecords: [{
            ttl: 10,
            type: "A",
        }],
        namespaceId: examplePrivateDnsNamespace.id,
        routingPolicy: "MULTIVALUE",
    },
    healthCheckCustomConfig: {
        failureThreshold: 1,
    },
});
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const examplePublicDnsNamespace = new aws.servicediscovery.PublicDnsNamespace("example", {
    description: "example",
});
const exampleService = new aws.servicediscovery.Service("example", {
    dnsConfig: {
        dnsRecords: [{
            ttl: 10,
            type: "A",
        }],
        namespaceId: examplePublicDnsNamespace.id,
    },
    healthCheckConfig: {
        failureThreshold: 10,
        resourcePath: "path",
        type: "HTTP",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_service.html.markdown.



## Create a Service Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/servicediscovery/#Service">Service</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/servicediscovery/#ServiceArgs">ServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Service</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>dns_config=None<span class="p">, </span>health_check_config=None<span class="p">, </span>health_check_custom_config=None<span class="p">, </span>name=None<span class="p">, </span>namespace_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceArgs">ServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#Service">Service</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.Service.html">Service</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceArgs.html">ServiceArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Service resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Dns<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">*Service<wbr>Dns<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">*Service<wbr>Health<wbr>Check<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">*Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">servicediscovery.<wbr>Service<wbr>Dns<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Dict[Service<wbr>Dns<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>custom_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Service Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Dns<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">*Service<wbr>Dns<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">*Service<wbr>Health<wbr>Check<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">*Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">servicediscovery.<wbr>Service<wbr>Dns<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Dict[Service<wbr>Dns<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>custom_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Service Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/servicediscovery/#ServiceState">ServiceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/servicediscovery/#Service">Service</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>dns_config=None<span class="p">, </span>health_check_config=None<span class="p">, </span>health_check_custom_config=None<span class="p">, </span>name=None<span class="p">, </span>namespace_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceState">ServiceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#Service">Service</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.Service.html">Service</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceState.html">ServiceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Service resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Dns<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">*Service<wbr>Dns<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">*Service<wbr>Health<wbr>Check<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">*Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">servicediscovery.<wbr>Service<wbr>Dns<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Custom<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">servicediscovery.<wbr>Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfig">Dict[Service<wbr>Dns<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for an optional health check. Only for Public DNS namespaces.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>custom_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#servicehealthcheckcustomconfig">Dict[Service<wbr>Health<wbr>Check<wbr>Custom<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A complex type that contains settings for ECS managed health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ServiceDnsConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ServiceDnsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ServiceDnsConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceDnsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceDnsConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceDnsConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceDnsConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Dns<wbr>Records</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfigdnsrecord">List&lt;Pulumi.<wbr>Aws.<wbr>Servicediscovery.<wbr>Service<wbr>Dns<wbr>Config<wbr>Dns<wbr>Record<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An array that contains one DnsRecord object for each resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Dns<wbr>Records</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfigdnsrecord">[]Service<wbr>Dns<wbr>Config<wbr>Dns<wbr>Record</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An array that contains one DnsRecord object for each resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">dns<wbr>Records</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfigdnsrecord">servicediscovery.<wbr>Service<wbr>Dns<wbr>Config<wbr>Dns<wbr>Record[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An array that contains one DnsRecord object for each resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">dns<wbr>Records</td>
            <td class="align-top">
                
                <code><a href="#servicednsconfigdnsrecord">List[Service<wbr>Dns<wbr>Config<wbr>Dns<wbr>Record]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An array that contains one DnsRecord object for each resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the namespace to use for DNS configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ServiceDnsConfigDnsRecord
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ServiceDnsConfigDnsRecord">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ServiceDnsConfigDnsRecord">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceDnsConfigDnsRecordArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceDnsConfigDnsRecordOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceDnsConfigDnsRecordArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceDnsConfigDnsRecord.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ServiceHealthCheckConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ServiceHealthCheckConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ServiceHealthCheckConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceHealthCheckConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceHealthCheckConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceHealthCheckConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceHealthCheckConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don&#39;t specify a value, the default value is /.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don&#39;t specify a value, the default value is /.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don&#39;t specify a value, the default value is /.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">failure_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don&#39;t specify a value, the default value is /.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ServiceHealthCheckCustomConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ServiceHealthCheckCustomConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ServiceHealthCheckCustomConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceHealthCheckCustomConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/servicediscovery?tab=doc#ServiceHealthCheckCustomConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceHealthCheckCustomConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Servicediscovery.ServiceHealthCheckCustomConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">failure<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">failure_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







