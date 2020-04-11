
---
title: "BackendService"
block_external_search_index: true
---



A Backend Service defines a group of virtual machines that will serve
traffic for load balancing. This resource is a global backend service,
appropriate for external load balancing or self-managed internal load balancing.
For managed internal load balancing, use a regional backend service instead.

Currently self-managed internal load balancing is only available in beta.


To get more information about BackendService, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/v1/backendServices)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service.html.markdown.



## Create a BackendService Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendService">BackendService</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendServiceArgs">BackendServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BackendService</span><span class="p">(resource_name, opts=None, </span>affinity_cookie_ttl_sec=None<span class="p">, </span>backends=None<span class="p">, </span>cdn_policy=None<span class="p">, </span>circuit_breakers=None<span class="p">, </span>connection_draining_timeout_sec=None<span class="p">, </span>consistent_hash=None<span class="p">, </span>custom_request_headers=None<span class="p">, </span>description=None<span class="p">, </span>enable_cdn=None<span class="p">, </span>health_checks=None<span class="p">, </span>iap=None<span class="p">, </span>load_balancing_scheme=None<span class="p">, </span>locality_lb_policy=None<span class="p">, </span>log_config=None<span class="p">, </span>name=None<span class="p">, </span>outlier_detection=None<span class="p">, </span>port_name=None<span class="p">, </span>project=None<span class="p">, </span>protocol=None<span class="p">, </span>security_policy=None<span class="p">, </span>session_affinity=None<span class="p">, </span>timeout_sec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBackendService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceArgs">BackendServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendService">BackendService</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendService.html">BackendService</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendServiceArgs.html">BackendServiceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List&lt;Backend<wbr>Service<wbr>Backend<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">[]Backend<wbr>Service<wbr>Backend</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">*Backend<wbr>Service<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">*Backend<wbr>Service<wbr>Circuit<wbr>Breakers</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">*Backend<wbr>Service<wbr>Consistent<wbr>Hash</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">*Backend<wbr>Service<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">*Backend<wbr>Service<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">*Backend<wbr>Service<wbr>Outlier<wbr>Detection</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">Backend<wbr>Service<wbr>Backend[]?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>affinity_<wbr>cookie_<wbr>ttl_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List[Backend<wbr>Service<wbr>Backend]</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Dict[Backend<wbr>Service<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>circuit_<wbr>breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Dict[Backend<wbr>Service<wbr>Circuit<wbr>Breakers]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>draining_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consistent_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Dict[Backend<wbr>Service<wbr>Consistent<wbr>Hash]</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>request_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Dict[Backend<wbr>Service<wbr>Iap]</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancing_<wbr>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality_<wbr>lb_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Dict[Backend<wbr>Service<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outlier_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Dict[Backend<wbr>Service<wbr>Outlier<wbr>Detection]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## BackendService Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List&lt;Backend<wbr>Service<wbr>Backend&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">[]Backend<wbr>Service<wbr>Backend</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">*Backend<wbr>Service<wbr>Circuit<wbr>Breakers</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">*Backend<wbr>Service<wbr>Consistent<wbr>Hash</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">*Backend<wbr>Service<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">*Backend<wbr>Service<wbr>Outlier<wbr>Detection</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">Backend<wbr>Service<wbr>Backend[]?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>affinity_<wbr>cookie_<wbr>ttl_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List[Backend<wbr>Service<wbr>Backend]</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Dict[Backend<wbr>Service<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>circuit_<wbr>breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Dict[Backend<wbr>Service<wbr>Circuit<wbr>Breakers]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>draining_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>consistent_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Dict[Backend<wbr>Service<wbr>Consistent<wbr>Hash]</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>request_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health_<wbr>checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Dict[Backend<wbr>Service<wbr>Iap]</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load_<wbr>balancing_<wbr>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>locality_<wbr>lb_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Dict[Backend<wbr>Service<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>outlier_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Dict[Backend<wbr>Service<wbr>Outlier<wbr>Detection]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>session_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing BackendService Resource

Get an existing BackendService resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendServiceState">BackendServiceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendService">BackendService</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>affinity_cookie_ttl_sec=None<span class="p">, </span>backends=None<span class="p">, </span>cdn_policy=None<span class="p">, </span>circuit_breakers=None<span class="p">, </span>connection_draining_timeout_sec=None<span class="p">, </span>consistent_hash=None<span class="p">, </span>creation_timestamp=None<span class="p">, </span>custom_request_headers=None<span class="p">, </span>description=None<span class="p">, </span>enable_cdn=None<span class="p">, </span>fingerprint=None<span class="p">, </span>health_checks=None<span class="p">, </span>iap=None<span class="p">, </span>load_balancing_scheme=None<span class="p">, </span>locality_lb_policy=None<span class="p">, </span>log_config=None<span class="p">, </span>name=None<span class="p">, </span>outlier_detection=None<span class="p">, </span>port_name=None<span class="p">, </span>project=None<span class="p">, </span>protocol=None<span class="p">, </span>security_policy=None<span class="p">, </span>self_link=None<span class="p">, </span>session_affinity=None<span class="p">, </span>timeout_sec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBackendService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceState">BackendServiceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendService">BackendService</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendService.html">BackendService</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendServiceState.html">BackendServiceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List&lt;Backend<wbr>Service<wbr>Backend<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">[]Backend<wbr>Service<wbr>Backend</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">*Backend<wbr>Service<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">*Backend<wbr>Service<wbr>Circuit<wbr>Breakers</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">*Backend<wbr>Service<wbr>Consistent<wbr>Hash</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">*Backend<wbr>Service<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">*Backend<wbr>Service<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">*Backend<wbr>Service<wbr>Outlier<wbr>Detection</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>affinity<wbr>Cookie<wbr>Ttl<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">Backend<wbr>Service<wbr>Backend[]?</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>circuit<wbr>Breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Backend<wbr>Service<wbr>Circuit<wbr>Breakers?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Draining<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consistent<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Backend<wbr>Service<wbr>Consistent<wbr>Hash?</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Request<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Backend<wbr>Service<wbr>Iap?</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancing<wbr>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality<wbr>Lb<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Backend<wbr>Service<wbr>Log<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outlier<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Backend<wbr>Service<wbr>Outlier<wbr>Detection?</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>affinity_<wbr>cookie_<wbr>ttl_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and
lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the
load balancing scheme is INTERNAL, this field is not used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backends</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicebackend">List[Backend<wbr>Service<wbr>Backend]</a></span>
    </dt>
    <dd>{{% md %}}The set of backends that serve this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicy">Dict[Backend<wbr>Service<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>circuit_<wbr>breakers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakers">Dict[Backend<wbr>Service<wbr>Circuit<wbr>Breakers]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling the volume of connections to a backend service. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>draining_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Time for which instance will be drained (not accept new connections, but still work to finish started).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consistent_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthash">Dict[Backend<wbr>Service<wbr>Consistent<wbr>Hash]</a></span>
    </dt>
    <dd>{{% md %}}Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or
other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular
destination host will be lost when one or more hosts are added/removed from the destination service. This field
specifies parameters that control consistent hashing. This field only applies if the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED. This field is only applicable when locality_lb_policy is set to MAGLEV or RING_HASH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>request_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Headers that the HTTP/S load balancer should add to proxied requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendService.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>checks</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently
at most one health check can be specified, and a health check is required. For internal load balancing, a URL to a
HealthCheck resource must be specified instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceiap">Dict[Backend<wbr>Service<wbr>Iap]</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancing_<wbr>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the backend service will be used with internal or external load balancing. A backend service created
for one type of load balancing cannot be used with the other. Must be 'EXTERNAL' or 'INTERNAL_SELF_MANAGED' for a global
backend service. Defaults to 'EXTERNAL'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality_<wbr>lb_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancing algorithm used within the scope of the locality. The possible values are - ROUND_ROBIN - This is a
simple policy in which each healthy backend is selected in round robin order. LEAST_REQUEST - An O(1) algorithm which
selects two random healthy hosts and picks the host which has fewer active requests. RING_HASH - The ring/modulo hash
load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a
host from a set of N hosts only affects 1/N of the requests. RANDOM - The load balancer selects a random healthy host.
ORIGINAL_DESTINATION - Backend host is selected based on the client connection metadata, i.e., connections are opened to
the same address as the destination address of the incoming connection before the connection was redirected to the load
balancer. MAGLEV - used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash
but has faster table lookup build times and host selection times. For more information about Maglev, refer to
https://ai.google/research/pubs/pub44824 This field is applicable only when the load_balancing_scheme is set to
INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicelogconfig">Dict[Backend<wbr>Service<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}This field denotes the logging options for the load balancer traffic served by this backend service. If logging is
enabled, logs will be exported to Stackdriver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outlier_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetection">Dict[Backend<wbr>Service<wbr>Outlier<wbr>Detection]</a></span>
    </dt>
    <dd>{{% md %}}Settings controlling eviction of unhealthy hosts from the load balancing pool. This field is applicable only when the
load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the
load balancing scheme is EXTERNAL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, and
SSL. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if
used with the GA API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The security policy associated with this backend service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is
[1, 86400].
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Backend<wbr>Service<wbr>Backend</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceBackend">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceBackend">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceBackendArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceBackendOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Balancing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity<wbr>Scaler</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Balancing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacity<wbr>Scaler</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Rate<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>balancing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity<wbr>Scaler</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>balancing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacity<wbr>Scaler</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate<wbr>Per<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Rate<wbr>Per<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Cdn<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceCdnPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceCdnPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCdnPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCdnPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Key<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicycachekeypolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Cache<wbr>Key<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Key<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicycachekeypolicy">*Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Cache<wbr>Key<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Key<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicycachekeypolicy">Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Cache<wbr>Key<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Key<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecdnpolicycachekeypolicy">Dict[Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Cache<wbr>Key<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Cdn<wbr>Policy<wbr>Cache<wbr>Key<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceCdnPolicyCacheKeyPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceCdnPolicyCacheKeyPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCdnPolicyCacheKeyPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCdnPolicyCacheKeyPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Query<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>String<wbr>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>String<wbr>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Query<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>String<wbr>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>String<wbr>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Query<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>String<wbr>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>String<wbr>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Query<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>String<wbr>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>String<wbr>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Circuit<wbr>Breakers</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceCircuitBreakers">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceCircuitBreakers">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCircuitBreakersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCircuitBreakersOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakersconnecttimeout">Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Connect<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pending<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Requests<wbr>Per<wbr>Connection</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakersconnecttimeout">*Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Connect<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pending<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Requests<wbr>Per<wbr>Connection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakersconnecttimeout">Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Connect<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pending<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Requests<wbr>Per<wbr>Connection</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicecircuitbreakersconnecttimeout">Dict[Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Connect<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pending<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Requests<wbr>Per<wbr>Connection</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Circuit<wbr>Breakers<wbr>Connect<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceCircuitBreakersConnectTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceCircuitBreakersConnectTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCircuitBreakersConnectTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceCircuitBreakersConnectTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Consistent<wbr>Hash</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceConsistentHash">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceConsistentHash">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookie">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Ring<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookie">*Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Ring<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookie">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Ring<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookie">Dict[Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Ring<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceConsistentHashHttpCookie">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceConsistentHashHttpCookie">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashHttpCookieArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashHttpCookieOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookiettl">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Ttl<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookiettl">*Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Ttl</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookiettl">Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Ttl?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceconsistenthashhttpcookiettl">Dict[Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Ttl]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Consistent<wbr>Hash<wbr>Http<wbr>Cookie<wbr>Ttl</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceConsistentHashHttpCookieTtl">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceConsistentHashHttpCookieTtl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashHttpCookieTtlArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceConsistentHashHttpCookieTtlOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Iap</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceIap">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceIap">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceIapArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceIapOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Log<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceLogConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceLogConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceLogConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceLogConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sample<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sample<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sample<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sample<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Outlier<wbr>Detection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceOutlierDetection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceOutlierDetection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Base<wbr>Ejection<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectionbaseejectiontime">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Base<wbr>Ejection<wbr>Time<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Success<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectioninterval">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Interval<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ejection<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Minimum<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Request<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Stdev<wbr>Factor</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Base<wbr>Ejection<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectionbaseejectiontime">*Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Base<wbr>Ejection<wbr>Time</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforcing<wbr>Success<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectioninterval">*Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Interval</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ejection<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Minimum<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Request<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Rate<wbr>Stdev<wbr>Factor</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>base<wbr>Ejection<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectionbaseejectiontime">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Base<wbr>Ejection<wbr>Time?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Success<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectioninterval">Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Interval?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Ejection<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Minimum<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Request<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Stdev<wbr>Factor</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>base<wbr>Ejection<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectionbaseejectiontime">Dict[Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Base<wbr>Ejection<wbr>Time]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Consecutive<wbr>Errors</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Consecutive<wbr>Gateway<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforcing<wbr>Success<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserviceoutlierdetectioninterval">Dict[Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Interval]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Ejection<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Minimum<wbr>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Request<wbr>Volume</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Rate<wbr>Stdev<wbr>Factor</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Base<wbr>Ejection<wbr>Time</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceOutlierDetectionBaseEjectionTime">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceOutlierDetectionBaseEjectionTime">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionBaseEjectionTimeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionBaseEjectionTimeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Outlier<wbr>Detection<wbr>Interval</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendServiceOutlierDetectionInterval">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendServiceOutlierDetectionInterval">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionIntervalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendServiceOutlierDetectionIntervalOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

