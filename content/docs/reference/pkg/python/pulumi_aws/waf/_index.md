---
title: Module waf
---

<div class="section" id="waf">
<h1>waf<a class="headerlink" href="#waf" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.waf"></span><dl class="class">
<dt id="pulumi_aws.waf.AwaitableGetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.AwaitableGetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetRuleResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.AwaitableGetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.ByteMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">ByteMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">byte_match_tuples=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Byte Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Byte Match Set.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.byte_match_tuples">
<code class="sig-name descname">byte_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.byte_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Byte Match Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.ByteMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">byte_match_tuples=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ByteMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] byte_match_tuples: Specifies the bytes (typically a string that corresponds</p>
<blockquote>
<div><p>with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Byte Match Set.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.ByteMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.ByteMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.GeoMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GeoMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">geo_match_constraints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Geo Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the GeoMatchSet.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_geo_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_geo_match_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.geo_match_constraints">
<code class="sig-name descname">geo_match_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.geo_match_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the GeoMatchSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.GeoMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">geo_match_constraints=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GeoMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] geo_match_constraints: The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.
:param pulumi.Input[str] name: The name or description of the GeoMatchSet.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_geo_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_geo_match_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.GeoMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.GeoMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.GetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpset.</p>
<dl class="attribute">
<dt id="pulumi_aws.waf.GetIpsetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetIpsetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.GetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetRuleResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="attribute">
<dt id="pulumi_aws.waf.GetRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.GetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWebAcl.</p>
<dl class="attribute">
<dt id="pulumi_aws.waf.GetWebAclResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetWebAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.waf.IpSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">IpSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_set_descriptors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF IPSet Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_ipset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_ipset.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.ip_set_descriptors">
<code class="sig-name descname">ip_set_descriptors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.ip_set_descriptors" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.IpSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the IPSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.IpSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">ip_set_descriptors=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the WAF IPSet.
:param pulumi.Input[list] ip_set_descriptors: One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.
:param pulumi.Input[str] name: The name or description of the IPSet.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_ipset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_ipset.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.IpSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.IpSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.RateBasedRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RateBasedRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">rate_key=None</em>, <em class="sig-param">rate_limit=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rate Based Rule Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>rate_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid value is IP.</p></li>
<li><p><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rate_based_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rate_based_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.predicates">
<code class="sig-name descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_key">
<code class="sig-name descname">rate_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid value is IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_limit">
<code class="sig-name descname">rate_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RateBasedRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">rate_key=None</em>, <em class="sig-param">rate_limit=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateBasedRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
:param pulumi.Input[str] name: The name or description of the rule.
:param pulumi.Input[list] predicates: The objects to include in a rule (documented below).
:param pulumi.Input[str] rate_key: Valid value is IP.
:param pulumi.Input[float] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rate_based_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rate_based_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RateBasedRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RateBasedRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.RegexMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RegexMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regex Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Match Set.</p></li>
<li><p><strong>regex_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Match Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.regex_match_tuples">
<code class="sig-name descname">regex_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.regex_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name or description of the Regex Match Set.
:param pulumi.Input[list] regex_match_tuples: The regular expression pattern that you want AWS WAF to search for in web requests,</p>
<blockquote>
<div><p>the location in requests that you want AWS WAF to search, and other settings. See below.</p>
</div></blockquote>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.RegexPatternSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RegexPatternSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_pattern_strings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regex Pattern Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Pattern Set.</p></li>
<li><p><strong>regex_pattern_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_pattern_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_pattern_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Pattern Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.regex_pattern_strings">
<code class="sig-name descname">regex_pattern_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.regex_pattern_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexPatternSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_pattern_strings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexPatternSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
:param pulumi.Input[list] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_pattern_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_pattern_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RegexPatternSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexPatternSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.Rule.predicates">
<code class="sig-name descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.
:param pulumi.Input[str] name: The name or description of the rule.
:param pulumi.Input[list] predicates: The objects to include in a rule (documented below).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.RuleGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RuleGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activated_rules=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Group Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activated_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of activated rules, see below</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the metrics from the rule group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the rule group</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.activated_rules">
<code class="sig-name descname">activated_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.activated_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of activated rules, see below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the metrics from the rule group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.RuleGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the rule group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RuleGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activated_rules=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] activated_rules: A list of activated rules, see below
:param pulumi.Input[str] metric_name: A friendly name for the metrics from the rule group
:param pulumi.Input[str] name: A friendly name of the rule group</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_rule_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.RuleGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RuleGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.SizeConstraintSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">SizeConstraintSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">size_constraints=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Size Constraint Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Size Constraint Set.</p></li>
<li><p><strong>size_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the parts of web requests that you want to inspect the size of.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_size_constraint_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_size_constraint_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Size Constraint Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.size_constraints">
<code class="sig-name descname">size_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.size_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parts of web requests that you want to inspect the size of.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SizeConstraintSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">size_constraints=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SizeConstraintSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name or description of the Size Constraint Set.
:param pulumi.Input[list] size_constraints: Specifies the parts of web requests that you want to inspect the size of.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_size_constraint_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_size_constraint_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">SqlInjectionMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sql_injection_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF SQL Injection Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SQL Injection Match Set.</p></li>
<li><p><strong>sql_injection_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_sql_injection_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_sql_injection_match_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SQL Injection Match Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples">
<code class="sig-name descname">sql_injection_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sql_injection_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlInjectionMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name or description of the SQL Injection Match Set.
:param pulumi.Input[list] sql_injection_match_tuples: The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_sql_injection_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_sql_injection_match_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.WebAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">WebAcl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">logging_configuration=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Web ACL Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</p></li>
<li><p><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_web_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_web_acl.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.default_action">
<code class="sig-name descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.logging_configuration">
<code class="sig-name descname">logging_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.logging_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to enable WAF logging. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.WebAcl.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.WebAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">logging_configuration=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] default_action: Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
:param pulumi.Input[dict] logging_configuration: Configuration block to enable WAF logging. Detailed below.
:param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this web ACL.
:param pulumi.Input[str] name: The name or description of the web ACL.
:param pulumi.Input[list] rules: Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_web_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_web_acl.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.WebAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.WebAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.waf.XssMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">XssMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xss_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF XSS Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</p></li>
<li><p><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_xss_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_xss_match_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.waf.XssMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.waf.XssMatchSet.xss_match_tuples">
<code class="sig-name descname">xss_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.xss_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.XssMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xss_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing XssMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name or description of the SizeConstraintSet.
:param pulumi.Input[list] xss_match_tuples: The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_xss_match_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_xss_match_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.waf.XssMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.XssMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.waf.get_ipset">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_ipset</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_ipset" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.IpSet</span></code> Retrieves a WAF IP Set Resource Id.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_ipset.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_ipset.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.waf.get_rule">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.Rule</span></code> Retrieves a WAF Rule Resource Id.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.waf.get_web_acl">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_web_acl</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_web_acl" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.Rule</span></code> Retrieves a WAF Web ACL Resource Id.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_web_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_web_acl.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
