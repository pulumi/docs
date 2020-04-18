---
title: Module idp
title_tag: Module idp | Package pulumi_okta | Python SDK
linktitle: idp
notitle: true
---

<div class="section" id="idp">
<h1>idp<a class="headerlink" href="#idp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.idp"></span><dl class="class">
<dt id="pulumi_okta.idp.AwaitableGetMetadataSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">AwaitableGetMetadataSamlResult</code><span class="sig-paren">(</span><em class="sig-param">assertions_signed=None</em>, <em class="sig-param">authn_request_signed=None</em>, <em class="sig-param">encryption_certificate=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">signing_certificate=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.AwaitableGetMetadataSamlResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.idp.AwaitableGetSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">AwaitableGetSamlResult</code><span class="sig-paren">(</span><em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.AwaitableGetSamlResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.idp.GetMetadataSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">GetMetadataSamlResult</code><span class="sig-paren">(</span><em class="sig-param">assertions_signed=None</em>, <em class="sig-param">authn_request_signed=None</em>, <em class="sig-param">encryption_certificate=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">signing_certificate=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMetadataSaml.</p>
<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.assertions_signed">
<code class="sig-name descname">assertions_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.assertions_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>whether assertions are signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.authn_request_signed">
<code class="sig-name descname">authn_request_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.authn_request_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>whether authn requests are signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.encryption_certificate">
<code class="sig-name descname">encryption_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.encryption_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML request encryption certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.entity_id">
<code class="sig-name descname">entity_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.entity_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity URL for instance <code class="docutils literal notranslate"><span class="pre">https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.http_post_binding">
<code class="sig-name descname">http_post_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.http_post_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.http_redirect_binding">
<code class="sig-name descname">http_redirect_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.http_redirect_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>raw IdP metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetMetadataSamlResult.signing_certificate">
<code class="sig-name descname">signing_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetMetadataSamlResult.signing_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML request signing certificate.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.idp.GetSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">GetSamlResult</code><span class="sig-paren">(</span><em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSaml.</p>
<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.acs_binding">
<code class="sig-name descname">acs_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.acs_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP binding used to receive a SAMLResponse message from the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.acs_type">
<code class="sig-name descname">acs_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.acs_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether to publish an instance-specific (trust) or organization (shared) ACS endpoint in the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that identifies the target Okta IdP instance (SP)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id of idp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that identifies the issuer (IdP).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>indicates whether Okta uses the original Okta org domain URL, or a custom domain URL in the request to the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.kid">
<code class="sig-name descname">kid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.kid" title="Permalink to this definition">¶</a></dt>
<dd><p>Key ID reference to the IdP’s X.509 signature certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of the idp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.sso_binding">
<code class="sig-name descname">sso_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.sso_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>single sign on binding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.sso_destination">
<code class="sig-name descname">sso_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.sso_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>SSO request binding, HTTP-POST or HTTP-REDIRECT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.sso_url">
<code class="sig-name descname">sso_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.sso_url" title="Permalink to this definition">¶</a></dt>
<dd><p>single sign on url.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.subject_filter">
<code class="sig-name descname">subject_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.subject_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>regular expression pattern used to filter untrusted IdP usernames.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.subject_formats">
<code class="sig-name descname">subject_formats</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.subject_formats" title="Permalink to this definition">¶</a></dt>
<dd><p>Expression to generate or transform a unique username for the IdP user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.GetSamlResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.GetSamlResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>type of idp.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.idp.Oidc">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">Oidc</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">issuer_url=None</em>, <em class="sig-param">jwks_binding=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">user_info_binding=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Oidc" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an OIDC Identity Provider.</p>
<p>This resource allows you to create and configure an OIDC Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>acs_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>acs_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ACS. Default is <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code>.</p></li>
<li><p><strong>authorization_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an authorization request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>authorization_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>issuer_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that identifies the issuer.</p></li>
<li><p><strong>jwks_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making a request for the OIDC JWKS. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint where the signer of the keys publishes its keys in a JWK Set.</p></li>
<li><p><strong>max_clock_skew</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum allowable clock-skew when processing messages from the IdP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The scopes of the IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>token_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making a token request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>token_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.</p></li>
<li><p><strong>user_info_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protected resource endpoint that returns claims about the authenticated user.</p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.account_link_action">
<code class="sig-name descname">account_link_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.account_link_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the account linking action for an IdP user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.account_link_group_includes">
<code class="sig-name descname">account_link_group_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.account_link_group_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Group memberships to determine link candidates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.acs_binding">
<code class="sig-name descname">acs_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.acs_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.acs_type">
<code class="sig-name descname">acs_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.acs_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of ACS. Default is <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.authorization_binding">
<code class="sig-name descname">authorization_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.authorization_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making an authorization request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.authorization_url">
<code class="sig-name descname">authorization_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.authorization_url" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier issued by AS for the Okta IdP instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret issued by AS for the Okta IdP instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.deprovisioned_action">
<code class="sig-name descname">deprovisioned_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.deprovisioned_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.groups_action">
<code class="sig-name descname">groups_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.groups_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.groups_assignments">
<code class="sig-name descname">groups_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.groups_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.groups_attribute">
<code class="sig-name descname">groups_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.groups_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.groups_filters">
<code class="sig-name descname">groups_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.groups_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.issuer_url">
<code class="sig-name descname">issuer_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.issuer_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that identifies the issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.jwks_binding">
<code class="sig-name descname">jwks_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.jwks_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making a request for the OIDC JWKS. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.jwks_url">
<code class="sig-name descname">jwks_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.jwks_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Endpoint where the signer of the keys publishes its keys in a JWK Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.max_clock_skew">
<code class="sig-name descname">max_clock_skew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.max_clock_skew" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum allowable clock-skew when processing messages from the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.profile_master">
<code class="sig-name descname">profile_master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.profile_master" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the IdP should act as a source of truth for user profile attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.provisioning_action">
<code class="sig-name descname">provisioning_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.provisioning_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for an IdP user during authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.subject_match_attribute">
<code class="sig-name descname">subject_match_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.subject_match_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.subject_match_type">
<code class="sig-name descname">subject_match_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.subject_match_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.suspended_action">
<code class="sig-name descname">suspended_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.suspended_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.token_binding">
<code class="sig-name descname">token_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.token_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making a token request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.token_url">
<code class="sig-name descname">token_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.token_url" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of OIDC IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.user_info_url">
<code class="sig-name descname">user_info_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.user_info_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Protected resource endpoint that returns claims about the authenticated user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Oidc.username_template">
<code class="sig-name descname">username_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Oidc.username_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta EL Expression to generate or transform a unique username for the IdP user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Oidc.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">issuer_url=None</em>, <em class="sig-param">jwks_binding=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_info_binding=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Oidc.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Oidc resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>acs_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>acs_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ACS. Default is <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code>.</p></li>
<li><p><strong>authorization_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an authorization request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>authorization_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>issuer_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that identifies the issuer.</p></li>
<li><p><strong>jwks_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making a request for the OIDC JWKS. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>jwks_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint where the signer of the keys publishes its keys in a JWK Set.</p></li>
<li><p><strong>max_clock_skew</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum allowable clock-skew when processing messages from the IdP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The scopes of the IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>token_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making a token request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>token_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of OIDC IdP.</p></li>
<li><p><strong>user_info_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protected resource endpoint that returns claims about the authenticated user.</p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Oidc.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Oidc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.Oidc.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Oidc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.Saml">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">Saml</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_format=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a SAML Identity Provider.</p>
<p>This resource allows you to create and configure a SAML Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>acs_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>acs_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ACS. It can be <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG&quot;</span></code>.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that identifies the issuer.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>kid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the signing key.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>name_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name identifier format to use. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML digital signature algorithm used when signing an AuthnRequest message.</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p></li>
<li><p><strong>sso_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an SSO request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>sso_destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI reference indicating the address to which the AuthnRequest message is sent.</p></li>
<li><p><strong>sso_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of binding-specific endpoint to send an AuthnRequest message to IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional regular expression pattern used to filter untrusted IdP usernames.</p></li>
<li><p><strong>subject_formats</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The name formate. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.account_link_action">
<code class="sig-name descname">account_link_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.account_link_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the account linking action for an IdP user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.account_link_group_includes">
<code class="sig-name descname">account_link_group_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.account_link_group_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Group memberships to determine link candidates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.acs_binding">
<code class="sig-name descname">acs_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.acs_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.acs_type">
<code class="sig-name descname">acs_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.acs_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of ACS. It can be <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>The audience restriction for the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.deprovisioned_action">
<code class="sig-name descname">deprovisioned_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.deprovisioned_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.groups_action">
<code class="sig-name descname">groups_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.groups_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.groups_assignments">
<code class="sig-name descname">groups_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.groups_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.groups_attribute">
<code class="sig-name descname">groups_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.groups_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.groups_filters">
<code class="sig-name descname">groups_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.groups_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that identifies the issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.kid">
<code class="sig-name descname">kid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.kid" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the signing key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.name_format">
<code class="sig-name descname">name_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.name_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The name identifier format to use. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.profile_master">
<code class="sig-name descname">profile_master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.profile_master" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the IdP should act as a source of truth for user profile attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.provisioning_action">
<code class="sig-name descname">provisioning_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.provisioning_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for an IdP user during authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML digital signature algorithm used when signing an AuthnRequest message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.sso_binding">
<code class="sig-name descname">sso_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.sso_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making an SSO request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.sso_destination">
<code class="sig-name descname">sso_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.sso_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>URI reference indicating the address to which the AuthnRequest message is sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.sso_url">
<code class="sig-name descname">sso_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.sso_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of binding-specific endpoint to send an AuthnRequest message to IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.subject_filter">
<code class="sig-name descname">subject_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.subject_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional regular expression pattern used to filter untrusted IdP usernames.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.subject_formats">
<code class="sig-name descname">subject_formats</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.subject_formats" title="Permalink to this definition">¶</a></dt>
<dd><p>The name formate. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.subject_match_attribute">
<code class="sig-name descname">subject_match_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.subject_match_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.subject_match_type">
<code class="sig-name descname">subject_match_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.subject_match_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.suspended_action">
<code class="sig-name descname">suspended_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.suspended_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Saml.username_template">
<code class="sig-name descname">username_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Saml.username_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta EL Expression to generate or transform a unique username for the IdP user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Saml.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_format=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Saml.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Saml resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>acs_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an ACS request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>acs_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ACS. It can be <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG&quot;</span></code>.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The audience restriction for the IdP.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that identifies the issuer.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>kid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the signing key.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>name_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name identifier format to use. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML digital signature algorithm used when signing an AuthnRequest message.</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p></li>
<li><p><strong>sso_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an SSO request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>sso_destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI reference indicating the address to which the AuthnRequest message is sent.</p></li>
<li><p><strong>sso_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of binding-specific endpoint to send an AuthnRequest message to IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional regular expression pattern used to filter untrusted IdP usernames.</p></li>
<li><p><strong>subject_formats</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The name formate. By default <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified&quot;</span></code>.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the IdP.</p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Saml.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Saml.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.Saml.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Saml.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.SamlKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">SamlKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">x5cs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.SamlKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a SAML Identity Provider Signing Key.</p>
<p>This resource allows you to create and configure a SAML Identity Provider Signing Key.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>x5cs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – base64-encoded X.509 certificate chain with DER encoding.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Date created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the cert expires.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.kid">
<code class="sig-name descname">kid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.kid" title="Permalink to this definition">¶</a></dt>
<dd><p>Key ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.kty">
<code class="sig-name descname">kty</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.kty" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the cryptographic algorithm family used with the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.use">
<code class="sig-name descname">use</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.use" title="Permalink to this definition">¶</a></dt>
<dd><p>Intended use of the public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.x5cs">
<code class="sig-name descname">x5cs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.x5cs" title="Permalink to this definition">¶</a></dt>
<dd><p>base64-encoded X.509 certificate chain with DER encoding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.SamlKey.x5t_s256">
<code class="sig-name descname">x5t_s256</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.SamlKey.x5t_s256" title="Permalink to this definition">¶</a></dt>
<dd><p>base64url-encoded SHA-256 thumbprint of the DER encoding of an X.509 certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.SamlKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">kty=None</em>, <em class="sig-param">use=None</em>, <em class="sig-param">x5cs=None</em>, <em class="sig-param">x5t_s256=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.SamlKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date created.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date the cert expires.</p></li>
<li><p><strong>kid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key ID.</p></li>
<li><p><strong>kty</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the cryptographic algorithm family used with the key.</p></li>
<li><p><strong>use</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Intended use of the public key.</p></li>
<li><p><strong>x5cs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – base64-encoded X.509 certificate chain with DER encoding.</p></li>
<li><p><strong>x5t_s256</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – base64url-encoded SHA-256 thumbprint of the DER encoding of an X.509 certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.SamlKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.SamlKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.SamlKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.SamlKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.Social">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">Social</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">match_attribute=None</em>, <em class="sig-param">match_type=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Social" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Social Identity Provider.</p>
<p>This resource allows you to create and configure an Social Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>max_clock_skew</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum allowable clock-skew when processing messages from the IdP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML digital signature algorithm used when signing an AuthnRequest message.</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The scopes of the IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Social IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;FACEBOOK&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LINKEDIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MICROSOFT&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;GOOGLE&quot;</span></code>.</p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.idp.Social.account_link_action">
<code class="sig-name descname">account_link_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.account_link_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the account linking action for an IdP user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.account_link_group_includes">
<code class="sig-name descname">account_link_group_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.account_link_group_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Group memberships to determine link candidates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.authorization_binding">
<code class="sig-name descname">authorization_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.authorization_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making an authorization request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.authorization_url">
<code class="sig-name descname">authorization_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.authorization_url" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier issued by AS for the Okta IdP instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret issued by AS for the Okta IdP instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.deprovisioned_action">
<code class="sig-name descname">deprovisioned_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.deprovisioned_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.groups_action">
<code class="sig-name descname">groups_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.groups_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.groups_assignments">
<code class="sig-name descname">groups_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.groups_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.groups_attribute">
<code class="sig-name descname">groups_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.groups_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.groups_filters">
<code class="sig-name descname">groups_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.groups_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.max_clock_skew">
<code class="sig-name descname">max_clock_skew</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.max_clock_skew" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum allowable clock-skew when processing messages from the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.profile_master">
<code class="sig-name descname">profile_master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.profile_master" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the IdP should act as a source of truth for user profile attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.provisioning_action">
<code class="sig-name descname">provisioning_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.provisioning_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioning action for an IdP user during authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML digital signature algorithm used when signing an AuthnRequest message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the IdP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.subject_match_attribute">
<code class="sig-name descname">subject_match_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.subject_match_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.subject_match_type">
<code class="sig-name descname">subject_match_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.subject_match_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.suspended_action">
<code class="sig-name descname">suspended_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.suspended_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.token_binding">
<code class="sig-name descname">token_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.token_binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of making a token request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.token_url">
<code class="sig-name descname">token_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.token_url" title="Permalink to this definition">¶</a></dt>
<dd><p>IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Social IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;FACEBOOK&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LINKEDIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MICROSOFT&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;GOOGLE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.idp.Social.username_template">
<code class="sig-name descname">username_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.idp.Social.username_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Okta EL Expression to generate or transform a unique username for the IdP user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Social.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">match_attribute=None</em>, <em class="sig-param">match_type=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Social.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Social resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_link_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the account linking action for an IdP user.</p></li>
<li><p><strong>account_link_group_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Group memberships to determine link candidates.</p></li>
<li><p><strong>authorization_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making an authorization request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>authorization_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret issued by AS for the Okta IdP instance.</p></li>
<li><p><strong>deprovisioned_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously deprovisioned IdP user during authentication. Can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REACTIVATE&quot;</span></code>.</p></li>
<li><p><strong>groups_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for IdP user’s group memberships. It can be <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code>.</p></li>
<li><p><strong>groups_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta Group IDs to add an IdP user as a member with the <code class="docutils literal notranslate"><span class="pre">&quot;ASSIGN&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>groups_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.</p></li>
<li><p><strong>groups_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Whitelist of Okta Group identifiers that are allowed for the <code class="docutils literal notranslate"><span class="pre">&quot;APPEND&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;SYNC&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">groups_action</span></code>.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code>.</p></li>
<li><p><strong>max_clock_skew</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum allowable clock-skew when processing messages from the IdP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>profile_master</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the IdP should act as a source of truth for user profile attributes.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of protocol to use. It can be <code class="docutils literal notranslate"><span class="pre">&quot;OIDC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OAUTH2&quot;</span></code>.</p></li>
<li><p><strong>provisioning_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioning action for an IdP user during authentication.</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML digital signature algorithm used when signing an AuthnRequest message.</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not to digitally sign an AuthnRequest messages to the IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;REQUEST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be <code class="docutils literal notranslate"><span class="pre">&quot;RESPONSE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ASSERTION&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;ANY&quot;</span></code>.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The scopes of the IdP.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the IdP.</p></li>
<li><p><strong>subject_match_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta user profile attribute for matching transformed IdP username. Only for matchType <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>subject_match_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default it is set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EMAIL&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USERNAME_OR_EMAIL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_ATTRIBUTE&quot;</span></code>.</p></li>
<li><p><strong>suspended_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for a previously suspended IdP user during authentication. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;UNSUSPEND&quot;</span></code></p></li>
<li><p><strong>token_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of making a token request. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-POST&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;HTTP-REDIRECT&quot;</span></code>.</p></li>
<li><p><strong>token_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Social IdP. It can be <code class="docutils literal notranslate"><span class="pre">&quot;FACEBOOK&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;LINKEDIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MICROSOFT&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;GOOGLE&quot;</span></code>.</p></li>
<li><p><strong>username_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Okta EL Expression to generate or transform a unique username for the IdP user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.idp.Social.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Social.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.Social.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.Social.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.idp.get_metadata_saml">
<code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">get_metadata_saml</code><span class="sig-paren">(</span><em class="sig-param">idp_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.get_metadata_saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve SAML IdP metadata from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>idp_id</strong> (<em>str</em>) – The id of the IdP to retrieve metadata for.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.idp.get_saml">
<code class="sig-prename descclassname">pulumi_okta.idp.</code><code class="sig-name descname">get_saml</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.idp.get_saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a SAML IdP from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The id of the idp to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the idp to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
