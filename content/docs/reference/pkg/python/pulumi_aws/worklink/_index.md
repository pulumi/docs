---
title: Module worklink
title_tag: Module worklink | Package pulumi_aws | Python SDK
linktitle: worklink
notitle: true
---

<div class="section" id="worklink">
<h1>worklink<a class="headerlink" href="#worklink" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.worklink"></span><dl class="class">
<dt id="pulumi_aws.worklink.Fleet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.worklink.</code><code class="sig-name descname">Fleet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audit_stream_arn=None</em>, <em class="sig-param">device_ca_certificate=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">identity_provider=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">optimize_for_end_user_location=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Fleet resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] audit_stream_arn: The ARN of the Amazon Kinesis data stream that receives the audit events.
:param pulumi.Input[str] device_ca_certificate: The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
:param pulumi.Input[str] display_name: The name of the fleet.
:param pulumi.Input[dict] identity_provider: Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.
:param pulumi.Input[str] name: A region-unique name for the AMI.
:param pulumi.Input[dict] network: Provide this to allow manage the company network configuration for the fleet. Fields documented below.
:param pulumi.Input[bool] optimize_for_end_user_location: The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<p>The <strong>identity_provider</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">samlMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SAML metadata document provided by the customer’s identity provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of identity provider.</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of security group IDs associated with access to the provided subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VPC ID with connectivity to associated websites.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the created WorkLink Fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.audit_stream_arn">
<code class="sig-name descname">audit_stream_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.audit_stream_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Amazon Kinesis data stream that receives the audit events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.company_code">
<code class="sig-name descname">company_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.company_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier used by users to sign in to the Amazon WorkLink app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.created_time">
<code class="sig-name descname">created_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.created_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time that the fleet was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.device_ca_certificate">
<code class="sig-name descname">device_ca_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.device_ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.identity_provider">
<code class="sig-name descname">identity_provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.identity_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">samlMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SAML metadata document provided by the customer’s identity provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of identity provider.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.last_updated_time">
<code class="sig-name descname">last_updated_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.last_updated_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time that the fleet was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A region-unique name for the AMI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow manage the company network configuration for the fleet. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of security group IDs associated with access to the provided subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The VPC ID with connectivity to associated websites.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.Fleet.optimize_for_end_user_location">
<code class="sig-name descname">optimize_for_end_user_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.Fleet.optimize_for_end_user_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.Fleet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">audit_stream_arn=None</em>, <em class="sig-param">company_code=None</em>, <em class="sig-param">created_time=None</em>, <em class="sig-param">device_ca_certificate=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">identity_provider=None</em>, <em class="sig-param">last_updated_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">optimize_for_end_user_location=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Fleet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the created WorkLink Fleet.</p></li>
<li><p><strong>audit_stream_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Amazon Kinesis data stream that receives the audit events.</p></li>
<li><p><strong>company_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier used by users to sign in to the Amazon WorkLink app.</p></li>
<li><p><strong>created_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time that the fleet was created.</p></li>
<li><p><strong>device_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the fleet.</p></li>
<li><p><strong>identity_provider</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.</p></li>
<li><p><strong>last_updated_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time that the fleet was last updated.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A region-unique name for the AMI.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow manage the company network configuration for the fleet. Fields documented below.</p></li>
<li><p><strong>optimize_for_end_user_location</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity_provider</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">samlMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SAML metadata document provided by the customer’s identity provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of identity provider.</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of security group IDs associated with access to the provided subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VPC ID with connectivity to associated websites.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.Fleet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.Fleet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.Fleet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.worklink.</code><code class="sig-name descname">WebsiteCertificateAuthorityAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fleet_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a WebsiteCertificateAuthorityAssociation resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] certificate: The root certificate of the Certificate Authority.
:param pulumi.Input[str] display_name: The certificate name to display.
:param pulumi.Input[str] fleet_arn: The ARN of the fleet.</p>
<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The root certificate of the Certificate Authority.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate name to display.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.fleet_arn">
<code class="sig-name descname">fleet_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.fleet_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the fleet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.website_ca_id">
<code class="sig-name descname">website_ca_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.website_ca_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for the Certificate Authority.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fleet_arn=None</em>, <em class="sig-param">website_ca_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebsiteCertificateAuthorityAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The root certificate of the Certificate Authority.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate name to display.</p></li>
<li><p><strong>fleet_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the fleet.</p></li>
<li><p><strong>website_ca_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for the Certificate Authority.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.worklink.WebsiteCertificateAuthorityAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
