---
title: Module kms
title_tag: Module kms | Package pulumi_alicloud | Python SDK
linktitle: kms
notitle: true
---

<div class="section" id="kms">
<h1>kms<a class="headerlink" href="#kms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.kms"></span><dl class="class">
<dt id="pulumi_alicloud.kms.AwaitableGetCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.AwaitableGetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetKeysResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">keys=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.AwaitableGetPlaintextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">AwaitableGetPlaintextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.AwaitableGetPlaintextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.Ciphertext">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Ciphertext</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Ciphertext resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The globally unique ID of the CMK.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `encryption_context` -
(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted which must be encoded in Base64.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>The ciphertext of the data key encrypted with the primary CMK version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique ID of the CMK.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_context</span></code> -
(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.Ciphertext.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>The plaintext to be encrypted which must be encoded in Base64.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.kms.Ciphertext.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ciphertext resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ciphertext_blob</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ciphertext of the data key encrypted with the primary CMK version.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The globally unique ID of the CMK.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `encryption_context` -
(Optional, ForceNew) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted which must be encoded in Base64.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.kms.Ciphertext.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Ciphertext.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Ciphertext.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.GetCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCiphertext.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetCiphertextResult.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>The ciphertext of the data key encrypted with the primary CMK version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetCiphertextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetCiphertextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.GetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetKeysResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">keys=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeys.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS key IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.keys">
<code class="sig-name descname">keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS keys. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the key. Possible values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">PendingDeletion</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetKeysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.GetPlaintextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">GetPlaintextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlaintext.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique ID of the CMK. It is the ID of the CMK used to decrypt ciphertext.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>The decrypted plaintext.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.GetPlaintextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.GetPlaintextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.kms.Key">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">Key</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>A kms key can help user to protect data security in the transmission process.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Defaults to true.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.kms.Key.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alicloud Resource Name (ARN) of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.Key.deletion_window_in_days">
<code class="sig-name descname">deletion_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.Key.is_enabled">
<code class="sig-name descname">is_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the key is enabled. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.kms.Key.key_usage">
<code class="sig-name descname">key_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.kms.Key.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.kms.Key.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">key_usage=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Key resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alicloud Resource Name (ARN) of the key.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Defaults to true.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the usage of CMK. Currently, default to ‘ENCRYPT/DECRYPT’, indicating that CMK is used for encryption and decryption.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/kms_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.kms.Key.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.Key.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.kms.get_ciphertext">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_ciphertext</code><span class="sig-paren">(</span><em class="sig-param">encryption_context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key_id</strong> (<em>str</em>) – The globally unique ID of the CMK.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `encryption_context` -
(Optional) The Encryption context. If you specify this parameter here, it is also required when you call the Decrypt API operation. For more information, see [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>plaintext</strong> (<em>str</em>) – The plaintext to be encrypted which must be encoded in Base64.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.kms.get_keys">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_keys</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of KMS keys in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter the results by the KMS key description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of KMS key IDs.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Filter the results by status of the KMS keys. Valid values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">PendingDeletion</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_keys.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_keys.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.kms.get_plaintext">
<code class="sig-prename descclassname">pulumi_alicloud.kms.</code><code class="sig-name descname">get_plaintext</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">encryption_context=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.kms.get_plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>ciphertext_blob</strong> (<em>str</em>) – The ciphertext to be decrypted.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_plaintext.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kms_plaintext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
