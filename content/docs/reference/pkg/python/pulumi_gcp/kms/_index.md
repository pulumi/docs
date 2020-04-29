---
title: Module kms
title_tag: Module kms | Package pulumi_gcp | Python SDK
linktitle: kms
notitle: true
---

<div class="section" id="kms">
<h1>kms<a class="headerlink" href="#kms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.kms"></span><dl class="class">
<dt id="pulumi_gcp.kms.AwaitableGetKMSCryptoKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">AwaitableGetKMSCryptoKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">key_ring=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">version_templates=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.AwaitableGetKMSCryptoKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.AwaitableGetKMSCryptoKeyVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">AwaitableGetKMSCryptoKeyVersionResult</code><span class="sig-paren">(</span><em class="sig-param">algorithm=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">protection_level=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.AwaitableGetKMSCryptoKeyVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.AwaitableGetKMSKeyRingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">AwaitableGetKMSKeyRingResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.AwaitableGetKMSKeyRingResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.AwaitableGetKMSSecretCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">AwaitableGetKMSSecretCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.AwaitableGetKMSSecretCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.AwaitableGetKMSSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">AwaitableGetKMSSecretResult</code><span class="sig-paren">(</span><em class="sig-param">additional_authenticated_data=None</em>, <em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.AwaitableGetKMSSecretResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.CryptoKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">CryptoKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_ring=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">version_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">CryptoKey</span></code> represents a logical key that can be used for cryptographic operations.</p>
<blockquote>
<div><p><strong>Note:</strong> CryptoKeys cannot be deleted from Google Cloud Platform.
Destroying a provider-managed CryptoKey will remove it from state
and delete all CryptoKeyVersions, rendering the key unusable, but <em>will
not delete the resource on the server.</em> When the provider destroys these keys,
any data previously encrypted with these keys will be irrecoverable.
For this reason, it is strongly recommended that you add lifecycle hooks
to the resource to prevent accidental destruction.</p>
</div></blockquote>
<p>To get more information about CryptoKey, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/creating-keys#create_a_key">Creating a key</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_ring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The KeyRing that this key belongs to.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Labels with user-defined metadata to apply to this resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the CryptoKey.</p></li>
<li><p><strong>purpose</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The immutable purpose of this CryptoKey. See the
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose">purpose reference</a>
for possible inputs.</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
The first rotation will take place after the specified period. The rotation period has
the format of a decimal number with up to 9 fractional digits, followed by the
letter <code class="docutils literal notranslate"><span class="pre">s</span></code> (seconds). It must be greater than a day (ie, 86400).</p></li>
<li><p><strong>version_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A template describing settings for new crypto key versions.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>version_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The algorithm to use when creating a version based on this template.
See the <a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm">algorithm reference</a> for possible inputs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectionLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protection level to use when creating a version based on this template.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.key_ring">
<code class="sig-name descname">key_ring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.key_ring" title="Permalink to this definition">¶</a></dt>
<dd><p>The KeyRing that this key belongs to.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Labels with user-defined metadata to apply to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the CryptoKey.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.purpose">
<code class="sig-name descname">purpose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.purpose" title="Permalink to this definition">¶</a></dt>
<dd><p>The immutable purpose of this CryptoKey. See the
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose">purpose reference</a>
for possible inputs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.rotation_period">
<code class="sig-name descname">rotation_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.rotation_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
The first rotation will take place after the specified period. The rotation period has
the format of a decimal number with up to 9 fractional digits, followed by the
letter <code class="docutils literal notranslate"><span class="pre">s</span></code> (seconds). It must be greater than a day (ie, 86400).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKey.version_template">
<code class="sig-name descname">version_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.version_template" title="Permalink to this definition">¶</a></dt>
<dd><p>A template describing settings for new crypto key versions.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The algorithm to use when creating a version based on this template.
See the <a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm">algorithm reference</a> for possible inputs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectionLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protection level to use when creating a version based on this template.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_ring=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">version_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CryptoKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_ring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The KeyRing that this key belongs to.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Labels with user-defined metadata to apply to this resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the CryptoKey.</p></li>
<li><p><strong>purpose</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The immutable purpose of this CryptoKey. See the
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose">purpose reference</a>
for possible inputs.</p>
</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
The first rotation will take place after the specified period. The rotation period has
the format of a decimal number with up to 9 fractional digits, followed by the
letter <code class="docutils literal notranslate"><span class="pre">s</span></code> (seconds). It must be greater than a day (ie, 86400).</p></li>
<li><p><strong>version_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A template describing settings for new crypto key versions.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>version_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The algorithm to use when creating a version based on this template.
See the <a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm">algorithm reference</a> for possible inputs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectionLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protection level to use when creating a version based on this template.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">CryptoKeyIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS crypto key. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the crypto key and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the crypto key are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the crypto key are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.crypto_key_id">
<code class="sig-name descname">crypto_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.crypto_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CryptoKeyIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">CryptoKeyIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS crypto key. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the crypto key and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the crypto key are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the crypto key are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.crypto_key_id">
<code class="sig-name descname">crypto_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.crypto_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CryptoKeyIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">CryptoKeyIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS crypto key. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the crypto key and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the crypto key are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the crypto key are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<p>With IAM Conditions:</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.crypto_key_id">
<code class="sig-name descname">crypto_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.crypto_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">crypto_key_id=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CryptoKeyIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>crypto_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The crypto key ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}/{crypto_key_name}</span></code>. In the second form,
the provider’s project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.CryptoKeyIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.CryptoKeyIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">GetKMSCryptoKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">key_ring=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">version_templates=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKMSCryptoKey.</p>
<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyResult.purpose">
<code class="sig-name descname">purpose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyResult.purpose" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the cryptographic capabilities of the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyResult.rotation_period">
<code class="sig-name descname">rotation_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyResult.rotation_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Every time this period passes, generate a new CryptoKeyVersion and set it as
the primary. The first rotation will take place after the specified period. The rotation period has the format
of a decimal number with up to 9 fractional digits, followed by the letter s (seconds).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The self link of the created CryptoKey. Its format is <code class="docutils literal notranslate"><span class="pre">projects/{projectId}/locations/{location}/keyRings/{keyRingName}/cryptoKeys/{cryptoKeyName}</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">GetKMSCryptoKeyVersionResult</code><span class="sig-paren">(</span><em class="sig-param">algorithm=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">protection_level=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKMSCryptoKeyVersion.</p>
<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.protection_level">
<code class="sig-name descname">protection_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.protection_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. See the <a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel">protection_level reference</a> for possible outputs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>If the enclosing CryptoKey has purpose <code class="docutils literal notranslate"><span class="pre">ASYMMETRIC_SIGN</span></code> or <code class="docutils literal notranslate"><span class="pre">ASYMMETRIC_DECRYPT</span></code>, this block contains details about the public key associated to this CryptoKeyVersion. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSCryptoKeyVersionResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the CryptoKeyVersion. See the <a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState">state reference</a> for possible outputs.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.GetKMSKeyRingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">GetKMSKeyRingResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.GetKMSKeyRingResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKMSKeyRing.</p>
<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSKeyRingResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSKeyRingResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSKeyRingResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSKeyRingResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The self link of the created KeyRing. Its format is <code class="docutils literal notranslate"><span class="pre">projects/{projectId}/locations/{location}/keyRings/{keyRingName}</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.GetKMSSecretCiphertextResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">GetKMSSecretCiphertextResult</code><span class="sig-paren">(</span><em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretCiphertextResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKMSSecretCiphertext.</p>
<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSSecretCiphertextResult.ciphertext">
<code class="sig-name descname">ciphertext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretCiphertextResult.ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the result of encrypting the provided plaintext, encoded in base64.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSSecretCiphertextResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretCiphertextResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.GetKMSSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">GetKMSSecretResult</code><span class="sig-paren">(</span><em class="sig-param">additional_authenticated_data=None</em>, <em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKMSSecret.</p>
<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSSecretResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.GetKMSSecretResult.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.GetKMSSecretResult.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the result of decrypting the provided ciphertext.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.kms.KeyRing">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">KeyRing</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRing" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">KeyRing</span></code> is a toplevel logical grouping of <code class="docutils literal notranslate"><span class="pre">CryptoKeys</span></code>.</p>
<blockquote>
<div><p><strong>Note:</strong> KeyRings cannot be deleted from Google Cloud Platform.
Destroying a provider-managed KeyRing will remove it from state but
<em>will not delete the resource on the server.</em></p>
</div></blockquote>
<p>To get more information about KeyRing, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/creating-keys#create_a_key_ring">Creating a key ring</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location for the KeyRing.
A full list of valid locations can be found by running <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">kms</span> <span class="pre">locations</span> <span class="pre">list</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the KeyRing.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRing.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location for the KeyRing.
A full list of valid locations can be found by running <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">kms</span> <span class="pre">locations</span> <span class="pre">list</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRing.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the KeyRing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRing.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRing.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyRing resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location for the KeyRing.
A full list of valid locations can be found by running <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">kms</span> <span class="pre">locations</span> <span class="pre">list</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the KeyRing.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRing.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRing.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">KeyRingIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the key ring’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.key_ring_id">
<code class="sig-name descname">key_ring_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.key_ring_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyRingIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the key ring’s IAM policy.</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">KeyRingIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the key ring’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.key_ring_id">
<code class="sig-name descname">key_ring_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.key_ring_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyRingIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the key ring’s IAM policy.</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Textual representation of an expression in Common Expression Language syntax.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title for the expression, i.e. a short string describing its purpose.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">KeyRingIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">kms.KeyRingIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the key ring’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.key_ring_id">
<code class="sig-name descname">key_ring_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.key_ring_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">key_ring_id=None</em>, <em class="sig-param">policy_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyRingIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the key ring’s IAM policy.</p></li>
<li><p><strong>key_ring_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ring ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{key_ring_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{key_ring_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.KeyRingIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.KeyRingIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.Registry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">Registry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">event_notification_configs=None</em>, <em class="sig-param">http_config=None</em>, <em class="sig-param">log_level=None</em>, <em class="sig-param">mqtt_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">state_notification_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated: gcp.Registry has been deprecated in favour of gcp.Registry</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>event_notification_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subfolderMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>mqtt_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>state_notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_gcp.kms.Registry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">event_notification_configs=None</em>, <em class="sig-param">http_config=None</em>, <em class="sig-param">log_level=None</em>, <em class="sig-param">mqtt_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">state_notification_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.Registry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Registry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>event_notification_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subfolderMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>mqtt_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>state_notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.Registry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.Registry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.Registry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.Registry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.SecretCiphertext">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">SecretCiphertext</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_authenticated_data=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypts secret data with Google Cloud KMS and provides access to the ciphertext.</p>
<blockquote>
<div><p><strong>NOTE</strong>: Using this resource will allow you to conceal secret data within your
resource definitions, but it does not take care of protecting that data in the
logging output, plan output, or state output.  Please take care to secure your secret
data outside of resource definitions.</p>
</div></blockquote>
<p>To get more information about SecretCiphertext, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/kms/docs/encrypt-decrypt">Encrypting and decrypting data with a symmetric key</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_authenticated_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The additional authenticated data used for integrity checks during encryption and decryption.</p></li>
<li><p><strong>crypto_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the CryptoKey that will be used to encrypt the provided plaintext.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'</span></code></p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.kms.SecretCiphertext.additional_authenticated_data">
<code class="sig-name descname">additional_authenticated_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.additional_authenticated_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The additional authenticated data used for integrity checks during encryption and decryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.SecretCiphertext.ciphertext">
<code class="sig-name descname">ciphertext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the result of encrypting the provided plaintext, encoded in base64.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.SecretCiphertext.crypto_key">
<code class="sig-name descname">crypto_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.crypto_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the CryptoKey that will be used to encrypt the provided plaintext.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.kms.SecretCiphertext.plaintext">
<code class="sig-name descname">plaintext</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.plaintext" title="Permalink to this definition">¶</a></dt>
<dd><p>The plaintext to be encrypted.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.SecretCiphertext.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_authenticated_data=None</em>, <em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">plaintext=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretCiphertext resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_authenticated_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The additional authenticated data used for integrity checks during encryption and decryption.</p></li>
<li><p><strong>ciphertext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the result of encrypting the provided plaintext, encoded in base64.</p></li>
<li><p><strong>crypto_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the CryptoKey that will be used to encrypt the provided plaintext.
Format: <code class="docutils literal notranslate"><span class="pre">'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}'</span></code></p></li>
<li><p><strong>plaintext</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext to be encrypted.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.kms.SecretCiphertext.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.SecretCiphertext.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.SecretCiphertext.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.kms.get_kms_crypto_key">
<code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">get_kms_crypto_key</code><span class="sig-paren">(</span><em class="sig-param">key_ring=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.get_kms_crypto_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to a Google Cloud Platform KMS CryptoKey. For more information see
<a class="reference external" href="https://cloud.google.com/kms/docs/object-hierarchy#key">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys">API</a>.</p>
<p>A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
Google Cloud KMS KeyRing.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_ring</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">self_link</span></code> of the Google Cloud Platform KeyRing to which the key belongs.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The CryptoKey’s name.
A CryptoKey’s name belonging to the specified Google Cloud Platform KeyRing and match the regular expression <code class="docutils literal notranslate"><span class="pre">[a-zA-Z0-9_-]{1,63}</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.kms.get_kms_crypto_key_version">
<code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">get_kms_crypto_key_version</code><span class="sig-paren">(</span><em class="sig-param">crypto_key=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.get_kms_crypto_key_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to a Google Cloud Platform KMS CryptoKeyVersion. For more information see
<a class="reference external" href="https://cloud.google.com/kms/docs/object-hierarchy#key_version">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions">API</a>.</p>
<p>A CryptoKeyVersion represents an individual cryptographic key, and the associated key material.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>crypto_key</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">self_link</span></code> of the Google Cloud Platform CryptoKey to which the key version belongs.</p></li>
<li><p><strong>version</strong> (<em>float</em>) – The version number for this CryptoKeyVersion. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.kms.get_kms_key_ring">
<code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">get_kms_key_ring</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.get_kms_key_ring" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to Google Cloud Platform KMS KeyRing. For more information see
<a class="reference external" href="https://cloud.google.com/kms/docs/object-hierarchy#key_ring">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings">API</a>.</p>
<p>A KeyRing is a grouping of CryptoKeys for organizational purposes. A KeyRing belongs to a Google Cloud Platform Project
and resides in a specific location.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – The Google Cloud Platform location for the KeyRing.
A full list of valid locations can be found by running <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">kms</span> <span class="pre">locations</span> <span class="pre">list</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The KeyRing’s name.
A KeyRing name must exist within the provided location and match the regular expression <code class="docutils literal notranslate"><span class="pre">[a-zA-Z0-9_-]{1,63}</span></code></p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.kms.get_kms_secret">
<code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">get_kms_secret</code><span class="sig-paren">(</span><em class="sig-param">additional_authenticated_data=None</em>, <em class="sig-param">ciphertext=None</em>, <em class="sig-param">crypto_key=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.get_kms_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source allows you to use data encrypted with Google Cloud KMS
within your resource definitions.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/kms/docs/encrypt-decrypt">the official documentation</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong>: Using this data provider will allow you to conceal secret data within your
resource definitions, but it does not take care of protecting that data in the
logging output, plan output, or state output.  Please take care to secure your secret
data outside of resource definitions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>additional_authenticated_data</strong> (<em>str</em>) – The <a class="reference external" href="https://cloud.google.com/kms/docs/additional-authenticated-data">additional authenticated data</a> used for integrity checks during encryption and decryption.</p></li>
<li><p><strong>ciphertext</strong> (<em>str</em>) – The ciphertext to be decrypted, encoded in base64</p></li>
<li><p><strong>crypto_key</strong> (<em>str</em>) – The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
<code class="docutils literal notranslate"><span class="pre">{projectId}/{location}/{keyRingName}/{cryptoKeyName}</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.kms.get_kms_secret_ciphertext">
<code class="sig-prename descclassname">pulumi_gcp.kms.</code><code class="sig-name descname">get_kms_secret_ciphertext</code><span class="sig-paren">(</span><em class="sig-param">crypto_key=None</em>, <em class="sig-param">plaintext=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.kms.get_kms_secret_ciphertext" title="Permalink to this definition">¶</a></dt>
<dd><p>!&gt; <strong>Warning:</strong> This data source is deprecated. Use the <code class="docutils literal notranslate"><span class="pre">kms.SecretCiphertext</span></code> <strong>resource</strong> instead.</p>
<p>This data source allows you to encrypt data with Google Cloud KMS and use the
ciphertext within your resource definitions.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/kms/docs/encrypt-decrypt">the official documentation</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong>: Using this data source will allow you to conceal secret data within your
resource definitions, but it does not take care of protecting that data in the
logging output, plan output, or state output.  Please take care to secure your secret
data outside of resource definitions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>crypto_key</strong> (<em>str</em>) – The id of the CryptoKey that will be used to
encrypt the provided plaintext. This is represented by the format
<code class="docutils literal notranslate"><span class="pre">{projectId}/{location}/{keyRingName}/{cryptoKeyName}</span></code>.</p></li>
<li><p><strong>plaintext</strong> (<em>str</em>) – The plaintext to be encrypted</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
