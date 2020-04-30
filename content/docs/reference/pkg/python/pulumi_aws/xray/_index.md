---
title: Module xray
title_tag: Module xray | Package pulumi_aws | Python SDK
linktitle: xray
notitle: true
---

<div class="section" id="xray">
<h1>xray<a class="headerlink" href="#xray" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.xray"></span><dl class="py class">
<dt id="pulumi_aws.xray.SamplingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.xray.</code><code class="sig-name descname">SamplingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fixed_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reservoir_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS XRay Sampling Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Matches attributes derived from the request.</p></li>
<li><p><strong>fixed_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of matching requests to instrument, after the reservoir is exhausted.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the hostname from a request URL.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the HTTP method of a request.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the sampling rule.</p></li>
<li><p><strong>reservoir_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the ARN of the AWS resource on which the service runs.</p></li>
<li><p><strong>rule_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the sampling rule.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">name</span></code> that the service uses to identify itself in segments.</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">origin</span></code> that the service uses to identify its type in segments.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the path from a request URL.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version of the sampling rule format (<code class="docutils literal notranslate"><span class="pre">1</span></code> )</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the sampling rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.attributes">
<code class="sig-name descname">attributes</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches attributes derived from the request.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.fixed_rate">
<code class="sig-name descname">fixed_rate</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.fixed_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of matching requests to instrument, after the reservoir is exhausted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.host">
<code class="sig-name descname">host</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the hostname from a request URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.http_method">
<code class="sig-name descname">http_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the HTTP method of a request.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the sampling rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.reservoir_size">
<code class="sig-name descname">reservoir_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.reservoir_size" title="Permalink to this definition">¶</a></dt>
<dd><p>A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the ARN of the AWS resource on which the service runs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.rule_name">
<code class="sig-name descname">rule_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.rule_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the sampling rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.service_name">
<code class="sig-name descname">service_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the <code class="docutils literal notranslate"><span class="pre">name</span></code> that the service uses to identify itself in segments.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.service_type">
<code class="sig-name descname">service_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the <code class="docutils literal notranslate"><span class="pre">origin</span></code> that the service uses to identify its type in segments.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.url_path">
<code class="sig-name descname">url_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.url_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Matches the path from a request URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.xray.SamplingRule.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the sampling rule format (<code class="docutils literal notranslate"><span class="pre">1</span></code> )</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.xray.SamplingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fixed_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reservoir_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamplingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the sampling rule.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Matches attributes derived from the request.</p></li>
<li><p><strong>fixed_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of matching requests to instrument, after the reservoir is exhausted.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the hostname from a request URL.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the HTTP method of a request.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the sampling rule.</p></li>
<li><p><strong>reservoir_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the ARN of the AWS resource on which the service runs.</p></li>
<li><p><strong>rule_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the sampling rule.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">name</span></code> that the service uses to identify itself in segments.</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the <code class="docutils literal notranslate"><span class="pre">origin</span></code> that the service uses to identify its type in segments.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Matches the path from a request URL.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version of the sampling rule format (<code class="docutils literal notranslate"><span class="pre">1</span></code> )</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.xray.SamplingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.xray.SamplingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.xray.SamplingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
