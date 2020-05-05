---
title: Module profile
title_tag: Module profile | Package pulumi_okta | Python SDK
linktitle: profile
notitle: true
---

<div class="section" id="profile">
<h1>profile<a class="headerlink" href="#profile" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.profile"></span><dl class="py class">
<dt id="pulumi_okta.profile.Mapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.profile.</code><code class="sig-name descname">Mapping</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_when_absent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.profile.Mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Mapping resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] delete_when_absent: When turned on this flag will trigger the provider to delete mapping properties that are not defined in config. By</p>
<blockquote>
<div><p>default, we do not delete missing properties.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source id of the mapping to manage.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target id of the mapping to manage.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pushStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.profile.Mapping.delete_when_absent">
<code class="sig-name descname">delete_when_absent</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.profile.Mapping.delete_when_absent" title="Permalink to this definition">¶</a></dt>
<dd><p>When turned on this flag will trigger the provider to delete mapping properties that are not defined in config. By
default, we do not delete missing properties.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.profile.Mapping.source_id">
<code class="sig-name descname">source_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.profile.Mapping.source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The source id of the mapping to manage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.profile.Mapping.target_id">
<code class="sig-name descname">target_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.profile.Mapping.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The target id of the mapping to manage.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.profile.Mapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_when_absent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.profile.Mapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Mapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_when_absent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When turned on this flag will trigger the provider to delete mapping properties that are not defined in config. By
default, we do not delete missing properties.</p></li>
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source id of the mapping to manage.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target id of the mapping to manage.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pushStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.profile.Mapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.profile.Mapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.profile.Mapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.profile.Mapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
