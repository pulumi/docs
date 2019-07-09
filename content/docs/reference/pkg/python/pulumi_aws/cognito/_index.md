---
---

<div class="section" id="module-pulumi_aws.cognito">
<span id="cognito"></span><h1>cognito<a class="headerlink" href="#module-pulumi_aws.cognito" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cognito.GetUserPoolsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">GetUserPoolsResult</code><span class="sig-paren">(</span><em>arns=None</em>, <em>ids=None</em>, <em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUserPools.</p>
<dl class="attribute">
<dt id="pulumi_aws.cognito.GetUserPoolsResult.ids">
<code class="descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of cognito user pool ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.GetUserPoolsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.GetUserPoolsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cognito.IdentityPool">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">IdentityPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_unauthenticated_identities=None</em>, <em>cognito_identity_providers=None</em>, <em>developer_provider_name=None</em>, <em>identity_pool_name=None</em>, <em>openid_connect_provider_arns=None</em>, <em>saml_provider_arns=None</em>, <em>supported_login_providers=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Cognito Identity Pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_unauthenticated_identities</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the identity pool supports unauthenticated logins or not.</li>
<li><strong>cognito_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Cognito Identity user pools and their client IDs.</li>
<li><strong>developer_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “domain” by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.</li>
<li><strong>identity_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cognito Identity Pool name.</li>
<li><strong>openid_connect_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of OpendID Connect provider ARNs.</li>
<li><strong>saml_provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.</li>
<li><strong>supported_login_providers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-Value pairs mapping provider names to provider app IDs.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.allow_unauthenticated_identities">
<code class="descname">allow_unauthenticated_identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.allow_unauthenticated_identities" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the identity pool supports unauthenticated logins or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the identity pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.cognito_identity_providers">
<code class="descname">cognito_identity_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.cognito_identity_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Amazon Cognito Identity user pools and their client IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.developer_provider_name">
<code class="descname">developer_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.developer_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The “domain” by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.identity_pool_name">
<code class="descname">identity_pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.identity_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cognito Identity Pool name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.openid_connect_provider_arns">
<code class="descname">openid_connect_provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.openid_connect_provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OpendID Connect provider ARNs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.saml_provider_arns">
<code class="descname">saml_provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.saml_provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPool.supported_login_providers">
<code class="descname">supported_login_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.supported_login_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-Value pairs mapping provider names to provider app IDs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">IdentityPoolRoleAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>identity_pool_id=None</em>, <em>role_mappings=None</em>, <em>roles=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Cognito Identity Pool Roles Attachment.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>identity_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identity pool ID in the format REGION:GUID.</li>
<li><strong>role_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of Role Mapping.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of roles associated with this pool. For a given role, the key will be either “authenticated” or “unauthenticated” and the value will be the Role ARN.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.identity_pool_id">
<code class="descname">identity_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.identity_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An identity pool ID in the format REGION:GUID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.role_mappings">
<code class="descname">role_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.role_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of Role Mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of roles associated with this pool. For a given role, the key will be either “authenticated” or “unauthenticated” and the value will be the Role ARN.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityPoolRoleAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityProvider">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">IdentityProvider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attribute_mapping=None</em>, <em>idp_identifiers=None</em>, <em>provider_details=None</em>, <em>provider_name=None</em>, <em>provider_type=None</em>, <em>user_pool_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Identity Provider resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attribute_mapping</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of attribute mapping of user pool attributes. <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping">AttributeMapping in AWS API documentation</a></li>
<li><strong>idp_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of identity providers.</li>
<li><strong>provider_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of identity details, such as access token</li>
<li><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider name</li>
<li><strong>provider_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type.  <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType">See AWS API for valid values</a></li>
<li><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool id</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_provider.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.attribute_mapping">
<code class="descname">attribute_mapping</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.attribute_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of attribute mapping of user pool attributes. <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping">AttributeMapping in AWS API documentation</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.idp_identifiers">
<code class="descname">idp_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.idp_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_details">
<code class="descname">provider_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of identity details, such as access token</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_name">
<code class="descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.provider_type">
<code class="descname">provider_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.provider_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type.  <a class="reference external" href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType">See AWS API for valid values</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.IdentityProvider.user_pool_id">
<code class="descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool id</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.IdentityProvider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.IdentityProvider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.IdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.ResourceServer">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">ResourceServer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>identifier=None</em>, <em>name=None</em>, <em>scopes=None</em>, <em>user_pool_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito Resource Server.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identifier for the resource server.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the resource server.</li>
<li><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Authorization Scope.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.identifier">
<code class="descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>An identifier for the resource server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the resource server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.scopes">
<code class="descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Authorization Scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.ResourceServer.scope_identifiers">
<code class="descname">scope_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.scope_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of all scopes configured for this resource server in the format identifier/scope_name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.ResourceServer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.ResourceServer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.ResourceServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">UserGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>precedence=None</em>, <em>role_arn=None</em>, <em>user_pool_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group.</li>
<li><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The precedence of the user group.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be associated with the user group.</li>
<li><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.precedence">
<code class="descname">precedence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The precedence of the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role to be associated with the user group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserGroup.user_pool_id">
<code class="descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPool">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">UserPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_create_user_config=None</em>, <em>alias_attributes=None</em>, <em>auto_verified_attributes=None</em>, <em>device_configuration=None</em>, <em>email_configuration=None</em>, <em>email_verification_message=None</em>, <em>email_verification_subject=None</em>, <em>lambda_config=None</em>, <em>mfa_configuration=None</em>, <em>name=None</em>, <em>password_policy=None</em>, <em>schemas=None</em>, <em>sms_authentication_message=None</em>, <em>sms_configuration=None</em>, <em>sms_verification_message=None</em>, <em>tags=None</em>, <em>user_pool_add_ons=None</em>, <em>username_attributes=None</em>, <em>verification_message_template=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_create_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for AdminCreateUser requests.</li>
<li><strong>alias_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with <code class="docutils literal notranslate"><span class="pre">username_attributes</span></code>.</li>
<li><strong>auto_verified_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The attributes to be auto-verified. Possible values: email, phone_number.</li>
<li><strong>device_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for the user pool’s device tracking.</li>
<li><strong>email_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Email Configuration.</li>
<li><strong>email_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_message</span></code> argument.</li>
<li><strong>email_verification_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the email verification subject. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_subject</span></code> argument.</li>
<li><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for the AWS Lambda triggers associated with the user pool.</li>
<li><strong>mfa_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attribute.</li>
<li><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A container for information about the user pool password policy.</li>
<li><strong>schemas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A container with the schema attributes of a user pool. Maximum of 50 attributes.</li>
<li><strong>sms_authentication_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS authentication message.</li>
<li><strong>sms_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SMS Configuration.</li>
<li><strong>sms_verification_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the SMS verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">sms_message</span></code> argument.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the User Pool.</li>
<li><strong>user_pool_add_ons</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for user pool add-ons to enable user pool advanced security mode features.</li>
<li><strong>username_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with <code class="docutils literal notranslate"><span class="pre">alias_attributes</span></code>.</li>
<li><strong>verification_message_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The verification message templates configuration.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.admin_create_user_config">
<code class="descname">admin_create_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.admin_create_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for AdminCreateUser requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.alias_attributes">
<code class="descname">alias_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.alias_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with <code class="docutils literal notranslate"><span class="pre">username_attributes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the user pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.auto_verified_attributes">
<code class="descname">auto_verified_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.auto_verified_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>The attributes to be auto-verified. Possible values: email, phone_number.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the user pool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.device_configuration">
<code class="descname">device_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.device_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for the user pool’s device tracking.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_configuration">
<code class="descname">email_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The Email Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_verification_message">
<code class="descname">email_verification_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_verification_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the email verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_message</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.email_verification_subject">
<code class="descname">email_verification_subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.email_verification_subject" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the email verification subject. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">email_subject</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.lambda_config">
<code class="descname">lambda_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.lambda_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A container for the AWS Lambda triggers associated with the user pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.last_modified_date">
<code class="descname">last_modified_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.last_modified_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the user pool was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.mfa_configuration">
<code class="descname">mfa_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.mfa_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the attribute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.password_policy">
<code class="descname">password_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.password_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A container for information about the user pool password policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.schemas">
<code class="descname">schemas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.schemas" title="Permalink to this definition">¶</a></dt>
<dd><p>A container with the schema attributes of a user pool. Maximum of 50 attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_authentication_message">
<code class="descname">sms_authentication_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_authentication_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the SMS authentication message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_configuration">
<code class="descname">sms_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The SMS Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.sms_verification_message">
<code class="descname">sms_verification_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.sms_verification_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the SMS verification message. Conflicts with <code class="docutils literal notranslate"><span class="pre">verification_message_template</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">sms_message</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the User Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.user_pool_add_ons">
<code class="descname">user_pool_add_ons</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.user_pool_add_ons" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for user pool add-ons to enable user pool advanced security mode features.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.username_attributes">
<code class="descname">username_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.username_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with <code class="docutils literal notranslate"><span class="pre">alias_attributes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPool.verification_message_template">
<code class="descname">verification_message_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPool.verification_message_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The verification message templates configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolClient">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">UserPoolClient</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_oauth_flows=None</em>, <em>allowed_oauth_flows_user_pool_client=None</em>, <em>allowed_oauth_scopes=None</em>, <em>callback_urls=None</em>, <em>default_redirect_uri=None</em>, <em>explicit_auth_flows=None</em>, <em>generate_secret=None</em>, <em>logout_urls=None</em>, <em>name=None</em>, <em>read_attributes=None</em>, <em>refresh_token_validity=None</em>, <em>supported_identity_providers=None</em>, <em>user_pool_id=None</em>, <em>write_attributes=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool Client resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_oauth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth flows (code, implicit, client_credentials).</li>
<li><strong>allowed_oauth_flows_user_pool_client</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.</li>
<li><strong>allowed_oauth_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).</li>
<li><strong>callback_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed callback URLs for the identity providers.</li>
<li><strong>default_redirect_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default redirect URI. Must be in the list of callback URLs.</li>
<li><strong>explicit_auth_flows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).</li>
<li><strong>generate_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should an application secret be generated.</li>
<li><strong>logout_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed logout URLs for the identity providers.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application client.</li>
<li><strong>read_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can read from.</li>
<li><strong>refresh_token_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time limit in days refresh tokens are valid for.</li>
<li><strong>supported_identity_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of provider names for the identity providers that are supported on this client.</li>
<li><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool the client belongs to.</li>
<li><strong>write_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user pool attributes the application client can write to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows">
<code class="descname">allowed_oauth_flows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed OAuth flows (code, implicit, client_credentials).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows_user_pool_client">
<code class="descname">allowed_oauth_flows_user_pool_client</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_flows_user_pool_client" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.allowed_oauth_scopes">
<code class="descname">allowed_oauth_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.allowed_oauth_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.callback_urls">
<code class="descname">callback_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.callback_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed callback URLs for the identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.client_secret">
<code class="descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret of the user pool client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.default_redirect_uri">
<code class="descname">default_redirect_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.default_redirect_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The default redirect URI. Must be in the list of callback URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.explicit_auth_flows">
<code class="descname">explicit_auth_flows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.explicit_auth_flows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.generate_secret">
<code class="descname">generate_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.generate_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Should an application secret be generated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.logout_urls">
<code class="descname">logout_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.logout_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed logout URLs for the identity providers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.read_attributes">
<code class="descname">read_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.read_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user pool attributes the application client can read from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.refresh_token_validity">
<code class="descname">refresh_token_validity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.refresh_token_validity" title="Permalink to this definition">¶</a></dt>
<dd><p>The time limit in days refresh tokens are valid for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.supported_identity_providers">
<code class="descname">supported_identity_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.supported_identity_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of provider names for the identity providers that are supported on this client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.user_pool_id">
<code class="descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool the client belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolClient.write_attributes">
<code class="descname">write_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.write_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user pool attributes the application client can write to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolClient.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolClient.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolClient.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolDomain">
<em class="property">class </em><code class="descclassname">pulumi_aws.cognito.</code><code class="descname">UserPoolDomain</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_arn=None</em>, <em>domain=None</em>, <em>user_pool_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cognito User Pool Domain resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain string.</li>
<li><strong>user_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user pool ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_domain.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.aws_account_id">
<code class="descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID for the user pool owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.cloudfront_distribution_arn">
<code class="descname">cloudfront_distribution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.cloudfront_distribution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the CloudFront distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.s3_bucket">
<code class="descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket where the static files for this domain are stored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.user_pool_id">
<code class="descname">user_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.user_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user pool ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cognito.UserPoolDomain.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The app version.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cognito.UserPoolDomain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.UserPoolDomain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.UserPoolDomain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cognito.get_user_pools">
<code class="descclassname">pulumi_aws.cognito.</code><code class="descname">get_user_pools</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cognito.get_user_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of cognito user pools.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cognito_user_pools.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cognito_user_pools.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
