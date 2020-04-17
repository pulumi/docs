---
title: Module inline
title_tag: Module inline | Package pulumi_okta | Python SDK
linktitle: inline
notitle: true
---

<div class="section" id="inline">
<h1>inline<a class="headerlink" href="#inline" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.inline"></span><dl class="class">
<dt id="pulumi_okta.inline.Hook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.inline.</code><code class="sig-name descname">Hook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth=None</em>, <em class="sig-param">channel=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.inline.Hook" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an inline hook.</p>
<p>This resource allows you to create and configure an inline hook.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Authentication required for inline hook request.</p></li>
<li><p><strong>channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Details of the endpoint the inline hook will hit.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Map of headers to send along in inline hook request.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The inline hook display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the endpoint.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Authentication secret.</p></li>
</ul>
<p>The <strong>channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request method to use. Default is <code class="docutils literal notranslate"><span class="pre">&quot;POST&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI the hook will hit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the endpoint.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Authentication secret.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.auth">
<code class="sig-name descname">auth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication required for inline hook request.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Authentication secret.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.channel">
<code class="sig-name descname">channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the endpoint the inline hook will hit.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request method to use. Default is <code class="docutils literal notranslate"><span class="pre">&quot;POST&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI the hook will hit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the endpoint.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.headers">
<code class="sig-name descname">headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of headers to send along in inline hook request.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Authentication secret.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The inline hook display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.inline.Hook.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.inline.Hook.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the endpoint.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.inline.Hook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth=None</em>, <em class="sig-param">channel=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.inline.Hook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Authentication required for inline hook request.</p></li>
<li><p><strong>channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Details of the endpoint the inline hook will hit.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Map of headers to send along in inline hook request.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The inline hook display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the endpoint.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Authentication secret.</p></li>
</ul>
<p>The <strong>channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request method to use. Default is <code class="docutils literal notranslate"><span class="pre">&quot;POST&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The type of hook to trigger. Currently only <code class="docutils literal notranslate"><span class="pre">&quot;HTTP&quot;</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI the hook will hit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the endpoint.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key to use for authentication, usually the header name, for example <code class="docutils literal notranslate"><span class="pre">&quot;Authorization&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Authentication secret.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.inline.Hook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.inline.Hook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.inline.Hook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.inline.Hook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
