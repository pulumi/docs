---
---

<div class="section" id="acm">
<h1>acm<a class="headerlink" href="#acm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.acm"></span><dl class="class">
<dt id="pulumi_aws.acm.AwaitableGetCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>domain=None</em>, <em>key_types=None</em>, <em>most_recent=None</em>, <em>statuses=None</em>, <em>types=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.acm.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_authority_arn=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>domain_name=None</em>, <em>options=None</em>, <em>private_key=None</em>, <em>subject_alternative_names=None</em>, <em>tags=None</em>, <em>validation_method=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.</p>
<p>It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a <code class="docutils literal notranslate"><span class="pre">acm.CertificateValidation</span></code> resource for this.</p>
<p>Most commonly, this resource is used to together with <code class="docutils literal notranslate"><span class="pre">route53.Record</span></code> and
<code class="docutils literal notranslate"><span class="pre">acm.CertificateValidation</span></code> to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.</p>
<p>Domain validation through E-Mail is also supported but should be avoided as it requires a manual step outside
of this provider.</p>
<p>It’s recommended to specify <code class="docutils literal notranslate"><span class="pre">create_before_destroy</span> <span class="pre">=</span> <span class="pre">true</span></code> in a [lifecycle][1] block to replace a certificate
which is currently in use (eg, by <code class="docutils literal notranslate"><span class="pre">lb.Listener</span></code>).</p>
<p>Supported nested arguments for the <code class="docutils literal notranslate"><span class="pre">options</span></code> configuration block:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">certificate_transparency_logging_preference</span></code> - (Optional) Specifies whether certificate details should be added to a certificate transparency log. Valid values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency">https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency</a> for more details.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_authority_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of an ACMPCA</li>
<li><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted public key</li>
<li><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted chain</li>
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
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A domain name for which the certificate should be issued</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted private key</li>
<li><strong>subject_alternative_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of domains that should be SANs in the issued certificate</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>validation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which method to use for validation. <code class="docutils literal notranslate"><span class="pre">DNS</span></code> or <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code> are valid, <code class="docutils literal notranslate"><span class="pre">NONE</span></code> can be used for certificates that were imported into ACM and then into state managed by this provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.certificate_authority_arn">
<code class="descname">certificate_authority_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.certificate_authority_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of an ACMPCA</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.certificate_body">
<code class="descname">certificate_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.certificate_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate’s PEM-formatted public key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate’s PEM-formatted chain</p>
<ul class="simple">
<li>Creating a private CA issued certificate</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A domain name for which the certificate should be issued</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.domain_validation_options">
<code class="descname">domain_validation_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.domain_validation_options" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if <code class="docutils literal notranslate"><span class="pre">DNS</span></code>-validation was used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate’s PEM-formatted private key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.subject_alternative_names">
<code class="descname">subject_alternative_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.subject_alternative_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of domains that should be SANs in the issued certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.validation_emails">
<code class="descname">validation_emails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.validation_emails" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of addresses that received a validation E-Mail. Only set if <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>-validation was used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.validation_method">
<code class="descname">validation_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.validation_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Which method to use for validation. <code class="docutils literal notranslate"><span class="pre">DNS</span></code> or <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code> are valid, <code class="docutils literal notranslate"><span class="pre">NONE</span></code> can be used for certificates that were imported into ACM and then into state managed by this provider.</p>
<ul class="simple">
<li>Importing an existing certificate</li>
</ul>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.acm.Certificate.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>certificate_authority_arn=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>domain_name=None</em>, <em>domain_validation_options=None</em>, <em>options=None</em>, <em>private_key=None</em>, <em>subject_alternative_names=None</em>, <em>tags=None</em>, <em>validation_emails=None</em>, <em>validation_method=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the certificate
:param pulumi.Input[str] certificate_authority_arn: ARN of an ACMPCA
:param pulumi.Input[str] certificate_body: The certificate’s PEM-formatted public key
:param pulumi.Input[str] certificate_chain: The certificate’s PEM-formatted chain</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A domain name for which the certificate should be issued</li>
<li><strong>domain_validation_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if <code class="docutils literal notranslate"><span class="pre">DNS</span></code>-validation was used.</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted private key</li>
<li><strong>subject_alternative_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of domains that should be SANs in the issued certificate</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>validation_emails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of addresses that received a validation E-Mail. Only set if <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>-validation was used.</li>
<li><strong>validation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which method to use for validation. <code class="docutils literal notranslate"><span class="pre">DNS</span></code> or <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code> are valid, <code class="docutils literal notranslate"><span class="pre">NONE</span></code> can be used for certificates that were imported into ACM and then into state managed by this provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.acm.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acm.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acm.CertificateValidation">
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">CertificateValidation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_arn=None</em>, <em>validation_record_fqdns=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource represents a successful validation of an ACM certificate in concert
with other resources.</p>
<p>Most commonly, this resource is used together with <code class="docutils literal notranslate"><span class="pre">route53.Record</span></code> and
<code class="docutils literal notranslate"><span class="pre">acm.Certificate</span></code> to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.</p>
<blockquote>
<div><strong>WARNING:</strong> This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the certificate that is being validated.</li>
<li><strong>validation_record_fqdns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.acm.CertificateValidation.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the certificate that is being validated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.CertificateValidation.validation_record_fqdns">
<code class="descname">validation_record_fqdns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation.validation_record_fqdns" title="Permalink to this definition">¶</a></dt>
<dd><p>List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.acm.CertificateValidation.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>certificate_arn=None</em>, <em>validation_record_fqdns=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertificateValidation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] certificate_arn: The ARN of the certificate that is being validated.
:param pulumi.Input[list] validation_record_fqdns: List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.acm.CertificateValidation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acm.CertificateValidation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.acm.GetCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">GetCertificateResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>domain=None</em>, <em>key_types=None</em>, <em>most_recent=None</em>, <em>statuses=None</em>, <em>types=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_aws.acm.GetCertificateResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.GetCertificateResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ARN of the found certificate, suitable for referencing in other resources that support ACM certificates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.acm.GetCertificateResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.acm.get_certificate">
<code class="descclassname">pulumi_aws.acm.</code><code class="descname">get_certificate</code><span class="sig-paren">(</span><em>domain=None</em>, <em>key_types=None</em>, <em>most_recent=None</em>, <em>statuses=None</em>, <em>types=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a certificate in AWS Certificate
Manager (ACM), you can reference
it by domain without having to hard code the ARNs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/acm_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/acm_certificate.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
