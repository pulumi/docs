<div class="section" id="module-pulumi_aws.acmpca">
<span id="acmpca"></span><h1>acmpca<a class="headerlink" href="#module-pulumi_aws.acmpca" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.acmpca.CertificateAuthority">
<em class="property">class </em><code class="descclassname">pulumi_aws.acmpca.</code><code class="descname">CertificateAuthority</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_authority_configuration=None</em>, <em>enabled=None</em>, <em>revocation_configuration=None</em>, <em>tags=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS Certificate Manager Private Certificate Authorities (ACM PCA Certificate Authorities).</p>
<p>&gt; <strong>NOTE:</strong> Creating this resource will leave the certificate authority in a <cite>PENDING_CERTIFICATE</cite> status, which means it cannot yet issue certificates. To complete this setup, you must fully sign the certificate authority CSR available in the <cite>certificate_signing_request</cite> attribute and import the signed certificate outside of Terraform. Terraform can support another resource to manage that workflow automatically in the future.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_authority_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing algorithms and certificate subject information. Defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <cite>false</cite>.</li>
<li><strong>revocation_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing revocation configuration. Defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a key-value map of user-defined tags that are attached to the certificate authority.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the certificate authority. Currently, this must be <cite>SUBORDINATE</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_authority_configuration">
<code class="descname">certificate_authority_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_authority_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing algorithms and certificate subject information. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_signing_request">
<code class="descname">certificate_signing_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_signing_request" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.not_after">
<code class="descname">not_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.not_after" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.not_before">
<code class="descname">not_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.not_before" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.revocation_configuration">
<code class="descname">revocation_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.revocation_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing revocation configuration. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.serial">
<code class="descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the certificate authority. Currently, this must be <cite>SUBORDINATE</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.acmpca.CertificateAuthority.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acmpca.CertificateAuthority.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.acmpca.</code><code class="descname">GetCertificateAuthorityResult</code><span class="sig-paren">(</span><em>certificate=None</em>, <em>certificate_chain=None</em>, <em>certificate_signing_request=None</em>, <em>not_after=None</em>, <em>not_before=None</em>, <em>revocation_configurations=None</em>, <em>serial=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificateAuthority.</p>
<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_signing_request">
<code class="descname">certificate_signing_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_signing_request" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.not_after">
<code class="descname">not_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.not_after" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.not_before">
<code class="descname">not_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.not_before" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.revocation_configurations">
<code class="descname">revocation_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.revocation_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing revocation configuration.
* <cite>revocation_configuration.0.crl_configuration</cite> - Nested attribute containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority.
* <cite>revocation_configuration.0.crl_configuration.0.custom_cname</cite> - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point.
* <cite>revocation_configuration.0.crl_configuration.0.enabled</cite> - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
* <cite>revocation_configuration.0.crl_configuration.0.expiration_in_days</cite> - Number of days until a certificate expires.
* <cite>revocation_configuration.0.crl_configuration.0.s3_bucket_name</cite> - Name of the S3 bucket that contains the CRL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.serial">
<code class="descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.acmpca.get_certificate_authority">
<code class="descclassname">pulumi_aws.acmpca.</code><code class="descname">get_certificate_authority</code><span class="sig-paren">(</span><em>arn=None</em>, <em>revocation_configurations=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.get_certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a AWS Certificate Manager Private Certificate Authority (ACM PCA Certificate Authority).</p>
</dd></dl>

</div>
