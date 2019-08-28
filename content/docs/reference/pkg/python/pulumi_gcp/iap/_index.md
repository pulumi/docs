---
title: Module iap
---

<div class="section" id="iap">
<h1>iap<a class="headerlink" href="#iap" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.iap"></span><dl class="class">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iap.</code><code class="sig-name descname">TunnelInstanceIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMBinding resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TunnelInstanceIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] etag: (Computed) The etag of the instance’s IAM policy.
:param pulumi.Input[str] instance: The name of the instance.
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div><p>is not provided, the provider project is used.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iap.</code><code class="sig-name descname">TunnelInstanceIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMMember resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TunnelInstanceIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] etag: (Computed) The etag of the instance’s IAM policy.
:param pulumi.Input[str] instance: The name of the instance.
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div><p>is not provided, the provider project is used.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">iap.TunnelInstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iap.</code><code class="sig-name descname">TunnelInstanceIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TunnelInstanceIAMPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TunnelInstanceIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] etag: (Computed) The etag of the instance’s IAM policy.
:param pulumi.Input[str] instance: The name of the instance.
:param pulumi.Input[str] policy_data: The policy data generated by</p>
<blockquote>
<div><p>a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_tunnel_instance_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iap.TunnelInstanceIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
