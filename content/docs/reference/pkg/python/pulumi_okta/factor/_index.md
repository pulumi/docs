---
title: Module factor
title_tag: Module factor | Package pulumi_okta | Python SDK
linktitle: factor
notitle: true
---

<div class="section" id="factor">
<h1>factor<a class="headerlink" href="#factor" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.factor"></span><dl class="class">
<dt id="pulumi_okta.factor.Factor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.factor.</code><code class="sig-name descname">Factor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">provider_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.factor.Factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage the activation of Okta MFA methods.</p>
<p>This resource allows you to manage Okta MFA methods.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/factor.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/factor.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to activate the provider, by default it is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Factor provider ID</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.factor.Factor.active">
<code class="sig-name descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.factor.Factor.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to activate the provider, by default it is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.factor.Factor.provider_id">
<code class="sig-name descname">provider_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.factor.Factor.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Factor provider ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.factor.Factor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">provider_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.factor.Factor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Factor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to activate the provider, by default it is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Factor provider ID</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.factor.Factor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.factor.Factor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.factor.Factor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.factor.Factor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
