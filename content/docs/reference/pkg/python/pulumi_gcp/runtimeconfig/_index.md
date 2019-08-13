---
title: Module runtimeconfig
---

<div class="section" id="runtimeconfig">
<h1>runtimeconfig<a class="headerlink" href="#runtimeconfig" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.runtimeconfig"></span><dl class="class">
<dt id="pulumi_gcp.runtimeconfig.Config">
<em class="property">class </em><code class="descclassname">pulumi_gcp.runtimeconfig.</code><code class="descname">Config</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RuntimeConfig resource in Google Cloud. For more information, see the
<a class="reference external" href="https://cloud.google.com/deployment-manager/runtime-configurator/">official documentation</a>,
or the
<a class="reference external" href="https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/">JSON API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description to associate with the runtime
config.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the runtime config.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_config.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Config.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description to associate with the runtime
config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Config.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the runtime config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Config.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.runtimeconfig.Config.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Config resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description to associate with the runtime</p>
<blockquote>
<div>config.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the runtime config.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_config.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.runtimeconfig.Config.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.runtimeconfig.Config.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Config.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.runtimeconfig.Variable">
<em class="property">class </em><code class="descclassname">pulumi_gcp.runtimeconfig.</code><code class="descname">Variable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>project=None</em>, <em>text=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a RuntimeConfig variable in Google Cloud. For more information, see the
<a class="reference external" href="https://cloud.google.com/deployment-manager/runtime-configurator/">official documentation</a>,
or the
<a class="reference external" href="https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/">JSON API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable to manage. Note that variable
names can be hierarchical using slashes (e.g. “prod-variables/hostname”).</li>
<li><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the RuntimeConfig resource containing this
variable.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_variable.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Variable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the variable to manage. Note that variable
names can be hierarchical using slashes (e.g. “prod-variables/hostname”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Variable.parent">
<code class="descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the RuntimeConfig resource containing this
variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Variable.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.runtimeconfig.Variable.update_time">
<code class="descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format,
accurate to nanoseconds, representing when the variable was last updated.
Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.runtimeconfig.Variable.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>project=None</em>, <em>text=None</em>, <em>update_time=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Variable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name of the variable to manage. Note that variable</p>
<blockquote>
<div>names can be hierarchical using slashes (e.g. “prod-variables/hostname”).</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the RuntimeConfig resource containing this
variable.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The timestamp in RFC3339 UTC “Zulu” format,
accurate to nanoseconds, representing when the variable was last updated.
Example: “2016-10-09T12:33:37.578138407Z”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/runtimeconfig_variable.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.runtimeconfig.Variable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.runtimeconfig.Variable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.runtimeconfig.Variable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
