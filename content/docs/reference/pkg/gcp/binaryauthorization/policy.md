
---
title: "Policy"
block_external_search_index: true
---



A policy for container image binary authorization.


To get more information about Policy, see:

* [API documentation](https://cloud.google.com/binary-authorization/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/binary-authorization/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/binary_authorization_policy.html.markdown.



## Create a Policy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/binaryauthorization/#Policy">Policy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/binaryauthorization/#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Policy</span><span class="p">(resource_name, opts=None, </span>admission_whitelist_patterns=None<span class="p">, </span>cluster_admission_rules=None<span class="p">, </span>default_admission_rule=None<span class="p">, </span>description=None<span class="p">, </span>global_policy_evaluation_mode=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Binaryauthorization.Policy.html">Policy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BinaryAuthorization.PolicyArgs.html">PolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List&lt;Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List&lt;Policy<wbr>Cluster<wbr>Admission<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">[]Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">[]Policy<wbr>Cluster<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern[]?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">Policy<wbr>Cluster<wbr>Admission<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admission_<wbr>whitelist_<wbr>patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List[Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern]</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>admission_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List[Policy<wbr>Cluster<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default_<wbr>admission_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Dict[Policy<wbr>Default<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>global_<wbr>policy_<wbr>evaluation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}







## Policy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List&lt;Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List&lt;Policy<wbr>Cluster<wbr>Admission<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">[]Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">[]Policy<wbr>Cluster<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern[]?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">Policy<wbr>Cluster<wbr>Admission<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admission_<wbr>whitelist_<wbr>patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List[Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern]</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>admission_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List[Policy<wbr>Cluster<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>admission_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Dict[Policy<wbr>Default<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>global_<wbr>policy_<wbr>evaluation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}








## Look up an Existing Policy Resource

Get an existing Policy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/binaryauthorization/#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/binaryauthorization/#Policy">Policy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admission_whitelist_patterns=None<span class="p">, </span>cluster_admission_rules=None<span class="p">, </span>default_admission_rule=None<span class="p">, </span>description=None<span class="p">, </span>global_policy_evaluation_mode=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Binaryauthorization.Policy.html">Policy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Binaryauthorization.PolicyState.html">PolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List&lt;Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List&lt;Policy<wbr>Cluster<wbr>Admission<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">[]Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">[]Policy<wbr>Cluster<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">*Policy<wbr>Default<wbr>Admission<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admission<wbr>Whitelist<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern[]?</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Admission<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">Policy<wbr>Cluster<wbr>Admission<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Admission<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Policy<wbr>Default<wbr>Admission<wbr>Rule?</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>global<wbr>Policy<wbr>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admission_<wbr>whitelist_<wbr>patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyadmissionwhitelistpattern">List[Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern]</a></span>
    </dt>
    <dd>{{% md %}}A whitelist of image patterns to exclude from admission rules. If an image's name matches a whitelist pattern, the
image's admission requests will always be permitted regardless of your admission rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>admission_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyclusteradmissionrule">List[Policy<wbr>Cluster<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Per-cluster admission rules. An admission rule specifies either that all container images used in a pod creation request
must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be
denied. There can be at most one admission rule per cluster spec. Identifier format: '{{location}}.{{clusterId}}'. A
location is either a compute zone (e.g. 'us-central1-a') or a region (e.g. 'us-central1').
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>admission_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policydefaultadmissionrule">Dict[Policy<wbr>Default<wbr>Admission<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Default admission rule for a cluster without a per-cluster admission rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A descriptive comment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>global_<wbr>policy_<wbr>evaluation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not
covered by the global policy will be subject to the project admission policy.
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

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Policy<wbr>Admission<wbr>Whitelist<wbr>Pattern</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyAdmissionWhitelistPattern">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyAdmissionWhitelistPattern">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyAdmissionWhitelistPatternArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyAdmissionWhitelistPatternOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>Cluster<wbr>Admission<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyClusterAdmissionRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyClusterAdmissionRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyClusterAdmissionRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyClusterAdmissionRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Attestations<wbr>Bies</span>
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
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>Default<wbr>Admission<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyDefaultAdmissionRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyDefaultAdmissionRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyDefaultAdmissionRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/binaryauthorization?tab=doc#PolicyDefaultAdmissionRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Attestations<wbr>Bies</span>
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
        <span>enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enforcement<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>evaluation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Attestations<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
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

