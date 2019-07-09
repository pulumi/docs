---
---

<div class="section" id="ses">
<h1>ses<a class="headerlink" href="#ses" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ses"></span><dl class="class">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">ActiveReceiptRuleSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>rule_set_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to designate the active SES receipt rule set</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_active_receipt_rule_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_active_receipt_rule_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.rule_set_name">
<code class="descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfgurationSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">ConfgurationSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES configuration set resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_configuration_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_configuration_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.ConfgurationSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ConfgurationSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfgurationSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainDkim">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">DomainDkim</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain DKIM generation resource.</p>
<p>Domain ownership needs to be confirmed first using <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ses_domain_identity.html">ses_domain_identity Resource</a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_dkim.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_dkim.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainDkim.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Verified domain name to generate DKIM tokens for.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainDkim.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainDkim.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentity">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">DomainIdentity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain identity resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name to assign to SES</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentity.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the domain identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentity.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name to assign to SES</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentity.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentity.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentityVerification">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">DomainIdentityVerification</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a successful verification of an SES domain identity.</p>
<p>Most commonly, this resource is used together with <code class="docutils literal notranslate"><span class="pre">aws_route53_record</span></code> and
<code class="docutils literal notranslate"><span class="pre">aws_ses_domain_identity</span></code> to request an SES domain identity,
deploy the required DNS verification records, and wait for verification to complete.</p>
<blockquote>
<div><strong>WARNING:</strong> This resource implements a part of the verification workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the SES domain identity to verify.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity_verification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity_verification.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentityVerification.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the domain identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentityVerification.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the SES domain identity to verify.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentityVerification.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentityVerification.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EmailIdentity">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">EmailIdentity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>email=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES email identity resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to assign to SES</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_email_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_email_identity.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.EmailIdentity.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the email identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EmailIdentity.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to assign to SES</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EmailIdentity.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EmailIdentity.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EventDestination">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">EventDestination</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cloudwatch_destinations=None</em>, <em>configuration_set_name=None</em>, <em>enabled=None</em>, <em>kinesis_destination=None</em>, <em>matching_types=None</em>, <em>name=None</em>, <em>sns_destination=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES event destination</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cloudwatch_destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – CloudWatch destination for the events</li>
<li><strong>configuration_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the event destination will be enabled</li>
<li><strong>kinesis_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to a kinesis firehose destination</li>
<li><strong>matching_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of matching types. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;send&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reject&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;bounce&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;complaint&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;delivery&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;open&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;click&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;renderingFailure&quot;</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the event destination</li>
<li><strong>sns_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to an SNS Topic destination</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_event_destination.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_event_destination.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.cloudwatch_destinations">
<code class="descname">cloudwatch_destinations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.cloudwatch_destinations" title="Permalink to this definition">¶</a></dt>
<dd><p>CloudWatch destination for the events</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.configuration_set_name">
<code class="descname">configuration_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.configuration_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the event destination will be enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.kinesis_destination">
<code class="descname">kinesis_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.kinesis_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Send the events to a kinesis firehose destination</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.matching_types">
<code class="descname">matching_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.matching_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matching types. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;send&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reject&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;bounce&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;complaint&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;delivery&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;open&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;click&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;renderingFailure&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the event destination</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.sns_destination">
<code class="descname">sns_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.sns_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Send the events to an SNS Topic destination</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EventDestination.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EventDestination.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityNotificationTopic">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">IdentityNotificationTopic</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>identity=None</em>, <em>include_original_headers=None</em>, <em>notification_type=None</em>, <em>topic_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing SES Identity Notification Topics</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).</li>
<li><strong>include_original_headers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether SES should include original email headers in SNS notifications of this type. <em>false</em> by default.</li>
<li><strong>notification_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: <em>Bounce</em>, <em>Complaint</em> or <em>Delivery</em>.</li>
<li><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to “” (an empty string) to disable publishing.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_identity_notification_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_identity_notification_topic.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.include_original_headers">
<code class="descname">include_original_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.include_original_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether SES should include original email headers in SNS notifications of this type. <em>false</em> by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.notification_type">
<code class="descname">notification_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.notification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: <em>Bounce</em>, <em>Complaint</em> or <em>Delivery</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.topic_arn">
<code class="descname">topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to “” (an empty string) to disable publishing.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityNotificationTopic.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">IdentityPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>identity=None</em>, <em>name=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SES Identity Policy. More information about SES Sending Authorization Policies can be found in the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html">SES Developer Guide</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or Amazon Resource Name (ARN) of the SES Identity.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_identity_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_identity_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityPolicy.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or Amazon Resource Name (ARN) of the SES Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityPolicy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.MailFrom">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">MailFrom</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>behavior_on_mx_failure=None</em>, <em>domain=None</em>, <em>mail_from_domain=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain MAIL FROM resource.</p>
<blockquote>
<div><strong>NOTE:</strong> For the MAIL FROM domain to be fully usable, this resource should be paired with the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ses_domain_identity.html">aws_ses_domain_identity resource</a>. To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html">Amazon SES MAIL FROM documentation</a> for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>behavior_on_mx_failure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to <code class="docutils literal notranslate"><span class="pre">UseDefaultValue</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html">SES API documentation</a> for more information.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</li>
<li><strong>mail_from_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_mail_from.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_mail_from.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.behavior_on_mx_failure">
<code class="descname">behavior_on_mx_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.behavior_on_mx_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to <code class="docutils literal notranslate"><span class="pre">UseDefaultValue</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html">SES API documentation</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Verified domain name to generate DKIM tokens for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.mail_from_domain">
<code class="descname">mail_from_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.mail_from_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.MailFrom.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.MailFrom.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptFilter">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">ReceiptFilter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cidr=None</em>, <em>name=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt filter resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address or address range to filter, in CIDR notation</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the filter</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Block or Allow</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_filter.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_filter.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.cidr">
<code class="descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address or address range to filter, in CIDR notation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the filter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Block or Allow</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptFilter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptFilter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">ReceiptRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>add_header_actions=None</em>, <em>after=None</em>, <em>bounce_actions=None</em>, <em>enabled=None</em>, <em>lambda_actions=None</em>, <em>name=None</em>, <em>recipients=None</em>, <em>rule_set_name=None</em>, <em>s3_actions=None</em>, <em>scan_enabled=None</em>, <em>sns_actions=None</em>, <em>stop_actions=None</em>, <em>tls_policy=None</em>, <em>workmail_actions=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt rule resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>add_header_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Add Header Action blocks. Documented below.</li>
<li><strong>after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule to place this rule after</li>
<li><strong>bounce_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Bounce Action blocks. Documented below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the rule will be enabled</li>
<li><strong>lambda_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Lambda Action blocks. Documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</li>
<li><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of email addresses</li>
<li><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</li>
<li><strong>s3_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of S3 Action blocks. Documented below.</li>
<li><strong>scan_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, incoming emails will be scanned for spam and viruses</li>
<li><strong>sns_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SNS Action blocks. Documented below.</li>
<li><strong>stop_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Stop Action blocks. Documented below.</li>
<li><strong>tls_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Require or Optional</li>
<li><strong>workmail_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of WorkMail Action blocks. Documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.add_header_actions">
<code class="descname">add_header_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.add_header_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Add Header Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.after">
<code class="descname">after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.after" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule to place this rule after</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.bounce_actions">
<code class="descname">bounce_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.bounce_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Bounce Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the rule will be enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.lambda_actions">
<code class="descname">lambda_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.lambda_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Lambda Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.recipients">
<code class="descname">recipients</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.recipients" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of email addresses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.rule_set_name">
<code class="descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.s3_actions">
<code class="descname">s3_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.s3_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of S3 Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.scan_enabled">
<code class="descname">scan_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.scan_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, incoming emails will be scanned for spam and viruses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.sns_actions">
<code class="descname">sns_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.sns_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SNS Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.stop_actions">
<code class="descname">stop_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.stop_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Stop Action blocks. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.tls_policy">
<code class="descname">tls_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.tls_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Require or Optional</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.workmail_actions">
<code class="descname">workmail_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.workmail_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of WorkMail Action blocks. Documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRuleSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">ReceiptRuleSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>rule_set_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt rule set resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_rule_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_rule_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRuleSet.rule_set_name">
<code class="descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRuleSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRuleSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.Template">
<em class="property">class </em><code class="descclassname">pulumi_aws.ses.</code><code class="descname">Template</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>html=None</em>, <em>name=None</em>, <em>subject=None</em>, <em>text=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a SES template.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>html</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.</li>
<li><strong>subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject line of the email.</li>
<li><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_template.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ses.Template.html">
<code class="descname">html</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.html" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.subject">
<code class="descname">subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject line of the email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.text">
<code class="descname">text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.text" title="Permalink to this definition">¶</a></dt>
<dd><p>The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.Template.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.Template.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
