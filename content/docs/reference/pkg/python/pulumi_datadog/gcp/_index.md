---
title: Module gcp
---

<div class="section" id="gcp">
<h1>gcp<a class="headerlink" href="#gcp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_datadog.gcp"></span><dl class="class">
<dt id="pulumi_datadog.gcp.Integration">
<em class="property">class </em><code class="descclassname">pulumi_datadog.gcp.</code><code class="descname">Integration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>client_email=None</em>, <em>client_id=None</em>, <em>host_filters=None</em>, <em>private_key=None</em>, <em>private_key_id=None</em>, <em>project_id=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog - Google Cloud Platform integration resource. This can be used to create and manage Datadog - Google Cloud Platform integration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your email found in your JSON service account key.</li>
<li><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your ID found in your JSON service account key.</li>
<li><strong>host_filters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key name found in your JSON service account key.</li>
<li><strong>private_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key ID found in your JSON service account key.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Google Cloud project ID found in your JSON service account key.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.client_email">
<code class="descname">client_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.client_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Your email found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.client_id">
<code class="descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your ID found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.host_filters">
<code class="descname">host_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.host_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your private key name found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.private_key_id">
<code class="descname">private_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.private_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your private key ID found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Google Cloud project ID found in your JSON service account key.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_datadog.gcp.Integration.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>client_email=None</em>, <em>client_id=None</em>, <em>host_filters=None</em>, <em>private_key=None</em>, <em>private_key_id=None</em>, <em>project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] client_email: Your email found in your JSON service account key.
:param pulumi.Input[str] client_id: Your ID found in your JSON service account key.
:param pulumi.Input[str] host_filters: Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.
:param pulumi.Input[str] private_key: Your private key name found in your JSON service account key.
:param pulumi.Input[str] private_key_id: Your private key ID found in your JSON service account key.
:param pulumi.Input[str] project_id: Your Google Cloud project ID found in your JSON service account key.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.gcp.Integration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.gcp.Integration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
