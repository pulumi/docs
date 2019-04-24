<div class="section" id="module-pulumi_aws.acm">
<span id="acm"></span><h1>acm<a class="headerlink" href="#module-pulumi_aws.acm" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.acm.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>domain_name=None</em>, <em>private_key=None</em>, <em>subject_alternative_names=None</em>, <em>tags=None</em>, <em>validation_method=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.</p>
<p>It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a <code class="docutils literal notranslate"><span class="pre">aws_acm_certificate_validation</span></code> resource for this.</p>
<p>Most commonly, this resource is used to together with <code class="docutils literal notranslate"><span class="pre">aws_route53_record</span></code> and
<code class="docutils literal notranslate"><span class="pre">aws_acm_certificate_validation</span></code> to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.</p>
<p>Domain validation through E-Mail is also supported but should be avoided as it requires a manual step outside
of Terraform.</p>
<p>It’s recommended to specify <code class="docutils literal notranslate"><span class="pre">create_before_destroy</span> <span class="pre">=</span> <span class="pre">true</span></code> in a [lifecycle][1] block to replace a certificate
which is currently in use (eg, by <code class="docutils literal notranslate"><span class="pre">aws_lb_listener</span></code>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted public key</li>
<li><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted chain</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A domain name for which the certificate should be issued</li>
<li><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate’s PEM-formatted private key</li>
<li><strong>subject_alternative_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of domains that should be SANs in the issued certificate</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>validation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which method to use for validation. <code class="docutils literal notranslate"><span class="pre">DNS</span></code> or <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code> are valid, <code class="docutils literal notranslate"><span class="pre">NONE</span></code> can be used for certificates that were imported into ACM and then into Terraform.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.acm.Certificate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.acm.Certificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the certificate</p>
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
<dd><p>Which method to use for validation. <code class="docutils literal notranslate"><span class="pre">DNS</span></code> or <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code> are valid, <code class="docutils literal notranslate"><span class="pre">NONE</span></code> can be used for certificates that were imported into ACM and then into Terraform.</p>
<ul class="simple">
<li>Importing an existing certificate</li>
</ul>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">CertificateValidation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_arn=None</em>, <em>validation_record_fqdns=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.CertificateValidation" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource represents a successful validation of an ACM certificate in concert
with other resources.</p>
<p>Most commonly, this resource is used together with <code class="docutils literal notranslate"><span class="pre">aws_route53_record</span></code> and
<code class="docutils literal notranslate"><span class="pre">aws_acm_certificate</span></code> to request a DNS validated certificate,
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
<em class="property">class </em><code class="descclassname">pulumi_aws.acm.</code><code class="descname">GetCertificateResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>domain=None</em>, <em>most_recent=None</em>, <em>statuses=None</em>, <em>types=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
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
<code class="descclassname">pulumi_aws.acm.</code><code class="descname">get_certificate</code><span class="sig-paren">(</span><em>domain=None</em>, <em>most_recent=None</em>, <em>statuses=None</em>, <em>types=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.acm.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a certificate in AWS Certificate
Manager (ACM), you can reference
it by domain without having to hard code the ARNs as input.</p>
</dd></dl>

</div>
