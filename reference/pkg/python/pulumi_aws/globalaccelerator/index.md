<div class="section" id="module-pulumi_aws.globalaccelerator">
<span id="globalaccelerator"></span><h1>globalaccelerator<a class="headerlink" href="#module-pulumi_aws.globalaccelerator" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.globalaccelerator.Accelerator">
<em class="property">class </em><code class="descclassname">pulumi_aws.globalaccelerator.</code><code class="descname">Accelerator</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>attributes=None</em>, <em>enabled=None</em>, <em>ip_address_type=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator accelerator.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The attributes of the accelerator. Fields documented below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</li>
<li><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value for the address type must be <cite>IPV4</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the accelerator.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>The attributes of the accelerator. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_address_type">
<code class="descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The value for the address type must be <cite>IPV4</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_sets">
<code class="descname">ip_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address set associated with the accelerator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the accelerator.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
