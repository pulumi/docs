---
---

<div class="section" id="kms">
<h1>kms<a class="headerlink" href="#kms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.kms"></span><dl class="class">
<dt id="pulumi_aws.kms.Alias">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">Alias</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>target_key_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Alias resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates an unique alias beginning with the specified prefix.
The name must start with the word “alias” followed by a forward slash (alias/).  Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>target_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the key for which the alias is for, can be either an ARN or key_id.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_alias.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the alias. The name must start with the word “alias” followed by a forward slash (alias/)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an unique alias beginning with the specified prefix.
The name must start with the word “alias” followed by a forward slash (alias/).  Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.target_key_arn">
<code class="descname">target_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.target_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the target key identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Alias.target_key_id">
<code class="descname">target_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Alias.target_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier for the key for which the alias is for, can be either an ARN or key_id.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Alias.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Alias.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Ciphertext">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">Ciphertext</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>context=None</em>, <em>key_id=None</em>, <em>plaintext=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS ciphertext resource allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key. The value returned by this resource
is stable across every apply. For a changing ciphertext value each apply, see
the <cite>``aws_kms_ciphertext`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/kms_ciphertext.html">https://www.terraform.io/docs/providers/aws/d/kms_ciphertext.html</a>&gt;`_.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the plaintext be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An optional mapping that makes up the encryption context.</li>
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Globally unique key ID for the customer master key.</li>
<li><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_ciphertext.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.ciphertext_blob">
<code class="descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded ciphertext</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.context">
<code class="descname">context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.context" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional mapping that makes up the encryption context.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Globally unique key ID for the customer master key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Ciphertext.plaintext">
<code class="descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Ciphertext.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Ciphertext.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Ciphertext.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.ExternalKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">ExternalKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>deletion_window_in_days=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>key_material_base64=None</em>, <em>policy=None</em>, <em>tags=None</em>, <em>valid_to=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a KMS Customer Master Key that uses external key material. To instead manage a KMS Customer Master Key where AWS automatically generates and potentially rotates key material, see the <cite>``aws_kms_key`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/kms_key.html">https://www.terraform.io/docs/providers/aws/r/kms_key.html</a>&gt;`_.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the key material will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted after destruction of the resource. Must be between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> days. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the key.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Keys pending import can only be <code class="docutils literal notranslate"><span class="pre">false</span></code>. Imported keys default to <code class="docutils literal notranslate"><span class="pre">true</span></code> unless expired.</li>
<li><strong>key_material_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value map of tags to assign to the key.</li>
<li><strong>valid_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_external_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.deletion_window_in_days">
<code class="descname">deletion_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted after destruction of the resource. Must be between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> days. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the key is enabled. Keys pending import can only be <code class="docutils literal notranslate"><span class="pre">false</span></code>. Imported keys default to <code class="docutils literal notranslate"><span class="pre">true</span></code> unless expired.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.expiration_model">
<code class="descname">expiration_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.expiration_model" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the key material expires. Empty when pending key material import, otherwise <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_EXPIRES</span></code> or <code class="docutils literal notranslate"><span class="pre">KEY_MATERIAL_DOES_NOT_EXPIRE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_material_base64">
<code class="descname">key_material_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_material_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_state">
<code class="descname">key_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.key_usage">
<code class="descname">key_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>The cryptographic operations for which you can use the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of tags to assign to the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.ExternalKey.valid_to">
<code class="descname">valid_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.valid_to" title="Permalink to this definition">¶</a></dt>
<dd><p>Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 time string</a> (<code class="docutils literal notranslate"><span class="pre">YYYY-MM-DDTHH:MM:SSZ</span></code>)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.ExternalKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.ExternalKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.ExternalKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.GetAliasResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">GetAliasResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>target_key_arn=None</em>, <em>target_key_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlias.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name(ARN) of the key alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.target_key_arn">
<code class="descname">target_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.target_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN pointed to by the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.target_key_id">
<code class="descname">target_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.target_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Key identifier pointed to by the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetAliasResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetAliasResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetCipherTextResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">GetCipherTextResult</code><span class="sig-paren">(</span><em>ciphertext_blob=None</em>, <em>context=None</em>, <em>key_id=None</em>, <em>plaintext=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCipherText.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetCipherTextResult.ciphertext_blob">
<code class="descname">ciphertext_blob</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult.ciphertext_blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded ciphertext</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetCipherTextResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetCipherTextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">GetKeyResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>aws_account_id=None</em>, <em>creation_date=None</em>, <em>deletion_date=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>expiration_model=None</em>, <em>grant_tokens=None</em>, <em>key_id=None</em>, <em>key_manager=None</em>, <em>key_state=None</em>, <em>key_usage=None</em>, <em>origin=None</em>, <em>valid_to=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetSecretResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">GetSecretResult</code><span class="sig-paren">(</span><em>secrets=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.GetSecretsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">GetSecretsResult</code><span class="sig-paren">(</span><em>plaintext=None</em>, <em>secrets=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecrets.</p>
<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretsResult.plaintext">
<code class="descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Map containing each <code class="docutils literal notranslate"><span class="pre">secret</span></code> <code class="docutils literal notranslate"><span class="pre">name</span></code> as the key with its decrypted plaintext value</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.GetSecretsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.GetSecretsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kms.Grant">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">Grant</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>constraints=None</em>, <em>grant_creation_tokens=None</em>, <em>grantee_principal=None</em>, <em>key_id=None</em>, <em>name=None</em>, <em>operations=None</em>, <em>retire_on_delete=None</em>, <em>retiring_principal=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource-based access control mechanism for a KMS customer master key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html">Encryption Context</a>.</li>
<li><strong>grant_creation_tokens</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of grant tokens to be used when creating the grant. See <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a> for more information about grant tokens.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for identifying the grant.</li>
<li><strong>operations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of operations that the grant permits. The permitted values are: <code class="docutils literal notranslate"><span class="pre">Decrypt,</span> <span class="pre">Encrypt,</span> <span class="pre">GenerateDataKey,</span> <span class="pre">GenerateDataKeyWithoutPlaintext,</span> <span class="pre">ReEncryptFrom,</span> <span class="pre">ReEncryptTo,</span> <span class="pre">CreateGrant,</span> <span class="pre">RetireGrant,</span> <span class="pre">DescribeKey</span></code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_grant.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.constraints">
<code class="descname">constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html">Encryption Context</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_creation_tokens">
<code class="descname">grant_creation_tokens</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_creation_tokens" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of grant tokens to be used when creating the grant. See <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a> for more information about grant tokens.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">retire_on_delete</span></code> -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
See <a class="reference external" href="https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html">RetireGrant</a> for more information.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_id">
<code class="descname">grant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.grant_token">
<code class="descname">grant_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.grant_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The grant token for the created grant. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token">Grant Tokens</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for identifying the grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Grant.operations">
<code class="descname">operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Grant.operations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of operations that the grant permits. The permitted values are: <code class="docutils literal notranslate"><span class="pre">Decrypt,</span> <span class="pre">Encrypt,</span> <span class="pre">GenerateDataKey,</span> <span class="pre">GenerateDataKeyWithoutPlaintext,</span> <span class="pre">ReEncryptFrom,</span> <span class="pre">ReEncryptTo,</span> <span class="pre">CreateGrant,</span> <span class="pre">RetireGrant,</span> <span class="pre">DescribeKey</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Grant.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Grant.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Key">
<em class="property">class </em><code class="descclassname">pulumi_aws.kms.</code><code class="descname">Key</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>deletion_window_in_days=None</em>, <em>description=None</em>, <em>enable_key_rotation=None</em>, <em>is_enabled=None</em>, <em>key_usage=None</em>, <em>policy=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a KMS customer master key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>deletion_window_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the key as viewed in AWS console.</li>
<li><strong>enable_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">key rotation</a>
is enabled. Defaults to false.</li>
<li><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the key is enabled. Defaults to true.</li>
<li><strong>key_usage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kms_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kms.Key.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.deletion_window_in_days">
<code class="descname">deletion_window_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.deletion_window_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the key as viewed in AWS console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.enable_key_rotation">
<code class="descname">enable_key_rotation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.enable_key_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether <a class="reference external" href="http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html">key rotation</a>
is enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.is_enabled">
<code class="descname">is_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the key is enabled. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The globally unique identifier for the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.key_usage">
<code class="descname">key_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.key_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kms.Key.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kms.Key.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kms.Key.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kms.Key.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.kms.get_alias">
<code class="descclassname">pulumi_aws.kms.</code><code class="descname">get_alias</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a KMS key alias.
By using this data source, you can reference key alias
without having to hard code the ARN as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_alias.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_cipher_text">
<code class="descclassname">pulumi_aws.kms.</code><code class="descname">get_cipher_text</code><span class="sig-paren">(</span><em>context=None</em>, <em>key_id=None</em>, <em>plaintext=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_cipher_text" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS ciphertext data source allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key. The value returned by this data source
changes every apply. For a stable ciphertext value, see the <cite>``aws_kms_ciphertext`</cite>
resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/kms_ciphertext.html">https://www.terraform.io/docs/providers/aws/r/kms_ciphertext.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the plaintext be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_ciphertext.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_ciphertext.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_key">
<code class="descclassname">pulumi_aws.kms.</code><code class="descname">get_key</code><span class="sig-paren">(</span><em>grant_tokens=None</em>, <em>key_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get detailed information about 
the specified KMS Key with flexible key id input. 
This can be useful to reference key alias 
without having to hard code the ARN as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_key.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_secret">
<code class="descclassname">pulumi_aws.kms.</code><code class="descname">get_secret</code><span class="sig-paren">(</span><em>secrets=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secret.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secret.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kms.get_secrets">
<code class="descclassname">pulumi_aws.kms.</code><code class="descname">get_secrets</code><span class="sig-paren">(</span><em>secrets=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kms.get_secrets" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
