---
title: Module transit
title_tag: Module transit | Package pulumi_vault | Python SDK
linktitle: transit
notitle: true
---

<div class="section" id="transit">
<h1>transit<a class="headerlink" href="#transit" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.transit"></span><dl class="class">
<dt id="pulumi_vault.transit.SecretBackendKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.transit.</code><code class="sig-name descname">SecretBackendKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_plaintext_backup=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">convergent_encryption=None</em>, <em class="sig-param">deletion_allowed=None</em>, <em class="sig-param">derived=None</em>, <em class="sig-param">exportable=None</em>, <em class="sig-param">min_decryption_version=None</em>, <em class="sig-param">min_encryption_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Encryption Keyring on a Transit Secret Backend for Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_plaintext_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables taking backup of entire keyring in the plaintext format. Once set, this cannot be disabled.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Refer</span> <span class="n">to</span> <span class="n">Vault</span> <span class="n">API</span> <span class="n">documentation</span> <span class="n">on</span> <span class="n">key</span> <span class="n">backups</span> <span class="k">for</span> <span class="n">more</span> <span class="n">information</span><span class="p">:</span> <span class="p">[</span><span class="n">Backup</span> <span class="n">Key</span><span class="p">](</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">vaultproject</span><span class="o">.</span><span class="n">io</span><span class="o">/</span><span class="n">api</span><span class="o">/</span><span class="n">secret</span><span class="o">/</span><span class="n">transit</span><span class="o">/</span><span class="n">index</span><span class="o">.</span><span class="n">html</span><span class="c1">#backup-key)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>convergent_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to support convergent encryption, where the same plaintext creates the same ciphertext. This requires <code class="docutils literal notranslate"><span class="pre">derived</span></code> to be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>derived</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if key derivation is to be used. If enabled, all encrypt/decrypt requests to this key must provide a context which is used for key derivation.</p></li>
<li><p><strong>exportable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables keys to be exportable. This allows for all valid private keys in the keyring to be exported. Once set, this cannot be disabled.</p></li>
<li><p><strong>min_decryption_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum key version to use for decryption.</p></li>
<li><p><strong>min_encryption_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum key version to use for encryption</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this key within the backend. Must be unique within the backend.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of key to create. The currently-supported types are: <code class="docutils literal notranslate"><span class="pre">aes256-gcm96</span></code> (default), <code class="docutils literal notranslate"><span class="pre">chacha20-poly1305</span></code>, <code class="docutils literal notranslate"><span class="pre">ed25519</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-p256</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa-2048</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-4096</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Refer</span> <span class="n">to</span> <span class="n">the</span> <span class="n">Vault</span> <span class="n">documentation</span> <span class="n">on</span> <span class="n">transit</span> <span class="n">key</span> <span class="n">types</span> <span class="k">for</span> <span class="n">more</span> <span class="n">information</span><span class="p">:</span> <span class="p">[</span><span class="n">Key</span> <span class="n">Types</span><span class="p">](</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">vaultproject</span><span class="o">.</span><span class="n">io</span><span class="o">/</span><span class="n">docs</span><span class="o">/</span><span class="n">secrets</span><span class="o">/</span><span class="n">transit</span><span class="o">/</span><span class="n">index</span><span class="o">.</span><span class="n">html</span><span class="c1">#key-types)</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_backend_key.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_backend_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.allow_plaintext_backup">
<code class="sig-name descname">allow_plaintext_backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.allow_plaintext_backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables taking backup of entire keyring in the plaintext format. Once set, this cannot be disabled.</p>
<ul class="simple">
<li><p>Refer to Vault API documentation on key backups for more information: <a class="reference external" href="https://www.vaultproject.io/api/secret/transit/index.html#backup-key">Backup Key</a></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.convergent_encryption">
<code class="sig-name descname">convergent_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.convergent_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to support convergent encryption, where the same plaintext creates the same ciphertext. This requires <code class="docutils literal notranslate"><span class="pre">derived</span></code> to be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.derived">
<code class="sig-name descname">derived</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.derived" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if key derivation is to be used. If enabled, all encrypt/decrypt requests to this key must provide a context which is used for key derivation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.exportable">
<code class="sig-name descname">exportable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.exportable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables keys to be exportable. This allows for all valid private keys in the keyring to be exported. Once set, this cannot be disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.keys">
<code class="sig-name descname">keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>List of key versions in the keyring. This attribute is zero-indexed and will contain a map of values depending on the <code class="docutils literal notranslate"><span class="pre">type</span></code> of the encryption key.</p>
<ul class="simple">
<li><p>for key types <code class="docutils literal notranslate"><span class="pre">aes256-gcm96</span></code> and <code class="docutils literal notranslate"><span class="pre">chacha20-poly1305</span></code>, each key version will be a map of a single value <code class="docutils literal notranslate"><span class="pre">id</span></code> which is just a hash of the key’s metadata.</p></li>
<li><p>for key types <code class="docutils literal notranslate"><span class="pre">ed25519</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-p256</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa-2048</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-4096</span></code>, each key version will be a map of the following:</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.latest_version">
<code class="sig-name descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest key version available. This value is 1-indexed, so if <code class="docutils literal notranslate"><span class="pre">latest_version</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>, then the key’s information can be referenced from <code class="docutils literal notranslate"><span class="pre">keys</span></code> by selecting element <code class="docutils literal notranslate"><span class="pre">0</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.min_available_version">
<code class="sig-name descname">min_available_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.min_available_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum key version available for use. If keys have been archived by increasing <code class="docutils literal notranslate"><span class="pre">min_decryption_version</span></code>, this attribute will reflect that change.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.min_decryption_version">
<code class="sig-name descname">min_decryption_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.min_decryption_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum key version to use for decryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.min_encryption_version">
<code class="sig-name descname">min_encryption_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.min_encryption_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum key version to use for encryption</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify this key within the backend. Must be unique within the backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.supports_decryption">
<code class="sig-name descname">supports_decryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.supports_decryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the key supports decryption, based on key type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.supports_derivation">
<code class="sig-name descname">supports_derivation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.supports_derivation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the key supports derivation, based on key type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.supports_encryption">
<code class="sig-name descname">supports_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.supports_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the key supports encryption, based on key type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.supports_signing">
<code class="sig-name descname">supports_signing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.supports_signing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the key supports signing, based on key type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretBackendKey.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of key to create. The currently-supported types are: <code class="docutils literal notranslate"><span class="pre">aes256-gcm96</span></code> (default), <code class="docutils literal notranslate"><span class="pre">chacha20-poly1305</span></code>, <code class="docutils literal notranslate"><span class="pre">ed25519</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-p256</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa-2048</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-4096</span></code>.</p>
<ul class="simple">
<li><p>Refer to the Vault documentation on transit key types for more information: <a class="reference external" href="https://www.vaultproject.io/docs/secrets/transit/index.html#key-types">Key Types</a></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.transit.SecretBackendKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_plaintext_backup=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">convergent_encryption=None</em>, <em class="sig-param">deletion_allowed=None</em>, <em class="sig-param">derived=None</em>, <em class="sig-param">exportable=None</em>, <em class="sig-param">keys=None</em>, <em class="sig-param">latest_version=None</em>, <em class="sig-param">min_available_version=None</em>, <em class="sig-param">min_decryption_version=None</em>, <em class="sig-param">min_encryption_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">supports_decryption=None</em>, <em class="sig-param">supports_derivation=None</em>, <em class="sig-param">supports_encryption=None</em>, <em class="sig-param">supports_signing=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_plaintext_backup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables taking backup of entire keyring in the plaintext format. Once set, this cannot be disabled.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Refer</span> <span class="n">to</span> <span class="n">Vault</span> <span class="n">API</span> <span class="n">documentation</span> <span class="n">on</span> <span class="n">key</span> <span class="n">backups</span> <span class="k">for</span> <span class="n">more</span> <span class="n">information</span><span class="p">:</span> <span class="p">[</span><span class="n">Backup</span> <span class="n">Key</span><span class="p">](</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">vaultproject</span><span class="o">.</span><span class="n">io</span><span class="o">/</span><span class="n">api</span><span class="o">/</span><span class="n">secret</span><span class="o">/</span><span class="n">transit</span><span class="o">/</span><span class="n">index</span><span class="o">.</span><span class="n">html</span><span class="c1">#backup-key)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>convergent_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to support convergent encryption, where the same plaintext creates the same ciphertext. This requires <code class="docutils literal notranslate"><span class="pre">derived</span></code> to be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>derived</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if key derivation is to be used. If enabled, all encrypt/decrypt requests to this key must provide a context which is used for key derivation.</p></li>
<li><p><strong>exportable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables keys to be exportable. This allows for all valid private keys in the keyring to be exported. Once set, this cannot be disabled.</p></li>
<li><p><strong>keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of key versions in the keyring. This attribute is zero-indexed and will contain a map of values depending on the <code class="docutils literal notranslate"><span class="pre">type</span></code> of the encryption key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* for key types `aes256-gcm96` and `chacha20-poly1305`, each key version will be a map of a single value `id` which is just a hash of the key&#39;s metadata.
* for key types `ed25519`, `ecdsa-p256`, `rsa-2048` and `rsa-4096`, each key version will be a map of the following:
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>latest_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Latest key version available. This value is 1-indexed, so if <code class="docutils literal notranslate"><span class="pre">latest_version</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>, then the key’s information can be referenced from <code class="docutils literal notranslate"><span class="pre">keys</span></code> by selecting element <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><strong>min_available_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum key version available for use. If keys have been archived by increasing <code class="docutils literal notranslate"><span class="pre">min_decryption_version</span></code>, this attribute will reflect that change.</p></li>
<li><p><strong>min_decryption_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum key version to use for decryption.</p></li>
<li><p><strong>min_encryption_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum key version to use for encryption</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this key within the backend. Must be unique within the backend.</p></li>
<li><p><strong>supports_decryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the key supports decryption, based on key type.</p></li>
<li><p><strong>supports_derivation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the key supports derivation, based on key type.</p></li>
<li><p><strong>supports_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the key supports encryption, based on key type.</p></li>
<li><p><strong>supports_signing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the key supports signing, based on key type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of key to create. The currently-supported types are: <code class="docutils literal notranslate"><span class="pre">aes256-gcm96</span></code> (default), <code class="docutils literal notranslate"><span class="pre">chacha20-poly1305</span></code>, <code class="docutils literal notranslate"><span class="pre">ed25519</span></code>, <code class="docutils literal notranslate"><span class="pre">ecdsa-p256</span></code>, <code class="docutils literal notranslate"><span class="pre">rsa-2048</span></code> and <code class="docutils literal notranslate"><span class="pre">rsa-4096</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Refer</span> <span class="n">to</span> <span class="n">the</span> <span class="n">Vault</span> <span class="n">documentation</span> <span class="n">on</span> <span class="n">transit</span> <span class="n">key</span> <span class="n">types</span> <span class="k">for</span> <span class="n">more</span> <span class="n">information</span><span class="p">:</span> <span class="p">[</span><span class="n">Key</span> <span class="n">Types</span><span class="p">](</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">vaultproject</span><span class="o">.</span><span class="n">io</span><span class="o">/</span><span class="n">docs</span><span class="o">/</span><span class="n">secrets</span><span class="o">/</span><span class="n">transit</span><span class="o">/</span><span class="n">index</span><span class="o">.</span><span class="n">html</span><span class="c1">#key-types)</span>
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_backend_key.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_backend_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.transit.SecretBackendKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.transit.SecretBackendKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretBackendKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.transit.SecretCacheConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.transit.</code><code class="sig-name descname">SecretCacheConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure the cache for the Transit Secret Backend in Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of cache entries. 0 means unlimited.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_cache_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_cache_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.transit.SecretCacheConfig.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.transit.SecretCacheConfig.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of cache entries. 0 means unlimited.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.transit.SecretCacheConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretCacheConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the transit secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of cache entries. 0 means unlimited.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_cache_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/transit_secret_cache_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.transit.SecretCacheConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.transit.SecretCacheConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.transit.SecretCacheConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
