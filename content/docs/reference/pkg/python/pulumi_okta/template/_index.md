---
title: Module template
title_tag: Module template | Package pulumi_okta | Python SDK
linktitle: template
notitle: true
---

<div class="section" id="template">
<h1>template<a class="headerlink" href="#template" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.template"></span><dl class="class">
<dt id="pulumi_okta.template.Email">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.template.</code><code class="sig-name descname">Email</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_language=None</em>, <em class="sig-param">translations=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.template.Email" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta Email Template.</p>
<p>This resource allows you to create and configure an Okta Email Template.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default language, by default is set to <code class="docutils literal notranslate"><span class="pre">&quot;en&quot;</span></code>.</p></li>
<li><p><strong>translations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of translations for particular template.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email template type</p></li>
</ul>
</dd>
</dl>
<p>The <strong>translations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">language</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The language to map tthe template to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email subject line.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email body.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/template_email.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/template_email.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.template.Email.default_language">
<code class="sig-name descname">default_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.template.Email.default_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The default language, by default is set to <code class="docutils literal notranslate"><span class="pre">&quot;en&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.template.Email.translations">
<code class="sig-name descname">translations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.template.Email.translations" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of translations for particular template.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">language</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The language to map tthe template to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email subject line.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email body.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.template.Email.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.template.Email.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Email template type</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.template.Email.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_language=None</em>, <em class="sig-param">translations=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.template.Email.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Email resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default language, by default is set to <code class="docutils literal notranslate"><span class="pre">&quot;en&quot;</span></code>.</p></li>
<li><p><strong>translations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of translations for particular template.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email template type</p></li>
</ul>
</dd>
</dl>
<p>The <strong>translations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">language</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The language to map tthe template to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email subject line.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email body.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/template_email.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/template_email.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.template.Email.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.template.Email.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.template.Email.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.template.Email.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
