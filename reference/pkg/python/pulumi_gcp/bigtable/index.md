<div class="section" id="module-pulumi_gcp.bigtable">
<span id="bigtable"></span><h1>bigtable<a class="headerlink" href="#module-pulumi_gcp.bigtable" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.bigtable.Instance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.bigtable.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>clusters=None</em>, <em>display_name=None</em>, <em>instance_type=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Bigtable instance. For more information see
<a class="reference external" href="https://cloud.google.com/bigtable/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigtable/docs/go/reference">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>clusters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable display name of the Bigtable instance. Defaults to the instance <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance type to create. One of <code class="docutils literal notranslate"><span class="pre">&quot;DEVELOPMENT&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.clusters">
<code class="descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable display name of the Bigtable instance. Defaults to the instance <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type to create. One of <code class="docutils literal notranslate"><span class="pre">&quot;DEVELOPMENT&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Table">
<em class="property">class </em><code class="descclassname">pulumi_gcp.bigtable.</code><code class="descname">Table</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>column_families=None</em>, <em>instance_name=None</em>, <em>name=None</em>, <em>project=None</em>, <em>split_keys=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Cloud Bigtable table inside an instance. For more information see
<a class="reference external" href="https://cloud.google.com/bigtable/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigtable/docs/go/reference">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>column_families</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.</li>
<li><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Bigtable instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>split_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of predefined keys to split the table on.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.column_families">
<code class="descname">column_families</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.column_families" title="Permalink to this definition">¶</a></dt>
<dd><p>A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.instance_name">
<code class="descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Bigtable instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.split_keys">
<code class="descname">split_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.split_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of predefined keys to split the table on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Table.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Table.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
