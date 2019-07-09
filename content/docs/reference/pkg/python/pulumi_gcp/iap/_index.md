---
---

<div class="section" id="iap">
<h1>iap<a class="headerlink" href="#iap" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp/issues">terraform-providers/terraform-provider-gcp repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.iap"></span><dl class="class">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.iap.</code><code class="descname">TunnelInstanceIAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMBinding resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_iap_tunnel_instance_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_iap_tunnel_instance_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.iap.</code><code class="descname">TunnelInstanceIAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMMember resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_iap_tunnel_instance_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_iap_tunnel_instance_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.iap.</code><code class="descname">TunnelInstanceIAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance=None</em>, <em>policy_data=None</em>, <em>project=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMPolicy resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
