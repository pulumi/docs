---
---

<div class="section" id="module-pulumi_datadog.pagerduty">
<span id="pagerduty"></span><h1>pagerduty<a class="headerlink" href="#module-pulumi_datadog.pagerduty" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_datadog.pagerduty.Integration">
<em class="property">class </em><code class="descclassname">pulumi_datadog.pagerduty.</code><code class="descname">Integration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_token=None</em>, <em>schedules=None</em>, <em>services=None</em>, <em>subdomain=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog - PagerDuty resource. This can be used to create and manage Datadog - PagerDuty integration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty API token.</li>
<li><strong>schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of your schedule URLs.</li>
<li><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of PagerDuty service objects.</li>
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
<dt id="pulumi_datadog.pagerduty.Integration.schedules">
<code class="descname">schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of your schedule URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.services">
<code class="descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of PagerDuty service objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.subdomain">
<code class="descname">subdomain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.subdomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Your PagerDuty account’s personalized subdomain name.</p>
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

</div>
