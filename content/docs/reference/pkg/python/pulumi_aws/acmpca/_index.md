---
title: Module acmpca
title_tag: Module acmpca | Package pulumi_aws | Python SDK
linktitle: acmpca
notitle: true
---

<div class="section" id="acmpca">
<h1>acmpca<a class="headerlink" href="#acmpca" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.acmpca"></span><dl class="class">
<dt id="pulumi_aws.acmpca.AwaitableGetCertificateAuthorityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.acmpca.</code><code class="sig-name descname">AwaitableGetCertificateAuthorityResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">certificate_signing_request=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">not_after=None</em>, <em class="sig-param">not_before=None</em>, <em class="sig-param">revocation_configurations=None</em>, <em class="sig-param">serial=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.AwaitableGetCertificateAuthorityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.acmpca.CertificateAuthority">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.acmpca.</code><code class="sig-name descname">CertificateAuthority</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_authority_configuration=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">permanent_deletion_time_in_days=None</em>, <em class="sig-param">revocation_configuration=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS Certificate Manager Private Certificate Authorities (ACM PCA Certificate Authorities).</p>
<blockquote>
<div><p><strong>NOTE:</strong> Creating this resource will leave the certificate authority in a <code class="docutils literal notranslate"><span class="pre">PENDING_CERTIFICATE</span></code> status, which means it cannot yet issue certificates. To complete this setup, you must fully sign the certificate authority CSR available in the <code class="docutils literal notranslate"><span class="pre">certificate_signing_request</span></code> attribute and import the signed certificate using the AWS SDK, CLI or Console. This provider can support another resource to manage that workflow automatically in the future.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_authority_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing algorithms and certificate subject information. Defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>permanent_deletion_time_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.</p></li>
<li><p><strong>revocation_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing revocation configuration. Defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the certificate authority. Defaults to <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ROOT</span></code> and <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate_authority_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signingAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the algorithm your private CA uses to sign certificate requests. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that contains X.500 distinguished name information. At least one nested attribute must be specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name (FQDN) associated with the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Two digit code that specifies the country in which the certificate subject located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distinguishedNameQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Disambiguating information for the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generationQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">givenName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - First name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Concatenation that typically contains the first letter of the <code class="docutils literal notranslate"><span class="pre">given_name</span></code>, the first letter of the middle name if one exists, and the first letter of the <code class="docutils literal notranslate"><span class="pre">surname</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The locality (such as a city or town) in which the certificate subject is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Legal name of the organization with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudonym</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Typically a shortened version of a longer <code class="docutils literal notranslate"><span class="pre">given_name</span></code>. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State in which the subject of the certificate is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">surname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Family name. In the US and the UK for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title such as Mr. or Ms. which is pre-pended to the name to refer formally to the certificate subject.</p></li>
</ul>
</li>
</ul>
<p>The <strong>revocation_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">crlConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customCname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don’t want the name of your S3 bucket to be public.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of days until a certificate expires. Must be between 1 and 5000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the S3 bucket that contains the CRL. If you do not provide a value for the <code class="docutils literal notranslate"><span class="pre">custom_cname</span></code> argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_authority_configuration">
<code class="sig-name descname">certificate_authority_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_authority_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing algorithms and certificate subject information. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signingAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the algorithm your private CA uses to sign certificate requests. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that contains X.500 distinguished name information. At least one nested attribute must be specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Fully qualified domain name (FQDN) associated with the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Two digit code that specifies the country in which the certificate subject located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distinguishedNameQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Disambiguating information for the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generationQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">givenName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - First name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initials</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Concatenation that typically contains the first letter of the <code class="docutils literal notranslate"><span class="pre">given_name</span></code>, the first letter of the middle name if one exists, and the first letter of the <code class="docutils literal notranslate"><span class="pre">surname</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The locality (such as a city or town) in which the certificate subject is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Legal name of the organization with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudonym</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Typically a shortened version of a longer <code class="docutils literal notranslate"><span class="pre">given_name</span></code>. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - State in which the subject of the certificate is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">surname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Family name. In the US and the UK for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A title such as Mr. or Ms. which is pre-pended to the name to refer formally to the certificate subject.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_chain">
<code class="sig-name descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.certificate_signing_request">
<code class="sig-name descname">certificate_signing_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.certificate_signing_request" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.not_after">
<code class="sig-name descname">not_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.not_after" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.not_before">
<code class="sig-name descname">not_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.not_before" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.permanent_deletion_time_in_days">
<code class="sig-name descname">permanent_deletion_time_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.permanent_deletion_time_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.revocation_configuration">
<code class="sig-name descname">revocation_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.revocation_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing revocation configuration. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">crlConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customCname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don’t want the name of your S3 bucket to be public.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of days until a certificate expires. Must be between 1 and 5000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the S3 bucket that contains the CRL. If you do not provide a value for the <code class="docutils literal notranslate"><span class="pre">custom_cname</span></code> argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.serial">
<code class="sig-name descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.CertificateAuthority.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the certificate authority. Defaults to <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ROOT</span></code> and <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.acmpca.CertificateAuthority.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_authority_configuration=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">certificate_signing_request=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">not_after=None</em>, <em class="sig-param">not_before=None</em>, <em class="sig-param">permanent_deletion_time_in_days=None</em>, <em class="sig-param">revocation_configuration=None</em>, <em class="sig-param">serial=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertificateAuthority resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the certificate authority.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.</p></li>
<li><p><strong>certificate_authority_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing algorithms and certificate subject information. Defined below.</p></li>
<li><p><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.</p></li>
<li><p><strong>certificate_signing_request</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>not_after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p></li>
<li><p><strong>not_before</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p></li>
<li><p><strong>permanent_deletion_time_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.</p></li>
<li><p><strong>revocation_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing revocation configuration. Defined below.</p></li>
<li><p><strong>serial</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the certificate authority.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the certificate authority. Defaults to <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">ROOT</span></code> and <code class="docutils literal notranslate"><span class="pre">SUBORDINATE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate_authority_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signingAlgorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the algorithm your private CA uses to sign certificate requests. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CertificateAuthorityConfiguration.html">ACM PCA Documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that contains X.500 distinguished name information. At least one nested attribute must be specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name (FQDN) associated with the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Two digit code that specifies the country in which the certificate subject located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distinguishedNameQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Disambiguating information for the certificate subject.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generationQualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">givenName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - First name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Concatenation that typically contains the first letter of the <code class="docutils literal notranslate"><span class="pre">given_name</span></code>, the first letter of the middle name if one exists, and the first letter of the <code class="docutils literal notranslate"><span class="pre">surname</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locality</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The locality (such as a city or town) in which the certificate subject is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Legal name of the organization with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudonym</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Typically a shortened version of a longer <code class="docutils literal notranslate"><span class="pre">given_name</span></code>. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - State in which the subject of the certificate is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">surname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Family name. In the US and the UK for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A title such as Mr. or Ms. which is pre-pended to the name to refer formally to the certificate subject.</p></li>
</ul>
</li>
</ul>
<p>The <strong>revocation_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">crlConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customCname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point. Use this value if you don’t want the name of your S3 bucket to be public.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of days until a certificate expires. Must be between 1 and 5000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the S3 bucket that contains the CRL. If you do not provide a value for the <code class="docutils literal notranslate"><span class="pre">custom_cname</span></code> argument, the name of your S3 bucket is placed into the CRL Distribution Points extension of the issued certificate. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.acmpca.CertificateAuthority.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acmpca.CertificateAuthority.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.CertificateAuthority.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.acmpca.</code><code class="sig-name descname">GetCertificateAuthorityResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">certificate_signing_request=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">not_after=None</em>, <em class="sig-param">not_before=None</em>, <em class="sig-param">revocation_configurations=None</em>, <em class="sig-param">serial=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificateAuthority.</p>
<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_chain">
<code class="sig-name descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_signing_request">
<code class="sig-name descname">certificate_signing_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.certificate_signing_request" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.not_after">
<code class="sig-name descname">not_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.not_after" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.not_before">
<code class="sig-name descname">not_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.not_before" title="Permalink to this definition">¶</a></dt>
<dd><p>Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.revocation_configurations">
<code class="sig-name descname">revocation_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.revocation_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing revocation configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">revocation_configuration.0.crl_configuration</span></code> - Nested attribute containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revocation_configuration.0.crl_configuration.0.custom_cname</span></code> - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revocation_configuration.0.crl_configuration.0.enabled</span></code> - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revocation_configuration.0.crl_configuration.0.expiration_in_days</span></code> - Number of days until a certificate expires.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revocation_configuration.0.crl_configuration.0.s3_bucket_name</span></code> - Name of the S3 bucket that contains the CRL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.serial">
<code class="sig-name descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acmpca.GetCertificateAuthorityResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acmpca.GetCertificateAuthorityResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the certificate authority.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.acmpca.get_certificate_authority">
<code class="sig-prename descclassname">pulumi_aws.acmpca.</code><code class="sig-name descname">get_certificate_authority</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">revocation_configurations=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acmpca.get_certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on a AWS Certificate Manager Private Certificate Authority (ACM PCA Certificate Authority).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>arn</strong> (<em>str</em>) – Amazon Resource Name (ARN) of the certificate authority.</p></li>
<li><p><strong>revocation_configurations</strong> (<em>list</em>) – Nested attribute containing revocation configuration.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `revocation_configuration.0.crl_configuration` - Nested attribute containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority.
* `revocation_configuration.0.crl_configuration.0.custom_cname` - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point.
* `revocation_configuration.0.crl_configuration.0.enabled` - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
* `revocation_configuration.0.crl_configuration.0.expiration_in_days` - Number of days until a certificate expires.
* `revocation_configuration.0.crl_configuration.0.s3_bucket_name` - Name of the S3 bucket that contains the CRL.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>tags</strong> (<em>dict</em>) – Specifies a key-value map of user-defined tags that are attached to the certificate authority.</p>
</dd>
</dl>
<p>The <strong>revocation_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">crlConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customCname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

</div>
