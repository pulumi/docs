---
title: Module securitycenter
title_tag: Module securitycenter | Package pulumi_gcp | Python SDK
linktitle: securitycenter
notitle: true
---

<div class="section" id="securitycenter">
<h1>securitycenter<a class="headerlink" href="#securitycenter" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.securitycenter"></span><dl class="class">
<dt id="pulumi_gcp.securitycenter.Source">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.securitycenter.</code><code class="sig-name descname">Source</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">organization=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.securitycenter.Source" title="Permalink to this definition">¶</a></dt>
<dd><p>A Cloud Security Command Center’s (Cloud SCC) finding source. A finding
source is an entity or a mechanism that can produce a finding. A source is
like a container of findings that come from the same scanner, logger,
monitor, etc.</p>
<p>To get more information about Source, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.sources">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/binary-authorization/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the source (max of 1024 characters).</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source’s display name. A source’s display name must be unique
amongst its siblings, for example, two sources with the same parent
can’t share the same display name. The display name must start and end
with a letter or digit, may contain letters, digits, spaces, hyphens,
and underscores, and can be no longer than 32 characters.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization whose Cloud Security Command Center the Source
lives in.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.securitycenter.Source.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the source (max of 1024 characters).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.securitycenter.Source.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The source’s display name. A source’s display name must be unique
amongst its siblings, for example, two sources with the same parent
can’t share the same display name. The display name must start and end
with a letter or digit, may contain letters, digits, spaces, hyphens,
and underscores, and can be no longer than 32 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.securitycenter.Source.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of this source, in the format ‘organizations/{{organization}}/sources/{{source}}’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.securitycenter.Source.organization">
<code class="sig-name descname">organization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization whose Cloud Security Command Center the Source
lives in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.securitycenter.Source.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">organization=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Source resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the source (max of 1024 characters).</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source’s display name. A source’s display name must be unique
amongst its siblings, for example, two sources with the same parent
can’t share the same display name. The display name must start and end
with a letter or digit, may contain letters, digits, spaces, hyphens,
and underscores, and can be no longer than 32 characters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of this source, in the format ‘organizations/{{organization}}/sources/{{source}}’.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization whose Cloud Security Command Center the Source
lives in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.securitycenter.Source.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.securitycenter.Source.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.securitycenter.Source.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
