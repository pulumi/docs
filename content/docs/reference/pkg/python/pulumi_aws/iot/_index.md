---
title: Module iot
---

<div class="section" id="iot">
<h1>iot<a class="headerlink" href="#iot" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.iot"></span><dl class="class">
<dt id="pulumi_aws.iot.AwaitableGetEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">AwaitableGetEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_address=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.AwaitableGetEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.iot.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to indicate if the certificate should be active</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate signing request. Review
<a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html">CreateCertificateFromCsr</a>
for more information on generating a certificate from a certificate signing request (CSR).
If none is specified both the certificate and keys will be generated, review <a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html">CreateKeysAndCertificate</a>
for more information on generating keys and a certificate.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.active">
<code class="sig-name descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to indicate if the certificate should be active</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.certificate_pem">
<code class="sig-name descname">certificate_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.certificate_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate data, in PEM format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.csr">
<code class="sig-name descname">csr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate signing request. Review
<a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html">CreateCertificateFromCsr</a>
for more information on generating a certificate from a certificate signing request (CSR).
If none is specified both the certificate and keys will be generated, review <a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html">CreateKeysAndCertificate</a>
for more information on generating keys and a certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>When no CSR is provided, the private key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>When no CSR is provided, the public key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate_pem=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">public_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active
:param pulumi.Input[str] arn: The ARN of the created certificate.
:param pulumi.Input[str] certificate_pem: The certificate data, in PEM format.
:param pulumi.Input[str] csr: The certificate signing request. Review</p>
<blockquote>
<div><p><a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html">CreateCertificateFromCsr</a>
for more information on generating a certificate from a certificate signing request (CSR).
If none is specified both the certificate and keys will be generated, review <a class="reference external" href="https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html">CreateKeysAndCertificate</a>
for more information on generating keys and a certificate.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When no CSR is provided, the private key.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When no CSR is provided, the public key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.GetEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">GetEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_address=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_aws.iot.GetEndpointResult.endpoint_address">
<code class="sig-name descname">endpoint_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult.endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint based on <code class="docutils literal notranslate"><span class="pre">endpoint_type</span></code>:</p>
<ul class="simple">
<li><p>No <cite>endpoint_type</cite>: Either <cite>iot:Data``or`</cite>iot:Data-ATS` <a class="reference external" href="https://aws.amazon.com/blogs/iot/aws-iot-core-ats-endpoints/">depending on region</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iot:CredentialsProvider</span></code>: <code class="docutils literal notranslate"><span class="pre">IDENTIFIER.credentials.iot.REGION.amazonaws.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iot:Data</span></code>: <code class="docutils literal notranslate"><span class="pre">IDENTIFIER.iot.REGION.amazonaws.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iot:Data-ATS</span></code>: <code class="docutils literal notranslate"><span class="pre">IDENTIFIER-ats.iot.REGION.amazonaws.com</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iot:Job</span></code>: <code class="docutils literal notranslate"><span class="pre">IDENTIFIER.jobs.iot.REGION.amazonaws.com</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.GetEndpointResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iot.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IoT policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string. Use the <a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">IoT Developer Guide</a> for more information on IoT Policies.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.default_version_id">
<code class="sig-name descname">default_version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.default_version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. Use the <a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">IoT Developer Guide</a> for more information on IoT Policies.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">default_version_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN assigned by AWS to this policy.
:param pulumi.Input[str] default_version_id: The default version of this policy.
:param pulumi.Input[str] name: The name of the policy.
:param pulumi.Input[str] policy: The policy document. This is a JSON formatted string. Use the <a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">IoT Developer Guide</a> for more information on IoT Policies.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.PolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">PolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IoT policy attachment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy to attach.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity to which the policy is attached.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.PolicyAttachment.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.PolicyAttachment.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity to which the policy is attached.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.PolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] policy: The name of the policy to attach.
:param pulumi.Input[str] target: The identity to which the policy is attached.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_policy_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.PolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.PolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.RoleAlias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">RoleAlias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">credential_duration=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.RoleAlias" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IoT role alias.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role alias.</p></li>
<li><p><strong>credential_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity of the role to which the alias refers.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_role_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_role_alias.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.RoleAlias.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.RoleAlias.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to this role alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.RoleAlias.credential_duration">
<code class="sig-name descname">credential_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.credential_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.RoleAlias.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity of the role to which the alias refers.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.RoleAlias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alias=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">credential_duration=None</em>, <em class="sig-param">role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RoleAlias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] alias: The name of the role alias.
:param pulumi.Input[str] arn: The ARN assigned by AWS to this role alias.
:param pulumi.Input[float] credential_duration: The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).
:param pulumi.Input[str] role_arn: The identity of the role to which the alias refers.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_role_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_role_alias.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.RoleAlias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.RoleAlias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.RoleAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Thing">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">Thing</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">thing_type_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT Thing.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes of the thing.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing.</p></li>
<li><p><strong>thing_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thing type name.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.attributes">
<code class="sig-name descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.default_client_id">
<code class="sig-name descname">default_client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.default_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default client ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.thing_type_name">
<code class="sig-name descname">thing_type_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.thing_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The thing type name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the thing record in the registry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Thing.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">default_client_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">thing_type_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Thing resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the thing.
:param pulumi.Input[dict] attributes: Map of attributes of the thing.
:param pulumi.Input[str] default_client_id: The default client ID.
:param pulumi.Input[str] name: The name of the thing.
:param pulumi.Input[str] thing_type_name: The thing type name.
:param pulumi.Input[float] version: The current version of the thing record in the registry.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Thing.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Thing.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingPrincipalAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">ThingPrincipalAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">principal=None</em>, <em class="sig-param">thing=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches Principal to AWS IoT Thing.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS IoT Certificate ARN or Amazon Cognito Identity ID.</p></li>
<li><p><strong>thing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_principal_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_principal_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.principal">
<code class="sig-name descname">principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS IoT Certificate ARN or Amazon Cognito Identity ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.thing">
<code class="sig-name descname">thing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.thing" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">principal=None</em>, <em class="sig-param">thing=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThingPrincipalAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] principal: The AWS IoT Certificate ARN or Amazon Cognito Identity ID.
:param pulumi.Input[str] thing: The name of the thing.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_principal_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_principal_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingType">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">ThingType</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deprecated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT Thing Type.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deprecated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the thing type is deprecated. If true, no new things could be associated with this type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_type.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_type.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created AWS IoT Thing Type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.deprecated">
<code class="sig-name descname">deprecated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.deprecated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the thing type is deprecated. If true, no new things could be associated with this type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing type.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingType.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">deprecated=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThingType resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the created AWS IoT Thing Type.
:param pulumi.Input[bool] deprecated: Whether the thing type is deprecated. If true, no new things could be associated with this type.
:param pulumi.Input[str] name: The name of the thing type.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_type.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing_type.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingType.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingType.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.TopicRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">TopicRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_alarm=None</em>, <em class="sig-param">cloudwatch_metric=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">firehose=None</em>, <em class="sig-param">kinesis=None</em>, <em class="sig-param">lambda_=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">republish=None</em>, <em class="sig-param">s3=None</em>, <em class="sig-param">sns=None</em>, <em class="sig-param">sql=None</em>, <em class="sig-param">sql_version=None</em>, <em class="sig-param">sqs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TopicRule resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the rule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule.</p></li>
<li><p><strong>sql</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference">http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference</a>) in the AWS IoT Developer Guide.</p></li>
<li><p><strong>sql_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the SQL rules engine to use when evaluating the rule.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_topic_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_topic_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the topic rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the rule is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.sql">
<code class="sig-name descname">sql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.sql" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference">http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference</a>) in the AWS IoT Developer Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.sql_version">
<code class="sig-name descname">sql_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.sql_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the SQL rules engine to use when evaluating the rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.TopicRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cloudwatch_alarm=None</em>, <em class="sig-param">cloudwatch_metric=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">firehose=None</em>, <em class="sig-param">kinesis=None</em>, <em class="sig-param">lambda_=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">republish=None</em>, <em class="sig-param">s3=None</em>, <em class="sig-param">sns=None</em>, <em class="sig-param">sql=None</em>, <em class="sig-param">sql_version=None</em>, <em class="sig-param">sqs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN of the topic rule
:param pulumi.Input[str] description: The description of the rule.
:param pulumi.Input[bool] enabled: Specifies whether the rule is enabled.
:param pulumi.Input[str] name: The name of the rule.
:param pulumi.Input[str] sql: The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference">http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference</a>) in the AWS IoT Developer Guide.
:param pulumi.Input[str] sql_version: The version of the SQL rules engine to use when evaluating the rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_topic_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_topic_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.TopicRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.TopicRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.get_endpoint">
<code class="sig-prename descclassname">pulumi_aws.iot.</code><code class="sig-name descname">get_endpoint</code><span class="sig-paren">(</span><em class="sig-param">endpoint_type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.get_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a unique endpoint specific to the AWS account making the call.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iot_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iot_endpoint.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
