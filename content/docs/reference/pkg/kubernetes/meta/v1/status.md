
---
title: "Status"
block_external_search_index: true
---



Status is a return value for calls that don't return other objects.


## Create a Status Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/meta/v1/#Status">Status</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Status">Status</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Status</span><span class="p">(resource_name, opts=None, </span>code=None<span class="p">, </span>details=None<span class="p">, </span>message=None<span class="p">, </span>metadata=None<span class="p">, </span>reason=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewStatus<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#StatusArgs">StatusArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#Status">Status</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Meta.V1.Status.html">Status</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Types.Inputs.Meta.V1.StatusArgs.html">StatusArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Suggested HTTP return code for this status, 0 if not set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statusdetails">Status<wbr>Details<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the status of this operation.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Suggested HTTP return code for this status, 0 if not set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statusdetails">*Status<wbr>Details</a></span>
    </dt>
    <dd>{{% md %}}Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the status of this operation.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">*List<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Suggested HTTP return code for this status, 0 if not set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statusdetails">Status<wbr>Details?</a></span>
    </dt>
    <dd>{{% md %}}Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the status of this operation.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">List<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Suggested HTTP return code for this status, 0 if not set.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statusdetails">Dict[Status<wbr>Details]</a></span>
    </dt>
    <dd>{{% md %}}Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the status of this operation.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listmeta">Dict[List<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Status Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status{{% /md %}}</dd>

</dl>
{{% /choosable %}}












## Supporting Types

<h4>List<wbr>Meta</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ListMeta">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ListMeta">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ListMetaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ListMetaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remaining<wbr>Item<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue_</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remaining_<wbr>item_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}selfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Status<wbr>Cause</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#StatusCause">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#StatusCause">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#StatusCauseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#StatusCauseOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the cause of the error.  This field may be presented as-is to a reader.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of the cause of the error. If this value is empty there is no information available.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the cause of the error.  This field may be presented as-is to a reader.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of the cause of the error. If this value is empty there is no information available.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the cause of the error.  This field may be presented as-is to a reader.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of the cause of the error. If this value is empty there is no information available.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-readable description of the cause of the error.  This field may be presented as-is to a reader.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A machine-readable description of the cause of the error. If this value is empty there is no information available.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Status<wbr>Details</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#StatusDetails">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#StatusDetails">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#StatusDetailsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#StatusDetailsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Causes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statuscause">List&lt;Status<wbr>Cause<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The group attribute of the resource associated with the status StatusReason.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>After<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Causes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statuscause">[]Status<wbr>Cause</a></span>
    </dt>
    <dd>{{% md %}}The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The group attribute of the resource associated with the status StatusReason.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>After<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>causes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statuscause">Status<wbr>Cause[]?</a></span>
    </dt>
    <dd>{{% md %}}The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The group attribute of the resource associated with the status StatusReason.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>After<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>causes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#statuscause">List[Status<wbr>Cause]</a></span>
    </dt>
    <dd>{{% md %}}The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The group attribute of the resource associated with the status StatusReason.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>after_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-kubernetes">https://github.com/pulumi/pulumi-kubernetes</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

