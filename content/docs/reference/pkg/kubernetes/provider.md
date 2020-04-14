
---
title: "Provider"
block_external_search_index: true
---



The provider type for the kubernetes package.


## Create a Provider Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/#Provider">Provider</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#Provider">Provider</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Provider</span><span class="p">(resource_name, opts=None, </span>cluster=None<span class="p">, </span>context=None<span class="p">, </span>enable_dry_run=None<span class="p">, </span>kubeconfig=None<span class="p">, </span>namespace=None<span class="p">, </span>suppress_deprecation_warnings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProvider<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/?tab=doc#ProviderArgs">ProviderArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/?tab=doc#Provider">Provider</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes..Provider.html">Provider</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Types.Inputs..ProviderArgs.html">ProviderArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig cluster to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig context to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dry<wbr>Run</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}BETA FEATURE - If present and set to true, enable server-side diff calculations.
This feature is in developer preview, and is disabled by default.

This config can be specified in the following ways, using this precedence:
1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubeconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The contents of a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the default namespace to use. This flag is ignored for cluster-scoped resources.

A namespace can be specified in multiple places, and the precedence is as follows:
1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suppress<wbr>Deprecation<wbr>Warnings</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If present and set to true, suppress apiVersion deprecation warnings from the CLI.

This config can be specified in the following ways, using this precedence:
1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig cluster to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig context to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dry<wbr>Run</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}BETA FEATURE - If present and set to true, enable server-side diff calculations.
This feature is in developer preview, and is disabled by default.

This config can be specified in the following ways, using this precedence:
1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubeconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The contents of a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If present, the default namespace to use. This flag is ignored for cluster-scoped resources.

A namespace can be specified in multiple places, and the precedence is as follows:
1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suppress<wbr>Deprecation<wbr>Warnings</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If present and set to true, suppress apiVersion deprecation warnings from the CLI.

This config can be specified in the following ways, using this precedence:
1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig cluster to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig context to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Dry<wbr>Run</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}BETA FEATURE - If present and set to true, enable server-side diff calculations.
This feature is in developer preview, and is disabled by default.

This config can be specified in the following ways, using this precedence:
1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubeconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The contents of a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If present, the default namespace to use. This flag is ignored for cluster-scoped resources.

A namespace can be specified in multiple places, and the precedence is as follows:
1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suppress<wbr>Deprecation<wbr>Warnings</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If present and set to true, suppress apiVersion deprecation warnings from the CLI.

This config can be specified in the following ways, using this precedence:
1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig cluster to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If present, the name of the kubeconfig context to use.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>dry_<wbr>run</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}BETA FEATURE - If present and set to true, enable server-side diff calculations.
This feature is in developer preview, and is disabled by default.

This config can be specified in the following ways, using this precedence:
1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubeconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The contents of a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If present, the default namespace to use. This flag is ignored for cluster-scoped resources.

A namespace can be specified in multiple places, and the precedence is as follows:
1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suppress_<wbr>deprecation_<wbr>warnings</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If present and set to true, suppress apiVersion deprecation warnings from the CLI.

This config can be specified in the following ways, using this precedence:
1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.{{% /md %}}</dd>

</dl>
{{% /choosable %}}















<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-kubernetes">https://github.com/pulumi/pulumi-kubernetes</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

