---
title: Module containeranalysis
title_tag: Module containeranalysis | Package pulumi_gcp | Python SDK
linktitle: containeranalysis
notitle: true
---

<div class="section" id="containeranalysis">
<h1>containeranalysis<a class="headerlink" href="#containeranalysis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.containeranalysis"></span><dl class="class">
<dt id="pulumi_gcp.containeranalysis.Note">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.containeranalysis.</code><code class="sig-name descname">Note</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestation_authority=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a detailed description of a Note.</p>
<p>To get more information about Note, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/container-analysis/api/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/container-analysis/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestation_authority</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Note kind that represents a logical attestation “role” or “authority”.
For example, an organization might have one AttestationAuthority for
“QA” and one for “build”. This Note is intended to act strictly as a
grouping mechanism for the attached Occurrences (Attestations). This
grouping mechanism also provides a security boundary, since IAM ACLs
gate the ability for a principle to attach an Occurrence to a given
Note. It also provides a single point of lookup to find all attached
Attestation Occurrences, even if they don’t all live in the same
project.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the note.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation_authority</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This submessage provides human-readable hints about the purpose of
the AttestationAuthority. Because the name of a Note acts as its
resource reference, it is important to disambiguate the canonical
name of the Note (which might be a UUID for security purposes)
from “readable” names more suitable for debug output. Note that
these hints should NOT be used to look up AttestationAuthorities
in security sensitive contexts, such as when looking up
Attestations to verify.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">humanReadableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The human readable name of this Attestation Authority, for
example “qa”.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.containeranalysis.Note.attestation_authority">
<code class="sig-name descname">attestation_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.attestation_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Note kind that represents a logical attestation “role” or “authority”.
For example, an organization might have one AttestationAuthority for
“QA” and one for “build”. This Note is intended to act strictly as a
grouping mechanism for the attached Occurrences (Attestations). This
grouping mechanism also provides a security boundary, since IAM ACLs
gate the ability for a principle to attach an Occurrence to a given
Note. It also provides a single point of lookup to find all attached
Attestation Occurrences, even if they don’t all live in the same
project.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hint</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - This submessage provides human-readable hints about the purpose of
the AttestationAuthority. Because the name of a Note acts as its
resource reference, it is important to disambiguate the canonical
name of the Note (which might be a UUID for security purposes)
from “readable” names more suitable for debug output. Note that
these hints should NOT be used to look up AttestationAuthorities
in security sensitive contexts, such as when looking up
Attestations to verify.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">humanReadableName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The human readable name of this Attestation Authority, for
example “qa”.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.containeranalysis.Note.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the note.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.containeranalysis.Note.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.containeranalysis.Note.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attestation_authority=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Note resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestation_authority</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Note kind that represents a logical attestation “role” or “authority”.
For example, an organization might have one AttestationAuthority for
“QA” and one for “build”. This Note is intended to act strictly as a
grouping mechanism for the attached Occurrences (Attestations). This
grouping mechanism also provides a security boundary, since IAM ACLs
gate the ability for a principle to attach an Occurrence to a given
Note. It also provides a single point of lookup to find all attached
Attestation Occurrences, even if they don’t all live in the same
project.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the note.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation_authority</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This submessage provides human-readable hints about the purpose of
the AttestationAuthority. Because the name of a Note acts as its
resource reference, it is important to disambiguate the canonical
name of the Note (which might be a UUID for security purposes)
from “readable” names more suitable for debug output. Note that
these hints should NOT be used to look up AttestationAuthorities
in security sensitive contexts, such as when looking up
Attestations to verify.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">humanReadableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The human readable name of this Attestation Authority, for
example “qa”.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.containeranalysis.Note.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.containeranalysis.Note.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
