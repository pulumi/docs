---
title: Module wafregional
title_tag: Module wafregional | Package pulumi_aws | Python SDK
linktitle: wafregional
notitle: true
---

<div class="section" id="wafregional">
<h1>wafregional<a class="headerlink" href="#wafregional" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.wafregional"></span><dl class="class">
<dt id="pulumi_aws.wafregional.AwaitableGetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">AwaitableGetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.AwaitableGetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.AwaitableGetRateBasedModResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">AwaitableGetRateBasedModResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.AwaitableGetRateBasedModResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.AwaitableGetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">AwaitableGetRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.AwaitableGetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.AwaitableGetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">AwaitableGetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.AwaitableGetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.ByteMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">ByteMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">byte_match_tuples=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Byte Match Set Resource for use with Application Load Balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the ByteMatchSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>byte_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Settings for the ByteMatchTuple. FieldToMatch documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Within the portion of a web request that you want to search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The formatting way for web request.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.ByteMatchSet.byte_match_tuples">
<code class="sig-name descname">byte_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.byte_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Settings for the ByteMatchTuple. FieldToMatch documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Within the portion of a web request that you want to search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The formatting way for web request.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.ByteMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the ByteMatchSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.ByteMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">byte_match_tuples=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ByteMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>byte_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the ByteMatchSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>byte_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Settings for the ByteMatchTuple. FieldToMatch documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">positionalConstraint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Within the portion of a web request that you want to search.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The formatting way for web request.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.ByteMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.ByteMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.ByteMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.GeoMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">GeoMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">geo_match_constraints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Geo Match Set Resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Geo Match Set.</p></li>
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
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GeoMatchSet.geo_match_constraints">
<code class="sig-name descname">geo_match_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.geo_match_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">RU</span></code>, <code class="docutils literal notranslate"><span class="pre">CN</span></code>, etc.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html">docs</a> for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.GeoMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Geo Match Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.GeoMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">geo_match_constraints=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GeoMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>geo_match_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Geo Match Set.</p></li>
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

<dl class="method">
<dt id="pulumi_aws.wafregional.GeoMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.GeoMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GeoMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.GetIpsetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">GetIpsetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GetIpsetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpset.</p>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GetIpsetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GetIpsetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.GetRateBasedModResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">GetRateBasedModResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GetRateBasedModResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRateBasedMod.</p>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GetRateBasedModResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GetRateBasedModResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.GetRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">GetRuleResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GetRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRule.</p>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GetRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GetRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.GetWebAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">GetWebAclResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.GetWebAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWebAcl.</p>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.GetWebAclResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.GetWebAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.wafregional.IpSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">IpSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_set_descriptors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional IPSet Resource for use with Application Load Balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_set_descriptors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string like IPV4 or IPV6.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR notation.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF IPSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.ip_set_descriptors">
<code class="sig-name descname">ip_set_descriptors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.ip_set_descriptors" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The string like IPV4 or IPV6.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CIDR notation.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.IpSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the IPSet.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.IpSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">ip_set_descriptors=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF IPSet.</p></li>
<li><p><strong>ip_set_descriptors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the IPSet.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_set_descriptors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string like IPV4 or IPV6.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR notation.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.IpSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.IpSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RateBasedRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">RateBasedRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">rate_key=None</em>, <em class="sig-param">rate_limit=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF Regional Rate Based Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.predicates">
<code class="sig-name descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.predicates" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.rate_key">
<code class="sig-name descname">rate_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.rate_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid value is IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.rate_limit">
<code class="sig-name descname">rate_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RateBasedRule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RateBasedRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">rate_key=None</em>, <em class="sig-param">rate_limit=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateBasedRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF Regional Rate Based Rule.</p></li>
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

<dl class="method">
<dt id="pulumi_aws.wafregional.RateBasedRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RateBasedRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RateBasedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">RegexMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Regex Match Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Match Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexMatchSet.regex_match_tuples">
<code class="sig-name descname">regex_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.regex_match_tuples" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexPatternSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">RegexPatternSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_pattern_strings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Regex Pattern Set Resource</p>
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
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexPatternSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Regex Pattern Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RegexPatternSet.regex_pattern_strings">
<code class="sig-name descname">regex_pattern_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.regex_pattern_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexPatternSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">regex_pattern_strings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexPatternSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the Regex Pattern Set.</p></li>
<li><p><strong>regex_pattern_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regular expression (regex) patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RegexPatternSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RegexPatternSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an WAF Regional Rule Resource for use with Application Load Balancer.</p>
<p>See the <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_Predicate.html">WAF Documentation</a> for more information.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The type of predicate in a rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ByteMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">RegexMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">SizeConstraint</span></code>, <code class="docutils literal notranslate"><span class="pre">SqlInjectionMatch</span></code>, or <code class="docutils literal notranslate"><span class="pre">XssMatch</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data_id</span></code> - (Required) The unique identifier of a predicate, such as the ID of a <code class="docutils literal notranslate"><span class="pre">ByteMatchSet</span></code> or <code class="docutils literal notranslate"><span class="pre">IPSet</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> - (Required) Whether to use the settings or the negated settings that you specified in the objects.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF Regional Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.predicates">
<code class="sig-name descname">predicates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.predicates" title="Permalink to this definition">¶</a></dt>
<dd><p>The objects to include in a rule (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.Rule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.Rule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">predicates=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF Regional Rule.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the rule.</p></li>
<li><p><strong>predicates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The objects to include in a rule (documented below).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>predicates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RuleGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">RuleGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activated_rules=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Rule Group Resource</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.activated_rules">
<code class="sig-name descname">activated_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.activated_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of activated rules, see below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the WAF Regional Rule Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the metrics from the rule group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the rule group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.RuleGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RuleGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activated_rules=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RuleGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activated_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of activated rules, see below</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the WAF Regional Rule Group.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules are evaluated. Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">rule</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule type, either <cite>``REGULAR`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_, <cite>``RATE_BASED`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rate_based_rule.html</a>&gt;`_, or <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REGULAR</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.RuleGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.RuleGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.RuleGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SizeConstraintSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">SizeConstraintSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">size_constraints=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Size Constraint Set Resource for use with Application Load Balancer.</p>
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
<dl class="attribute">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the Size Constraint Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.size_constraints">
<code class="sig-name descname">size_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.size_constraints" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">size_constraints=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SizeConstraintSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.SizeConstraintSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SizeConstraintSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SizeConstraintSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">SqlInjectionMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sql_injection_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional SQL Injection Match Set Resource for use with Application Load Balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</p></li>
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
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_SqlInjectionMatchTuple.html#WAF-Type-regional_SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the SizeConstraintSet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.sql_injection_match_tuples">
<code class="sig-name descname">sql_injection_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.sql_injection_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies where in a web request to look for snippets of malicious SQL code.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want to search, e.g. <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>.
If <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit this field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string.
e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">BODY</span></code>.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_SqlInjectionMatchTuple.html#WAF-Type-regional_SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sql_injection_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlInjectionMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the SizeConstraintSet.</p></li>
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
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_FieldToMatch.html">docs</a>
for all supported values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on <code class="docutils literal notranslate"><span class="pre">field_to_match</span></code> before inspecting a request for a match.
e.g. <code class="docutils literal notranslate"><span class="pre">CMD_LINE</span></code>, <code class="docutils literal notranslate"><span class="pre">HTML_ENTITY_DECODE</span></code> or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
See <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_SqlInjectionMatchTuple.html#WAF-Type-regional_SqlInjectionMatchTuple-TextTransformation">docs</a>
for all supported values.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.SqlInjectionMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.SqlInjectionMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">WebAcl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">logging_configuration=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional Web ACL Resource for use with Application Load Balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action that you want AWS WAF Regional to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL.</p></li>
<li><p><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of configuration blocks containing rules for the web ACL. Detailed below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
<p>The <strong>logging_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block of the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block of the override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the associated WAF (Regional) rule (e.g. <cite>``wafregional.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_). WAF (Global) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the WAF Regional WebACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.default_action">
<code class="sig-name descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action that you want AWS WAF Regional to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.logging_configuration">
<code class="sig-name descname">logging_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.logging_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to enable WAF logging. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description for the Amazon CloudWatch metric of this web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or description of the web ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of configuration blocks containing rules for the web ACL. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block of the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block of the override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the associated WAF (Regional) rule (e.g. <cite>``wafregional.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_). WAF (Global) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAcl.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">default_action=None</em>, <em class="sig-param">logging_configuration=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the WAF Regional WebACL.</p></li>
<li><p><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action that you want AWS WAF Regional to take when a request doesn’t match the criteria in any of the rules that are associated with the web ACL.</p></li>
<li><p><strong>logging_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to enable WAF logging. Detailed below.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description for the Amazon CloudWatch metric of this web ACL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or description of the web ACL.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of configuration blocks containing rules for the web ACL. Detailed below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
<p>The <strong>logging_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">log_destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redactedFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing parts of the request that you want redacted from the logs. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of configuration blocks for fields to redact. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block of the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Not used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block of the override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule.  Only used if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the associated WAF (Regional) rule (e.g. <cite>``wafregional.Rule`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html">https://www.terraform.io/docs/providers/aws/r/wafregional_rule.html</a>&gt;`_). WAF (Global) rules cannot be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how you want AWS WAF Regional to respond to requests that match the settings in a rule. e.g. <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">BLOCK</span></code> or <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAclAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">WebAclAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">resource_arn=None</em>, <em class="sig-param">web_acl_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an association with WAF Regional Web ACL.</p>
<blockquote>
<div><p><strong>Note:</strong> An Application Load Balancer can only be associated with one WAF Regional WebACL.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Regional WebACL to create an association.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAclAssociation.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.WebAclAssociation.web_acl_id">
<code class="sig-name descname">web_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.web_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Regional WebACL to create an association.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAclAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">resource_arn=None</em>, <em class="sig-param">web_acl_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebAclAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Regional WebACL to create an association.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.WebAclAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.WebAclAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.WebAclAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.XssMatchSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">XssMatchSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xss_match_tuples=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Regional XSS Match Set Resource for use with Application Load Balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the set</p></li>
<li><p><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>xss_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code> or <code class="docutils literal notranslate"><span class="pre">METHOD</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.wafregional.XssMatchSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.wafregional.XssMatchSet.xss_match_tuples">
<code class="sig-name descname">xss_match_tuples</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.xss_match_tuples" title="Permalink to this definition">¶</a></dt>
<dd><p>The parts of web requests that you want to inspect for cross-site scripting attacks.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The part of the web request that you want AWS WAF to search for a specified string. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code> or <code class="docutils literal notranslate"><span class="pre">METHOD</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.XssMatchSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">xss_match_tuples=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing XssMatchSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the set</p></li>
<li><p><strong>xss_match_tuples</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parts of web requests that you want to inspect for cross-site scripting attacks.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>xss_match_tuples</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldToMatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies where in a web request to look for cross-site scripting attacks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">HEADER</span></code>, enter the name of the header that you want the WAF to search, for example, <code class="docutils literal notranslate"><span class="pre">User-Agent</span></code> or <code class="docutils literal notranslate"><span class="pre">Referer</span></code>. If the value of <code class="docutils literal notranslate"><span class="pre">type</span></code> is any other value, omit <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The part of the web request that you want AWS WAF to search for a specified string. e.g. <code class="docutils literal notranslate"><span class="pre">HEADER</span></code> or <code class="docutils literal notranslate"><span class="pre">METHOD</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">textTransformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.wafregional.XssMatchSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.XssMatchSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.XssMatchSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafregional.get_ipset">
<code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">get_ipset</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.get_ipset" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">wafregional.IpSet</span></code> Retrieves a WAF Regional IP Set Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF Regional IP set.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.wafregional.get_rate_based_mod">
<code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">get_rate_based_mod</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.get_rate_based_mod" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">wafregional.RateBasedRule</span></code> Retrieves a WAF Regional Rate Based Rule Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF Regional rate based rule.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.wafregional.get_rule">
<code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">get_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.get_rule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">wafregional.Rule</span></code> Retrieves a WAF Regional Rule Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF Regional rule.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.wafregional.get_web_acl">
<code class="sig-prename descclassname">pulumi_aws.wafregional.</code><code class="sig-name descname">get_web_acl</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafregional.get_web_acl" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">wafregional.WebAcl</span></code> Retrieves a WAF Regional Web ACL Resource Id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the WAF Regional Web ACL.</p>
</dd>
</dl>
</dd></dl>

</div>
