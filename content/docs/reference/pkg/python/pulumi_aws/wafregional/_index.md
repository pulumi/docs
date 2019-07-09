---
---

<div class="section" id="module-pulumi_aws.wafregional">
<span id="wafregional"></span><h1>wafregional<a class="headerlink" href="#module-pulumi_aws.wafregional" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.wafregional.ByteMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">ByteMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>byte_match_tuples=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Byte Match Set Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the ByteMatchSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_byte_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_byte_match_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.ByteMatchSet.byte_match_tuples">
<code class="descname">byte_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.byte_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.ByteMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the ByteMatchSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.ByteMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.ByteMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.GeoMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">GeoMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>geo_match_constraints=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Geo Match Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Geo Match Set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_geo_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_geo_match_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GeoMatchSet.geo_match_constraints">
<code class="descname">geo_match_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.geo_match_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.GeoMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Geo Match Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.GeoMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.GeoMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.IpSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">IpSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip_set_descriptors=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional IPSet Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_ipset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_ipset.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.ip_set_descriptors">
<code class="descname">ip_set_descriptors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.ip_set_descriptors" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the IPSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.IpSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.IpSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RateBasedRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">RateBasedRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>predicates=None</em>, <em>rate_key=None</em>, <em>rate_limit=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rate Based Rule Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</li>
<li><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</li>
<li><strong>rate_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid value is IP.</li>
<li><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rate_based_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rate_based_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.predicates">
<code class="descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.rate_key">
<code class="descname">rate_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.rate_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid value is IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.rate_limit">
<code class="descname">rate_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RateBasedRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RateBasedRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">RegexMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>regex_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Regex Match Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Match Set.</li>
<li><strong>regex_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_regex_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_regex_match_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Match Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexMatchSet.regex_match_tuples">
<code class="descname">regex_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.regex_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexPatternSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">RegexPatternSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>regex_pattern_strings=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Regex Pattern Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Pattern Set.</li>
<li><strong>regex_pattern_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_regex_pattern_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_regex_pattern_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexPatternSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Pattern Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexPatternSet.regex_pattern_strings">
<code class="descname">regex_pattern_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.regex_pattern_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexPatternSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexPatternSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.Rule">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">Rule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>predicates=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an WAF Regional Rule Resource for use with Application Load Balancer.</p>
<p>See the <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_Predicate.html">WAF Documentation</a> for more information.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">data_id</span></code> - (Required) The unique identifier of a predicate, such as the ID of a <code class="docutils literal notranslate"><span class="pre">ByteMatchSet</span></code> or <code class="docutils literal notranslate"><span class="pre">IPSet</span></code>.</li>
<li><code class="docutils literal notranslate"><span class="pre">negated</span></code> - (Required) Whether to use the settings or the negated settings that you specified in the objects.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</li>
<li><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.predicates">
<code class="descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.Rule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.Rule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RuleGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">RuleGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>activated_rules=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Rule Group Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>activated_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of activated rules, see below</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the metrics from the rule group</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the rule group</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_rule_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.activated_rules">
<code class="descname">activated_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.activated_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of activated rules, see below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the metrics from the rule group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the rule group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RuleGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RuleGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SizeConstraintSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">SizeConstraintSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>size_constraints=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Size Constraint Set Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Size Constraint Set.</li>
<li><strong>size_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the parts of web requests that you want to inspect the size of.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_size_constraint_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_size_constraint_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Size Constraint Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.size_constraints">
<code class="descname">size_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.size_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parts of web requests that you want to inspect the size of.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SizeConstraintSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">SqlInjectionMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>sql_injection_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional SQL Injection Match Set Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</li>
<li><strong>sql_injection_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_sql_injection_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_sql_injection_match_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.sql_injection_match_tuples">
<code class="descname">sql_injection_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.sql_injection_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAcl">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">WebAcl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_action=None</em>, <em>logging_configuration=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>rules=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Web ACL Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action that you want AWS WAF Regional to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL.</li>
<li><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of configuration blocks containing rules for the web ACL. Detailed below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_web_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_web_acl.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the WAF Regional WebACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.default_action">
<code class="descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action that you want AWS WAF Regional to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.logging_configuration">
<code class="descname">logging_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.logging_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to enable WAF logging. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of configuration blocks containing rules for the web ACL. Detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAcl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAcl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAclAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">WebAclAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>resource_arn=None</em>, <em>web_acl_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an association with WAF Regional Web ACL.</p>
<blockquote>
<div><strong>Note:</strong> An Application Load Balancer can only be associated with one WAF Regional WebACL.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.</li>
<li><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Regional WebACL to create an association.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_web_acl_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_web_acl_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAclAssociation.resource_arn">
<code class="descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAclAssociation.web_acl_id">
<code class="descname">web_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.web_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Regional WebACL to create an association.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAclAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAclAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.XssMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.wafregional.</code><code class="descname">XssMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>xss_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional XSS Match Set Resource for use with Application Load Balancer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the set</li>
<li><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_xss_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_xss_match_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.XssMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.XssMatchSet.xss_match_tuples">
<code class="descname">xss_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.xss_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.XssMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.XssMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
