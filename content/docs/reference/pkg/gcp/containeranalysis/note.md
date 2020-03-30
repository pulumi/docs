
---
title: "Note"
block_external_search_index: true
---

Provides a detailed description of a Note.


To get more information about Note, see:

* [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/container-analysis/)

## Example Usage - Container Analysis Note Basic


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const note = new gcp.containeranalysis.Note("note", {
    attestationAuthority: {
        hint: {
            humanReadableName: "Attestor Note",
        },
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_analysis_note.html.markdown.



## Create a Note Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/containeranalysis/#Note">Note</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/containeranalysis/#NoteArgs">NoteArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Note</span><span class="p">(resource_name, opts=None, </span>attestation_authority=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNote<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteArgs">NoteArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#Note">Note</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Containeranalysis.Note.html">Note</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.ContainerAnalysis.Inputs.NoteArgs.html">NoteArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Pulumi.<wbr>Gcp.<wbr>Container<wbr>Analysis.<wbr>Inputs.<wbr>Note<wbr>Attestation<wbr>Authority<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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

    <dt class="property-required"
            title="Required">
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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

    <dt class="property-required"
            title="Required">
        <span>attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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

    <dt class="property-required"
            title="Required">
        <span>attestation_<wbr>authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Dict[Note<wbr>Attestation<wbr>Authority]</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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







## Note Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Pulumi.<wbr>Gcp.<wbr>Container<wbr>Analysis.<wbr>Outputs.<wbr>Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>attestation_<wbr>authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Dict[Note<wbr>Attestation<wbr>Authority]</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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








## Look up an Existing Note Resource

Get an existing Note resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/containeranalysis/#NoteState">NoteState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/containeranalysis/#Note">Note</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>attestation_authority=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNote<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteState">NoteState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#Note">Note</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Containeranalysis.Note.html">Note</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Containeranalysis.NoteState.html">NoteState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Pulumi.<wbr>Gcp.<wbr>Container<wbr>Analysis.<wbr>Inputs.<wbr>Note<wbr>Attestation<wbr>Authority<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>Attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">*Note<wbr>Attestation<wbr>Authority</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>attestation<wbr>Authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Note<wbr>Attestation<wbr>Authority?</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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
        <span>attestation_<wbr>authority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthority">Dict[Note<wbr>Attestation<wbr>Authority]</a></span>
    </dt>
    <dd>{{% md %}}Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one
AttestationAuthority for "QA" and one for "build". This Note is intended to act strictly as a grouping mechanism for the
attached Occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the
ability for a principle to attach an Occurrence to a given Note. It also provides a single point of lookup to find all
attached Attestation Occurrences, even if they don't all live in the same project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the note.
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

<h4>Note<wbr>Attestation<wbr>Authority</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NoteAttestationAuthority">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NoteAttestationAuthority">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteAttestationAuthorityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteAttestationAuthorityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Hint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthorityhint">Pulumi.<wbr>Gcp.<wbr>Container<wbr>Analysis.<wbr>Inputs.<wbr>Note<wbr>Attestation<wbr>Authority<wbr>Hint<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Hint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthorityhint">Note<wbr>Attestation<wbr>Authority<wbr>Hint</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthorityhint">Note<wbr>Attestation<wbr>Authority<wbr>Hint</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#noteattestationauthorityhint">Dict[Note<wbr>Attestation<wbr>Authority<wbr>Hint]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Note<wbr>Attestation<wbr>Authority<wbr>Hint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NoteAttestationAuthorityHint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NoteAttestationAuthorityHint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteAttestationAuthorityHintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/containeranalysis?tab=doc#NoteAttestationAuthorityHintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Human<wbr>Readable<wbr>Name</span>
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
        <span>Human<wbr>Readable<wbr>Name</span>
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
        <span>human<wbr>Readable<wbr>Name</span>
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
        <span>human<wbr>Readable<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







