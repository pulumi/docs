---
title: Module kms
title_tag: Module kms | Package pulumi_alicloud | Python SDK
linktitle: kms
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="kms">
<h1>kms<a class="headerlink" href="#kms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.kms"></span><dl class="py class">
<dt id="pulumi_alicloud.kms.Alias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Alias</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Create an alias for the master key (CMK).</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.77.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">this_key</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">Key</span><span class="p">(</span><span class="s2">&quot;thisKey&quot;</span><span class="p">)</span>
<span class="n">this_alias</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">Alias</span><span class="p">(</span><span class="s2">&quot;thisAlias&quot;</span><span class="p">,</span>
    <span class="n">alias_name</span><span class="o">=</span><span class="s2">&quot;alias/test_kms_alias&quot;</span><span class="p">,</span>
    <span class="n">key_id</span><span class="o">=</span><span class="n">this_key</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias of CMK. <code class="docutils literal notranslate"><span class="pre">Encrypt</span></code>、<code class="docutils literal notranslate"><span class="pre">GenerateDataKey</span></code>、<code class="docutils literal notranslate"><span class="pre">DescribeKey</span></code> can be called using aliases. Length of characters other than prefixes: minimum length of 1 character and maximum length of 255 characters. Must contain prefix <code class="docutils literal notranslate"><span class="pre">alias/</span></code>.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the key.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Alias.alias_name">
<code class="sig-name descname">alias_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Alias.alias_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias of CMK. <code class="docutils literal notranslate"><span class="pre">Encrypt</span></code>、<code class="docutils literal notranslate"><span class="pre">GenerateDataKey</span></code>、<code class="docutils literal notranslate"><span class="pre">DescribeKey</span></code> can be called using aliases. Length of characters other than prefixes: minimum length of 1 character and maximum length of 255 characters. Must contain prefix <code class="docutils literal notranslate"><span class="pre">alias/</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Alias.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Alias.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Alias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Alias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias of CMK. <code class="docutils literal notranslate"><span class="pre">Encrypt</span></code>、<code class="docutils literal notranslate"><span class="pre">GenerateDataKey</span></code>、<code class="docutils literal notranslate"><span class="pre">DescribeKey</span></code> can be called using aliases. Length of characters other than prefixes: minimum length of 1 character and maximum length of 255 characters. Must contain prefix <code class="docutils literal notranslate"><span class="pre">alias/</span></code>.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Alias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Alias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.AwaitableGetAliasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetAliasesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetAliasesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetKeyVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetKeyVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetKeyVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetPlaintextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetPlaintextResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetPlaintextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetSecretVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetSecretVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetSecretVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.AwaitableGetSecretsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetSecretsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fetch_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secrets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetSecretsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.Ciphertext">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Ciphertext</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Ciphertext resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] encryption_context: -</p>
<blockquote>
<div><p>(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The globally unique ID of the CMK.</p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted which must be encoded in Base64.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>The ciphertext of the data key encrypted with the primary CMK version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.encryption_context">
<code class="sig-name descname">encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li></li>
</ul>
<p>(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique ID of the CMK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.plaintext">
<code class="sig-name descname">plaintext</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>The plaintext to be encrypted which must be encoded in Base64.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Ciphertext.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ciphertext resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ciphertext_blob</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ciphertext of the data key encrypted with the primary CMK version.</p></li>
<li><p><strong>encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <ul>
<li></li>
</ul>
<p>(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p>
</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The globally unique ID of the CMK.</p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted which must be encoded in Base64.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Ciphertext.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Ciphertext.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.GetAliasesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetAliasesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetAliasesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAliases.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetAliasesResult.aliases">
<code class="sig-name descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetAliasesResult.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS User alias. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetAliasesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetAliasesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetAliasesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetAliasesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of kms aliases IDs. The value is same as KMS alias_name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetAliasesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetAliasesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS alias name.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCiphertext.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetCiphertextResult.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>The ciphertext of the data key encrypted with the primary CMK version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetCiphertextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetKeyVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetKeyVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetKeyVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyVersions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeyVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeyVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeyVersionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeyVersionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS KeyVersion IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeyVersionsResult.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeyVersionsResult.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeyVersionsResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeyVersionsResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS KeyVersions. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeys.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS key IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.keys">
<code class="sig-name descname">keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS keys. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the key. Possible values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">PendingDeletion</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetPlaintextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetPlaintextResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlaintext.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique ID of the CMK. It is the ID of the CMK used to decrypt ciphertext.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>The decrypted plaintext.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetSecretVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetSecretVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecretVersions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretVersionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretVersionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Kms Secret Version ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretVersionsResult.secret_name">
<code class="sig-name descname">secret_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretVersionsResult.secret_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretVersionsResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretVersionsResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS Secret Versions. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.GetSecretsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetSecretsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fetch_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secrets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecrets.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Kms Secret ids. The value is same as KMS secret_name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS Secret names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretsResult.secrets">
<code class="sig-name descname">secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult.secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS Secrets. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.GetSecretsResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetSecretsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.kms.Key">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_rotation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_usage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pending_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protection_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rotation_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>A kms key can help user to protect data security in the transmission process. For information about Alikms Key and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28947.htm">What is Resource Alikms Key</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.85.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">key</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">Key</span><span class="p">(</span><span class="s2">&quot;key&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Hello KMS&quot;</span><span class="p">,</span>
    <span class="n">key_state</span><span class="o">=</span><span class="s2">&quot;Enabled&quot;</span><span class="p">,</span>
    <span class="n">pending_window_in_days</span><span class="o">=</span><span class="s2">&quot;7&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automatic_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to enable automatic key rotation. Default:”Disabled”.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘deletion_window_in_days’ has been deprecated from provider version 1.85.0. New field ‘pending_window_in_days’ instead.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the key as viewed in Alicloud console.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Field ‘is_enabled’ has been deprecated from provider version 1.85.0. New field ‘key_state’ instead.</p></li>
<li><p><strong>key_spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the CMK.</p></li>
<li><p><strong>key_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of CMK. Defaults to Enabled.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the key material for the CMK. Defaults to “Aliyun_KMS”.</p></li>
<li><p><strong>pending_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>protection_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protection level of the CMK. Defaults to “SOFTWARE”.</p></li>
<li><p><strong>rotation_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of automatic key rotation. Unit: seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alicloud Resource Name (ARN) of the key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creation_date</span></code> -The date and time when the CMK was created. The time is displayed in UTC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">creator</span></code> -The creator of the CMK.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_date</span></code> -The scheduled date to delete CMK. The time is displayed in UTC. This value is returned only when the KeyState value is PendingDeletion.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.automatic_rotation">
<code class="sig-name descname">automatic_rotation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.automatic_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable automatic key rotation. Default:”Disabled”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.deletion_window_in_days">
<code class="sig-name descname">deletion_window_in_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘deletion_window_in_days’ has been deprecated from provider version 1.85.0. New field ‘pending_window_in_days’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the key as viewed in Alicloud console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.is_enabled">
<code class="sig-name descname">is_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘is_enabled’ has been deprecated from provider version 1.85.0. New field ‘key_state’ instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.key_spec">
<code class="sig-name descname">key_spec</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.key_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the CMK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.key_state">
<code class="sig-name descname">key_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.key_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of CMK. Defaults to Enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.key_usage">
<code class="sig-name descname">key_usage</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.last_rotation_date">
<code class="sig-name descname">last_rotation_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.last_rotation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the last rotation was performed. The time is displayed in UTC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.material_expire_time">
<code class="sig-name descname">material_expire_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.material_expire_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time and date the key material for the CMK expires. The time is displayed in UTC. If the value is empty, the key material for the CMK does not expire.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.next_rotation_date">
<code class="sig-name descname">next_rotation_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.next_rotation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the next rotation is scheduled for execution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.origin">
<code class="sig-name descname">origin</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the key material for the CMK. Defaults to “Aliyun_KMS”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.pending_window_in_days">
<code class="sig-name descname">pending_window_in_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.pending_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.primary_key_version">
<code class="sig-name descname">primary_key_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.primary_key_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the current primary key version of the symmetric CMK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.protection_level">
<code class="sig-name descname">protection_level</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.protection_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The protection level of the CMK. Defaults to “SOFTWARE”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Key.rotation_interval">
<code class="sig-name descname">rotation_interval</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.rotation_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of automatic key rotation. Unit: seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Key.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_rotation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_usage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_rotation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">material_expire_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_rotation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pending_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_key_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protection_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rotation_interval</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Key resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alicloud Resource Name (ARN) of the key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `creation_date` -The date and time when the CMK was created. The time is displayed in UTC.
* `creator` -The creator of the CMK.
* `delete_date` -The scheduled date to delete CMK. The time is displayed in UTC. This value is returned only when the KeyState value is PendingDeletion.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>automatic_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to enable automatic key rotation. Default:”Disabled”.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘deletion_window_in_days’ has been deprecated from provider version 1.85.0. New field ‘pending_window_in_days’ instead.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the key as viewed in Alicloud console.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Field ‘is_enabled’ has been deprecated from provider version 1.85.0. New field ‘key_state’ instead.</p></li>
<li><p><strong>key_spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the CMK.</p></li>
<li><p><strong>key_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of CMK. Defaults to Enabled.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p></li>
<li><p><strong>last_rotation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time the last rotation was performed. The time is displayed in UTC.</p></li>
<li><p><strong>material_expire_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time and date the key material for the CMK expires. The time is displayed in UTC. If the value is empty, the key material for the CMK does not expire.</p></li>
<li><p><strong>next_rotation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the next rotation is scheduled for execution.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the key material for the CMK. Defaults to “Aliyun_KMS”.</p></li>
<li><p><strong>pending_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>primary_key_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the current primary key version of the symmetric CMK.</p></li>
<li><p><strong>protection_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protection level of the CMK. Defaults to “SOFTWARE”.</p></li>
<li><p><strong>rotation_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of automatic key rotation. Unit: seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Key.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Key.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.KeyVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">KeyVersion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Alikms Key Version resource. For information about Alikms Key Version and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/133838.htm">What is Resource Alikms Key Version</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.85.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">this</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">Key</span><span class="p">(</span><span class="s2">&quot;this&quot;</span><span class="p">)</span>
<span class="n">keyversion</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">KeyVersion</span><span class="p">(</span><span class="s2">&quot;keyversion&quot;</span><span class="p">,</span> <span class="n">key_id</span><span class="o">=</span><span class="n">this</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the master key (CMK).</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.KeyVersion.creation_date">
<code class="sig-name descname">creation_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time (UTC time) when the Alikms key version was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.KeyVersion.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the master key (CMK).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.KeyVersion.key_version_id">
<code class="sig-name descname">key_version_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.key_version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the Alikms key version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.KeyVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_version_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>creation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time (UTC time) when the Alikms key version was created.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the master key (CMK).</p></li>
<li><p><strong>key_version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the Alikms key version.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.KeyVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.KeyVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.KeyVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Secret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete_without_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_stages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Secret resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the secret.
:param pulumi.Input[str] encryption_key_id: The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.
:param pulumi.Input[bool] force_delete_without_recovery: Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.
:param pulumi.Input[float] recovery_window_in_days: Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when <code class="docutils literal notranslate"><span class="pre">force_delete_without_recovery</span></code> is true.
:param pulumi.Input[str] secret_data: The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.
:param pulumi.Input[str] secret_data_type: The type of the secret value. Valid values: text, binary. Default to “text”.
:param pulumi.Input[str] secret_name: The name of the secret.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] version_id: The version number of the initial version. Version numbers are unique in each secret object.
:param pulumi.Input[list] version_stages: ) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with “ACSCurrent”.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alicloud Resource Name (ARN) of the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.encryption_key_id">
<code class="sig-name descname">encryption_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.encryption_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.force_delete_without_recovery">
<code class="sig-name descname">force_delete_without_recovery</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.force_delete_without_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.planned_delete_time">
<code class="sig-name descname">planned_delete_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.planned_delete_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the secret is scheduled to be deleted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.recovery_window_in_days">
<code class="sig-name descname">recovery_window_in_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.recovery_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when <code class="docutils literal notranslate"><span class="pre">force_delete_without_recovery</span></code> is true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.secret_data">
<code class="sig-name descname">secret_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.secret_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.secret_data_type">
<code class="sig-name descname">secret_data_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.secret_data_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the secret value. Valid values: text, binary. Default to “text”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.secret_name">
<code class="sig-name descname">secret_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.secret_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.version_id">
<code class="sig-name descname">version_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number of the initial version. Version numbers are unique in each secret object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.kms.Secret.version_stages">
<code class="sig-name descname">version_stages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Secret.version_stages" title="Permalink to this definition">¶</a></dt>
<dd><p>) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with “ACSCurrent”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Secret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete_without_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">planned_delete_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_window_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_stages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Secret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Secret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alicloud Resource Name (ARN) of the secret.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the secret.</p></li>
<li><p><strong>encryption_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.</p></li>
<li><p><strong>force_delete_without_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.</p></li>
<li><p><strong>planned_delete_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the secret is scheduled to be deleted.</p></li>
<li><p><strong>recovery_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when <code class="docutils literal notranslate"><span class="pre">force_delete_without_recovery</span></code> is true.</p></li>
<li><p><strong>secret_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.</p></li>
<li><p><strong>secret_data_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the secret value. Valid values: text, binary. Default to “text”.</p></li>
<li><p><strong>secret_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the secret.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number of the initial version. Version numbers are unique in each secret object.</p></li>
<li><p><strong>version_stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with “ACSCurrent”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.kms.Secret.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Secret.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.get_aliases">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_aliases</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS aliases in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.79.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">kms_aliases</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_aliases</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;d89e8a53-b708-41aa-8c67-6873axxx&quot;</span><span class="p">],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;alias/tf-testKmsAlias_123&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstKeyId&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;kms.getKeys&quot;</span><span class="p">][</span><span class="s2">&quot;kms_keys_ds&quot;</span><span class="p">][</span><span class="s2">&quot;keys&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS aliases IDs. The value is same as KMS alias_name.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter the results by the KMS alias name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_ciphertext">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_ciphertext</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>encryption_context</strong> (<em>dict</em>) – <ul>
<li></li>
</ul>
<p>(Optional) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p>
</p></li>
<li><p><strong>key_id</strong> (<em>str</em>) – The globally unique ID of the CMK.</p></li>
<li><p><strong>plaintext</strong> (<em>str</em>) – The plaintext to be encrypted which must be encoded in Base64.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_key_versions">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_key_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_key_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS KeyVersions in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p>NOTE: Available in v1.85.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">alicloud_kms_key_versions_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_key_versions</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;d89e8a53-b708-41aa-8c67-6873axxx&quot;</span><span class="p">],</span>
    <span class="n">key_id</span><span class="o">=</span><span class="s2">&quot;08438c-b4d5-4d05-928c-07b7xxxx&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;allVersions&quot;</span><span class="p">,</span> <span class="n">alicloud_kms_key_versions_ds</span><span class="o">.</span><span class="n">versions</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS KeyVersion IDs.</p></li>
<li><p><strong>key_id</strong> (<em>str</em>) – The id of kms key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_keys">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS keys in an Alibaba Cloud account according to the specified filters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">kms_keys_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_keys</span><span class="p">(</span><span class="n">description_regex</span><span class="o">=</span><span class="s2">&quot;Hello KMS&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;kms_keys.json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstKeyId&quot;</span><span class="p">,</span> <span class="n">kms_keys_ds</span><span class="o">.</span><span class="n">keys</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter the results by the KMS key description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS key IDs.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Filter the results by status of the KMS keys. Valid values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">PendingDeletion</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_plaintext">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_plaintext</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ciphertext_blob</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ciphertext_blob</strong> (<em>str</em>) – The ciphertext to be decrypted.</p></li>
<li><p><strong>encryption_context</strong> (<em>dict</em>) – <ul>
<li></li>
</ul>
<p>(Optional) The Encryption context. If you specify this parameter in the Encrypt or GenerateDataKey API operation, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_secret_versions">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_secret_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_secret_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS Secret Versions in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.88.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">kms_secret_versions_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_secret_versions</span><span class="p">(</span><span class="n">enable_details</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">secret_name</span><span class="o">=</span><span class="s2">&quot;secret_name&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstSecretData&quot;</span><span class="p">,</span> <span class="n">kms_secret_versions_ds</span><span class="o">.</span><span class="n">versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;secret_data&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enable_details</strong> (<em>bool</em>) – Default to false and only output <code class="docutils literal notranslate"><span class="pre">secret_name</span></code>, <code class="docutils literal notranslate"><span class="pre">version_id</span></code>, <code class="docutils literal notranslate"><span class="pre">version_stages</span></code>. Set it to true can output more details.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS Secret Version ids.</p></li>
<li><p><strong>include_deprecated</strong> (<em>str</em>) – Specifies whether to return deprecated secret versions. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>secret_name</strong> (<em>str</em>) – The name of the secret.</p></li>
<li><p><strong>version_stage</strong> (<em>str</em>) – The stage of the secret version.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.kms.get_secrets">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_secrets</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fetch_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS Secrets in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.86.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">kms_secrets_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">kms</span><span class="o">.</span><span class="n">get_secrets</span><span class="p">(</span><span class="n">fetch_tags</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;name_regex&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;k-aa&quot;</span><span class="p">:</span> <span class="s2">&quot;v-aa&quot;</span><span class="p">,</span>
        <span class="s2">&quot;k-bb&quot;</span><span class="p">:</span> <span class="s2">&quot;v-bb&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstSecretId&quot;</span><span class="p">,</span> <span class="n">kms_secrets_ds</span><span class="o">.</span><span class="n">secrets</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fetch_tags</strong> (<em>bool</em>) – Whether to include the predetermined resource tag in the return value. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS Secret ids. The value is same as KMS secret_name.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter the results by the KMS secret_name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
