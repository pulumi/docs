---
---

<div class="section" id="xray">
<h1>xray<a class="headerlink" href="#xray" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.xray"></span><dl class="class">
<dt id="pulumi_aws.xray.SamplingRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.xray.</code><code class="descname">SamplingRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attributes=None</em>, <em>fixed_rate=None</em>, <em>host=None</em>, <em>http_method=None</em>, <em>priority=None</em>, <em>reservoir_size=None</em>, <em>resource_arn=None</em>, <em>rule_name=None</em>, <em>service_name=None</em>, <em>service_type=None</em>, <em>url_path=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS XRay Sampling Rule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Matches attributes derived from the request.</li>
<li><strong>fixed_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of matching requests to instrument, after the reservoir is exhausted.</li>
<li><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the hostname from a request URL.</li>
<li><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the HTTP method of a request.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the sampling rule.</li>
<li><strong>reservoir_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</li>
<li><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the ARN of the AWS resource on which the service runs.</li>
<li><strong>rule_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the sampling rule.</li>
<li><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">name</span></code> that the service uses to identify itself in segments.</li>
<li><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">origin</span></code> that the service uses to identify its type in segments.</li>
<li><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the path from a request URL.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version of the sampling rule format (<code class="docutils literal notranslate"><span class="pre">1</span></code> )</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/xray_sampling_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/xray_sampling_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the sampling rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches attributes derived from the request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.fixed_rate">
<code class="descname">fixed_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.fixed_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of matching requests to instrument, after the reservoir is exhausted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the hostname from a request URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.http_method">
<code class="descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the HTTP method of a request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the sampling rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.reservoir_size">
<code class="descname">reservoir_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.reservoir_size" title="Permalink to this definition">¶</a></dt>
<dd><p>A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.resource_arn">
<code class="descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the ARN of the AWS resource on which the service runs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.rule_name">
<code class="descname">rule_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.rule_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the sampling rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the <code class="docutils literal notranslate"><span class="pre">name</span></code> that the service uses to identify itself in segments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.service_type">
<code class="descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the <code class="docutils literal notranslate"><span class="pre">origin</span></code> that the service uses to identify its type in segments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.url_path">
<code class="descname">url_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.url_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the path from a request URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.xray.SamplingRule.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the sampling rule format (<code class="docutils literal notranslate"><span class="pre">1</span></code> )</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.xray.SamplingRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.xray.SamplingRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
