---
title: Module pki_secret
title_tag: Module pki_secret | Package pulumi_vault | Python SDK
linktitle: pki_secret
notitle: true
---

<div class="section" id="pki-secret">
<h1>pki_secret<a class="headerlink" href="#pki-secret" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.pki_secret"></span><dl class="py class">
<dt id="pulumi_vault.pki_secret.SecretBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an PKI Secret Backend for Vault. PKI secret backends can then issue certificates, once a role has been added to
the backend.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested for credentials issued by this backend.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackend.default_lease_ttl_seconds">
<code class="sig-name descname">default_lease_ttl_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL for credentials issued by this backend.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackend.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly description for this backend.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackend.max_lease_ttl_seconds">
<code class="sig-name descname">max_lease_ttl_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL that can be requested for credentials issued by this backend.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackend.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique path this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested for credentials issued by this backend.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendCert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_seconds_remaining</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendCert resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of certificate to create</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>min_seconds_remaining</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role to create the certificate against</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_cert.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.alt_names">
<code class="sig-name descname">alt_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.alt_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.ca_chain">
<code class="sig-name descname">ca_chain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.ca_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA chain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.common_name">
<code class="sig-name descname">common_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>CN of certificate to create</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.exclude_cn_from_sans">
<code class="sig-name descname">exclude_cn_from_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.exclude_cn_from_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to exclude CN from SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.expiration">
<code class="sig-name descname">expiration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date of the certificate in unix epoch format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of data</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.ip_sans">
<code class="sig-name descname">ip_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative IPs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.issuing_ca">
<code class="sig-name descname">issuing_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.issuing_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuing CA</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.min_seconds_remaining">
<code class="sig-name descname">min_seconds_remaining</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.min_seconds_remaining" title="Permalink to this definition">¶</a></dt>
<dd><p>Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role to create the certificate against</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.other_sans">
<code class="sig-name descname">other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of other SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.private_key">
<code class="sig-name descname">private_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.private_key_format">
<code class="sig-name descname">private_key_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.private_key_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.private_key_type">
<code class="sig-name descname">private_key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.private_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.serial_number">
<code class="sig-name descname">serial_number</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.serial_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial number</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_chain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_seconds_remaining</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>ca_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA chain</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of certificate to create</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The expiration date of the certificate in unix epoch format</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>issuing_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The issuing CA</p></li>
<li><p><strong>min_seconds_remaining</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role to create the certificate against</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>private_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key type</p></li>
<li><p><strong>serial_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serial number</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_cert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendConfigCa</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pem_bundle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendConfigCa resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>pem_bundle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key and certificate PEM bundle</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_ca.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_ca.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa.pem_bundle">
<code class="sig-name descname">pem_bundle</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa.pem_bundle" title="Permalink to this definition">¶</a></dt>
<dd><p>The key and certificate PEM bundle</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pem_bundle</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendConfigCa resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>pem_bundle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key and certificate PEM bundle</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_ca.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_ca.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendConfigCa.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigCa.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendConfigUrls</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">crl_distribution_points</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocsp_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting the issuing certificate endpoints, CRL distribution points, and OCSP server endpoints that will be encoded into issued certificates.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>crl_distribution_points</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the CRL Distribution Points field.</p></li>
<li><p><strong>issuing_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the Issuing Certificate field.</p></li>
<li><p><strong>ocsp_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the OCSP Servers field.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_urls.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_urls.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.crl_distribution_points">
<code class="sig-name descname">crl_distribution_points</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.crl_distribution_points" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URL values for the CRL Distribution Points field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.issuing_certificates">
<code class="sig-name descname">issuing_certificates</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.issuing_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URL values for the Issuing Certificate field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.ocsp_servers">
<code class="sig-name descname">ocsp_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.ocsp_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URL values for the OCSP Servers field.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">crl_distribution_points</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocsp_servers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendConfigUrls resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>crl_distribution_points</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the CRL Distribution Points field.</p></li>
<li><p><strong>issuing_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the Issuing Certificate field.</p></li>
<li><p><strong>ocsp_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the URL values for the OCSP Servers field.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_urls.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_config_urls.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendConfigUrls.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendConfigUrls.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendCrlConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting the duration for which the generated CRL should be marked valid. If the CRL is disabled, it will return a signed but zero-length CRL for any request. If enabled, it will re-build the CRL.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>disable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables or enables CRL building.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time until expiration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_crl_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_crl_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.disable">
<code class="sig-name descname">disable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.disable" title="Permalink to this definition">¶</a></dt>
<dd><p>Disables or enables CRL building.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.expiry">
<code class="sig-name descname">expiry</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the time until expiration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendCrlConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>disable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables or enables CRL building.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time until expiration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_crl_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_crl_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendCrlConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendCrlConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendIntermediateCertRequest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendIntermediateCertRequest resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits to use</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired key type</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of intermediate to create. Must be either “exported” or “internal”</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_cert_request.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_cert_request.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.alt_names">
<code class="sig-name descname">alt_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.alt_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.common_name">
<code class="sig-name descname">common_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>CN of intermediate to create</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.country">
<code class="sig-name descname">country</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.csr">
<code class="sig-name descname">csr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CSR</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.exclude_cn_from_sans">
<code class="sig-name descname">exclude_cn_from_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.exclude_cn_from_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to exclude CN from SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of data</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.ip_sans">
<code class="sig-name descname">ip_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative IPs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.key_bits">
<code class="sig-name descname">key_bits</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.key_bits" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bits to use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.key_type">
<code class="sig-name descname">key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired key type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.locality">
<code class="sig-name descname">locality</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.locality" title="Permalink to this definition">¶</a></dt>
<dd><p>The locality</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.other_sans">
<code class="sig-name descname">other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of other SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.ou">
<code class="sig-name descname">ou</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.ou" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization unit</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.postal_code">
<code class="sig-name descname">postal_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.postal_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key">
<code class="sig-name descname">private_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key_format">
<code class="sig-name descname">private_key_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key_type">
<code class="sig-name descname">private_key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.private_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.province">
<code class="sig-name descname">province</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.province" title="Permalink to this definition">¶</a></dt>
<dd><p>The province</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.street_address">
<code class="sig-name descname">street_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of intermediate to create. Must be either “exported” or “internal”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.uri_sans">
<code class="sig-name descname">uri_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative URIs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendIntermediateCertRequest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CSR</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits to use</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired key type</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>private_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key type</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of intermediate to create. Must be either “exported” or “internal”</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_cert_request.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_cert_request.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateCertRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendIntermediateSetSigned</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendIntermediateSetSigned resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_set_signed.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_set_signed.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendIntermediateSetSigned resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_set_signed.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_intermediate_set_signed.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendIntermediateSetSigned.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_any_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_bare_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_glob_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_localhost</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_subdomains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">basic_constraints_valid_for_non_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_signing_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">countries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_protection_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_key_usages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generate_lease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_usages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">localities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_store</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_before_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_identifiers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provinces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_cn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a role on an PKI Secret Backend for Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_any_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow any name</p></li>
<li><p><strong>allow_bare_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates matching the actual domain</p></li>
<li><p><strong>allow_glob_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow names containing glob patterns.</p></li>
<li><p><strong>allow_ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow IP SANs</p></li>
<li><p><strong>allow_localhost</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates for localhost</p></li>
<li><p><strong>allow_subdomains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates matching subdomains</p></li>
<li><p><strong>allowed_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed domains for certificates</p></li>
<li><p><strong>allowed_other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines allowed custom SANs</p></li>
<li><p><strong>allowed_uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines allowed URI SANs</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>basic_constraints_valid_for_non_ca</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to mark basic constraints valid when issuing non-CA certificates</p></li>
<li><p><strong>client_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for client use</p></li>
<li><p><strong>code_signing_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for code signing use</p></li>
<li><p><strong>countries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The country of generated certificates</p></li>
<li><p><strong>email_protection_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for email protection use</p></li>
<li><p><strong>enforce_hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow only valid host names</p></li>
<li><p><strong>ext_key_usages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the allowed extended key usage constraint on issued certificates</p></li>
<li><p><strong>generate_lease</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to generate leases with certificates</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits of generated keys</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of generated keys</p></li>
<li><p><strong>key_usages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the allowed key usage constraint on issued certificates</p></li>
<li><p><strong>localities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The locality of generated certificates</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum TTL</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend. Must be unique within the backend.</p></li>
<li><p><strong>no_store</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to not store certificates in the storage backend</p></li>
<li><p><strong>not_before_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the duration by which to backdate the NotBefore property.</p></li>
<li><p><strong>organizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The organization of generated certificates</p></li>
<li><p><strong>organization_unit</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The organization unit of generated certificates</p></li>
<li><p><strong>policy_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the list of allowed policies IODs</p></li>
<li><p><strong>postal_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The postal code of generated certificates</p></li>
<li><p><strong>provinces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The province of generated certificates</p></li>
<li><p><strong>require_cn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to force CN usage</p></li>
<li><p><strong>server_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for server use</p></li>
<li><p><strong>street_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The street address of generated certificates</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL</p></li>
<li><p><strong>use_csr_common_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to use the CN in the CSR</p></li>
<li><p><strong>use_csr_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to use the SANs in the CSR</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_any_name">
<code class="sig-name descname">allow_any_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_any_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow any name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_bare_domains">
<code class="sig-name descname">allow_bare_domains</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_bare_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow certificates matching the actual domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_glob_domains">
<code class="sig-name descname">allow_glob_domains</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_glob_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow names containing glob patterns.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_ip_sans">
<code class="sig-name descname">allow_ip_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow IP SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_localhost">
<code class="sig-name descname">allow_localhost</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_localhost" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow certificates for localhost</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allow_subdomains">
<code class="sig-name descname">allow_subdomains</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allow_subdomains" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow certificates matching subdomains</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allowed_domains">
<code class="sig-name descname">allowed_domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allowed_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed domains for certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allowed_other_sans">
<code class="sig-name descname">allowed_other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allowed_other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines allowed custom SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.allowed_uri_sans">
<code class="sig-name descname">allowed_uri_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.allowed_uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines allowed URI SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.basic_constraints_valid_for_non_ca">
<code class="sig-name descname">basic_constraints_valid_for_non_ca</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.basic_constraints_valid_for_non_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to mark basic constraints valid when issuing non-CA certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.client_flag">
<code class="sig-name descname">client_flag</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.client_flag" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to specify certificates for client use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.code_signing_flag">
<code class="sig-name descname">code_signing_flag</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.code_signing_flag" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to specify certificates for code signing use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.countries">
<code class="sig-name descname">countries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.countries" title="Permalink to this definition">¶</a></dt>
<dd><p>The country of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.email_protection_flag">
<code class="sig-name descname">email_protection_flag</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.email_protection_flag" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to specify certificates for email protection use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.enforce_hostnames">
<code class="sig-name descname">enforce_hostnames</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.enforce_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow only valid host names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.ext_key_usages">
<code class="sig-name descname">ext_key_usages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.ext_key_usages" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the allowed extended key usage constraint on issued certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.generate_lease">
<code class="sig-name descname">generate_lease</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.generate_lease" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to generate leases with certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.key_bits">
<code class="sig-name descname">key_bits</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.key_bits" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bits of generated keys</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.key_type">
<code class="sig-name descname">key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of generated keys</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.key_usages">
<code class="sig-name descname">key_usages</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.key_usages" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the allowed key usage constraint on issued certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.localities">
<code class="sig-name descname">localities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.localities" title="Permalink to this definition">¶</a></dt>
<dd><p>The locality of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify this role within the backend. Must be unique within the backend.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.no_store">
<code class="sig-name descname">no_store</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.no_store" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to not store certificates in the storage backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.not_before_duration">
<code class="sig-name descname">not_before_duration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.not_before_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the duration by which to backdate the NotBefore property.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.organizations">
<code class="sig-name descname">organizations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.organizations" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.organization_unit">
<code class="sig-name descname">organization_unit</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.organization_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization unit of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.policy_identifiers">
<code class="sig-name descname">policy_identifiers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.policy_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the list of allowed policies IODs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.postal_codes">
<code class="sig-name descname">postal_codes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.postal_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.provinces">
<code class="sig-name descname">provinces</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.provinces" title="Permalink to this definition">¶</a></dt>
<dd><p>The province of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.require_cn">
<code class="sig-name descname">require_cn</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.require_cn" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to force CN usage</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.server_flag">
<code class="sig-name descname">server_flag</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.server_flag" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to specify certificates for server use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.street_addresses">
<code class="sig-name descname">street_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.street_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address of generated certificates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.use_csr_common_name">
<code class="sig-name descname">use_csr_common_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.use_csr_common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to use the CN in the CSR</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.use_csr_sans">
<code class="sig-name descname">use_csr_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.use_csr_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to use the SANs in the CSR</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_any_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_bare_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_glob_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_localhost</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_subdomains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">basic_constraints_valid_for_non_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_signing_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">countries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_protection_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_key_usages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generate_lease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_usages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">localities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_store</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_before_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_identifiers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provinces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_cn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_flag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_sans</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_any_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow any name</p></li>
<li><p><strong>allow_bare_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates matching the actual domain</p></li>
<li><p><strong>allow_glob_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow names containing glob patterns.</p></li>
<li><p><strong>allow_ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow IP SANs</p></li>
<li><p><strong>allow_localhost</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates for localhost</p></li>
<li><p><strong>allow_subdomains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow certificates matching subdomains</p></li>
<li><p><strong>allowed_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed domains for certificates</p></li>
<li><p><strong>allowed_other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines allowed custom SANs</p></li>
<li><p><strong>allowed_uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines allowed URI SANs</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the PKI secret backend is mounted at, with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>basic_constraints_valid_for_non_ca</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to mark basic constraints valid when issuing non-CA certificates</p></li>
<li><p><strong>client_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for client use</p></li>
<li><p><strong>code_signing_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for code signing use</p></li>
<li><p><strong>countries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The country of generated certificates</p></li>
<li><p><strong>email_protection_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for email protection use</p></li>
<li><p><strong>enforce_hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow only valid host names</p></li>
<li><p><strong>ext_key_usages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the allowed extended key usage constraint on issued certificates</p></li>
<li><p><strong>generate_lease</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to generate leases with certificates</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits of generated keys</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of generated keys</p></li>
<li><p><strong>key_usages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the allowed key usage constraint on issued certificates</p></li>
<li><p><strong>localities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The locality of generated certificates</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum TTL</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend. Must be unique within the backend.</p></li>
<li><p><strong>no_store</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to not store certificates in the storage backend</p></li>
<li><p><strong>not_before_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the duration by which to backdate the NotBefore property.</p></li>
<li><p><strong>organizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The organization of generated certificates</p></li>
<li><p><strong>organization_unit</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The organization unit of generated certificates</p></li>
<li><p><strong>policy_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify the list of allowed policies IODs</p></li>
<li><p><strong>postal_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The postal code of generated certificates</p></li>
<li><p><strong>provinces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The province of generated certificates</p></li>
<li><p><strong>require_cn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to force CN usage</p></li>
<li><p><strong>server_flag</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to specify certificates for server use</p></li>
<li><p><strong>street_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The street address of generated certificates</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL</p></li>
<li><p><strong>use_csr_common_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to use the CN in the CSR</p></li>
<li><p><strong>use_csr_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to use the SANs in the CSR</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendRootCert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_path_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permitted_dns_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendRootCert resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits to use</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired key type</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>max_path_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum path length to encode in the generated certificate</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>permitted_dns_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of domains for which certificates are allowed to be issued</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of intermediate to create. Must be either “exported” or “internal”</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_cert.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.alt_names">
<code class="sig-name descname">alt_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.alt_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.common_name">
<code class="sig-name descname">common_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>CN of intermediate to create</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.country">
<code class="sig-name descname">country</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.exclude_cn_from_sans">
<code class="sig-name descname">exclude_cn_from_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.exclude_cn_from_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to exclude CN from SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of data</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.ip_sans">
<code class="sig-name descname">ip_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative IPs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.issuing_ca">
<code class="sig-name descname">issuing_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.issuing_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuing CA</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.key_bits">
<code class="sig-name descname">key_bits</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.key_bits" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bits to use</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.key_type">
<code class="sig-name descname">key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired key type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.locality">
<code class="sig-name descname">locality</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.locality" title="Permalink to this definition">¶</a></dt>
<dd><p>The locality</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.max_path_length">
<code class="sig-name descname">max_path_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.max_path_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum path length to encode in the generated certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.other_sans">
<code class="sig-name descname">other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of other SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.ou">
<code class="sig-name descname">ou</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.ou" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization unit</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.permitted_dns_domains">
<code class="sig-name descname">permitted_dns_domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.permitted_dns_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>List of domains for which certificates are allowed to be issued</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.postal_code">
<code class="sig-name descname">postal_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.postal_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.private_key_format">
<code class="sig-name descname">private_key_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.private_key_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.province">
<code class="sig-name descname">province</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.province" title="Permalink to this definition">¶</a></dt>
<dd><p>The province</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.serial">
<code class="sig-name descname">serial</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.street_address">
<code class="sig-name descname">street_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of intermediate to create. Must be either “exported” or “internal”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.uri_sans">
<code class="sig-name descname">uri_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative URIs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_bits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_path_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permitted_dns_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRootCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>issuing_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The issuing CA</p></li>
<li><p><strong>key_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bits to use</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired key type</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>max_path_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum path length to encode in the generated certificate</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>permitted_dns_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of domains for which certificates are allowed to be issued</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>private_key_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key format</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>serial</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serial</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of intermediate to create. Must be either “exported” or “internal”</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_cert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRootCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendRootSignIntermediate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_path_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permitted_dns_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_values</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an PKI certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CSR</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>max_path_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum path length to encode in the generated certificate</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>permitted_dns_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of domains for which certificates are allowed to be issued</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
<li><p><strong>use_csr_values</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Preserve CSR values</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_sign_intermediate.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_sign_intermediate.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.alt_names">
<code class="sig-name descname">alt_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.alt_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ca_chain">
<code class="sig-name descname">ca_chain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ca_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA chain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.common_name">
<code class="sig-name descname">common_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>CN of intermediate to create</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.country">
<code class="sig-name descname">country</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.csr">
<code class="sig-name descname">csr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CSR</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.exclude_cn_from_sans">
<code class="sig-name descname">exclude_cn_from_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.exclude_cn_from_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to exclude CN from SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of data</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ip_sans">
<code class="sig-name descname">ip_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative IPs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.issuing_ca">
<code class="sig-name descname">issuing_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.issuing_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuing CA</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.locality">
<code class="sig-name descname">locality</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.locality" title="Permalink to this definition">¶</a></dt>
<dd><p>The locality</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.max_path_length">
<code class="sig-name descname">max_path_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.max_path_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum path length to encode in the generated certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.other_sans">
<code class="sig-name descname">other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of other SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ou">
<code class="sig-name descname">ou</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ou" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization unit</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.permitted_dns_domains">
<code class="sig-name descname">permitted_dns_domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.permitted_dns_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>List of domains for which certificates are allowed to be issued</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.postal_code">
<code class="sig-name descname">postal_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.postal_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The postal code</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.province">
<code class="sig-name descname">province</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.province" title="Permalink to this definition">¶</a></dt>
<dd><p>The province</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.serial">
<code class="sig-name descname">serial</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.street_address">
<code class="sig-name descname">street_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The street address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.uri_sans">
<code class="sig-name descname">uri_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative URIs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.use_csr_values">
<code class="sig-name descname">use_csr_values</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.use_csr_values" title="Permalink to this definition">¶</a></dt>
<dd><p>Preserve CSR values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_chain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locality</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_path_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ou</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permitted_dns_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">postal_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">province</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">street_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_csr_values</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRootSignIntermediate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>ca_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA chain</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of intermediate to create</p></li>
<li><p><strong>country</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The country</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CSR</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>issuing_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The issuing CA</p></li>
<li><p><strong>locality</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locality</p></li>
<li><p><strong>max_path_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum path length to encode in the generated certificate</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization unit</p></li>
<li><p><strong>permitted_dns_domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of domains for which certificates are allowed to be issued</p></li>
<li><p><strong>postal_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The postal code</p></li>
<li><p><strong>province</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The province</p></li>
<li><p><strong>serial</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serial</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The street address</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative URIs</p></li>
<li><p><strong>use_csr_values</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Preserve CSR values</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_sign_intermediate.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_root_sign_intermediate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendRootSignIntermediate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendSign">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.pki_secret.</code><code class="sig-name descname">SecretBackendSign</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_seconds_remaining</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendSign resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of certificate to create</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CSR</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>min_seconds_remaining</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role to create the certificate against</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alterative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_sign.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_sign.html.markdown</a>.</p>
</div></blockquote>
<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.alt_names">
<code class="sig-name descname">alt_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.alt_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative names</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The PKI secret backend the resource belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.ca_chains">
<code class="sig-name descname">ca_chains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.ca_chains" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA chain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.common_name">
<code class="sig-name descname">common_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>CN of certificate to create</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.csr">
<code class="sig-name descname">csr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CSR</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.exclude_cn_from_sans">
<code class="sig-name descname">exclude_cn_from_sans</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.exclude_cn_from_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to exclude CN from SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.expiration">
<code class="sig-name descname">expiration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration date of the certificate in unix epoch format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of data</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.ip_sans">
<code class="sig-name descname">ip_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.ip_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alternative IPs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.issuing_ca">
<code class="sig-name descname">issuing_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.issuing_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuing CA</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.min_seconds_remaining">
<code class="sig-name descname">min_seconds_remaining</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.min_seconds_remaining" title="Permalink to this definition">¶</a></dt>
<dd><p>Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role to create the certificate against</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.other_sans">
<code class="sig-name descname">other_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.other_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of other SANs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.serial">
<code class="sig-name descname">serial</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.uri_sans">
<code class="sig-name descname">uri_sans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alterative URIs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alt_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_chains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">common_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_cn_from_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuing_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_seconds_remaining</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">other_sans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri_sans</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendSign resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alt_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative names</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, certs will be renewed if the expiration is within <code class="docutils literal notranslate"><span class="pre">min_seconds_remaining</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PKI secret backend the resource belongs to.</p></li>
<li><p><strong>ca_chains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The CA chain</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate</p></li>
<li><p><strong>common_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CN of certificate to create</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CSR</p></li>
<li><p><strong>exclude_cn_from_sans</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to exclude CN from SANs</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The expiration date of the certificate in unix epoch format</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of data</p></li>
<li><p><strong>ip_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alternative IPs</p></li>
<li><p><strong>issuing_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The issuing CA</p></li>
<li><p><strong>min_seconds_remaining</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generate a new certificate when the expiration is within this number of seconds, default is 604800 (7 days)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role to create the certificate against</p></li>
<li><p><strong>other_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of other SANs</p></li>
<li><p><strong>serial</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serial</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time to live</p></li>
<li><p><strong>uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of alterative URIs</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_sign.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/pki_secret_backend_sign.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.pki_secret.SecretBackendSign.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.pki_secret.SecretBackendSign.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.pki_secret.SecretBackendSign.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
