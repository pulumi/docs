---
title: Module containeranalysis
title_tag: Module containeranalysis | Package pulumi_gcp | Python SDK
linktitle: containeranalysis
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "gcp" >}}

<div class="section" id="containeranalysis">
<h1>containeranalysis<a class="headerlink" href="#containeranalysis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.containeranalysis"></span><dl class="py class">
<dt id="pulumi_gcp.containeranalysis.Note">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.containeranalysis.</code><code class="sig-name descname">Note</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation_authority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">long_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_note_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note" title="Permalink to this definition">¶</a></dt>
<dd><p>A Container Analysis note is a high-level piece of metadata that
describes a type of analysis that can be done for a resource.</p>
<p>To get more information about Note, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/container-analysis/api/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/container-analysis/">Official Documentation</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/docs/making-attestations">Creating Attestations (Occurrences)</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">note</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">containeranalysis</span><span class="o">.</span><span class="n">Note</span><span class="p">(</span><span class="s2">&quot;note&quot;</span><span class="p">,</span> <span class="n">attestation_authority</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;hint&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;humanReadableName&quot;</span><span class="p">:</span> <span class="s2">&quot;Attestor Note&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">note</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">containeranalysis</span><span class="o">.</span><span class="n">Note</span><span class="p">(</span><span class="s2">&quot;note&quot;</span><span class="p">,</span>
    <span class="n">attestation_authority</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;hint&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;humanReadableName&quot;</span><span class="p">:</span> <span class="s2">&quot;Attestor Note&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">expiration_time</span><span class="o">=</span><span class="s2">&quot;2120-10-02T15:01:23.045123456Z&quot;</span><span class="p">,</span>
    <span class="n">long_description</span><span class="o">=</span><span class="s2">&quot;a longer description of test note&quot;</span><span class="p">,</span>
    <span class="n">related_urls</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
            <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;some.url&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;google.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">short_description</span><span class="o">=</span><span class="s2">&quot;test note&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of expiration for this note. Leave empty if note does not expire.</p></li>
<li><p><strong>long_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A detailed description of the note</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the note.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>related_note_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of other notes related to this note.</p></li>
<li><p><strong>related_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs associated with this note and related metadata.  Structure is documented below.</p></li>
<li><p><strong>short_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A one sentence description of the note.</p></li>
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
<p>The <strong>related_urls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Label to describe usage of the URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specific URL associated with the resource.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.attestation_authority">
<code class="sig-name descname">attestation_authority</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.attestation_authority" title="Permalink to this definition">¶</a></dt>
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

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.create_time">
<code class="sig-name descname">create_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time this note was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of expiration for this note. Leave empty if note does not expire.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of analysis this note describes</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.long_description">
<code class="sig-name descname">long_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.long_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A detailed description of the note</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the note.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.related_note_names">
<code class="sig-name descname">related_note_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.related_note_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of other notes related to this note.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.related_urls">
<code class="sig-name descname">related_urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.related_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>URLs associated with this note and related metadata.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Label to describe usage of the URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specific URL associated with the resource.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.short_description">
<code class="sig-name descname">short_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.short_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A one sentence description of the note.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Note.update_time">
<code class="sig-name descname">update_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time this note was last updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Note.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation_authority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">long_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_note_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time this note was created.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of expiration for this note. Leave empty if note does not expire.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of analysis this note describes</p></li>
<li><p><strong>long_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A detailed description of the note</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the note.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>related_note_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Names of other notes related to this note.</p></li>
<li><p><strong>related_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs associated with this note and related metadata.  Structure is documented below.</p></li>
<li><p><strong>short_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A one sentence description of the note.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time this note was last updated.</p></li>
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
<p>The <strong>related_urls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Label to describe usage of the URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specific URL associated with the resource.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Note.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Note.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_gcp.containeranalysis.Occurence">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.containeranalysis.</code><code class="sig-name descname">Occurence</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remediation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence" title="Permalink to this definition">¶</a></dt>
<dd><p>An occurrence is an instance of a Note, or type of analysis that
can be done for a resource.</p>
<p>To get more information about Occurrence, see:</p>
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
<li><p><strong>attestation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Occurrence that represents a single “attestation”. The authenticity
of an attestation can be verified using the attached signature.
If the verifier trusts the public key of the signer, then verifying
the signature is sufficient to establish trust. In this circumstance,
the authority to which this attestation is attached is primarily
useful for lookup (how to find this attestation if you already
know the authority and artifact to be verified) and intent (for
which authority this attestation was intended to sign.  Structure is documented below.</p></li>
<li><p><strong>note_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The analysis note associated with this occurrence, in the form of
projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
filter in list requests.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>remediation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of actions that can be taken to remedy the note.</p></li>
<li><p><strong>resource_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Immutable. A URI that represents the resource for which
the occurrence applies. For example,
<a class="reference external" href="https://gcr.io/project/image&#64;sha256:123abc">https://gcr.io/project/image&#64;sha256:123abc</a> for a Docker image.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serializedPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The serialized payload that is verified by one or
more signatures. A base64-encoded string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more signatures over serializedPayload.
Verifier implementations should consider this attestation
message verified if at least one signature verifies
serializedPayload. See Signature in common.proto for more
details on signature structure and verification.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for the public key that verifies this
signature. MUST be an RFC3986 conformant
URI. * When possible, the key id should be an
immutable reference, such as a cryptographic digest.
Examples of valid values:</p>
<ul>
<li><p>OpenPGP V4 public key fingerprint. See <a class="reference external" href="https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr">https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr</a>
for more details on this scheme.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA</span></code></p></li>
<li><p>RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):</p></li>
<li><p>“ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">signature</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content of the signature, an opaque bytestring.
The payload that this signature verifies MUST be
unambiguously provided with the Signature during
verification. A wrapper message might provide the
payload explicitly. Alternatively, a message might
have a canonical serialization that can always be
unambiguously computed to derive the payload.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.attestation">
<code class="sig-name descname">attestation</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.attestation" title="Permalink to this definition">¶</a></dt>
<dd><p>Occurrence that represents a single “attestation”. The authenticity
of an attestation can be verified using the attached signature.
If the verifier trusts the public key of the signer, then verifying
the signature is sufficient to establish trust. In this circumstance,
the authority to which this attestation is attached is primarily
useful for lookup (how to find this attestation if you already
know the authority and artifact to be verified) and intent (for
which authority this attestation was intended to sign.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serializedPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The serialized payload that is verified by one or
more signatures. A base64-encoded string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more signatures over serializedPayload.
Verifier implementations should consider this attestation
message verified if at least one signature verifies
serializedPayload. See Signature in common.proto for more
details on signature structure and verification.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for the public key that verifies this
signature. MUST be an RFC3986 conformant
URI. * When possible, the key id should be an
immutable reference, such as a cryptographic digest.
Examples of valid values:</p>
<ul>
<li><p>OpenPGP V4 public key fingerprint. See <a class="reference external" href="https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr">https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr</a>
for more details on this scheme.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA</span></code></p></li>
<li><p>RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):</p></li>
<li><p>“ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">signature</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content of the signature, an opaque bytestring.
The payload that this signature verifies MUST be
unambiguously provided with the Signature during
verification. A wrapper message might provide the
payload explicitly. Alternatively, a message might
have a canonical serialization that can always be
unambiguously computed to derive the payload.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.create_time">
<code class="sig-name descname">create_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the repository was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The note kind which explicitly denotes which of the occurrence details are specified. This field can be used as a filter
in list requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the occurrence.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.note_name">
<code class="sig-name descname">note_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.note_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The analysis note associated with this occurrence, in the form of
projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
filter in list requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.remediation">
<code class="sig-name descname">remediation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.remediation" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of actions that can be taken to remedy the note.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.resource_uri">
<code class="sig-name descname">resource_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.resource_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. Immutable. A URI that represents the resource for which
the occurrence applies. For example,
<a class="reference external" href="https://gcr.io/project/image&#64;sha256:123abc">https://gcr.io/project/image&#64;sha256:123abc</a> for a Docker image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.containeranalysis.Occurence.update_time">
<code class="sig-name descname">update_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the repository was last updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Occurence.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attestation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remediation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Occurence resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attestation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Occurrence that represents a single “attestation”. The authenticity
of an attestation can be verified using the attached signature.
If the verifier trusts the public key of the signer, then verifying
the signature is sufficient to establish trust. In this circumstance,
the authority to which this attestation is attached is primarily
useful for lookup (how to find this attestation if you already
know the authority and artifact to be verified) and intent (for
which authority this attestation was intended to sign.  Structure is documented below.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the repository was created.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The note kind which explicitly denotes which of the occurrence details are specified. This field can be used as a filter
in list requests.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the occurrence.</p></li>
<li><p><strong>note_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The analysis note associated with this occurrence, in the form of
projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
filter in list requests.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>remediation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of actions that can be taken to remedy the note.</p></li>
<li><p><strong>resource_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Immutable. A URI that represents the resource for which
the occurrence applies. For example,
<a class="reference external" href="https://gcr.io/project/image&#64;sha256:123abc">https://gcr.io/project/image&#64;sha256:123abc</a> for a Docker image.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the repository was last updated.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attestation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serializedPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The serialized payload that is verified by one or
more signatures. A base64-encoded string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signatures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more signatures over serializedPayload.
Verifier implementations should consider this attestation
message verified if at least one signature verifies
serializedPayload. See Signature in common.proto for more
details on signature structure and verification.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for the public key that verifies this
signature. MUST be an RFC3986 conformant
URI. * When possible, the key id should be an
immutable reference, such as a cryptographic digest.
Examples of valid values:</p>
<ul>
<li><p>OpenPGP V4 public key fingerprint. See <a class="reference external" href="https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr">https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr</a>
for more details on this scheme.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA</span></code></p></li>
<li><p>RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization):</p></li>
<li><p>“ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">signature</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content of the signature, an opaque bytestring.
The payload that this signature verifies MUST be
unambiguously provided with the Signature during
verification. A wrapper message might provide the
payload explicitly. Alternatively, a message might
have a canonical serialization that can always be
unambiguously computed to derive the payload.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Occurence.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.containeranalysis.Occurence.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Occurence.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
