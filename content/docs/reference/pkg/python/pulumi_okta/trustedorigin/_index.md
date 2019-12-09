---
title: Module trustedorigin
title_tag: Module trustedorigin | Package pulumi_okta | Python SDK
linktitle: trustedorigin
notitle: true
---

<div class="section" id="trustedorigin">
<h1>trustedorigin<a class="headerlink" href="#trustedorigin" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.trustedorigin"></span><dl class="class">
<dt id="pulumi_okta.trustedorigin.Origin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.trustedorigin.</code><code class="sig-name descname">Origin</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Trusted Origin.</p>
<p>This resource allows you to create and configure an Trusted Origin.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the Trusted Origin is active or not - can only be issued post-creation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Trusted Origin Resource.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The origin to trust.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scopes of the Trusted Origin - can be <code class="docutils literal notranslate"><span class="pre">&quot;CORS&quot;</span></code> and/or <code class="docutils literal notranslate"><span class="pre">&quot;REDIRECT&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/trusted_origin.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/trusted_origin.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.trustedorigin.Origin.active">
<code class="sig-name descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the Trusted Origin is active or not - can only be issued post-creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.trustedorigin.Origin.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Trusted Origin Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.trustedorigin.Origin.origin">
<code class="sig-name descname">origin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The origin to trust.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.trustedorigin.Origin.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Scopes of the Trusted Origin - can be <code class="docutils literal notranslate"><span class="pre">&quot;CORS&quot;</span></code> and/or <code class="docutils literal notranslate"><span class="pre">&quot;REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.trustedorigin.Origin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">scopes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Origin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the Trusted Origin is active or not - can only be issued post-creation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Trusted Origin Resource.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The origin to trust.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scopes of the Trusted Origin - can be <code class="docutils literal notranslate"><span class="pre">&quot;CORS&quot;</span></code> and/or <code class="docutils literal notranslate"><span class="pre">&quot;REDIRECT&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/trusted_origin.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/trusted_origin.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.trustedorigin.Origin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.trustedorigin.Origin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.trustedorigin.Origin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
