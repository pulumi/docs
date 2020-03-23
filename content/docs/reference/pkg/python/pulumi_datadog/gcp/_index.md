---
title: Module gcp
title_tag: Module gcp | Package pulumi_datadog | Python SDK
linktitle: gcp
notitle: true
---

<div class="section" id="gcp">
<h1>gcp<a class="headerlink" href="#gcp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_datadog.gcp"></span><dl class="class">
<dt id="pulumi_datadog.gcp.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.gcp.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_email=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">host_filters=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">private_key_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog - Google Cloud Platform integration resource. This can be used to create and manage Datadog - Google Cloud Platform integration.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_gcp.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your email found in your JSON service account key.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your ID found in your JSON service account key.</p></li>
<li><p><strong>host_filters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key name found in your JSON service account key.</p></li>
<li><p><strong>private_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key ID found in your JSON service account key.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Google Cloud project ID found in your JSON service account key.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.client_email">
<code class="sig-name descname">client_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.client_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Your email found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your ID found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.host_filters">
<code class="sig-name descname">host_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.host_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your private key name found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.private_key_id">
<code class="sig-name descname">private_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.private_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your private key ID found in your JSON service account key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.gcp.Integration.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.gcp.Integration.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Google Cloud project ID found in your JSON service account key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.gcp.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_email=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">host_filters=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">private_key_id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your email found in your JSON service account key.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your ID found in your JSON service account key.</p></li>
<li><p><strong>host_filters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key name found in your JSON service account key.</p></li>
<li><p><strong>private_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your private key ID found in your JSON service account key.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Google Cloud project ID found in your JSON service account key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.gcp.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.gcp.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.gcp.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
