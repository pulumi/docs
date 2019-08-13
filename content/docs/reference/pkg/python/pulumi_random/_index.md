---
title: Package pulumi_random
---

<div class="section" id="pulumi-random">
<h1>Pulumi Random<a class="headerlink" href="#pulumi-random" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-random/issues">pulumi/pulumi-random repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/issues">terraform-providers/terraform-provider-random repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_random"></span><dl class="class">
<dt id="pulumi_random.Provider">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the random package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_random.Provider.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomId">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomId</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>byte_length=None</em>, <em>keepers=None</em>, <em>prefix=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomId</span></code> generates random numbers that are intended to be
used as unique identifiers for other resources.</p>
<p>This resource <em>does</em> use a cryptographic random number generator in order
to minimize the chance of collisions, making the results of this resource
when a 16-byte identifier is requested of equivalent uniqueness to a
type-4 UUID.</p>
<p>This resource can be used in conjunction with resources that have
the <code class="docutils literal notranslate"><span class="pre">create_before_destroy</span></code> lifecycle flag set to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>byte_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of random bytes to produce. The
minimum value is 1, which produces eight bits of randomness.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary string to prefix the output value with. This
string is supplied as-is, meaning it is not guaranteed to be URL-safe or
base64 encoded.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/id.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/id.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomId.b64_std">
<code class="descname">b64_std</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.b64_std" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in base64 without additional transformations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.b64_url">
<code class="descname">b64_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.b64_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the characters <code class="docutils literal notranslate"><span class="pre">_</span></code> and <code class="docutils literal notranslate"><span class="pre">-</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.byte_length">
<code class="descname">byte_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.byte_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of random bytes to produce. The
minimum value is 1, which produces eight bits of randomness.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.dec">
<code class="descname">dec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.dec" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in non-padded decimal digits.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.hex">
<code class="descname">hex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.hex" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte length.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.prefix">
<code class="descname">prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary string to prefix the output value with. This
string is supplied as-is, meaning it is not guaranteed to be URL-safe or
base64 encoded.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomId.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>b64=None</em>, <em>b64_std=None</em>, <em>b64_url=None</em>, <em>byte_length=None</em>, <em>dec=None</em>, <em>hex=None</em>, <em>keepers=None</em>, <em>prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomId resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] b64_std: The generated id presented in base64 without additional transformations.
:param pulumi.Input[str] b64<em>url: The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the characters `</em><code class="docutils literal notranslate"><span class="pre">and</span></code>-<a href="#id1"><span class="problematic" id="id2">`</span></a>.
:param pulumi.Input[float] byte_length: The number of random bytes to produce. The</p>
<blockquote>
<div>minimum value is 1, which produces eight bits of randomness.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>dec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generated id presented in non-padded decimal digits.</li>
<li><strong>hex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte length.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary string to prefix the output value with. This
string is supplied as-is, meaning it is not guaranteed to be URL-safe or
base64 encoded.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/id.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/id.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomId.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomId.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomInteger">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomInteger</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>max=None</em>, <em>min=None</em>, <em>seed=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomInteger</span></code> generates random values from a given range, described by the <code class="docutils literal notranslate"><span class="pre">min</span></code> and <code class="docutils literal notranslate"><span class="pre">max</span></code> attributes of a given resource.</p>
<p>This resource can be used in conjunction with resources that have
the <code class="docutils literal notranslate"><span class="pre">create_before_destroy</span></code> lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum inclusive value of the range.</li>
<li><strong>min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum inclusive value of the range.</li>
<li><strong>seed</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom seed to always produce the same value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/integer.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/integer.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomInteger.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomInteger.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomInteger.max">
<code class="descname">max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomInteger.max" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum inclusive value of the range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomInteger.min">
<code class="descname">min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomInteger.min" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum inclusive value of the range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomInteger.result">
<code class="descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomInteger.result" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) The random Integer result.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomInteger.seed">
<code class="descname">seed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomInteger.seed" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom seed to always produce the same value.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomInteger.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>max=None</em>, <em>min=None</em>, <em>result=None</em>, <em>seed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomInteger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will</p>
<blockquote>
<div>trigger a new id to be generated. See
the main provider documentation for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum inclusive value of the range.</li>
<li><strong>min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum inclusive value of the range.</li>
<li><strong>result</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (int) The random Integer result.</li>
<li><strong>seed</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom seed to always produce the same value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/integer.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/integer.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomInteger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomInteger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomPet">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomPet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>prefix=None</em>, <em>separator=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomPet</span></code> generates random pet names that are intended to be
used as unique identifiers for other resources.</p>
<p>This resource can be used in conjunction with resources that have
the <code class="docutils literal notranslate"><span class="pre">create_before_destroy</span></code> lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length (in words) of the pet name.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string to prefix the name with.</li>
<li><strong>separator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The character to separate words in the pet name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/pet.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/pet.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomPet.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomPet.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomPet.length">
<code class="descname">length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomPet.length" title="Permalink to this definition">¶</a></dt>
<dd><p>The length (in words) of the pet name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomPet.prefix">
<code class="descname">prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomPet.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A string to prefix the name with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomPet.separator">
<code class="descname">separator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomPet.separator" title="Permalink to this definition">¶</a></dt>
<dd><p>The character to separate words in the pet name.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomPet.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>prefix=None</em>, <em>separator=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomPet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will</p>
<blockquote>
<div>trigger a new id to be generated. See
the main provider documentation for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length (in words) of the pet name.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string to prefix the name with.</li>
<li><strong>separator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The character to separate words in the pet name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/pet.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/pet.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomPet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomPet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomShuffle">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomShuffle</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>inputs=None</em>, <em>keepers=None</em>, <em>result_count=None</em>, <em>seed=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomShuffle</span></code> generates a random permutation of a list
of strings given as an argument.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of strings to shuffle.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>result_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of results to return. Defaults to
the number of items in the <code class="docutils literal notranslate"><span class="pre">input</span></code> list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/shuffle.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/shuffle.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.inputs">
<code class="descname">inputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of strings to shuffle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.results">
<code class="descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.results" title="Permalink to this definition">¶</a></dt>
<dd><p>Random permutation of the list of strings given in <code class="docutils literal notranslate"><span class="pre">input</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.result_count">
<code class="descname">result_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.result_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of results to return. Defaults to
the number of items in the <code class="docutils literal notranslate"><span class="pre">input</span></code> list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomShuffle.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>inputs=None</em>, <em>keepers=None</em>, <em>results=None</em>, <em>result_count=None</em>, <em>seed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomShuffle resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] inputs: The list of strings to shuffle.
:param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will</p>
<blockquote>
<div>trigger a new id to be generated. See
the main provider documentation for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>results</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Random permutation of the list of strings given in <code class="docutils literal notranslate"><span class="pre">input</span></code>.</li>
<li><strong>result_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of results to return. Defaults to
the number of items in the <code class="docutils literal notranslate"><span class="pre">input</span></code> list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/shuffle.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/shuffle.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomShuffle.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomShuffle.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomString">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomString</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>lower=None</em>, <em>min_lower=None</em>, <em>min_numeric=None</em>, <em>min_special=None</em>, <em>min_upper=None</em>, <em>number=None</em>, <em>override_special=None</em>, <em>special=None</em>, <em>upper=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomString</span></code> generates a random permutation of alphanumeric
characters and optionally special characters.</p>
<p>This resource <em>does</em> use a cryptographic random number generator.</p>
<p>Historically this resource’s intended usage has been ambiguous as the original example
used it in a password. For backwards compatibility it will
continue to exist. For unique ids please use random_id, for console and log safe
random values please use random_password.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of the string desired</li>
<li><strong>lower</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include lowercase alphabet characters
in random string.</li>
<li><strong>min_lower</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of lowercase alphabet
characters in random string.</li>
<li><strong>min_numeric</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of numeric characters
in random string.</li>
<li><strong>min_special</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of special characters
in random string.</li>
<li><strong>min_upper</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of uppercase alphabet
characters in random string.</li>
<li><strong>number</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include numeric characters in random
string.</li>
<li><strong>override*special</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Supply your own list of special characters to
use for string generation.  This overrides characters list in the special
argument.  The special argument must still be set to true for any overwritten
characters to be used in generation.</p>
</li>
<li><strong>special</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include special characters in random
string. These are ‘!&#64;#$%&amp;*()-<a href="#id5"><span class="problematic" id="id6">*</span></a>=+[]{}&lt;&gt;:?’</li>
<li><strong>upper</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include uppercase alphabet characters
in random string.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/string.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/string.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomString.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.length">
<code class="descname">length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.length" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of the string desired</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.lower">
<code class="descname">lower</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.lower" title="Permalink to this definition">¶</a></dt>
<dd><p>(default true) Include lowercase alphabet characters
in random string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.min_lower">
<code class="descname">min_lower</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.min_lower" title="Permalink to this definition">¶</a></dt>
<dd><p>(default 0) Minimum number of lowercase alphabet
characters in random string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.min_numeric">
<code class="descname">min_numeric</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.min_numeric" title="Permalink to this definition">¶</a></dt>
<dd><p>(default 0) Minimum number of numeric characters
in random string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.min_special">
<code class="descname">min_special</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.min_special" title="Permalink to this definition">¶</a></dt>
<dd><p>(default 0) Minimum number of special characters
in random string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.min_upper">
<code class="descname">min_upper</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.min_upper" title="Permalink to this definition">¶</a></dt>
<dd><p>(default 0) Minimum number of uppercase alphabet
characters in random string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.number">
<code class="descname">number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.number" title="Permalink to this definition">¶</a></dt>
<dd><p>(default true) Include numeric characters in random
string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.override_special">
<code class="descname">override_special</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.override_special" title="Permalink to this definition">¶</a></dt>
<dd><p>Supply your own list of special characters to
use for string generation.  This overrides characters list in the special
argument.  The special argument must still be set to true for any overwritten
characters to be used in generation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.result">
<code class="descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.result" title="Permalink to this definition">¶</a></dt>
<dd><p>Random string generated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.special">
<code class="descname">special</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.special" title="Permalink to this definition">¶</a></dt>
<dd><p>(default true) Include special characters in random
string. These are ‘!&#64;#$%&amp;*()-_=+[]{}&lt;&gt;:?’</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomString.upper">
<code class="descname">upper</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomString.upper" title="Permalink to this definition">¶</a></dt>
<dd><p>(default true) Include uppercase alphabet characters
in random string.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomString.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>lower=None</em>, <em>min_lower=None</em>, <em>min_numeric=None</em>, <em>min_special=None</em>, <em>min_upper=None</em>, <em>number=None</em>, <em>override_special=None</em>, <em>result=None</em>, <em>special=None</em>, <em>upper=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomString resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will</p>
<blockquote>
<div>trigger a new id to be generated. See
the main provider documentation for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of the string desired</li>
<li><strong>lower</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include lowercase alphabet characters
in random string.</li>
<li><strong>min_lower</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of lowercase alphabet
characters in random string.</li>
<li><strong>min_numeric</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of numeric characters
in random string.</li>
<li><strong>min_special</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of special characters
in random string.</li>
<li><strong>min_upper</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (default 0) Minimum number of uppercase alphabet
characters in random string.</li>
<li><strong>number</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include numeric characters in random
string.</li>
<li><strong>override*special</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Supply your own list of special characters to
use for string generation.  This overrides characters list in the special
argument.  The special argument must still be set to true for any overwritten
characters to be used in generation.</p>
</li>
<li><strong>result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Random string generated.</li>
<li><strong>special</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include special characters in random
string. These are ‘!&#64;#$%&amp;*()-<a href="#id9"><span class="problematic" id="id10">*</span></a>=+[]{}&lt;&gt;:?’</li>
<li><strong>upper</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include uppercase alphabet characters
in random string.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/string.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/string.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomString.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomString.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomUuid">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomUuid</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <code class="docutils literal notranslate"><span class="pre">.RandomUuid</span></code> generates random uuid string that is intended to be
used as unique identifiers for other resources.</p>
<p>This resource uses the <code class="docutils literal notranslate"><span class="pre">hashicorp/go-uuid</span></code> to generate a UUID-formatted string
for use with services needed a unique string identifier.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new uuid to be generated. See
the main provider documentation for more information.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/uuid.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/uuid.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_random.RandomUuid.keepers">
<code class="descname">keepers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomUuid.keepers" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary map of values that, when changed, will
trigger a new uuid to be generated. See
the main provider documentation for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomUuid.result">
<code class="descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomUuid.result" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated uuid presented in string format.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_random.RandomUuid.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>keepers=None</em>, <em>result=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RandomUuid resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will</p>
<blockquote>
<div>trigger a new uuid to be generated. See
the main provider documentation for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generated uuid presented in string format.</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/uuid.html.markdown">https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/uuid.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomUuid.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_random.RandomUuid.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
