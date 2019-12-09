---
title: Module auth
title_tag: Module auth | Package pulumi_okta | Python SDK
linktitle: auth
notitle: true
---

<div class="section" id="auth">
<h1>auth<a class="headerlink" href="#auth" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.auth"></span><dl class="class">
<dt id="pulumi_okta.auth.AwaitableGetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">AwaitableGetServerResult</code><span class="sig-paren">(</span><em class="sig-param">audiences=None</em>, <em class="sig-param">credentials_last_rotated=None</em>, <em class="sig-param">credentials_next_rotation=None</em>, <em class="sig-param">credentials_rotation_mode=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.AwaitableGetServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.auth.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param">audiences=None</em>, <em class="sig-param">credentials_last_rotated=None</em>, <em class="sig-param">credentials_next_rotation=None</em>, <em class="sig-param">credentials_rotation_mode=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.audiences">
<code class="sig-name descname">audiences</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.audiences" title="Permalink to this definition">¶</a></dt>
<dd><p>array of audiences,</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.credentials_last_rotated">
<code class="sig-name descname">credentials_last_rotated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.credentials_last_rotated" title="Permalink to this definition">¶</a></dt>
<dd><p>last time credentials were rotated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.credentials_next_rotation">
<code class="sig-name descname">credentials_next_rotation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.credentials_next_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>next time credentials will be rotated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.credentials_rotation_mode">
<code class="sig-name descname">credentials_rotation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.credentials_rotation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>mode of credential rotation, auto or manual.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>description of Authorization server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.kid">
<code class="sig-name descname">kid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.kid" title="Permalink to this definition">¶</a></dt>
<dd><p>auth server key id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the auth server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>the activation status of the authorization server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.GetServerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.auth.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audiences=None</em>, <em class="sig-param">credentials_rotation_mode=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Authorization Server.</p>
<p>This resource allows you to create and configure an Authorization Server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The recipients that the tokens are intended for. This becomes the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim in an access token.</p></li>
<li><p><strong>credentials_rotation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key rotation mode for the authorization server. Can be <code class="docutils literal notranslate"><span class="pre">&quot;AUTO&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;MANUAL&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the authorization server.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows you to use a custom issuer URL. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorization server.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the auth server. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.auth.Server.audiences">
<code class="sig-name descname">audiences</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.audiences" title="Permalink to this definition">¶</a></dt>
<dd><p>The recipients that the tokens are intended for. This becomes the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim in an access token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.credentials_last_rotated">
<code class="sig-name descname">credentials_last_rotated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.credentials_last_rotated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp when the authorization server started to use the <code class="docutils literal notranslate"><span class="pre">kid</span></code> for signing tokens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.credentials_next_rotation">
<code class="sig-name descname">credentials_next_rotation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.credentials_next_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp when the authorization server changes the key for signing tokens. Only returned when <code class="docutils literal notranslate"><span class="pre">credentials_rotation_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;AUTO&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.credentials_rotation_mode">
<code class="sig-name descname">credentials_rotation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.credentials_rotation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The key rotation mode for the authorization server. Can be <code class="docutils literal notranslate"><span class="pre">&quot;AUTO&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;MANUAL&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the authorization server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete URL for a Custom Authorization Server. This becomes the <code class="docutils literal notranslate"><span class="pre">iss</span></code> claim in an access token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to use a custom issuer URL. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.kid">
<code class="sig-name descname">kid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.kid" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the JSON Web Key used for signing tokens issued by the authorization server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the authorization server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.Server.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.Server.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the auth server. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audiences=None</em>, <em class="sig-param">credentials_last_rotated=None</em>, <em class="sig-param">credentials_next_rotation=None</em>, <em class="sig-param">credentials_rotation_mode=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The recipients that the tokens are intended for. This becomes the <code class="docutils literal notranslate"><span class="pre">aud</span></code> claim in an access token.</p></li>
<li><p><strong>credentials_last_rotated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp when the authorization server started to use the <code class="docutils literal notranslate"><span class="pre">kid</span></code> for signing tokens.</p></li>
<li><p><strong>credentials_next_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp when the authorization server changes the key for signing tokens. Only returned when <code class="docutils literal notranslate"><span class="pre">credentials_rotation_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;AUTO&quot;</span></code>.</p></li>
<li><p><strong>credentials_rotation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key rotation mode for the authorization server. Can be <code class="docutils literal notranslate"><span class="pre">&quot;AUTO&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;MANUAL&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the authorization server.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL for a Custom Authorization Server. This becomes the <code class="docutils literal notranslate"><span class="pre">iss</span></code> claim in an access token.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows you to use a custom issuer URL. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;CUSTOM_URL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;ORG_URL&quot;</span></code></p></li>
<li><p><strong>kid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the JSON Web Key used for signing tokens issued by the authorization server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorization server.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the auth server. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerClaim">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">ServerClaim</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_include_in_token=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">claim_type=None</em>, <em class="sig-param">group_filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">value_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerClaim" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Authorization Server Claim.</p>
<p>This resource allows you to create and configure an Authorization Server Claim.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_include_in_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to include claims in token, by default is is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>claim_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the claim is for an access token <code class="docutils literal notranslate"><span class="pre">&quot;RESOURCE&quot;</span></code> or ID token <code class="docutils literal notranslate"><span class="pre">&quot;IDENTITY&quot;</span></code>.</p></li>
<li><p><strong>group_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of group filter if <code class="docutils literal notranslate"><span class="pre">value_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. Can be set to one of the following <code class="docutils literal notranslate"><span class="pre">&quot;STARTS_WITH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EQUALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;CONTAINS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REGEX&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the claim.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of scopes the auth server claim is tied to.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the claim.</p></li>
<li><p><strong>value_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of value of the claim. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_claim.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_claim.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.always_include_in_token">
<code class="sig-name descname">always_include_in_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.always_include_in_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to include claims in token, by default is is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.auth_server_id">
<code class="sig-name descname">auth_server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.auth_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.claim_type">
<code class="sig-name descname">claim_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.claim_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the claim is for an access token <code class="docutils literal notranslate"><span class="pre">&quot;RESOURCE&quot;</span></code> or ID token <code class="docutils literal notranslate"><span class="pre">&quot;IDENTITY&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.group_filter_type">
<code class="sig-name descname">group_filter_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.group_filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of group filter if <code class="docutils literal notranslate"><span class="pre">value_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. Can be set to one of the following <code class="docutils literal notranslate"><span class="pre">&quot;STARTS_WITH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EQUALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;CONTAINS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REGEX&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the claim.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of scopes the auth server claim is tied to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the application. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the claim.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerClaim.value_type">
<code class="sig-name descname">value_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.value_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of value of the claim. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerClaim.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_include_in_token=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">claim_type=None</em>, <em class="sig-param">group_filter_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">value_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerClaim resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_include_in_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to include claims in token, by default is is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>claim_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the claim is for an access token <code class="docutils literal notranslate"><span class="pre">&quot;RESOURCE&quot;</span></code> or ID token <code class="docutils literal notranslate"><span class="pre">&quot;IDENTITY&quot;</span></code>.</p></li>
<li><p><strong>group_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of group filter if <code class="docutils literal notranslate"><span class="pre">value_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. Can be set to one of the following <code class="docutils literal notranslate"><span class="pre">&quot;STARTS_WITH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EQUALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;CONTAINS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REGEX&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the claim.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of scopes the auth server claim is tied to.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the claim.</p></li>
<li><p><strong>value_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of value of the claim. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUPS&quot;</span></code>. It defaults to <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_claim.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_claim.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerClaim.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerClaim.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerClaim.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">ServerPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">client_whitelists=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Authorization Server Policy.</p>
<p>This resource allows you to create and configure an Authorization Server Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Auth Server.</p></li>
<li><p><strong>client_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The clients to whitelist the policy for. <code class="docutils literal notranslate"><span class="pre">[&quot;ALL_CLIENTS&quot;]</span></code> is a special value that can be used to whitelist for all clients. Otherwise it is a list of client ids.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Auth Server Policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Auth Server Policy.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the Auth Server Policy.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Auth Server Policy.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Auth Server Policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.auth_server_id">
<code class="sig-name descname">auth_server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.auth_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Auth Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.client_whitelists">
<code class="sig-name descname">client_whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.client_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>The clients to whitelist the policy for. <code class="docutils literal notranslate"><span class="pre">[&quot;ALL_CLIENTS&quot;]</span></code> is a special value that can be used to whitelist for all clients. Otherwise it is a list of client ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Auth Server Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Auth Server Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the Auth Server Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Auth Server Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicy.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Auth Server Policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">client_whitelists=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Auth Server.</p></li>
<li><p><strong>client_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The clients to whitelist the policy for. <code class="docutils literal notranslate"><span class="pre">[&quot;ALL_CLIENTS&quot;]</span></code> is a special value that can be used to whitelist for all clients. Otherwise it is a list of client ids.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Auth Server Policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Auth Server Policy.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the Auth Server Policy.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Auth Server Policy.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Auth Server Policy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerPolicyClaim">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">ServerPolicyClaim</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_token_lifetime_minutes=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">grant_type_whitelists=None</em>, <em class="sig-param">group_blacklists=None</em>, <em class="sig-param">group_whitelists=None</em>, <em class="sig-param">inline_hook_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">refresh_token_lifetime_minutes=None</em>, <em class="sig-param">refresh_token_window_minutes=None</em>, <em class="sig-param">scope_whitelists=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_blacklists=None</em>, <em class="sig-param">user_whitelists=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Authorization Server Policy Rule.</p>
<p>This resource allows you to create and configure an Authorization Server Policy Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_token_lifetime_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime of access token. Can be set to a value between 5 and 1440.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server ID.</p></li>
<li><p><strong>grant_type_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Accepted grant type values, <code class="docutils literal notranslate"><span class="pre">&quot;authorization_code&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;implicit&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;password&quot;</span></code></p></li>
<li><p><strong>inline_hook_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the inline token to trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server Policy Rule name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the auth server policy rule.</p></li>
<li><p><strong>refresh_token_lifetime_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime of refresh token.</p></li>
<li><p><strong>scope_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scopes allowed for this policy rule. They can be whitelisted by name or all can be whitelisted with <code class="docutils literal notranslate"><span class="pre">&quot;*&quot;</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Auth Server Policy Rule.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Auth Server Policy Rule.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy_rule.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.access_token_lifetime_minutes">
<code class="sig-name descname">access_token_lifetime_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.access_token_lifetime_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Lifetime of access token. Can be set to a value between 5 and 1440.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.auth_server_id">
<code class="sig-name descname">auth_server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.auth_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth Server ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.grant_type_whitelists">
<code class="sig-name descname">grant_type_whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.grant_type_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Accepted grant type values, <code class="docutils literal notranslate"><span class="pre">&quot;authorization_code&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;implicit&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;password&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.inline_hook_id">
<code class="sig-name descname">inline_hook_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.inline_hook_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the inline token to trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth Server Policy Rule name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth Server Policy ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of the auth server policy rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.refresh_token_lifetime_minutes">
<code class="sig-name descname">refresh_token_lifetime_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.refresh_token_lifetime_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Lifetime of refresh token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.scope_whitelists">
<code class="sig-name descname">scope_whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.scope_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Scopes allowed for this policy rule. They can be whitelisted by name or all can be whitelisted with <code class="docutils literal notranslate"><span class="pre">&quot;*&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Auth Server Policy Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerPolicyClaim.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Auth Server Policy Rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerPolicyClaim.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_token_lifetime_minutes=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">grant_type_whitelists=None</em>, <em class="sig-param">group_blacklists=None</em>, <em class="sig-param">group_whitelists=None</em>, <em class="sig-param">inline_hook_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">refresh_token_lifetime_minutes=None</em>, <em class="sig-param">refresh_token_window_minutes=None</em>, <em class="sig-param">scope_whitelists=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_blacklists=None</em>, <em class="sig-param">user_whitelists=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerPolicyClaim resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_token_lifetime_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime of access token. Can be set to a value between 5 and 1440.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server ID.</p></li>
<li><p><strong>grant_type_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Accepted grant type values, <code class="docutils literal notranslate"><span class="pre">&quot;authorization_code&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;implicit&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;password&quot;</span></code></p></li>
<li><p><strong>inline_hook_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the inline token to trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server Policy Rule name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server Policy ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of the auth server policy rule.</p></li>
<li><p><strong>refresh_token_lifetime_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime of refresh token.</p></li>
<li><p><strong>scope_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scopes allowed for this policy rule. They can be whitelisted by name or all can be whitelisted with <code class="docutils literal notranslate"><span class="pre">&quot;*&quot;</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Auth Server Policy Rule.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Auth Server Policy Rule.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy_rule.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_policy_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerPolicyClaim.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerPolicyClaim.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerPolicyClaim.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerScope">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">ServerScope</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">consent=None</em>, <em class="sig-param">default=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">metadata_publish=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerScope" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Authorization Server Scope.</p>
<p>This resource allows you to create and configure an Authorization Server Scope.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server ID.</p></li>
<li><p><strong>consent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a consent dialog is needed for the scope. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;IMPLICIT&quot;</span></code>.</p></li>
<li><p><strong>default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A default scope will be returned in an access token when the client omits the scope parameter in a token request, provided this scope is allowed as part of the access policy rule.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Auth Server Scope.</p></li>
<li><p><strong>metadata_publish</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to publish metadata or not. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;ALL_CLIENTS&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NO_CLIENTS&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server scope name.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_scope.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_scope.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.auth_server_id">
<code class="sig-name descname">auth_server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.auth_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth Server ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.consent">
<code class="sig-name descname">consent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.consent" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a consent dialog is needed for the scope. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;IMPLICIT&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.default">
<code class="sig-name descname">default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.default" title="Permalink to this definition">¶</a></dt>
<dd><p>A default scope will be returned in an access token when the client omits the scope parameter in a token request, provided this scope is allowed as part of the access policy rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Auth Server Scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.metadata_publish">
<code class="sig-name descname">metadata_publish</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.metadata_publish" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to publish metadata or not. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;ALL_CLIENTS&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NO_CLIENTS&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.auth.ServerScope.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.auth.ServerScope.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth Server scope name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerScope.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_server_id=None</em>, <em class="sig-param">consent=None</em>, <em class="sig-param">default=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">metadata_publish=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerScope.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerScope resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server ID.</p></li>
<li><p><strong>consent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a consent dialog is needed for the scope. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;REQUIRED&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;IMPLICIT&quot;</span></code>.</p></li>
<li><p><strong>default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A default scope will be returned in an access token when the client omits the scope parameter in a token request, provided this scope is allowed as part of the access policy rule.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Auth Server Scope.</p></li>
<li><p><strong>metadata_publish</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to publish metadata or not. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;ALL_CLIENTS&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NO_CLIENTS&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth Server scope name.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_scope.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_scope.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.auth.ServerScope.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerScope.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.ServerScope.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.ServerScope.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.auth.get_server">
<code class="sig-prename descclassname">pulumi_okta.auth.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.auth.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve an auth server from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the auth server to retrieve.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/auth_server.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/auth_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
