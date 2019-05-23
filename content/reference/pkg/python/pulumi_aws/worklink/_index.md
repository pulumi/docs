---
---

<div class="section" id="module-pulumi_aws.worklink">
<span id="worklink"></span><h1>worklink<a class="headerlink" href="#module-pulumi_aws.worklink" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.worklink.Fleet">
<em class="property">class </em><code class="descclassname">pulumi_aws.worklink.</code><code class="descname">Fleet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>audit_stream_arn=None</em>, <em>device_ca_certificate=None</em>, <em>display_name=None</em>, <em>identity_provider=None</em>, <em>name=None</em>, <em>network=None</em>, <em>optimize_for_end_user_location=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Fleet resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>audit_stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Amazon Kinesis data stream that receives the audit events.</li>
<li><strong>device_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the fleet.</li>
<li><strong>identity_provider</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow manage the company network configuration for the fleet. Fields documented below.</li>
<li><strong>optimize_for_end_user_location</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created WorkLink Fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.audit_stream_arn">
<code class="descname">audit_stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.audit_stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Amazon Kinesis data stream that receives the audit events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.company_code">
<code class="descname">company_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.company_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier used by users to sign in to the Amazon WorkLink app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.created_time">
<code class="descname">created_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.created_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time that the fleet was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.device_ca_certificate">
<code class="descname">device_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.device_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.identity_provider">
<code class="descname">identity_provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.identity_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.last_updated_time">
<code class="descname">last_updated_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.last_updated_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time that the fleet was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow manage the company network configuration for the fleet. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.optimize_for_end_user_location">
<code class="descname">optimize_for_end_user_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.optimize_for_end_user_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.Fleet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.Fleet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.worklink.</code><code class="descname">WebsiteCertificateAuthorityAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate=None</em>, <em>display_name=None</em>, <em>fleet_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a WebsiteCertificateAuthorityAssociation resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The root certificate of the Certificate Authority.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate name to display.</li>
<li><strong>fleet_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the fleet.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The root certificate of the Certificate Authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate name to display.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.fleet_arn">
<code class="descname">fleet_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.fleet_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.website_ca_id">
<code class="descname">website_ca_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.website_ca_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for the Certificate Authority.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
