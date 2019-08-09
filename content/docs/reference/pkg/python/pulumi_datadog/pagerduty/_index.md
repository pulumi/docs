---
---

<div class="section" id="pagerduty">
<h1>pagerduty<a class="headerlink" href="#pagerduty" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_datadog.pagerduty"></span><dl class="class">
<dt id="pulumi_datadog.pagerduty.Integration">
<em class="property">class </em><code class="descclassname">pulumi_datadog.pagerduty.</code><code class="descname">Integration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_token=None</em>, <em>individual_services=None</em>, <em>schedules=None</em>, <em>services=None</em>, <em>subdomain=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Integration resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty API token.</li>
<li><strong>individual_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.</li>
<li><strong>schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of your schedule URLs.</li>
<li><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.</p>
</li>
<li><strong>subdomain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty account’s personalized subdomain name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.api_token">
<code class="descname">api_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.api_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your PagerDuty API token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.individual_services">
<code class="descname">individual_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.individual_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.schedules">
<code class="descname">schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of your schedule URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.services">
<code class="descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.subdomain">
<code class="descname">subdomain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.subdomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Your PagerDuty account’s personalized subdomain name.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_datadog.pagerduty.Integration.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>api_token=None</em>, <em>individual_services=None</em>, <em>schedules=None</em>, <em>services=None</em>, <em>subdomain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] api_token: Your PagerDuty API token.
:param pulumi.Input[bool] individual_services: Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.
:param pulumi.Input[list] schedules: Array of your schedule URLs.
:param pulumi.Input[list] services: Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.
:param pulumi.Input[str] subdomain: Your PagerDuty account’s personalized subdomain name.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.Integration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.Integration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.ServiceObject">
<em class="property">class </em><code class="descclassname">pulumi_datadog.pagerduty.</code><code class="descname">ServiceObject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>service_key=None</em>, <em>service_name=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to individual Service Objects of Datadog - PagerDuty integrations. Note that the Datadog - PagerDuty integration must be activated (either manually in the Datadog UI or by using <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty.html">pagerduty.Integration</a>) in order for this resource to be usable.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Service name in PagerDuty.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.ServiceObject.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Service name in PagerDuty.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_datadog.pagerduty.ServiceObject.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>service_key=None</em>, <em>service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceObject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] service_name: Your Service name in PagerDuty.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.ServiceObject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.ServiceObject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
