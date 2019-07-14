---
---

<div class="section" id="pulumi-tls">
<h1>Pulumi TLS<a class="headerlink" href="#pulumi-tls" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-tls/issues">pulumi/pulumi-tls repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/issues">terraform-providers/terraform-provider-tls repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_tls"></span><dl class="class">
<dt id="pulumi_tls.CertRequest">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">CertRequest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dns_names=None</em>, <em>ip_addresses=None</em>, <em>key_algorithm=None</em>, <em>private_key_pem=None</em>, <em>subjects=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CertRequest resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dns_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS names for which a certificate is being requested.</li>
<li><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses for which a certificate is being requested.</li>
<li><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</li>
<li><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested. This is
a nested configuration block whose structure is described below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/cert_request.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/cert_request.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_tls.CertRequest.cert_request_pem">
<code class="descname">cert_request_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.cert_request_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate request data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.dns_names">
<code class="descname">dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS names for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.ip_addresses">
<code class="descname">ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.key_algorithm">
<code class="descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.CertRequest.subjects">
<code class="descname">subjects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.CertRequest.subjects" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject for which a certificate is being requested. This is
a nested configuration block whose structure is described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.CertRequest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.CertRequest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.CertRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.GetPublicKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">GetPublicKeyResult</code><span class="sig-paren">(</span><em>algorithm=None</em>, <em>private_key_pem=None</em>, <em>public_key_fingerprint_md5=None</em>, <em>public_key_openssh=None</em>, <em>public_key_pem=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicKey.</p>
<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.private_key_pem">
<code class="descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_fingerprint_md5">
<code class="descname">public_key_fingerprint_md5</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_fingerprint_md5" title="Permalink to this definition">¶</a></dt>
<dd><p>The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. <code class="docutils literal notranslate"><span class="pre">aa:bb:cc:...</span></code>. Only available if the
selected private key format is compatible, as per the rules for
<code class="docutils literal notranslate"><span class="pre">public_key_openssh</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_openssh">
<code class="descname">public_key_openssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_openssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in OpenSSH <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code>
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves “P256”, “P384” and “P521”
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.public_key_pem">
<code class="descname">public_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.public_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.GetPublicKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.GetPublicKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_tls.LocallySignedCert">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">LocallySignedCert</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_uses=None</em>, <em>ca_cert_pem=None</em>, <em>ca_key_algorithm=None</em>, <em>ca_private_key_pem=None</em>, <em>cert_request_pem=None</em>, <em>early_renewal_hours=None</em>, <em>is_ca_certificate=None</em>, <em>validity_period_hours=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LocallySignedCert resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_uses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</li>
<li><strong>ca_cert_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded certificate data for the CA.</li>
<li><strong>ca_key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">ca_private_key_pem</span></code>.</li>
<li><strong>ca_private_key_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded private key data for the CA.
This can be read from a separate file using the <code class="docutils literal notranslate"><span class="pre">file</span></code> interpolation
function.</li>
<li><strong>cert_request_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded request certificate data.</li>
<li><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</li>
<li><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/locally_signed_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/locally_signed_cert.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.allowed_uses">
<code class="descname">allowed_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.allowed_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_cert_pem">
<code class="descname">ca_cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded certificate data for the CA.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_key_algorithm">
<code class="descname">ca_key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">ca_private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.ca_private_key_pem">
<code class="descname">ca_private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.ca_private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded private key data for the CA.
This can be read from a separate file using the <code class="docutils literal notranslate"><span class="pre">file</span></code> interpolation
function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.cert_pem">
<code class="descname">cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.cert_request_pem">
<code class="descname">cert_request_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.cert_request_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM-encoded request certificate data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.is_ca_certificate">
<code class="descname">is_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.is_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_end_time">
<code class="descname">validity_end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_period_hours">
<code class="descname">validity_period_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_period_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours after initial issuing that the
certificate will become invalid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.LocallySignedCert.validity_start_time">
<code class="descname">validity_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.LocallySignedCert.validity_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.LocallySignedCert.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.LocallySignedCert.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.LocallySignedCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.PrivateKey">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">PrivateKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>algorithm=None</em>, <em>ecdsa_curve=None</em>, <em>rsa_bits=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PrivateKey resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm to use for
the key. Currently-supported values are “RSA” and “ECDSA”.</li>
<li><strong>ecdsa_curve</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “ECDSA”, the name of the elliptic
curve to use. May be any one of “P224”, “P256”, “P384” or “P521”, with “P224” as the
default.</li>
<li><strong>rsa_bits</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “RSA”, the size of the generated
RSA key in bits. Defaults to 2048.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/private_key.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/private_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.algorithm">
<code class="descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm to use for
the key. Currently-supported values are “RSA” and “ECDSA”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.ecdsa_curve">
<code class="descname">ecdsa_curve</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.ecdsa_curve" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “ECDSA”, the name of the elliptic
curve to use. May be any one of “P224”, “P256”, “P384” or “P521”, with “P224” as the
default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.private_key_pem">
<code class="descname">private_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.private_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_fingerprint_md5">
<code class="descname">public_key_fingerprint_md5</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_fingerprint_md5" title="Permalink to this definition">¶</a></dt>
<dd><p>The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. <code class="docutils literal notranslate"><span class="pre">aa:bb:cc:...</span></code>. Only available if the
selected private key format is compatible, as per the rules for
<code class="docutils literal notranslate"><span class="pre">public_key_openssh</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_openssh">
<code class="descname">public_key_openssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_openssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in OpenSSH <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code>
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves “P256”, “P384” and “P521”
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.public_key_pem">
<code class="descname">public_key_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.public_key_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.PrivateKey.rsa_bits">
<code class="descname">rsa_bits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.PrivateKey.rsa_bits" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">algorithm</span></code> is “RSA”, the size of the generated
RSA key in bits. Defaults to 2048.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.PrivateKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.PrivateKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.PrivateKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.Provider">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the tls package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="method">
<dt id="pulumi_tls.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.SelfSignedCert">
<em class="property">class </em><code class="descclassname">pulumi_tls.</code><code class="descname">SelfSignedCert</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_uses=None</em>, <em>dns_names=None</em>, <em>early_renewal_hours=None</em>, <em>ip_addresses=None</em>, <em>is_ca_certificate=None</em>, <em>key_algorithm=None</em>, <em>private_key_pem=None</em>, <em>subjects=None</em>, <em>validity_period_hours=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SelfSignedCert resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_uses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</li>
<li><strong>dns_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS names for which a certificate is being requested.</li>
<li><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses for which a certificate is being requested.</li>
<li><strong>is_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</li>
<li><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</li>
<li><strong>subjects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for <code class="docutils literal notranslate"><span class="pre">tls_cert_request</span></code>.</li>
<li><strong>validity_period_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours after initial issuing that the
certificate will become invalid.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/self_signed_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/r/self_signed_cert.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.allowed_uses">
<code class="descname">allowed_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.allowed_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of keywords each describing a use that is permitted
for the issued certificate. The valid keywords are listed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.cert_pem">
<code class="descname">cert_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.cert_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate data in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.dns_names">
<code class="descname">dns_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.dns_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS names for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.ip_addresses">
<code class="descname">ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses for which a certificate is being requested.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.is_ca_certificate">
<code class="descname">is_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.is_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean controlling whether the CA flag will be set in the
generated certificate. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, meaning that the certificate does not represent
a certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.key_algorithm">
<code class="descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the algorithm for the key provided
in <code class="docutils literal notranslate"><span class="pre">private_key_pem</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.subjects">
<code class="descname">subjects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.subjects" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject for which a certificate is being requested.
This is a nested configuration block whose structure matches the
corresponding block for <code class="docutils literal notranslate"><span class="pre">tls_cert_request</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_end_time">
<code class="descname">validity_end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time until which the certificate is invalid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_period_hours">
<code class="descname">validity_period_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_period_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours after initial issuing that the
certificate will become invalid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_tls.SelfSignedCert.validity_start_time">
<code class="descname">validity_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_tls.SelfSignedCert.validity_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time after which the certificate is valid, as an
<a class="reference external" href="https://tools.ietf.org/html/rfc3339">RFC3339</a> timestamp.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_tls.SelfSignedCert.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.SelfSignedCert.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.SelfSignedCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_tls.get_public_key">
<code class="descclassname">pulumi_tls.</code><code class="descname">get_public_key</code><span class="sig-paren">(</span><em>private_key_pem=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_tls.get_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the public key from a PEM-encoded private key for use in other
resources.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/d/public_key.html.markdown">https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/d/public_key.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
