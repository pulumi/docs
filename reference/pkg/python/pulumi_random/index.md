<div class="section" id="module-pulumi_random">
<span id="pulumi-random"></span><h1>Pulumi Random<a class="headerlink" href="#module-pulumi_random" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_random.Provider">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the random package. By default, resources use package-wide configuration
settings, however an explicit <cite>Provider</cite> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
[documentation](<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">https://pulumi.io/reference/programming-model.html#providers</a>) for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="pulumi_random.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomId">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomId</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>byte_length=None</em>, <em>keepers=None</em>, <em>prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_id</cite> generates random numbers that are intended to be
used as unique identifiers for other resources.</p>
<p>This resource <em>does</em> use a cryptographic random number generator in order
to minimize the chance of collisions, making the results of this resource
when a 16-byte identifier is requested of equivalent uniqueness to a
type-4 UUID.</p>
<p>This resource can be used in conjunction with resources that have
the <cite>create_before_destroy</cite> lifecycle flag set to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>byte_length</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of random bytes to produce. The
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
<dl class="attribute">
<dt id="pulumi_random.RandomId.b64_std">
<code class="descname">b64_std</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.b64_std" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in base64 without additional transformations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomId.b64_url">
<code class="descname">b64_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomId.b64_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the characters <cite>_</cite> and <cite>-</cite>.</p>
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

<dl class="method">
<dt id="pulumi_random.RandomId.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomId.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomId.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomInteger">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomInteger</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>keepers=None</em>, <em>max=None</em>, <em>min=None</em>, <em>seed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_integer</cite> generates random values from a given range, described by the <cite>min</cite> and <cite>max</cite> attributes of a given resource.</p>
<p>This resource can be used in conjunction with resources that have
the <cite>create_before_destroy</cite> lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>max</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum inclusive value of the range.</li>
<li><strong>min</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum inclusive value of the range.</li>
<li><strong>seed</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom seed to always produce the same value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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

<dl class="method">
<dt id="pulumi_random.RandomInteger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomInteger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomInteger.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomPet">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomPet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>prefix=None</em>, <em>separator=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_pet</cite> generates random pet names that are intended to be
used as unique identifiers for other resources.</p>
<p>This resource can be used in conjunction with resources that have
the <cite>create_before_destroy</cite> lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The length (in words) of the pet name.</li>
<li><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string to prefix the name with.</li>
<li><strong>separator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The character to separate words in the pet name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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

<dl class="method">
<dt id="pulumi_random.RandomPet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomPet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomPet.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomShuffle">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomShuffle</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>inputs=None</em>, <em>keepers=None</em>, <em>result_count=None</em>, <em>seed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_shuffle</cite> generates a random permutation of a list
of strings given as an argument.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of strings to shuffle.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>result_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of results to return. Defaults to
the number of items in the <cite>input</cite> list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.</li>
<li><strong>seed</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary string with which to seed the random number
generator, in order to produce less-volatile permutations of the list.
<strong>Important:</strong> Even with an identical seed, it is not guaranteed that the
same permutation will be produced across different versions of Terraform.
This argument causes the result to be <em>less volatile</em>, but not fixed for
all time.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dd><p>Random permutation of the list of strings given in <cite>input</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.result_count">
<code class="descname">result_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.result_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of results to return. Defaults to
the number of items in the <cite>input</cite> list. If fewer items are requested,
some elements will be excluded from the result. If more items are requested,
items will be repeated in the result but not more frequently than the number
of items in the input list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_random.RandomShuffle.seed">
<code class="descname">seed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_random.RandomShuffle.seed" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary string with which to seed the random number
generator, in order to produce less-volatile permutations of the list.
<strong>Important:</strong> Even with an identical seed, it is not guaranteed that the
same permutation will be produced across different versions of Terraform.
This argument causes the result to be <em>less volatile</em>, but not fixed for
all time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomShuffle.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomShuffle.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomShuffle.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomString">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomString</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>keepers=None</em>, <em>length=None</em>, <em>lower=None</em>, <em>min_lower=None</em>, <em>min_numeric=None</em>, <em>min_special=None</em>, <em>min_upper=None</em>, <em>number=None</em>, <em>override_special=None</em>, <em>special=None</em>, <em>upper=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_string</cite> generates a random permutation of alphanumeric
characters and optionally special characters.</p>
<p>This resource <em>does</em> use a cryptographic random number generator.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
the main provider documentation for more information.</li>
<li><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The length of the string desired</li>
<li><strong>lower</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include lowercase alphabet characters
in random string.</li>
<li><strong>min_lower</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (default 0) Minimum number of lowercase alphabet
characters in random string.</li>
<li><strong>min_numeric</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (default 0) Minimum number of numeric characters
in random string.</li>
<li><strong>min_special</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (default 0) Minimum number of special characters
in random string.</li>
<li><strong>min_upper</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (default 0) Minimum number of uppercase alphabet
characters in random string.</li>
<li><strong>number</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include numeric characters in random
string.</li>
<li><strong>override_special</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Supply your own list of special characters to
use for string generation.  This overrides characters list in the special
argument.  The special argument must still be set to true for any overwritten
characters to be used in generation.</li>
<li><strong>special</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include special characters in random
string. These are ‘!&#64;#$%&amp;*()-_=+[]{}&lt;&gt;:?’</li>
<li><strong>upper</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (default true) Include uppercase alphabet characters
in random string.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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

<dl class="method">
<dt id="pulumi_random.RandomString.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomString.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomString.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_random.RandomUuid">
<em class="property">class </em><code class="descclassname">pulumi_random.</code><code class="descname">RandomUuid</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>keepers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource <cite>random_uuid</cite> generates random uuid string that is intended to be
used as unique identifiers for other resources.</p>
<p>This resource uses the <cite>hashicorp/go-uuid</cite> to generate a UUID-formatted string
for use with services needed a unique string identifier.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>keepers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Arbitrary map of values that, when changed, will
trigger a new uuid to be generated. See
the main provider documentation for more information.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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

<dl class="method">
<dt id="pulumi_random.RandomUuid.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_random.RandomUuid.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_random.RandomUuid.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
