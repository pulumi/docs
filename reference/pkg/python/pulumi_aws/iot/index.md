<div class="section" id="module-pulumi_aws.iot">
<span id="iot"></span><h1>iot<a class="headerlink" href="#module-pulumi_aws.iot" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.iot.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>active=None</em>, <em>csr=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT certificate.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to indicate if the certificate should be active</li>
<li><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate signing request. Review the
[IoT API Reference Guide] (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html">http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html</a>)
for more information on creating a certificate from a certificate signing request (CSR).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.active">
<code class="descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to indicate if the certificate should be active</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created AWS IoT certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Certificate.csr">
<code class="descname">csr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Certificate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate signing request. Review the
[IoT API Reference Guide] (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html">http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html</a>)
for more information on creating a certificate from a certificate signing request (CSR).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.GetEndpointResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">GetEndpointResult</code><span class="sig-paren">(</span><em>endpoint_address=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_aws.iot.GetEndpointResult.endpoint_address">
<code class="descname">endpoint_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult.endpoint_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint based on <cite>endpoint_type</cite>:
* No <cite>endpoint_type</cite>: Either <cite>iot:Data</cite> or <cite>iot:Data-ATS</cite> [depending on region](<a class="reference external" href="https://aws.amazon.com/blogs/iot/aws-iot-core-ats-endpoints/">https://aws.amazon.com/blogs/iot/aws-iot-core-ats-endpoints/</a>)
* <cite>iot:CredentialsProvider</cite>: <cite>IDENTIFIER.credentials.iot.REGION.amazonaws.com</cite>
* <cite>iot:Data</cite>: <cite>IDENTIFIER.iot.REGION.amazonaws.com</cite>
* <cite>iot:Data-ATS</cite>: <cite>IDENTIFIER-ats.iot.REGION.amazonaws.com</cite>
* <cite>iot:Job</cite>: <cite>IDENTIFIER.jobs.iot.REGION.amazonaws.com</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.GetEndpointResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.GetEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.iot.Policy">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IoT policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html</a>) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.default_version_id">
<code class="descname">default_version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.default_version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Policy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Policy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html">http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html</a>) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.PolicyAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">PolicyAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>policy=None</em>, <em>target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an IoT policy attachment.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy to attach.</li>
<li><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity to which the policy is attached.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.iot.PolicyAttachment.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.PolicyAttachment.target">
<code class="descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity to which the policy is attached.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.PolicyAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.PolicyAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.PolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Thing">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">Thing</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>attributes=None</em>, <em>name=None</em>, <em>thing_type_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT Thing.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes of the thing.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing.</li>
<li><strong>thing_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thing type name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.default_client_id">
<code class="descname">default_client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.default_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default client ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.thing_type_name">
<code class="descname">thing_type_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.thing_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The thing type name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.Thing.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.Thing.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the thing record in the registry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.Thing.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.Thing.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.Thing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingPrincipalAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">ThingPrincipalAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>principal=None</em>, <em>thing=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches Principal to AWS IoT Thing.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS IoT Certificate ARN or Amazon Cognito Identity ID.</li>
<li><strong>thing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.principal">
<code class="descname">principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS IoT Certificate ARN or Amazon Cognito Identity ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.thing">
<code class="descname">thing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.thing" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingPrincipalAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingPrincipalAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingType">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">ThingType</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>deprecated=None</em>, <em>name=None</em>, <em>properties=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages an AWS IoT Thing Type.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>deprecated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the thing type is deprecated. If true, no new things could be associated with this type.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the thing type.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] properties</p>
<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created AWS IoT Thing Type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.deprecated">
<code class="descname">deprecated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.deprecated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the thing type is deprecated. If true, no new things could be associated with this type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.ThingType.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.ThingType.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the thing type.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.ThingType.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.ThingType.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.ThingType.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.TopicRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.iot.</code><code class="descname">TopicRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cloudwatch_alarm=None</em>, <em>cloudwatch_metric=None</em>, <em>description=None</em>, <em>dynamodb=None</em>, <em>elasticsearch=None</em>, <em>enabled=None</em>, <em>firehose=None</em>, <em>kinesis=None</em>, <em>lambda_=None</em>, <em>name=None</em>, <em>republish=None</em>, <em>s3=None</em>, <em>sns=None</em>, <em>sql=None</em>, <em>sql_version=None</em>, <em>sqs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TopicRule resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] cloudwatch_alarm
:param pulumi.Input[dict] cloudwatch_metric
:param pulumi.Input[str] description: The description of the rule.
:param pulumi.Input[dict] dynamodb
:param pulumi.Input[dict] elasticsearch
:param pulumi.Input[bool] enabled: Specifies whether the rule is enabled.
:param pulumi.Input[dict] firehose
:param pulumi.Input[dict] kinesis
:param pulumi.Input[dict] <a href="#id1"><span class="problematic" id="id2">lambda_</span></a>
:param pulumi.Input[str] name: The name of the rule.
:param pulumi.Input[dict] republish
:param pulumi.Input[dict] s3
:param pulumi.Input[dict] sns
:param pulumi.Input[str] sql: The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference">http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference</a>) in the AWS IoT Developer Guide.
:param pulumi.Input[str] sql_version: The version of the SQL rules engine to use when evaluating the rule.
:param pulumi.Input[dict] sqs</p>
<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the topic rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the rule is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.sql">
<code class="descname">sql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.sql" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (<a class="reference external" href="http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference">http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference</a>) in the AWS IoT Developer Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.iot.TopicRule.sql_version">
<code class="descname">sql_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.iot.TopicRule.sql_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the SQL rules engine to use when evaluating the rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.iot.TopicRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.TopicRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.TopicRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.iot.get_endpoint">
<code class="descclassname">pulumi_aws.iot.</code><code class="descname">get_endpoint</code><span class="sig-paren">(</span><em>endpoint_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.iot.get_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a unique endpoint specific to the AWS account making the call.</p>
</dd></dl>

</div>
