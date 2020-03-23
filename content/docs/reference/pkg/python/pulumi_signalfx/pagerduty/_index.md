---
title: Module pagerduty
title_tag: Module pagerduty | Package pulumi_signalfx | Python SDK
linktitle: pagerduty
notitle: true
---

<div class="section" id="pagerduty">
<h1>pagerduty<a class="headerlink" href="#pagerduty" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.pagerduty"></span><dl class="class">
<dt id="pulumi_signalfx.pagerduty.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.pagerduty.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx PagerDuty integrations</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/pagerduty_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/pagerduty_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PagerDuty API key.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_signalfx.pagerduty.Integration.api_key">
<code class="sig-name descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>PagerDuty API key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.pagerduty.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.pagerduty.Integration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.pagerduty.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PagerDuty API key.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.pagerduty.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.pagerduty.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.pagerduty.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
