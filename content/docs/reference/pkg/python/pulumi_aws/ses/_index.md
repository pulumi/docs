---
title: Module ses
title_tag: Module ses | Package pulumi_aws | Python SDK
linktitle: ses
notitle: true
---

<div class="section" id="ses">
<h1>ses<a class="headerlink" href="#ses" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ses"></span><dl class="class">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ActiveReceiptRuleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rule_set_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to designate the active SES receipt rule set</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.rule_set_name">
<code class="sig-name descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rule_set_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActiveReceiptRuleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ActiveReceiptRuleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ActiveReceiptRuleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfgurationSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ConfgurationSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ConfgurationSet resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="method">
<dt id="pulumi_aws.ses.ConfgurationSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfgurationSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ConfgurationSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfgurationSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfgurationSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfigurationSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ConfigurationSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfigurationSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES configuration set resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.ConfigurationSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ConfigurationSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ConfigurationSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfigurationSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfigurationSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ConfigurationSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfigurationSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ConfigurationSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ConfigurationSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainDkim">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">DomainDkim</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain DKIM generation resource.</p>
<p>Domain ownership needs to be confirmed first using <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ses_domain_identity.html">ses_domain_identity Resource</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainDkim.dkim_tokens">
<code class="sig-name descname">dkim_tokens</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.dkim_tokens" title="Permalink to this definition">¶</a></dt>
<dd><p>DKIM tokens generated by SES.
These tokens should be used to create CNAME records used to verify SES Easy DKIM.
See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.
Find out more about verifying domains in Amazon SES
in the <a class="reference external" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html">AWS SES docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainDkim.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Verified domain name to generate DKIM tokens for.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainDkim.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dkim_tokens=None</em>, <em class="sig-param">domain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainDkim resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dkim_tokens</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>DKIM tokens generated by SES.
These tokens should be used to create CNAME records used to verify SES Easy DKIM.
See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.
Find out more about verifying domains in Amazon SES
in the <a class="reference external" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html">AWS SES docs</a>.</p>
</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainDkim.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainDkim.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainDkim.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">DomainIdentity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain identity resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name to assign to SES</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentity.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the domain identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentity.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name to assign to SES</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentity.verification_token">
<code class="sig-name descname">verification_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.verification_token" title="Permalink to this definition">¶</a></dt>
<dd><p>A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state “verification pending”
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the <a class="reference external" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html">AWS SES
docs</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">verification_token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the domain identity.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name to assign to SES</p></li>
<li><p><strong>verification_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state “verification pending”
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the <a class="reference external" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html">AWS SES
docs</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentityVerification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">DomainIdentityVerification</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a successful verification of an SES domain identity.</p>
<p>Most commonly, this resource is used together with <code class="docutils literal notranslate"><span class="pre">route53.Record</span></code> and
<code class="docutils literal notranslate"><span class="pre">ses.DomainIdentity</span></code> to request an SES domain identity,
deploy the required DNS verification records, and wait for verification to complete.</p>
<blockquote>
<div><p><strong>WARNING:</strong> This resource implements a part of the verification workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the SES domain identity to verify.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentityVerification.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the domain identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.DomainIdentityVerification.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the SES domain identity to verify.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentityVerification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">domain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainIdentityVerification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the domain identity.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the SES domain identity to verify.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.DomainIdentityVerification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.DomainIdentityVerification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.DomainIdentityVerification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EmailIdentity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">EmailIdentity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES email identity resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to assign to SES</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.EmailIdentity.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the email identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EmailIdentity.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to assign to SES</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EmailIdentity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">email=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EmailIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the email identity.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to assign to SES</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EmailIdentity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EmailIdentity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EmailIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EventDestination">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">EventDestination</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_destinations=None</em>, <em class="sig-param">configuration_set_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">kinesis_destination=None</em>, <em class="sig-param">matching_types=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sns_destination=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES event destination</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – CloudWatch destination for the events</p></li>
<li><p><strong>configuration_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the event destination will be enabled</p></li>
<li><p><strong>kinesis_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to a kinesis firehose destination</p></li>
<li><p><strong>matching_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of matching types. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;send&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reject&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;bounce&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;complaint&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;delivery&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;open&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;click&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;renderingFailure&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the event destination</p></li>
<li><p><strong>sns_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to an SNS Topic destination</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cloudwatch_destinations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for the event</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the dimension</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source for the value. It can be either <code class="docutils literal notranslate"><span class="pre">&quot;messageTag&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;emailHeader&quot;</span></code></p></li>
</ul>
<p>The <strong>kinesis_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the role that has permissions to access the Kinesis Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stream_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream</p></li>
</ul>
<p>The <strong>sns_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the SNS topic</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.cloudwatch_destinations">
<code class="sig-name descname">cloudwatch_destinations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.cloudwatch_destinations" title="Permalink to this definition">¶</a></dt>
<dd><p>CloudWatch destination for the events</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for the event</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name for the dimension</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source for the value. It can be either <code class="docutils literal notranslate"><span class="pre">&quot;messageTag&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;emailHeader&quot;</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.configuration_set_name">
<code class="sig-name descname">configuration_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.configuration_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the event destination will be enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.kinesis_destination">
<code class="sig-name descname">kinesis_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.kinesis_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Send the events to a kinesis firehose destination</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the role that has permissions to access the Kinesis Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stream_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Stream</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.matching_types">
<code class="sig-name descname">matching_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.matching_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matching types. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;send&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reject&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;bounce&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;complaint&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;delivery&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;open&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;click&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;renderingFailure&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the event destination</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.EventDestination.sns_destination">
<code class="sig-name descname">sns_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.EventDestination.sns_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Send the events to an SNS Topic destination</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the SNS topic</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EventDestination.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_destinations=None</em>, <em class="sig-param">configuration_set_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">kinesis_destination=None</em>, <em class="sig-param">matching_types=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sns_destination=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventDestination resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_destinations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – CloudWatch destination for the events</p></li>
<li><p><strong>configuration_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration set</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the event destination will be enabled</p></li>
<li><p><strong>kinesis_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to a kinesis firehose destination</p></li>
<li><p><strong>matching_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of matching types. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;send&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reject&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;bounce&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;complaint&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;delivery&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;open&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;click&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;renderingFailure&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the event destination</p></li>
<li><p><strong>sns_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Send the events to an SNS Topic destination</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cloudwatch_destinations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for the event</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the dimension</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source for the value. It can be either <code class="docutils literal notranslate"><span class="pre">&quot;messageTag&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;emailHeader&quot;</span></code></p></li>
</ul>
<p>The <strong>kinesis_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the role that has permissions to access the Kinesis Stream</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stream_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream</p></li>
</ul>
<p>The <strong>sns_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the SNS topic</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.EventDestination.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.EventDestination.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.EventDestination.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityNotificationTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">IdentityNotificationTopic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">include_original_headers=None</em>, <em class="sig-param">notification_type=None</em>, <em class="sig-param">topic_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing SES Identity Notification Topics</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).</p></li>
<li><p><strong>include_original_headers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether SES should include original email headers in SNS notifications of this type. <em>false</em> by default.</p></li>
<li><p><strong>notification_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: <em>Bounce</em>, <em>Complaint</em> or <em>Delivery</em>.</p></li>
<li><p><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to “” (an empty string) to disable publishing.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.include_original_headers">
<code class="sig-name descname">include_original_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.include_original_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether SES should include original email headers in SNS notifications of this type. <em>false</em> by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.notification_type">
<code class="sig-name descname">notification_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.notification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: <em>Bounce</em>, <em>Complaint</em> or <em>Delivery</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.topic_arn">
<code class="sig-name descname">topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to “” (an empty string) to disable publishing.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">include_original_headers=None</em>, <em class="sig-param">notification_type=None</em>, <em class="sig-param">topic_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityNotificationTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).</p></li>
<li><p><strong>include_original_headers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether SES should include original email headers in SNS notifications of this type. <em>false</em> by default.</p></li>
<li><p><strong>notification_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: <em>Bounce</em>, <em>Complaint</em> or <em>Delivery</em>.</p></li>
<li><p><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to “” (an empty string) to disable publishing.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityNotificationTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityNotificationTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityNotificationTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">IdentityPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SES Identity Policy. More information about SES Sending Authorization Policies can be found in the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html">SES Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or Amazon Resource Name (ARN) of the SES Identity.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityPolicy.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or Amazon Resource Name (ARN) of the SES Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.IdentityPolicy.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON string of the policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or Amazon Resource Name (ARN) of the SES Identity.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON string of the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.IdentityPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.IdentityPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.IdentityPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.MailFrom">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">MailFrom</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">behavior_on_mx_failure=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">mail_from_domain=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES domain MAIL FROM resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> For the MAIL FROM domain to be fully usable, this resource should be paired with the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ses_domain_identity.html">ses.DomainIdentity resource</a>. To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html">Amazon SES MAIL FROM documentation</a> for more information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>behavior_on_mx_failure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to <code class="docutils literal notranslate"><span class="pre">UseDefaultValue</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html">SES API documentation</a> for more information.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</p></li>
<li><p><strong>mail_from_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.behavior_on_mx_failure">
<code class="sig-name descname">behavior_on_mx_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.behavior_on_mx_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to <code class="docutils literal notranslate"><span class="pre">UseDefaultValue</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html">SES API documentation</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Verified domain name to generate DKIM tokens for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.MailFrom.mail_from_domain">
<code class="sig-name descname">mail_from_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.MailFrom.mail_from_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.MailFrom.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">behavior_on_mx_failure=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">mail_from_domain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MailFrom resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>behavior_on_mx_failure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to <code class="docutils literal notranslate"><span class="pre">UseDefaultValue</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html">SES API documentation</a> for more information.</p>
</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Verified domain name to generate DKIM tokens for.</p></li>
<li><p><strong>mail_from_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.MailFrom.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.MailFrom.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.MailFrom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptFilter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ReceiptFilter</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt filter resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address or address range to filter, in CIDR notation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the filter</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Block or Allow</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.cidr">
<code class="sig-name descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address or address range to filter, in CIDR notation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the filter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptFilter.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Block or Allow</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptFilter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReceiptFilter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address or address range to filter, in CIDR notation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the filter</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Block or Allow</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptFilter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptFilter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptFilter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ReceiptRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_header_actions=None</em>, <em class="sig-param">after=None</em>, <em class="sig-param">bounce_actions=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">lambda_actions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">rule_set_name=None</em>, <em class="sig-param">s3_actions=None</em>, <em class="sig-param">scan_enabled=None</em>, <em class="sig-param">sns_actions=None</em>, <em class="sig-param">stop_actions=None</em>, <em class="sig-param">tls_policy=None</em>, <em class="sig-param">workmail_actions=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt rule resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_header_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Add Header Action blocks. Documented below.</p></li>
<li><p><strong>after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule to place this rule after</p></li>
<li><p><strong>bounce_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Bounce Action blocks. Documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the rule will be enabled</p></li>
<li><p><strong>lambda_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Lambda Action blocks. Documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of email addresses</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
<li><p><strong>s3_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of S3 Action blocks. Documented below.</p></li>
<li><p><strong>scan_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, incoming emails will be scanned for spam and viruses</p></li>
<li><p><strong>sns_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SNS Action blocks. Documented below.</p></li>
<li><p><strong>stop_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Stop Action blocks. Documented below.</p></li>
<li><p><strong>tls_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Require or Optional</p></li>
<li><p><strong>workmail_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of WorkMail Action blocks. Documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>add_header_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
</ul>
<p>The <strong>bounce_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message to send</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sender</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of the sender</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpReplyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RFC 5321 SMTP reply code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RFC 3463 SMTP enhanced status code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>lambda_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function to invoke</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invocationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Event or RequestResponse</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>s3_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the KMS key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">objectKeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key prefix of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>sns_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>stop_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope to apply</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>workmail_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">organizationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the WorkMail organization</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.add_header_actions">
<code class="sig-name descname">add_header_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.add_header_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Add Header Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.after">
<code class="sig-name descname">after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.after" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule to place this rule after</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.bounce_actions">
<code class="sig-name descname">bounce_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.bounce_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Bounce Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The message to send</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sender</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address of the sender</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpReplyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RFC 5321 SMTP reply code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The RFC 3463 SMTP enhanced status code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the rule will be enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.lambda_actions">
<code class="sig-name descname">lambda_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.lambda_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Lambda Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Lambda function to invoke</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invocationType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Event or RequestResponse</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.recipients">
<code class="sig-name descname">recipients</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.recipients" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of email addresses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.rule_set_name">
<code class="sig-name descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.s3_actions">
<code class="sig-name descname">s3_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.s3_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of S3 Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the KMS key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">objectKeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key prefix of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.scan_enabled">
<code class="sig-name descname">scan_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.scan_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, incoming emails will be scanned for spam and viruses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.sns_actions">
<code class="sig-name descname">sns_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.sns_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SNS Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.stop_actions">
<code class="sig-name descname">stop_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.stop_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Stop Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scope to apply</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.tls_policy">
<code class="sig-name descname">tls_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.tls_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Require or Optional</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRule.workmail_actions">
<code class="sig-name descname">workmail_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.workmail_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of WorkMail Action blocks. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">organizationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the WorkMail organization</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_header_actions=None</em>, <em class="sig-param">after=None</em>, <em class="sig-param">bounce_actions=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">lambda_actions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">rule_set_name=None</em>, <em class="sig-param">s3_actions=None</em>, <em class="sig-param">scan_enabled=None</em>, <em class="sig-param">sns_actions=None</em>, <em class="sig-param">stop_actions=None</em>, <em class="sig-param">tls_policy=None</em>, <em class="sig-param">workmail_actions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReceiptRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_header_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Add Header Action blocks. Documented below.</p></li>
<li><p><strong>after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule to place this rule after</p></li>
<li><p><strong>bounce_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Bounce Action blocks. Documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the rule will be enabled</p></li>
<li><p><strong>lambda_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Lambda Action blocks. Documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of email addresses</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
<li><p><strong>s3_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of S3 Action blocks. Documented below.</p></li>
<li><p><strong>scan_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, incoming emails will be scanned for spam and viruses</p></li>
<li><p><strong>sns_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SNS Action blocks. Documented below.</p></li>
<li><p><strong>stop_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Stop Action blocks. Documented below.</p></li>
<li><p><strong>tls_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Require or Optional</p></li>
<li><p><strong>workmail_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of WorkMail Action blocks. Documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>add_header_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header to add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
</ul>
<p>The <strong>bounce_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message to send</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sender</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of the sender</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpReplyCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RFC 5321 SMTP reply code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The RFC 3463 SMTP enhanced status code</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>lambda_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function to invoke</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invocationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Event or RequestResponse</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>s3_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the KMS key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">objectKeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key prefix of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>sns_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>stop_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope to apply</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
<p>The <strong>workmail_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">organizationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the WorkMail organization</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The position of the action in the receipt rule</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an SNS topic to notify</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRuleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">ReceiptRuleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rule_set_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SES receipt rule set resource</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.ReceiptRuleSet.rule_set_name">
<code class="sig-name descname">rule_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.rule_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule set</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRuleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rule_set_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReceiptRuleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rule_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule set</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.ReceiptRuleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.ReceiptRuleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.ReceiptRuleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.Template">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ses.</code><code class="sig-name descname">Template</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">html=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">subject=None</em>, <em class="sig-param">text=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a SES template.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>html</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.</p></li>
<li><p><strong>subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject line of the email.</p></li>
<li><p><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.ses.Template.html">
<code class="sig-name descname">html</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.html" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.subject">
<code class="sig-name descname">subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject line of the email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ses.Template.text">
<code class="sig-name descname">text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ses.Template.text" title="Permalink to this definition">¶</a></dt>
<dd><p>The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.Template.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">html=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">subject=None</em>, <em class="sig-param">text=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Template resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>html</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.</p></li>
<li><p><strong>subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject line of the email.</p></li>
<li><p><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ses.Template.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ses.Template.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ses.Template.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
