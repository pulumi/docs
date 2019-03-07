<div class="section" id="module-pulumi_aws.waf">
<span id="waf"></span><h1>waf<a class="headerlink" href="#module-pulumi_aws.waf" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.waf.ByteMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">ByteMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>byte_match_tuples=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Byte Match Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Byte Match Set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.byte_match_tuples">
<code class="descname">byte_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.byte_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Byte Match Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.ByteMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.ByteMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.GeoMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">GeoMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>geo_match_constraints=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Geo Match Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the GeoMatchSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.geo_match_constraints">
<code class="descname">geo_match_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.geo_match_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the GeoMatchSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.GeoMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.GeoMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.IpSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">IpSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip_set_descriptors=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF IPSet Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.ip_set_descriptors">
<code class="descname">ip_set_descriptors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.ip_set_descriptors" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the IPSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.IpSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.IpSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RateBasedRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">RateBasedRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>predicates=None</em>, <em>rate_key=None</em>, <em>rate_limit=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule" title="Permalink to this definition">¶</a></dt>
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
<li><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.</li>
<li><strong>rate_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid value is IP.</li>
<li><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.predicates">
<code class="descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_key">
<code class="descname">rate_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid value is IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_limit">
<code class="descname">rate_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RateBasedRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RateBasedRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">RegexMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>regex_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regex Match Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Match Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.regex_match_tuples">
<code class="descname">regex_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.regex_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexPatternSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">RegexPatternSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>regex_pattern_strings=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regex Pattern Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Pattern Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.regex_pattern_strings">
<code class="descname">regex_pattern_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.regex_pattern_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexPatternSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexPatternSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.Rule">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">Rule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>predicates=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</li>
<li><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.predicates">
<code class="descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.Rule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.Rule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RuleGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">RuleGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>activated_rules=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Group Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.activated_rules">
<code class="descname">activated_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.activated_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of activated rules, see below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the metrics from the rule group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the rule group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RuleGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RuleGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SizeConstraintSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">SizeConstraintSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>size_constraints=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Size Constraint Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Size Constraint Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.size_constraints">
<code class="descname">size_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.size_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parts of web requests that you want to inspect the size of.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SqlInjectionMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">SqlInjectionMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>sql_injection_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF SQL Injection Match Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples">
<code class="descname">sql_injection_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.WebAcl">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">WebAcl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_action=None</em>, <em>logging_configuration=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>rules=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Web ACL Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</li>
<li><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.default_action">
<code class="descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.logging_configuration">
<code class="descname">logging_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.logging_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to enable WAF logging. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.WebAcl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.WebAcl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.XssMatchSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.waf.</code><code class="descname">XssMatchSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>xss_match_tuples=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF XSS Match Set Resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</li>
<li><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.waf.XssMatchSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.XssMatchSet.xss_match_tuples">
<code class="descname">xss_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.xss_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.XssMatchSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.XssMatchSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
