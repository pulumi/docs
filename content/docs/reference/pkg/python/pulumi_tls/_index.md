---
title: Package pulumi_tls
title_tag: Package pulumi_tls | Python SDK
linktitle: pulumi_tls
notitle: true
---

<div class="section" id="pulumi-tls">
<h1>Pulumi TLS<a class="headerlink" href="#pulumi-tls" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-tls/issues">pulumi/pulumi-tls repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/issues">terraform-providers/terraform-provider-tls repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_tls"></span><dl class="class">
<dt id="pulumi_tls.AwaitableGetPublicKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">AwaitableGetPublicKeyResult</code><span class="sig-paren">(</span><em class="sig-param">algorithm=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">public_key_fingerprint_md5=None</em>, <em class="sig-param">public_key_openssh=None</em>, <em class="sig-param">public_key_pem=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.AwaitableGetPublicKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_tls.CertRequest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">CertRequest</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_names=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">subjects=None</em>, <em class="sig-param">uris=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CertRequest resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] dns_names: List of DNS names for which a certificate is being requested.
:param pulumi.Input[list] ip_addresses: List of IP addresses for which a certificate is being requested.
:param pulumi.Input[str] key_algorithm: The name of the algorithm for the key provided</p>
<blockquote>
<div><p>in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key that the certificate will belong to</p></li>
<li><p><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested. This is
a nested configuration block whose structure is described below.</p></li>
<li><p><strong>uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for which a certificate is being requested.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subjects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_tls.CertRequest.cert_request_pem">
<code class="sig-name descname">cert_request_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.cert_request_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate request data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.dns_names">
<code class="sig-name descname">dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS names for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.ip_addresses">
<code class="sig-name descname">ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.key_algorithm">
<code class="sig-name descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.private_key_pem">
<code class="sig-name descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded private key that the certificate will belong to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.subjects">
<code class="sig-name descname">subjects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.subjects" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject for which a certificate is being requested. This is
a nested configuration block whose structure is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.uris">
<code class="sig-name descname">uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for which a certificate is being requested.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.CertRequest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cert_request_pem=None</em>, <em class="sig-param">dns_names=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">subjects=None</em>, <em class="sig-param">uris=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertRequest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cert_request_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate request data in PEM format.</p></li>
<li><p><strong>dns_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS names for which a certificate is being requested.</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses for which a certificate is being requested.</p></li>
<li><p><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key that the certificate will belong to</p></li>
<li><p><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested. This is
a nested configuration block whose structure is described below.</p></li>
<li><p><strong>uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for which a certificate is being requested.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subjects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.CertRequest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.CertRequest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.GetPublicKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">GetPublicKeyResult</code><span class="sig-paren">(</span><em class="sig-param">algorithm=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">public_key_fingerprint_md5=None</em>, <em class="sig-param">public_key_openssh=None</em>, <em class="sig-param">public_key_pem=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicKey.</p>
<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.private_key_pem">
<code class="sig-name descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_fingerprint_md5">
<code class="sig-name descname">public_key_fingerprint_md5</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_fingerprint_md5" title="Permalink to this definition">¶</a></dt>
<dd><p>The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. <code class="docutils literal notranslate"><span class="pre">aa:bb:cc:...</span></code>. Only available if the
selected private key format is compatible, as per the rules for
<code class="docutils literal notranslate"><span class="pre">public_key_openssh</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_openssh">
<code class="sig-name descname">public_key_openssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_openssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in OpenSSH <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code>
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves “P256”, “P384” and “P521”
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_pem">
<code class="sig-name descname">public_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in PEM format.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_tls.LocallySignedCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">LocallySignedCert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_uses=None</em>, <em class="sig-param">ca_cert_pem=None</em>, <em class="sig-param">ca_key_algorithm=None</em>, <em class="sig-param">ca_private_key_pem=None</em>, <em class="sig-param">cert_request_pem=None</em>, <em class="sig-param">early_renewal_hours=None</em>, <em class="sig-param">is_ca_certificate=None</em>, <em class="sig-param">set_subject_key_id=None</em>, <em class="sig-param">validity_period_hours=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LocallySignedCert resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] allowed_uses: List of keywords each describing a use that is permitted</p>
<blockquote>
<div><p>for the issued certificate. The valid keywords are listed below.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ca_cert_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded certificate data for the CA.</p></li>
<li><p><strong>ca_key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">ca_private_key_pem</span></code>.</p></li>
<li><p><strong>ca_private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key data for the CA.
This can be read from a separate file using the <code class="docutils literal notranslate"><span class="pre">file</span></code> interpolation
function.</p></li>
<li><p><strong>cert_request_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded request certificate data.</p></li>
<li><p><strong>early_renewal_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of hours before the certificates expiry when a new certificate will be generated</p></li>
<li><p><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p></li>
<li><p><strong>set_subject_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p></li>
<li><p><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.allowed_uses">
<code class="sig-name descname">allowed_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.allowed_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_cert_pem">
<code class="sig-name descname">ca_cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded certificate data for the CA.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_key_algorithm">
<code class="sig-name descname">ca_key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">ca_private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_private_key_pem">
<code class="sig-name descname">ca_private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded private key data for the CA.
This can be read from a separate file using the <code class="docutils literal notranslate"><span class="pre">file</span></code> interpolation
function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.cert_pem">
<code class="sig-name descname">cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.cert_request_pem">
<code class="sig-name descname">cert_request_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.cert_request_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded request certificate data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.early_renewal_hours">
<code class="sig-name descname">early_renewal_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.early_renewal_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of hours before the certificates expiry when a new certificate will be generated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.is_ca_certificate">
<code class="sig-name descname">is_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.is_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.set_subject_key_id">
<code class="sig-name descname">set_subject_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.set_subject_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_end_time">
<code class="sig-name descname">validity_end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_period_hours">
<code class="sig-name descname">validity_period_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_period_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours after initial issuing that the
certificate will become invalid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_start_time">
<code class="sig-name descname">validity_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.LocallySignedCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_uses=None</em>, <em class="sig-param">ca_cert_pem=None</em>, <em class="sig-param">ca_key_algorithm=None</em>, <em class="sig-param">ca_private_key_pem=None</em>, <em class="sig-param">cert_pem=None</em>, <em class="sig-param">cert_request_pem=None</em>, <em class="sig-param">early_renewal_hours=None</em>, <em class="sig-param">is_ca_certificate=None</em>, <em class="sig-param">ready_for_renewal=None</em>, <em class="sig-param">set_subject_key_id=None</em>, <em class="sig-param">validity_end_time=None</em>, <em class="sig-param">validity_period_hours=None</em>, <em class="sig-param">validity_start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LocallySignedCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_uses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p></li>
<li><p><strong>ca_cert_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded certificate data for the CA.</p></li>
<li><p><strong>ca_key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">ca_private_key_pem</span></code>.</p></li>
<li><p><strong>ca_private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key data for the CA.
This can be read from a separate file using the <code class="docutils literal notranslate"><span class="pre">file</span></code> interpolation
function.</p></li>
<li><p><strong>cert_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate data in PEM format.</p></li>
<li><p><strong>cert_request_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded request certificate data.</p></li>
<li><p><strong>early_renewal_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of hours before the certificates expiry when a new certificate will be generated</p></li>
<li><p><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p></li>
<li><p><strong>set_subject_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p></li>
<li><p><strong>validity_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</p></li>
<li><p><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</p></li>
<li><p><strong>validity_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.LocallySignedCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.LocallySignedCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.PrivateKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">PrivateKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">ecdsa_curve=None</em>, <em class="sig-param">rsa_bits=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PrivateKey resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] algorithm: The name of the algorithm to use for</p>
<blockquote>
<div><p>the key. Currently-supported values are “RSA” and “ECDSA”.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ecdsa_curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “ECDSA”, the name of the elliptic
curve to use. May be any one of “P224”, “P256”, “P384” or “P521”, with “P224” as the
default.</p></li>
<li><p><strong>rsa_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “RSA”, the size of the generated
RSA key in bits. Defaults to 2048.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm to use for
the key. Currently-supported values are “RSA” and “ECDSA”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.ecdsa_curve">
<code class="sig-name descname">ecdsa_curve</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.ecdsa_curve" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “ECDSA”, the name of the elliptic
curve to use. May be any one of “P224”, “P256”, “P384” or “P521”, with “P224” as the
default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.private_key_pem">
<code class="sig-name descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_fingerprint_md5">
<code class="sig-name descname">public_key_fingerprint_md5</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_fingerprint_md5" title="Permalink to this definition">¶</a></dt>
<dd><p>The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. <code class="docutils literal notranslate"><span class="pre">aa:bb:cc:...</span></code>. Only available if the
selected private key format is compatible, as per the rules for
<code class="docutils literal notranslate"><span class="pre">public_key_openssh</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_openssh">
<code class="sig-name descname">public_key_openssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_openssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in OpenSSH <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code>
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves “P256”, “P384” and “P521”
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_pem">
<code class="sig-name descname">public_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.rsa_bits">
<code class="sig-name descname">rsa_bits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.rsa_bits" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “RSA”, the size of the generated
RSA key in bits. Defaults to 2048.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.PrivateKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">ecdsa_curve=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">public_key_fingerprint_md5=None</em>, <em class="sig-param">public_key_openssh=None</em>, <em class="sig-param">public_key_pem=None</em>, <em class="sig-param">rsa_bits=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm to use for
the key. Currently-supported values are “RSA” and “ECDSA”.</p></li>
<li><p><strong>ecdsa_curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “ECDSA”, the name of the elliptic
curve to use. May be any one of “P224”, “P256”, “P384” or “P521”, with “P224” as the
default.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key data in PEM format.</p></li>
<li><p><strong>public_key_fingerprint_md5</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. <code class="docutils literal notranslate"><span class="pre">aa:bb:cc:...</span></code>. Only available if the
selected private key format is compatible, as per the rules for
<code class="docutils literal notranslate"><span class="pre">public_key_openssh</span></code>.</p></li>
<li><p><strong>public_key_openssh</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key data in OpenSSH <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code>
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves “P256”, “P384” and “P521”
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.</p></li>
<li><p><strong>public_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key data in PEM format.</p></li>
<li><p><strong>rsa_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “RSA”, the size of the generated
RSA key in bits. Defaults to 2048.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.PrivateKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.PrivateKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the tls package. By default, resources use package-wide configuration
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
<dl class="method">
<dt id="pulumi_tls.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.SelfSignedCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">SelfSignedCert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_uses=None</em>, <em class="sig-param">dns_names=None</em>, <em class="sig-param">early_renewal_hours=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">is_ca_certificate=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">set_subject_key_id=None</em>, <em class="sig-param">subjects=None</em>, <em class="sig-param">uris=None</em>, <em class="sig-param">validity_period_hours=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SelfSignedCert resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] allowed_uses: List of keywords each describing a use that is permitted</p>
<blockquote>
<div><p>for the issued certificate. The valid keywords are listed below.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dns_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS names for which a certificate is being requested.</p></li>
<li><p><strong>early_renewal_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of hours before the certificates expiry when a new certificate will be generated</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses for which a certificate is being requested.</p></li>
<li><p><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p></li>
<li><p><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key that the certificate will belong to</p></li>
<li><p><strong>set_subject_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p></li>
<li><p><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for <code class="docutils literal notranslate"><span class="pre">.CertRequest</span></code>.</p></li>
<li><p><strong>uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for which a certificate is being requested.</p></li>
<li><p><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subjects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.allowed_uses">
<code class="sig-name descname">allowed_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.allowed_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.cert_pem">
<code class="sig-name descname">cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.dns_names">
<code class="sig-name descname">dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS names for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.early_renewal_hours">
<code class="sig-name descname">early_renewal_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.early_renewal_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of hours before the certificates expiry when a new certificate will be generated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.ip_addresses">
<code class="sig-name descname">ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.is_ca_certificate">
<code class="sig-name descname">is_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.is_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.key_algorithm">
<code class="sig-name descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.private_key_pem">
<code class="sig-name descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded private key that the certificate will belong to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.set_subject_key_id">
<code class="sig-name descname">set_subject_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.set_subject_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.subjects">
<code class="sig-name descname">subjects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.subjects" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for <code class="docutils literal notranslate"><span class="pre">.CertRequest</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.uris">
<code class="sig-name descname">uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_end_time">
<code class="sig-name descname">validity_end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_period_hours">
<code class="sig-name descname">validity_period_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_period_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours after initial issuing that the
certificate will become invalid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_start_time">
<code class="sig-name descname">validity_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.SelfSignedCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_uses=None</em>, <em class="sig-param">cert_pem=None</em>, <em class="sig-param">dns_names=None</em>, <em class="sig-param">early_renewal_hours=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">is_ca_certificate=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">private_key_pem=None</em>, <em class="sig-param">ready_for_renewal=None</em>, <em class="sig-param">set_subject_key_id=None</em>, <em class="sig-param">subjects=None</em>, <em class="sig-param">uris=None</em>, <em class="sig-param">validity_end_time=None</em>, <em class="sig-param">validity_period_hours=None</em>, <em class="sig-param">validity_start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SelfSignedCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_uses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p></li>
<li><p><strong>cert_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate data in PEM format.</p></li>
<li><p><strong>dns_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS names for which a certificate is being requested.</p></li>
<li><p><strong>early_renewal_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of hours before the certificates expiry when a new certificate will be generated</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses for which a certificate is being requested.</p></li>
<li><p><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p></li>
<li><p><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p></li>
<li><p><strong>private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key that the certificate will belong to</p></li>
<li><p><strong>set_subject_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the certificate will include
the subject key identifier. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, in which case the subject
key identifier is not set at all.</p></li>
<li><p><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for <code class="docutils literal notranslate"><span class="pre">.CertRequest</span></code>.</p></li>
<li><p><strong>uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for which a certificate is being requested.</p></li>
<li><p><strong>validity_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</p></li>
<li><p><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</p></li>
<li><p><strong>validity_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subjects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postalCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">province</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serialNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">streetAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.SelfSignedCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.SelfSignedCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.get_public_key">
<code class="sig-prename descclassname">pulumi_tls.</code><code class="sig-name descname">get_public_key</code><span class="sig-paren">(</span><em class="sig-param">private_key_pem=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.get_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the public key from a PEM-encoded private key for use in other
resources.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>private_key_pem</strong> (<em>str</em>) – The private key to use. Currently-supported key types are “RSA” or “ECDSA”.</p>
</dd>
</dl>
</dd></dl>

</div>
