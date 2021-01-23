---
title: Package pulumi_cloudinit
title_tag: Package pulumi_cloudinit | Python SDK
linktitle: pulumi_cloudinit
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "cloudinit" >}}

<div class="section" id="pulumi-cloudinit">
<h1>Pulumi CloudInit<a class="headerlink" href="#pulumi-cloudinit" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudinit">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-cloudinit/issues">pulumi/pulumi-cloudinit repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudinit/issues">terraform-providers/terraform-provider-cloudinit repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_cloudinit"></span><dl class="py class">
<dt id="pulumi_cloudinit.AwaitableGetConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudinit.</code><code class="sig-name descname">AwaitableGetConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">base64_encode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boundary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rendered</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.AwaitableGetConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudinit.Config">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudinit.</code><code class="sig-name descname">Config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base64_encode</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boundary</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ConfigPartArgs, Mapping[str, Any], Awaitable[Union[ConfigPartArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ConfigPartArgs, Mapping[str, Any], Awaitable[Union[ConfigPartArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Config" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Config resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_cloudinit.Config.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base64_encode</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boundary</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ConfigPartArgs, Mapping[str, Any], Awaitable[Union[ConfigPartArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ConfigPartArgs, Mapping[str, Any], Awaitable[Union[ConfigPartArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rendered</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudinit.config.Config<a class="headerlink" href="#pulumi_cloudinit.Config.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Config resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rendered</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – rendered cloudinit configuration</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudinit.Config.rendered">
<em class="property">property </em><code class="sig-name descname">rendered</code><a class="headerlink" href="#pulumi_cloudinit.Config.rendered" title="Permalink to this definition">¶</a></dt>
<dd><p>rendered cloudinit configuration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudinit.Config.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Config.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudinit.Config.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Config.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudinit.GetConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudinit.</code><code class="sig-name descname">GetConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">base64_encode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boundary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rendered</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.GetConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConfig.</p>
<dl class="py method">
<dt id="pulumi_cloudinit.GetConfigResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudinit.GetConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudinit.GetConfigResult.rendered">
<em class="property">property </em><code class="sig-name descname">rendered</code><a class="headerlink" href="#pulumi_cloudinit.GetConfigResult.rendered" title="Permalink to this definition">¶</a></dt>
<dd><p>The final rendered multi-part cloud-init config.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudinit.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudinit.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudinit package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudinit.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudinit.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudinit.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudinit.get_config">
<code class="sig-prename descclassname">pulumi_cloudinit.</code><code class="sig-name descname">get_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">base64_encode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boundary</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetConfigPartArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudinit.get_config.AwaitableGetConfigResult<a class="headerlink" href="#pulumi_cloudinit.get_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Renders a <a class="reference external" href="https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive">multipart MIME configuration</a>
for use with <a class="reference external" href="https://cloudinit.readthedocs.io/">cloud-init</a>.</p>
<p>Cloud-init is a commonly-used startup configuration utility for cloud compute
instances. It accepts configuration via provider-specific user data mechanisms,
such as <code class="docutils literal notranslate"><span class="pre">user_data</span></code> for Amazon EC2 instances. Multipart MIME is one of the
data formats it accepts. For more information, see
<a class="reference external" href="https://cloudinit.readthedocs.io/en/latest/topics/format.html">User-Data Formats</a>
in the cloud-init manual.</p>
<p>This is not a generalized utility for producing multipart MIME messages. Its
featureset is specialized for the features of cloud-init.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudinit</span> <span class="k">as</span> <span class="nn">cloudinit</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">cloudinit</span><span class="o">.</span><span class="n">get_config</span><span class="p">(</span><span class="n">base64_encode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">gzip</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">cloudinit</span><span class="o">.</span><span class="n">GetConfigPartArgs</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="s2">&quot;baz&quot;</span><span class="p">,</span>
        <span class="n">content_type</span><span class="o">=</span><span class="s2">&quot;text/x-shellscript&quot;</span><span class="p">,</span>
        <span class="n">filename</span><span class="o">=</span><span class="s2">&quot;foobar.sh&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>base64_encode</strong> (<em>bool</em>) – Base64 encoding of the rendered output. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>,
and cannot be disabled if <code class="docutils literal notranslate"><span class="pre">gzip</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>boundary</strong> (<em>str</em>) – Define the Writer’s default boundary separator. Defaults to <code class="docutils literal notranslate"><span class="pre">MIMEBOUNDARY</span></code>.</p></li>
<li><p><strong>gzip</strong> (<em>bool</em>) – Specify whether or not to gzip the rendered output. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>parts</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetConfigPartArgs'</em><em>]</em><em>]</em>) – A nested block type which adds a file to the generated
cloud-init configuration. Use multiple <code class="docutils literal notranslate"><span class="pre">part</span></code> blocks to specify multiple
files, which will be included in order of declaration in the final MIME
document.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
