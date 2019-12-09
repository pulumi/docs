---
title: Module kms
title_tag: Module kms | Package pulumi_aws | Python SDK
linktitle: kms
notitle: true
---

<div class="section" id="kms">
<h1>kms<a class="headerlink" href="#kms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.kms"></span><dl class="class">
<dt id="pulumi_aws.kms.Alias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">Alias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">target_key_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases &amp; keys,
but API (hence this provider too) allows you to create as many aliases as
the <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/limits.html">account limits</a> allow you.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates an unique alias beginning with the specified prefix.
The name must start with the word “alias” followed by a forward slash (alias/).  Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>target_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the key for which the alias is for, can be either an ARN or key_id.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an unique alias beginning with the specified prefix.
The name must start with the word “alias” followed by a forward slash (alias/).  Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.target_key_arn">
<code class="sig-name descname">target_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.target_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the target key identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.target_key_id">
<code class="sig-name descname">target_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.target_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier for the key for which the alias is for, can be either an ARN or key_id.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Alias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">target_key_arn=None</em>, <em class="sig-param">target_key_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the key alias.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates an unique alias beginning with the specified prefix.
The name must start with the word “alias” followed by a forward slash (alias/).  Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>target_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the target key identifier.</p></li>
<li><p><strong>target_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the key for which the alias is for, can be either an ARN or key_id.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Alias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Alias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.AwaitableGetAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">AwaitableGetAliasResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">target_key_arn=None</em>, <em class="sig-param">target_key_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.AwaitableGetAliasResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.AwaitableGetCipherTextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">AwaitableGetCipherTextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.AwaitableGetCipherTextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.AwaitableGetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">AwaitableGetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">deletion_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">expiration_model=None</em>, <em class="sig-param">grant_tokens=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_manager=None</em>, <em class="sig-param">key_state=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">valid_to=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.AwaitableGetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.AwaitableGetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">AwaitableGetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">secrets=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.AwaitableGetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.AwaitableGetSecretsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">AwaitableGetSecretsResult</code><span class="sig-paren">(</span><em class="sig-param">plaintext=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.AwaitableGetSecretsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.Ciphertext">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">Ciphertext</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS ciphertext resource allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key. The value returned by this resource
is stable across every apply. For a changing ciphertext value each apply, see
the <cite>``kms.Ciphertext`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/kms_ciphertext.html">https://www.terraform.io/docs/providers/aws/d/kms_ciphertext.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the plaintext be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An optional mapping that makes up the encryption context.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Globally unique key ID for the customer master key.</p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded ciphertext</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.context">
<code class="sig-name descname">context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.context" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional mapping that makes up the encryption context.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Globally unique key ID for the customer master key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Ciphertext.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ciphertext resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ciphertext_blob</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded ciphertext</p></li>
<li><p><strong>context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An optional mapping that makes up the encryption context.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Globally unique key ID for the customer master key.</p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Ciphertext.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Ciphertext.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.ExternalKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">ExternalKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">key_material_base64=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">valid_to=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a KMS Customer Master Key that uses external key material. To instead manage a KMS Customer Master Key where AWS automatically generates and potentially rotates key material, see the <cite>``kms.Key`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/kms_key.html">https://www.terraform.io/docs/providers/aws/r/kms_key.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the key material will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted after destruction of the resource. Must be between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> days. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the key.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Keys pending import can only be <code class="docutils literal notranslate"><span class="pre">false</span></code>. Imported keys default to <code class="docutils literal notranslate"><span class="pre">true</span></code> unless expired.</p></li>
<li><p><strong>key_material_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value map of tags to assign to the key.</p></li>
<li><p><strong>valid_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.deletion_window_in_days">
<code class="sig-name descname">deletion_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted after destruction of the resource. Must be between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> days. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the key is enabled. Keys pending import can only be <code class="docutils literal notranslate"><span class="pre">false</span></code>. Imported keys default to <code class="docutils literal notranslate"><span class="pre">true</span></code> unless expired.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.expiration_model">
<code class="sig-name descname">expiration_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.expiration_model" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the key material expires. Empty when pending key material import, otherwise <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_EXPIRES</span></code> or <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_DOES_NOT_EXPIRE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_material_base64">
<code class="sig-name descname">key_material_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_material_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_state">
<code class="sig-name descname">key_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_usage">
<code class="sig-name descname">key_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>The cryptographic operations for which you can use the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of tags to assign to the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.valid_to">
<code class="sig-name descname">valid_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.valid_to" title="Permalink to this definition">¶</a></dt>
<dd><p>Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.ExternalKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">expiration_model=None</em>, <em class="sig-param">key_material_base64=None</em>, <em class="sig-param">key_state=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">valid_to=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExternalKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the key.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted after destruction of the resource. Must be between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> days. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the key.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Keys pending import can only be <code class="docutils literal notranslate"><span class="pre">false</span></code>. Imported keys default to <code class="docutils literal notranslate"><span class="pre">true</span></code> unless expired.</p></li>
<li><p><strong>expiration_model</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the key material expires. Empty when pending key material import, otherwise <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_EXPIRES</span></code> or <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_DOES_NOT_EXPIRE</span></code>.</p></li>
<li><p><strong>key_material_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.</p></li>
<li><p><strong>key_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the CMK.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cryptographic operations for which you can use the CMK.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value map of tags to assign to the key.</p></li>
<li><p><strong>valid_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.ExternalKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.ExternalKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.GetAliasResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">GetAliasResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">target_key_arn=None</em>, <em class="sig-param">target_key_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlias.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the key alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.target_key_arn">
<code class="sig-name descname">target_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.target_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN pointed to by the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.target_key_id">
<code class="sig-name descname">target_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.target_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Key identifier pointed to by the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetCipherTextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">GetCipherTextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext_blob=None</em>, <em class="sig-param">context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCipherText.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetCipherTextResult.ciphertext_blob">
<code class="sig-name descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded ciphertext</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetCipherTextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">GetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">deletion_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">expiration_model=None</em>, <em class="sig-param">grant_tokens=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_manager=None</em>, <em class="sig-param">key_state=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">valid_to=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">GetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">secrets=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetSecretsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">GetSecretsResult</code><span class="sig-paren">(</span><em class="sig-param">plaintext=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecrets.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretsResult.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Map containing each <code class="docutils literal notranslate"><span class="pre">secret</span></code> <code class="docutils literal notranslate"><span class="pre">name</span></code> as the key with its decrypted plaintext value</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.Grant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">Grant</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">constraints=None</em>, <em class="sig-param">grant_creation_tokens=None</em>, <em class="sig-param">grantee_principal=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operations=None</em>, <em class="sig-param">retire_on_delete=None</em>, <em class="sig-param">retiring_principal=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource-based access control mechanism for a KMS customer master key.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html">Encryption Context</a>.</p></li>
<li><p><strong>grant_creation_tokens</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of grant tokens to be used when creating the grant. See <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a> for more information about grant tokens.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `retire_on_delete` -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>grantee_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for identifying the grant.</p></li>
<li><p><strong>operations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of operations that the grant permits. The permitted values are: <code class="docutils literal notranslate"><span class="pre">Decrypt,</span> <span class="pre">Encrypt,</span> <span class="pre">GenerateDataKey,</span> <span class="pre">GenerateDataKeyWithoutPlaintext,</span> <span class="pre">ReEncryptFrom,</span> <span class="pre">ReEncryptTo,</span> <span class="pre">CreateGrant,</span> <span class="pre">RetireGrant,</span> <span class="pre">DescribeKey</span></code></p></li>
<li><p><strong>retiring_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextSubset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.constraints">
<code class="sig-name descname">constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html">Encryption Context</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextSubset</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_creation_tokens">
<code class="sig-name descname">grant_creation_tokens</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_creation_tokens" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of grant tokens to be used when creating the grant. See <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a> for more information about grant tokens.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retire_on_delete</span></code> -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See <a class="reference external" href="https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html">RetireGrant</a> for more information.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_id">
<code class="sig-name descname">grant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_token">
<code class="sig-name descname">grant_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The grant token for the created grant. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grantee_principal">
<code class="sig-name descname">grantee_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grantee_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for identifying the grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.operations">
<code class="sig-name descname">operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.operations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of operations that the grant permits. The permitted values are: <code class="docutils literal notranslate"><span class="pre">Decrypt,</span> <span class="pre">Encrypt,</span> <span class="pre">GenerateDataKey,</span> <span class="pre">GenerateDataKeyWithoutPlaintext,</span> <span class="pre">ReEncryptFrom,</span> <span class="pre">ReEncryptTo,</span> <span class="pre">CreateGrant,</span> <span class="pre">RetireGrant,</span> <span class="pre">DescribeKey</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.retiring_principal">
<code class="sig-name descname">retiring_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.retiring_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Grant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">constraints=None</em>, <em class="sig-param">grant_creation_tokens=None</em>, <em class="sig-param">grant_id=None</em>, <em class="sig-param">grant_token=None</em>, <em class="sig-param">grantee_principal=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operations=None</em>, <em class="sig-param">retire_on_delete=None</em>, <em class="sig-param">retiring_principal=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Grant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html">Encryption Context</a>.</p>
</p></li>
<li><p><strong>grant_creation_tokens</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of grant tokens to be used when creating the grant. See <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a> for more information about grant tokens.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `retire_on_delete` -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>grant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the grant.</p></li>
<li><p><strong>grant_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The grant token for the created grant. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a>.</p>
</p></li>
<li><p><strong>grantee_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for identifying the grant.</p></li>
<li><p><strong>operations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of operations that the grant permits. The permitted values are: <code class="docutils literal notranslate"><span class="pre">Decrypt,</span> <span class="pre">Encrypt,</span> <span class="pre">GenerateDataKey,</span> <span class="pre">GenerateDataKeyWithoutPlaintext,</span> <span class="pre">ReEncryptFrom,</span> <span class="pre">ReEncryptTo,</span> <span class="pre">CreateGrant,</span> <span class="pre">RetireGrant,</span> <span class="pre">DescribeKey</span></code></p></li>
<li><p><strong>retiring_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>constraints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextEquals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionContextSubset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Grant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Grant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Key">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">Key</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_key_rotation=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a KMS customer master key.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the key as viewed in AWS console.</p></li>
<li><p><strong>enable_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">key rotation</a>
is enabled. Defaults to false.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Defaults to true.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Key.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.deletion_window_in_days">
<code class="sig-name descname">deletion_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the key as viewed in AWS console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.enable_key_rotation">
<code class="sig-name descname">enable_key_rotation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.enable_key_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">key rotation</a>
is enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.is_enabled">
<code class="sig-name descname">is_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the key is enabled. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique identifier for the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.key_usage">
<code class="sig-name descname">key_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Key.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">deletion_window_in_days=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_key_rotation=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_usage=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Key resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the key.</p></li>
<li><p><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the key as viewed in AWS console.</p></li>
<li><p><strong>enable_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies whether <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">key rotation</a>
is enabled. Defaults to false.</p>
</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Defaults to true.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The globally unique identifier for the key.</p></li>
<li><p><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Key.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Key.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.get_alias">
<code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">get_alias</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a KMS key alias.
By using this data source, you can reference key alias
without having to hard code the ARN as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_cipher_text">
<code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">get_cipher_text</code><span class="sig-paren">(</span><em class="sig-param">context=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_cipher_text" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS ciphertext data source allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key. The value returned by this data source
changes every apply. For a stable ciphertext value, see the <cite>``kms.Ciphertext`</cite>
resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/kms_ciphertext.html">https://www.terraform.io/docs/providers/aws/r/kms_ciphertext.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the plaintext be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>context</strong> (<em>dict</em>) – An optional mapping that makes up the encryption context.</p></li>
<li><p><strong>key_id</strong> (<em>str</em>) – Globally unique key ID for the customer master key.</p></li>
<li><p><strong>plaintext</strong> (<em>str</em>) – Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_key">
<code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">get_key</code><span class="sig-paren">(</span><em class="sig-param">grant_tokens=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get detailed information about 
the specified KMS Key with flexible key id input. 
This can be useful to reference key alias 
without having to hard code the ARN as input.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>grant_tokens</strong> (<em>list</em>) – List of grant tokens</p></li>
<li><p><strong>key_id</strong> (<em>str</em>) – Key identifier which can be one of the following format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* Key ID. E.g: `1234abcd-12ab-34cd-56ef-1234567890ab`
* Key ARN. E.g.: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
* Alias name. E.g.: `alias/my-key`
* Alias ARN: E.g.: `arn:aws:kms:us-east-1:111122223333:alias/my-key`
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_secret">
<code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param">secrets=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>!&gt; <strong>WARNING:</strong> This data source was removed in version 2.0.0 of the AWS Provider. You can migrate existing configurations to the <cite>``kms.getSecrets`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/kms_secrets.html">https://www.terraform.io/docs/providers/aws/d/kms_secrets.html</a>&gt;`_ following instructions available in the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/version-2-upgrade.html#data-source-aws_kms_secret">Version 2 Upgrade Guide</a>.</p>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">context</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secret.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secret.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_secrets">
<code class="sig-prename descclassname">pulumi_aws.kms.</code><code class="sig-name descname">get_secrets</code><span class="sig-paren">(</span><em class="sig-param">secrets=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>Decrypt multiple secrets from data encrypted with the AWS KMS service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>secrets</strong> (<em>list</em>) – One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.</p>
</dd>
</dl>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">context</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An optional mapping that makes up the Encryption Context for the secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grantTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An optional list of Grant Tokens for the secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name to export this secret under in the attributes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded payload, as returned from a KMS encrypt operation.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
