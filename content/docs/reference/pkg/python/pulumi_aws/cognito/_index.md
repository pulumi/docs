---
title: Module cognito
title_tag: Module cognito | Package pulumi_aws | Python SDK
linktitle: cognito
notitle: true
---

<div class="section" id="cognito">
<h1>cognito<a class="headerlink" href="#cognito" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cognito"></span><dl class="class">
<dt id="pulumi_aws.cognito.AwaitableGetUserPoolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">AwaitableGetUserPoolsResult</code><span class="sig-paren">(</span><em class="sig-param">arns=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.AwaitableGetUserPoolsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.cognito.GetUserPoolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">GetUserPoolsResult</code><span class="sig-paren">(</span><em class="sig-param">arns=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUserPools.</p>
<dl class="attribute">
<dt id="pulumi_aws.cognito.GetUserPoolsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cognito user pool ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.GetUserPoolsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cognito.IdentityPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">IdentityPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_unauthenticated_identities=None</em>, <em class="sig-param">cognito_identity_providers=None</em>, <em class="sig-param">developer_provider_name=None</em>, <em class="sig-param">identity_pool_name=None</em>, <em class="sig-param">openid_connect_provider_arns=None</em>, <em class="sig-param">saml_provider_arns=None</em>, <em class="sig-param">supported_login_providers=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Cognito Identity Pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_unauthenticated_identities</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the identity pool supports unauthenticated logins or not.</p></li>
<li><p><strong>cognito_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Cognito Identity user pools and their client IDs.</p></li>
<li><p><strong>developer_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “domain” by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.</p></li>
<li><p><strong>identity_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cognito Identity Pool name.</p></li>
<li><p><strong>openid_connect_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of OpendID Connect provider ARNs.</p></li>
<li><p><strong>saml_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.</p></li>
<li><p><strong>supported_login_providers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-Value pairs mapping provider names to provider app IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Identity Pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cognito_identity_providers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client ID for the Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The provider name for an Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideTokenCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether server-side token validation is enabled for the identity provider’s token or not.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.allow_unauthenticated_identities">
<code class="sig-name descname">allow_unauthenticated_identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.allow_unauthenticated_identities" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the identity pool supports unauthenticated logins or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the identity pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.cognito_identity_providers">
<code class="sig-name descname">cognito_identity_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.cognito_identity_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Amazon Cognito Identity user pools and their client IDs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client ID for the Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The provider name for an Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideTokenCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether server-side token validation is enabled for the identity provider’s token or not.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.developer_provider_name">
<code class="sig-name descname">developer_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.developer_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The “domain” by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.identity_pool_name">
<code class="sig-name descname">identity_pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.identity_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cognito Identity Pool name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.openid_connect_provider_arns">
<code class="sig-name descname">openid_connect_provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.openid_connect_provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OpendID Connect provider ARNs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.saml_provider_arns">
<code class="sig-name descname">saml_provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.saml_provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.supported_login_providers">
<code class="sig-name descname">supported_login_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.supported_login_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-Value pairs mapping provider names to provider app IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Identity Pool.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_unauthenticated_identities=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cognito_identity_providers=None</em>, <em class="sig-param">developer_provider_name=None</em>, <em class="sig-param">identity_pool_name=None</em>, <em class="sig-param">openid_connect_provider_arns=None</em>, <em class="sig-param">saml_provider_arns=None</em>, <em class="sig-param">supported_login_providers=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_unauthenticated_identities</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the identity pool supports unauthenticated logins or not.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the identity pool.</p></li>
<li><p><strong>cognito_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Cognito Identity user pools and their client IDs.</p></li>
<li><p><strong>developer_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “domain” by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.</p></li>
<li><p><strong>identity_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cognito Identity Pool name.</p></li>
<li><p><strong>openid_connect_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of OpendID Connect provider ARNs.</p></li>
<li><p><strong>saml_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.</p></li>
<li><p><strong>supported_login_providers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-Value pairs mapping provider names to provider app IDs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Identity Pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cognito_identity_providers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client ID for the Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The provider name for an Amazon Cognito Identity User Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideTokenCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether server-side token validation is enabled for the identity provider’s token or not.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">IdentityPoolRoleAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity_pool_id=None</em>, <em class="sig-param">role_mappings=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Cognito Identity Pool Roles Attachment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identity pool ID in the format REGION:GUID.</p></li>
<li><p><strong>role_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of Role Mapping.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of roles associated with this pool. For a given role, the key will be either “authenticated” or “unauthenticated” and the value will be the Role ARN.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>role_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ambiguousRoleResolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. <code class="docutils literal notranslate"><span class="pre">Required</span></code> if you specify Token or Rules as the Type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string identifying the identity provider, for example, “graph.facebook.com” or “cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">claim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The claim name that must be present in the token, for example, “isAdmin” or “paid”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match condition that specifies how closely the claim value in the IdP token must match Value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A brief string that the claim must match, for example, “paid” or “yes”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role mapping type.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.identity_pool_id">
<code class="sig-name descname">identity_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.identity_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An identity pool ID in the format REGION:GUID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.role_mappings">
<code class="sig-name descname">role_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.role_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of Role Mapping.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ambiguousRoleResolution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. <code class="docutils literal notranslate"><span class="pre">Required</span></code> if you specify Token or Rules as the Type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string identifying the identity provider, for example, “graph.facebook.com” or “cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">claim</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The claim name that must be present in the token, for example, “isAdmin” or “paid”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The match condition that specifies how closely the claim value in the IdP token must match Value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A brief string that the claim must match, for example, “paid” or “yes”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role mapping type.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of roles associated with this pool. For a given role, the key will be either “authenticated” or “unauthenticated” and the value will be the Role ARN.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity_pool_id=None</em>, <em class="sig-param">role_mappings=None</em>, <em class="sig-param">roles=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityPoolRoleAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identity pool ID in the format REGION:GUID.</p></li>
<li><p><strong>role_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of Role Mapping.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of roles associated with this pool. For a given role, the key will be either “authenticated” or “unauthenticated” and the value will be the Role ARN.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>role_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ambiguousRoleResolution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. <code class="docutils literal notranslate"><span class="pre">Required</span></code> if you specify Token or Rules as the Type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string identifying the identity provider, for example, “graph.facebook.com” or “cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">claim</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The claim name that must be present in the token, for example, “isAdmin” or “paid”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match condition that specifies how closely the claim value in the IdP token must match Value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A brief string that the claim must match, for example, “paid” or “yes”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role mapping type.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthenticated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">IdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attribute_mapping=None</em>, <em class="sig-param">idp_identifiers=None</em>, <em class="sig-param">provider_details=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_type=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Identity Provider resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_mapping</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of attribute mapping of user pool attributes. <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping">AttributeMapping in AWS API documentation</a></p></li>
<li><p><strong>idp_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of identity providers.</p></li>
<li><p><strong>provider_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of identity details, such as access token</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider name</p></li>
<li><p><strong>provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type.  <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType">See AWS API for valid values</a></p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool id</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.attribute_mapping">
<code class="sig-name descname">attribute_mapping</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.attribute_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of attribute mapping of user pool attributes. <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping">AttributeMapping in AWS API documentation</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.idp_identifiers">
<code class="sig-name descname">idp_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.idp_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_details">
<code class="sig-name descname">provider_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of identity details, such as access token</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_type">
<code class="sig-name descname">provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type.  <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType">See AWS API for valid values</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.user_pool_id">
<code class="sig-name descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool id</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attribute_mapping=None</em>, <em class="sig-param">idp_identifiers=None</em>, <em class="sig-param">provider_details=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_type=None</em>, <em class="sig-param">user_pool_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_mapping</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The map of attribute mapping of user pool attributes. <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping">AttributeMapping in AWS API documentation</a></p>
</p></li>
<li><p><strong>idp_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of identity providers.</p></li>
<li><p><strong>provider_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of identity details, such as access token</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider name</p></li>
<li><p><strong>provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The provider type.  <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType">See AWS API for valid values</a></p>
</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool id</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.ResourceServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">ResourceServer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito Resource Server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identifier for the resource server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the resource server.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Authorization Scope.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scopes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scopeDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope name.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.identifier">
<code class="sig-name descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>An identifier for the resource server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the resource server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Authorization Scope.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scopeDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scope description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scope name.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.scope_identifiers">
<code class="sig-name descname">scope_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.scope_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all scopes configured for this resource server in the format identifier/scope_name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.ResourceServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">scope_identifiers=None</em>, <em class="sig-param">user_pool_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identifier for the resource server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the resource server.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Authorization Scope.</p></li>
<li><p><strong>scope_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of all scopes configured for this resource server in the format identifier/scope_name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scopes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scopeDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope name.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.ResourceServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.ResourceServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">UserGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">precedence=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Group resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The precedence of the user group.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be associated with the user group.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.precedence">
<code class="sig-name descname">precedence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The precedence of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role to be associated with the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.user_pool_id">
<code class="sig-name descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">precedence=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">user_pool_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The precedence of the user group.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be associated with the user group.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">UserPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_create_user_config=None</em>, <em class="sig-param">alias_attributes=None</em>, <em class="sig-param">auto_verified_attributes=None</em>, <em class="sig-param">device_configuration=None</em>, <em class="sig-param">email_configuration=None</em>, <em class="sig-param">email_verification_message=None</em>, <em class="sig-param">email_verification_subject=None</em>, <em class="sig-param">lambda_config=None</em>, <em class="sig-param">mfa_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_policy=None</em>, <em class="sig-param">schemas=None</em>, <em class="sig-param">sms_authentication_message=None</em>, <em class="sig-param">sms_configuration=None</em>, <em class="sig-param">sms_verification_message=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_pool_add_ons=None</em>, <em class="sig-param">username_attributes=None</em>, <em class="sig-param">verification_message_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_create_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for AdminCreateUser requests.</p></li>
<li><p><strong>alias_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with <code class="docutils literal notranslate"><span class="pre">username_attributes</span></code>.</p></li>
<li><p><strong>auto_verified_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The attributes to be auto-verified. Possible values: email, phone_number.</p></li>
<li><p><strong>device_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for the user pool’s device tracking.</p></li>
<li><p><strong>email_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Email Configuration.</p></li>
<li><p><strong>email_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_message</span></code> argument.</p></li>
<li><p><strong>email_verification_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification subject. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_subject</span></code> argument.</p></li>
<li><p><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for the AWS Lambda triggers associated with the user pool.</p></li>
<li><p><strong>mfa_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attribute.</p></li>
<li><p><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for information about the user pool password policy.</p></li>
<li><p><strong>schemas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A container with the schema attributes of a user pool. Schema attributes from the <a class="reference external" href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes">standard attribute set</a> only need to be specified if they are different from the default configuration. Maximum of 50 attributes.</p></li>
<li><p><strong>sms_authentication_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS authentication message.</p></li>
<li><p><strong>sms_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SMS Configuration.</p></li>
<li><p><strong>sms_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">sms_message</span></code> argument.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the User Pool.</p></li>
<li><p><strong>user_pool_add_ons</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for user pool add-ons to enable user pool advanced security mode features.</p></li>
<li><p><strong>username_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with <code class="docutils literal notranslate"><span class="pre">alias_attributes</span></code>.</p></li>
<li><p><strong>verification_message_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The verification message templates configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>admin_create_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowAdminCreateUserOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inviteMessageTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The invite message template structure.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unusedAccountValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - <strong>DEPRECATED</strong> Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.</p></li>
</ul>
<p>The <strong>device_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">challengeRequiredOnNewDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a challenge is required on a new device. Only applicable to a new device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceOnlyRememberedOnUserPrompt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, a device is only remembered on user prompt.</p></li>
</ul>
<p>The <strong>email_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSendingAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToEmailAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The REPLY-TO email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the email source.</p></li>
</ul>
<p>The <strong>lambda_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the lambda creating an authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A custom Message AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defineAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A post-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A post-confirmation AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A pre-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A pre-registration AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preTokenGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allow to customize identity token claims before token generation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userMigration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user migration Lambda config type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyAuthChallengeResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Verifies the authentication challenge response.</p></li>
</ul>
<p>The <strong>password_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">minimumLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum length of the password policy that you have set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireLowercase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one lowercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireNumbers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one number in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSymbols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one symbol in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireUppercase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one uppercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">temporaryPasswordValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.</p></li>
</ul>
<p>The <strong>schemas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeDataType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The attribute data type. Must be one of <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Number</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developerOnlyAttribute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the attribute type is developer only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the attribute can be changed once it has been created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the constraints for an attribute of the number type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum value of an attribute that is of the number data type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum value of an attribute that is of the number data type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stringAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - -Specifies the constraints for an attribute of the string type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum length of an attribute value of the string type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum length of an attribute value of the string type.</p></li>
</ul>
</li>
</ul>
<p>The <strong>sms_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">externalId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The external ID used in IAM role trust relationships. For more information about using external IDs, see <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to Use an External ID When Granting Access to Your AWS Resources to a Third Party</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snsCallerArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Amazon SNS caller. This is usually the IAM role that you’ve given Cognito permission to assume.</p></li>
</ul>
<p>The <strong>user_pool_add_ons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advancedSecurityMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode for advanced security, must be one of <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">AUDIT</span></code> or <code class="docutils literal notranslate"><span class="pre">ENFORCED</span></code>.</p></li>
</ul>
<p>The <strong>verification_message_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultEmailOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default email option. Must be either <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code> or <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_LINK</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessageByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template for sending a confirmation link to the user, it must contain the <code class="docutils literal notranslate"><span class="pre">{##Click</span> <span class="pre">Here##}</span></code> placeholder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubjectByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template for sending a confirmation link to the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.admin_create_user_config">
<code class="sig-name descname">admin_create_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.admin_create_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for AdminCreateUser requests.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowAdminCreateUserOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inviteMessageTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The invite message template structure.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unusedAccountValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - <strong>DEPRECATED</strong> Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.alias_attributes">
<code class="sig-name descname">alias_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.alias_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with <code class="docutils literal notranslate"><span class="pre">username_attributes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the user pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.auto_verified_attributes">
<code class="sig-name descname">auto_verified_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.auto_verified_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>The attributes to be auto-verified. Possible values: email, phone_number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the user pool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.device_configuration">
<code class="sig-name descname">device_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.device_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for the user pool’s device tracking.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">challengeRequiredOnNewDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether a challenge is required on a new device. Only applicable to a new device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceOnlyRememberedOnUserPrompt</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, a device is only remembered on user prompt.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_configuration">
<code class="sig-name descname">email_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The Email Configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSendingAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToEmailAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The REPLY-TO email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the email source.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_verification_message">
<code class="sig-name descname">email_verification_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_verification_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the email verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_message</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_verification_subject">
<code class="sig-name descname">email_verification_subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_verification_subject" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the email verification subject. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_subject</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.lambda_config">
<code class="sig-name descname">lambda_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.lambda_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A container for the AWS Lambda triggers associated with the user pool.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the lambda creating an authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A custom Message AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defineAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Defines the authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A post-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A post-confirmation AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A pre-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A pre-registration AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preTokenGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allow to customize identity token claims before token generation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userMigration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user migration Lambda config type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyAuthChallengeResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Verifies the authentication challenge response.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.last_modified_date">
<code class="sig-name descname">last_modified_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.last_modified_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the user pool was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.mfa_configuration">
<code class="sig-name descname">mfa_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.mfa_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the attribute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.password_policy">
<code class="sig-name descname">password_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.password_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A container for information about the user pool password policy.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">minimumLength</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum length of the password policy that you have set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireLowercase</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you have required users to use at least one lowercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireNumbers</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you have required users to use at least one number in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSymbols</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you have required users to use at least one symbol in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireUppercase</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether you have required users to use at least one uppercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">temporaryPasswordValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.schemas">
<code class="sig-name descname">schemas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.schemas" title="Permalink to this definition">¶</a></dt>
<dd><p>A container with the schema attributes of a user pool. Schema attributes from the <a class="reference external" href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes">standard attribute set</a> only need to be specified if they are different from the default configuration. Maximum of 50 attributes.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeDataType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The attribute data type. Must be one of <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Number</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developerOnlyAttribute</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether the attribute type is developer only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether the attribute can be changed once it has been created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the constraints for an attribute of the number type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum value of an attribute that is of the number data type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum value of an attribute that is of the number data type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stringAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - -Specifies the constraints for an attribute of the string type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLength</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum length of an attribute value of the string type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum length of an attribute value of the string type.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_authentication_message">
<code class="sig-name descname">sms_authentication_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_authentication_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the SMS authentication message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_configuration">
<code class="sig-name descname">sms_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The SMS Configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">externalId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The external ID used in IAM role trust relationships. For more information about using external IDs, see <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to Use an External ID When Granting Access to Your AWS Resources to a Third Party</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snsCallerArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Amazon SNS caller. This is usually the IAM role that you’ve given Cognito permission to assume.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_verification_message">
<code class="sig-name descname">sms_verification_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_verification_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the SMS verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">sms_message</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the User Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.user_pool_add_ons">
<code class="sig-name descname">user_pool_add_ons</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.user_pool_add_ons" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for user pool add-ons to enable user pool advanced security mode features.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advancedSecurityMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mode for advanced security, must be one of <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">AUDIT</span></code> or <code class="docutils literal notranslate"><span class="pre">ENFORCED</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.username_attributes">
<code class="sig-name descname">username_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.username_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with <code class="docutils literal notranslate"><span class="pre">alias_attributes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.verification_message_template">
<code class="sig-name descname">verification_message_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.verification_message_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The verification message templates configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultEmailOption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default email option. Must be either <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code> or <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_LINK</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessageByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email message template for sending a confirmation link to the user, it must contain the <code class="docutils literal notranslate"><span class="pre">{##Click</span> <span class="pre">Here##}</span></code> placeholder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubjectByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subject line for the email message template for sending a confirmation link to the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_create_user_config=None</em>, <em class="sig-param">alias_attributes=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">auto_verified_attributes=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">device_configuration=None</em>, <em class="sig-param">email_configuration=None</em>, <em class="sig-param">email_verification_message=None</em>, <em class="sig-param">email_verification_subject=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">lambda_config=None</em>, <em class="sig-param">last_modified_date=None</em>, <em class="sig-param">mfa_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_policy=None</em>, <em class="sig-param">schemas=None</em>, <em class="sig-param">sms_authentication_message=None</em>, <em class="sig-param">sms_configuration=None</em>, <em class="sig-param">sms_verification_message=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_pool_add_ons=None</em>, <em class="sig-param">username_attributes=None</em>, <em class="sig-param">verification_message_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_create_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for AdminCreateUser requests.</p></li>
<li><p><strong>alias_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with <code class="docutils literal notranslate"><span class="pre">username_attributes</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the user pool.</p></li>
<li><p><strong>auto_verified_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The attributes to be auto-verified. Possible values: email, phone_number.</p></li>
<li><p><strong>creation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the user pool was created.</p></li>
<li><p><strong>device_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for the user pool’s device tracking.</p></li>
<li><p><strong>email_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Email Configuration.</p></li>
<li><p><strong>email_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_message</span></code> argument.</p></li>
<li><p><strong>email_verification_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification subject. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_subject</span></code> argument.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy</p></li>
<li><p><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for the AWS Lambda triggers associated with the user pool.</p></li>
<li><p><strong>last_modified_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the user pool was last modified.</p></li>
<li><p><strong>mfa_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attribute.</p></li>
<li><p><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for information about the user pool password policy.</p></li>
<li><p><strong>schemas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A container with the schema attributes of a user pool. Schema attributes from the <a class="reference external" href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes">standard attribute set</a> only need to be specified if they are different from the default configuration. Maximum of 50 attributes.</p>
</p></li>
<li><p><strong>sms_authentication_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS authentication message.</p></li>
<li><p><strong>sms_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SMS Configuration.</p></li>
<li><p><strong>sms_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">sms_message</span></code> argument.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the User Pool.</p></li>
<li><p><strong>user_pool_add_ons</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for user pool add-ons to enable user pool advanced security mode features.</p></li>
<li><p><strong>username_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with <code class="docutils literal notranslate"><span class="pre">alias_attributes</span></code>.</p></li>
<li><p><strong>verification_message_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The verification message templates configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>admin_create_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowAdminCreateUserOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inviteMessageTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The invite message template structure.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">unusedAccountValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - <strong>DEPRECATED</strong> Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.</p></li>
</ul>
<p>The <strong>device_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">challengeRequiredOnNewDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a challenge is required on a new device. Only applicable to a new device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceOnlyRememberedOnUserPrompt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, a device is only remembered on user prompt.</p></li>
</ul>
<p>The <strong>email_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSendingAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replyToEmailAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The REPLY-TO email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the email source.</p></li>
</ul>
<p>The <strong>lambda_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the lambda creating an authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A custom Message AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defineAuthChallenge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the authentication challenge.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A post-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A post-confirmation AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A pre-authentication AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A pre-registration AWS Lambda trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preTokenGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allow to customize identity token claims before token generation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userMigration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user migration Lambda config type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyAuthChallengeResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Verifies the authentication challenge response.</p></li>
</ul>
<p>The <strong>password_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">minimumLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum length of the password policy that you have set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireLowercase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one lowercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireNumbers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one number in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSymbols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one symbol in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireUppercase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether you have required users to use at least one uppercase letter in their password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">temporaryPasswordValidityDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.</p></li>
</ul>
<p>The <strong>schemas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributeDataType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The attribute data type. Must be one of <code class="docutils literal notranslate"><span class="pre">Boolean</span></code>, <code class="docutils literal notranslate"><span class="pre">Number</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">DateTime</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developerOnlyAttribute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the attribute type is developer only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the attribute can be changed once it has been created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the constraints for an attribute of the number type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum value of an attribute that is of the number data type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum value of an attribute that is of the number data type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stringAttributeConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - -Specifies the constraints for an attribute of the string type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum length of an attribute value of the string type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum length of an attribute value of the string type.</p></li>
</ul>
</li>
</ul>
<p>The <strong>sms_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">externalId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The external ID used in IAM role trust relationships. For more information about using external IDs, see <a class="reference external" href="http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to Use an External ID When Granting Access to Your AWS Resources to a Third Party</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snsCallerArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Amazon SNS caller. This is usually the IAM role that you’ve given Cognito permission to assume.</p></li>
</ul>
<p>The <strong>user_pool_add_ons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advancedSecurityMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode for advanced security, must be one of <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">AUDIT</span></code> or <code class="docutils literal notranslate"><span class="pre">ENFORCED</span></code>.</p></li>
</ul>
<p>The <strong>verification_message_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultEmailOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default email option. Must be either <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code> or <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_LINK</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">CONFIRM_WITH_CODE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_message</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailMessageByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email message template for sending a confirmation link to the user, it must contain the <code class="docutils literal notranslate"><span class="pre">{##Click</span> <span class="pre">Here##}</span></code> placeholder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template. Conflicts with <code class="docutils literal notranslate"><span class="pre">email_verification_subject</span></code> argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubjectByLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subject line for the email message template for sending a confirmation link to the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SMS message template. Must contain the <code class="docutils literal notranslate"><span class="pre">{####}</span></code> placeholder. Conflicts with <code class="docutils literal notranslate"><span class="pre">sms_verification_message</span></code> argument.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolClient">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">UserPoolClient</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_oauth_flows=None</em>, <em class="sig-param">allowed_oauth_flows_user_pool_client=None</em>, <em class="sig-param">allowed_oauth_scopes=None</em>, <em class="sig-param">callback_urls=None</em>, <em class="sig-param">default_redirect_uri=None</em>, <em class="sig-param">explicit_auth_flows=None</em>, <em class="sig-param">generate_secret=None</em>, <em class="sig-param">logout_urls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_attributes=None</em>, <em class="sig-param">refresh_token_validity=None</em>, <em class="sig-param">supported_identity_providers=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">write_attributes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool Client resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_oauth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth flows (code, implicit, client_credentials).</p></li>
<li><p><strong>allowed_oauth_flows_user_pool_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.</p></li>
<li><p><strong>allowed_oauth_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).</p></li>
<li><p><strong>callback_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed callback URLs for the identity providers.</p></li>
<li><p><strong>default_redirect_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default redirect URI. Must be in the list of callback URLs.</p></li>
<li><p><strong>explicit_auth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).</p></li>
<li><p><strong>generate_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should an application secret be generated.</p></li>
<li><p><strong>logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed logout URLs for the identity providers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application client.</p></li>
<li><p><strong>read_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can read from.</p></li>
<li><p><strong>refresh_token_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time limit in days refresh tokens are valid for.</p></li>
<li><p><strong>supported_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of provider names for the identity providers that are supported on this client.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool the client belongs to.</p></li>
<li><p><strong>write_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can write to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows">
<code class="sig-name descname">allowed_oauth_flows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed OAuth flows (code, implicit, client_credentials).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows_user_pool_client">
<code class="sig-name descname">allowed_oauth_flows_user_pool_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows_user_pool_client" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_scopes">
<code class="sig-name descname">allowed_oauth_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.callback_urls">
<code class="sig-name descname">callback_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.callback_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed callback URLs for the identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret of the user pool client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.default_redirect_uri">
<code class="sig-name descname">default_redirect_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.default_redirect_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The default redirect URI. Must be in the list of callback URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.explicit_auth_flows">
<code class="sig-name descname">explicit_auth_flows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.explicit_auth_flows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.generate_secret">
<code class="sig-name descname">generate_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.generate_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Should an application secret be generated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.logout_urls">
<code class="sig-name descname">logout_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.logout_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed logout URLs for the identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.read_attributes">
<code class="sig-name descname">read_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.read_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user pool attributes the application client can read from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.refresh_token_validity">
<code class="sig-name descname">refresh_token_validity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.refresh_token_validity" title="Permalink to this definition">¶</a></dt>
<dd><p>The time limit in days refresh tokens are valid for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.supported_identity_providers">
<code class="sig-name descname">supported_identity_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.supported_identity_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of provider names for the identity providers that are supported on this client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.user_pool_id">
<code class="sig-name descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool the client belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.write_attributes">
<code class="sig-name descname">write_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.write_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user pool attributes the application client can write to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolClient.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_oauth_flows=None</em>, <em class="sig-param">allowed_oauth_flows_user_pool_client=None</em>, <em class="sig-param">allowed_oauth_scopes=None</em>, <em class="sig-param">callback_urls=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_redirect_uri=None</em>, <em class="sig-param">explicit_auth_flows=None</em>, <em class="sig-param">generate_secret=None</em>, <em class="sig-param">logout_urls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_attributes=None</em>, <em class="sig-param">refresh_token_validity=None</em>, <em class="sig-param">supported_identity_providers=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">write_attributes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPoolClient resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_oauth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth flows (code, implicit, client_credentials).</p></li>
<li><p><strong>allowed_oauth_flows_user_pool_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.</p></li>
<li><p><strong>allowed_oauth_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).</p></li>
<li><p><strong>callback_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed callback URLs for the identity providers.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the user pool client.</p></li>
<li><p><strong>default_redirect_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default redirect URI. Must be in the list of callback URLs.</p></li>
<li><p><strong>explicit_auth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).</p></li>
<li><p><strong>generate_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should an application secret be generated.</p></li>
<li><p><strong>logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed logout URLs for the identity providers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application client.</p></li>
<li><p><strong>read_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can read from.</p></li>
<li><p><strong>refresh_token_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time limit in days refresh tokens are valid for.</p></li>
<li><p><strong>supported_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of provider names for the identity providers that are supported on this client.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool the client belongs to.</p></li>
<li><p><strong>write_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can write to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolClient.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolClient.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolDomain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">UserPoolDomain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_arn=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool Domain resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain string.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID for the user pool owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.cloudfront_distribution_arn">
<code class="sig-name descname">cloudfront_distribution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.cloudfront_distribution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the CloudFront distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.s3_bucket">
<code class="sig-name descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket where the static files for this domain are stored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.user_pool_id">
<code class="sig-name descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The app version.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolDomain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">certificate_arn=None</em>, <em class="sig-param">cloudfront_distribution_arn=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">s3_bucket=None</em>, <em class="sig-param">user_pool_id=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPoolDomain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account ID for the user pool owner.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.</p></li>
<li><p><strong>cloudfront_distribution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the CloudFront distribution.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain string.</p></li>
<li><p><strong>s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket where the static files for this domain are stored.</p></li>
<li><p><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The app version.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolDomain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolDomain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.get_user_pools">
<code class="sig-prename descclassname">pulumi_aws.cognito.</code><code class="sig-name descname">get_user_pools</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.get_user_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of cognito user pools.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Name of the cognito user pools. Name is not a unique attribute for cognito user pool, so multiple pools might be returned with given name.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cognito_user_pools.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cognito_user_pools.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
