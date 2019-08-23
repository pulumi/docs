---
title: Package pulumi_dnsimple
---

<div class="section" id="pulumi-dnsimple">
<h1>Pulumi DNSimple<a class="headerlink" href="#pulumi-dnsimple" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-dnsimple/issues">pulumi/pulumi-dnsimple repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/issues">terraform-providers/terraform-provider-dnsimple repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_dnsimple"></span><dl class="class">
<dt id="pulumi_dnsimple.Provider">
<em class="property">class </em><code class="descclassname">pulumi_dnsimple.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account=None</em>, <em>email=None</em>, <em>token=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the dnsimple package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_dnsimple.Provider.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_dnsimple.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_dnsimple.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_dnsimple.Record">
<em class="property">class </em><code class="descclassname">pulumi_dnsimple.</code><code class="descname">Record</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DNSimple record resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add the record to</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The priority of the record - only useful for some record types</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL of the record</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the record</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/r/record.html.markdown">https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/r/record.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_dnsimple.Record.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to add the record to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.domain_id">
<code class="descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record - only useful for some record types</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_dnsimple.Record.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_dnsimple.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the record</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_dnsimple.Record.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>domain=None</em>, <em>domain_id=None</em>, <em>hostname=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] domain: The domain to add the record to
:param pulumi.Input[str] domain_id: The domain ID of the record
:param pulumi.Input[str] hostname: The FQDN of the record
:param pulumi.Input[str] name: The name of the record
:param pulumi.Input[str] priority: The priority of the record - only useful for some record types
:param pulumi.Input[str] ttl: The TTL of the record
:param pulumi.Input[str] type: The type of the record
:param pulumi.Input[str] value: The value of the record</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/r/record.html.markdown">https://github.com/terraform-providers/terraform-provider-dnsimple/blob/master/website/docs/r/record.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_dnsimple.Record.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_dnsimple.Record.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
