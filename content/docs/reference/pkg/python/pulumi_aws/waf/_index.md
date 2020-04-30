---
title: Module waf
title_tag: Module waf | Package pulumi_aws | Python SDK
linktitle: waf
notitle: true
---

<div class="section" id="waf">
<h1>waf<a class="headerlink" href="#waf" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.waf"></span><dl class="py class">
<dt id="pulumi_aws.waf.AwaitableGetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.AwaitableGetRateBasedRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetRateBasedRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetRateBasedRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.AwaitableGetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.AwaitableGetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">AwaitableGetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.AwaitableGetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.ByteMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">ByteMatchSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">byte_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>byte_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Within the portion of a web request that you want to search
(for example, in the query string, if any), specify where you want to search.
e.g. <code class="docutils literal notranslate"><span class="pre">CONTAINS</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINS_WORD</span></code> or <code class="docutils literal notranslate"><span class="pre">EXACTLY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-PositionalConstraint">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to search for. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TargetString">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.byte_match_tuples">
<code class="sig-name descname">byte_match_tuples</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.byte_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Within the portion of a web request that you want to search
(for example, in the query string, if any), specify where you want to search.
e.g. <code class="docutils literal notranslate"><span class="pre">CONTAINS</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINS_WORD</span></code> or <code class="docutils literal notranslate"><span class="pre">EXACTLY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-PositionalConstraint">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that you want to search for. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TargetString">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.ByteMatchSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Byte Match Set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.ByteMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">byte_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ByteMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Byte Match Set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>byte_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Within the portion of a web request that you want to search
(for example, in the query string, if any), specify where you want to search.
e.g. <code class="docutils literal notranslate"><span class="pre">CONTAINS</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINS_WORD</span></code> or <code class="docutils literal notranslate"><span class="pre">EXACTLY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-PositionalConstraint">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to search for. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TargetString">docs</a>
for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.ByteMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.ByteMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.ByteMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.GeoMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GeoMatchSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_match_constraints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>geo_match_constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">RU</span></code>, <code class="docutils literal notranslate"><span class="pre">CN</span></code>, etc.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html">docs</a> for all supported values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.geo_match_constraints">
<code class="sig-name descname">geo_match_constraints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.geo_match_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">RU</span></code>, <code class="docutils literal notranslate"><span class="pre">CN</span></code>, etc.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html">docs</a> for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.GeoMatchSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the GeoMatchSet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.GeoMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_match_constraints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GeoMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the GeoMatchSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>geo_match_constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">RU</span></code>, <code class="docutils literal notranslate"><span class="pre">CN</span></code>, etc.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html">docs</a> for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.GeoMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.GeoMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GeoMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.GetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpset.</p>
<dl class="py attribute">
<dt id="pulumi_aws.waf.GetIpsetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetIpsetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.GetRateBasedRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetRateBasedRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetRateBasedRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRateBasedRule.</p>
<dl class="py attribute">
<dt id="pulumi_aws.waf.GetRateBasedRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetRateBasedRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.GetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="py attribute">
<dt id="pulumi_aws.waf.GetRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.GetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">GetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.GetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWebAcl.</p>
<dl class="py attribute">
<dt id="pulumi_aws.waf.GetWebAclResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.GetWebAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.waf.IpSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">IpSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_set_descriptors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>ip_set_descriptors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the IP address - <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IPv4 or IPv6 address specified via CIDR notation.
e.g. <code class="docutils literal notranslate"><span class="pre">192.0.2.44/32</span></code> or <code class="docutils literal notranslate"><span class="pre">1111:0000:0000:0000:0000:0000:0000:0000/64</span></code></p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.IpSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF IPSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.IpSet.ip_set_descriptors">
<code class="sig-name descname">ip_set_descriptors</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.ip_set_descriptors" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the IP address - <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An IPv4 or IPv6 address specified via CIDR notation.
e.g. <code class="docutils literal notranslate"><span class="pre">192.0.2.44/32</span></code> or <code class="docutils literal notranslate"><span class="pre">1111:0000:0000:0000:0000:0000:0000:0000/64</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.IpSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the IPSet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.IpSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_set_descriptors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF IPSet.</p></li>
<li><p><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_set_descriptors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the IP address - <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IPv4 or IPv6 address specified via CIDR notation.
e.g. <code class="docutils literal notranslate"><span class="pre">192.0.2.44/32</span></code> or <code class="docutils literal notranslate"><span class="pre">1111:0000:0000:0000:0000:0000:0000:0000/64</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.IpSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.IpSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.RateBasedRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RateBasedRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <code class="docutils literal notranslate"><span class="pre">ByteMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">IPSet</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">XssMatchSet</span></code>, or <code class="docutils literal notranslate"><span class="pre">SizeConstraintSet</span></code>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.predicates">
<code class="sig-name descname">predicates</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <code class="docutils literal notranslate"><span class="pre">ByteMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">IPSet</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">XssMatchSet</span></code>, or <code class="docutils literal notranslate"><span class="pre">SizeConstraintSet</span></code>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_key">
<code class="sig-name descname">rate_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid value is IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.rate_limit">
<code class="sig-name descname">rate_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RateBasedRule.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RateBasedRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateBasedRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>rate_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid value is IP.</p></li>
<li><p><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <code class="docutils literal notranslate"><span class="pre">ByteMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">IPSet</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatchSet</span></code>, <code class="docutils literal notranslate"><span class="pre">XssMatchSet</span></code>, or <code class="docutils literal notranslate"><span class="pre">SizeConstraintSet</span></code>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RateBasedRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RateBasedRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RateBasedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.RegexMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RegexMatchSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regex_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>regex_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regexPatternSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html">Regex Pattern Set</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Match Set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexMatchSet.regex_match_tuples">
<code class="sig-name descname">regex_match_tuples</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.regex_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regexPatternSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html">Regex Pattern Set</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RegexMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regex_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Match Set.</p></li>
<li><p><strong>regex_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>regex_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The part of a web request that you want to search, such as a specified header or a query string.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regexPatternSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html">Regex Pattern Set</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RegexMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.RegexPatternSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RegexPatternSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regex_pattern_strings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Pattern Set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RegexPatternSet.regex_pattern_strings">
<code class="sig-name descname">regex_pattern_strings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.regex_pattern_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RegexPatternSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regex_pattern_strings</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexPatternSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Pattern Set.</p></li>
<li><p><strong>regex_pattern_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RegexPatternSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RegexPatternSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_byte_match_set.html">waf_byte_match_set</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_ipset.html">waf_ipset</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_size_constraint_set.html">waf.SizeConstraintSet</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_sql_injection_match_set.html">waf.SqlInjectionMatchSet</a> or <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_xss_match_set.html">waf.XssMatchSet</a>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.Rule.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.Rule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.Rule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.Rule.predicates">
<code class="sig-name descname">predicates</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_byte_match_set.html">waf_byte_match_set</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_ipset.html">waf_ipset</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_size_constraint_set.html">waf.SizeConstraintSet</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_sql_injection_match_set.html">waf.SqlInjectionMatchSet</a> or <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_xss_match_set.html">waf.XssMatchSet</a>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.Rule.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.Rule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">predicates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF rule.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique identifier for a predicate in the rule, such as Byte Match Set ID or IPSet ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to allow, block, or count requests
based on the settings in the specified <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_byte_match_set.html">waf_byte_match_set</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_ipset.html">waf_ipset</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_size_constraint_set.html">waf.SizeConstraintSet</a>, <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_sql_injection_match_set.html">waf.SqlInjectionMatchSet</a> or <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_xss_match_set.html">waf.XssMatchSet</a>.
For example, if an IPSet includes the IP address <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>, AWS WAF will allow or block requests based on that IP address.
If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, AWS WAF will allow, block, or count requests based on all IP addresses <em>except</em> <code class="docutils literal notranslate"><span class="pre">192.0.2.44</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.RuleGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">RuleGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activated_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Rule Group Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activated_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of activated rules, see below</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the metrics from the rule group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the rule group</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>activated_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.RuleGroup.activated_rules">
<code class="sig-name descname">activated_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.activated_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of activated rules, see below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RuleGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF rule group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RuleGroup.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the metrics from the rule group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RuleGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the rule group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.RuleGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RuleGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activated_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activated_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of activated rules, see below</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF rule group.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the metrics from the rule group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the rule group</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>activated_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.RuleGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.RuleGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.RuleGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.SizeConstraintSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">SizeConstraintSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_constraints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>size_constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison_operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of comparison you want to perform.
e.g. <code class="docutils literal notranslate"><span class="pre">EQ</span></code>, <code class="docutils literal notranslate"><span class="pre">NE</span></code>, <code class="docutils literal notranslate"><span class="pre">LT</span></code>, <code class="docutils literal notranslate"><span class="pre">GT</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator">docs</a> for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for the size constraint.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size in bytes that you want to compare against the size of the specified <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code>.
Valid values are between 0 - 21474836480 bytes (0 - 20 GB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation">docs</a>
for all supported values.
<strong>Note:</strong> if you choose <code class="docutils literal notranslate"><span class="pre">BODY</span></code> as <code class="docutils literal notranslate"><span class="pre">type</span></code>, you must choose <code class="docutils literal notranslate"><span class="pre">NONE</span></code> because CloudFront forwards only the first 8192 bytes for inspection.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Size Constraint Set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.SizeConstraintSet.size_constraints">
<code class="sig-name descname">size_constraints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.size_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parts of web requests that you want to inspect the size of.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison_operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of comparison you want to perform.
e.g. <code class="docutils literal notranslate"><span class="pre">EQ</span></code>, <code class="docutils literal notranslate"><span class="pre">NE</span></code>, <code class="docutils literal notranslate"><span class="pre">LT</span></code>, <code class="docutils literal notranslate"><span class="pre">GT</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator">docs</a> for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies where in a web request to look for the size constraint.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size in bytes that you want to compare against the size of the specified <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code>.
Valid values are between 0 - 21474836480 bytes (0 - 20 GB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation">docs</a>
for all supported values.
<strong>Note:</strong> if you choose <code class="docutils literal notranslate"><span class="pre">BODY</span></code> as <code class="docutils literal notranslate"><span class="pre">type</span></code>, you must choose <code class="docutils literal notranslate"><span class="pre">NONE</span></code> because CloudFront forwards only the first 8192 bytes for inspection.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.SizeConstraintSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_constraints</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SizeConstraintSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Size Constraint Set.</p></li>
<li><p><strong>size_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the parts of web requests that you want to inspect the size of.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>size_constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison_operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of comparison you want to perform.
e.g. <code class="docutils literal notranslate"><span class="pre">EQ</span></code>, <code class="docutils literal notranslate"><span class="pre">NE</span></code>, <code class="docutils literal notranslate"><span class="pre">LT</span></code>, <code class="docutils literal notranslate"><span class="pre">GT</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator">docs</a> for all supported values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for the size constraint.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size in bytes that you want to compare against the size of the specified <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code>.
Valid values are between 0 - 21474836480 bytes (0 - 20 GB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation">docs</a>
for all supported values.
<strong>Note:</strong> if you choose <code class="docutils literal notranslate"><span class="pre">BODY</span></code> as <code class="docutils literal notranslate"><span class="pre">type</span></code>, you must choose <code class="docutils literal notranslate"><span class="pre">NONE</span></code> because CloudFront forwards only the first 8192 bytes for inspection.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SizeConstraintSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SizeConstraintSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">SqlInjectionMatchSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_injection_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>sql_injection_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for snippets of malicious SQL code.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SQL Injection Match Set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples">
<code class="sig-name descname">sql_injection_match_tuples</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.sql_injection_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies where in a web request to look for snippets of malicious SQL code.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_injection_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlInjectionMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SQL Injection Match Set.</p></li>
<li><p><strong>sql_injection_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sql_injection_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for snippets of malicious SQL code.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.SqlInjectionMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.WebAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">WebAcl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
<p>The <strong>logging_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the associated WAF (Global) rule (e.g. <cite>``waf.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_). WAF (Regional) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF WebACL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.default_action">
<code class="sig-name descname">default_action</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.logging_configuration">
<code class="sig-name descname">logging_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.logging_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to enable WAF logging. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this web ACL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the web ACL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.rules">
<code class="sig-name descname">rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the associated WAF (Global) rule (e.g. <cite>``waf.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_). WAF (Regional) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.WebAcl.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.WebAcl.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.WebAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF WebACL.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with action that you want AWS WAF to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL. Detailed below.</p></li>
<li><p><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
<p>The <strong>logging_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the associated WAF (Global) rule (e.g. <cite>``waf.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/waf_rule.html">https://www.terraform.io/docs/providers/aws/r/waf_rule.html</a>&gt;`_). WAF (Regional) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html">Rule</a>, <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>, as defined by <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html">RateBasedRule</a>, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, as defined by <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html">RuleGroup</a>. The default is REGULAR. If you add a RATE_BASED rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">RATE_BASED</span></code>. If you add a GROUP rule, you need to set <code class="docutils literal notranslate"><span class="pre">type</span></code> as <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.WebAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.WebAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.WebAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.waf.XssMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">XssMatchSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">xss_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>xss_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_XssMatchTuple.html#WAF-Type-XssMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.waf.XssMatchSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.XssMatchSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.waf.XssMatchSet.xss_match_tuples">
<code class="sig-name descname">xss_match_tuples</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.xss_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_XssMatchTuple.html#WAF-Type-XssMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.XssMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">xss_match_tuples</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing XssMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</p></li>
<li><p><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>xss_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">target_string</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="http://docs.aws.amazon.com/waf/latest/APIReference/API_XssMatchTuple.html#WAF-Type-XssMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.waf.XssMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.waf.XssMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.XssMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.waf.get_ipset">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_ipset</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_ipset" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.IpSet</span></code> Retrieves a WAF IP Set Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF IP set.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.waf.get_rate_based_rule">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_rate_based_rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_rate_based_rule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.RateBasedRule</span></code> Retrieves a WAF Rate Based Rule Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF rate based rule.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.waf.get_rule">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.Rule</span></code> Retrieves a WAF Rule Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF rule.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.waf.get_web_acl">
<code class="sig-prename descclassname">pulumi_aws.waf.</code><code class="sig-name descname">get_web_acl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.waf.get_web_acl" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">waf.WebAcl</span></code> Retrieves a WAF Web ACL Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF Web ACL.</p>
</dd>
</dl>
</dd></dl>

</div>
