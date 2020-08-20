---
title: Package pulumi_okta
title_tag: Package pulumi_okta | Python SDK
linktitle: pulumi_okta
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "okta" >}}

<div class="section" id="pulumi-okta">
<h1>Pulumi Okta<a class="headerlink" href="#pulumi-okta" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta"></span><dl class="py class">
<dt id="pulumi_okta.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backoff</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_wait_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_wait_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parallelism</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the okta package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API Token granting privileges to Okta API.</p></li>
<li><p><strong>backoff</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use exponential back off strategy for rate limits.</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta url. (Use ‘oktapreview.com’ for Okta testing)</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – maximum number of retries to attempt before erroring out.</p></li>
<li><p><strong>max_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – maximum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.</p></li>
<li><p><strong>min_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – minimum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.</p></li>
<li><p><strong>org_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization to manage in Okta.</p></li>
<li><p><strong>parallelism</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of concurrent requests to make within a resource where bulk operations are not possible. Take note of
<a class="reference external" href="https://developer.okta.com/docs/api/getting_started/rate-limits">https://developer.okta.com/docs/api/getting_started/rate-limits</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_okta.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
