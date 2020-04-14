---
title: Module app
title_tag: Module app | Package pulumi_okta | Python SDK
linktitle: app
notitle: true
---

<div class="section" id="app">
<h1>app<a class="headerlink" href="#app" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.app"></span><dl class="class">
<dt id="pulumi_okta.app.AutoLogin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">AutoLogin</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_redirect_url=None</em>, <em class="sig-param">sign_on_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AutoLogin" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Auto Login Okta Application.</p>
<p>This resource allows you to create and configure an Auto Login Okta Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_auto_login.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_auto_login.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>credentials_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application credentials scheme</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tells Okta to use an existing application in their application catalog, as opposed to a custom application.</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>sign_on_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Post login redirect URL</p></li>
<li><p><strong>sign_on_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.credentials_scheme">
<code class="sig-name descname">credentials_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.credentials_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Application credentials scheme</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name assigned to the application by Okta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Tells Okta to use an existing application in their application catalog, as opposed to a custom application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.reveal_password">
<code class="sig-name descname">reveal_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.reveal_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow user to reveal password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.shared_password">
<code class="sig-name descname">shared_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.shared_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared password, required for certain schemes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.shared_username">
<code class="sig-name descname">shared_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.shared_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared username, required for certain schemes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.sign_on_redirect_url">
<code class="sig-name descname">sign_on_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.sign_on_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Post login redirect URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.sign_on_url">
<code class="sig-name descname">sign_on_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.sign_on_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.AutoLogin.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.AutoLogin.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.AutoLogin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">sign_on_redirect_url=None</em>, <em class="sig-param">sign_on_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AutoLogin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AutoLogin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>credentials_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application credentials scheme</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name assigned to the application by Okta.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tells Okta to use an existing application in their application catalog, as opposed to a custom application.</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>sign_on_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Post login redirect URL</p></li>
<li><p><strong>sign_on_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.AutoLogin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AutoLogin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.AutoLogin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AutoLogin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.AwaitableGetAppResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">AwaitableGetAppResult</code><span class="sig-paren">(</span><em class="sig-param">active_only=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AwaitableGetAppResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.AwaitableGetMetadataSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">AwaitableGetMetadataSamlResult</code><span class="sig-paren">(</span><em class="sig-param">app_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">want_authn_requests_signed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AwaitableGetMetadataSamlResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.AwaitableGetSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">AwaitableGetSamlResult</code><span class="sig-paren">(</span><em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">active_only=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.AwaitableGetSamlResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.BasicAuth">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">BasicAuth</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_url=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.BasicAuth" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Bsaic Auth Application.</p>
<p>This resource allows you to create and configure a Basic Auth Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_basic_auth.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_basic_auth.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the authenticating site for this app.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the sign-in page for this app.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.auth_url">
<code class="sig-name descname">auth_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.auth_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the authenticating site for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the sign-in page for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.BasicAuth.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.BasicAuth.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.BasicAuth.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_url=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.BasicAuth.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BasicAuth resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the authenticating site for this app.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the sign-in page for this app.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.BasicAuth.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.BasicAuth.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.BasicAuth.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.BasicAuth.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Bookmark">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">Bookmark</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">request_integration=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Bookmark" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Bookmark Application.</p>
<p>This resource allows you to create and configure a Bookmark Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_bookmark.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_bookmark.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>request_integration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Would you like Okta to add an integration for this app?</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the bookmark.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.request_integration">
<code class="sig-name descname">request_integration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.request_integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Would you like Okta to add an integration for this app?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the bookmark.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Bookmark.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Bookmark.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Bookmark.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_integration=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Bookmark.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Bookmark resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>request_integration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Would you like Okta to add an integration for this app?</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the bookmark.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Bookmark.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Bookmark.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Bookmark.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Bookmark.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.GetAppResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">GetAppResult</code><span class="sig-paren">(</span><em class="sig-param">active_only=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GetAppResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApp.</p>
<dl class="attribute">
<dt id="pulumi_okta.app.GetAppResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetAppResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">description</span></code> of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetAppResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetAppResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">id</span></code> of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetAppResult.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetAppResult.label" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">label</span></code> of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetAppResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetAppResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">name</span></code> of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetAppResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetAppResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">status</span></code> of application.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.GetMetadataSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">GetMetadataSamlResult</code><span class="sig-paren">(</span><em class="sig-param">app_id=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">want_authn_requests_signed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMetadataSaml.</p>
<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>public certificate from application metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.entity_id">
<code class="sig-name descname">entity_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.entity_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity URL for instance <code class="docutils literal notranslate"><span class="pre">https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.http_post_binding">
<code class="sig-name descname">http_post_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.http_post_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.http_redirect_binding">
<code class="sig-name descname">http_redirect_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.http_redirect_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>raw metadata of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetMetadataSamlResult.want_authn_requests_signed">
<code class="sig-name descname">want_authn_requests_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetMetadataSamlResult.want_authn_requests_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether authn requests are signed.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.GetSamlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">GetSamlResult</code><span class="sig-paren">(</span><em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">active_only=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GetSamlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSaml.</p>
<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.accessibility_login_redirect_url">
<code class="sig-name descname">accessibility_login_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.accessibility_login_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom login page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.app_settings_json">
<code class="sig-name descname">app_settings_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.app_settings_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Application settings in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.assertion_signed">
<code class="sig-name descname">assertion_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.assertion_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML assertion is digitally signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.attribute_statements">
<code class="sig-name descname">attribute_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.attribute_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Attribute statements.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>Audience restriction.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.authn_context_class_ref">
<code class="sig-name descname">authn_context_class_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.authn_context_class_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML authentication context class for the assertion’s authentication statement.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.default_relay_state">
<code class="sig-name descname">default_relay_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.default_relay_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies a specific application resource in an IDP initiated SSO scenario.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>description of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.digest_algorithm">
<code class="sig-name descname">digest_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.digest_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the digest algorithm used to digitally sign the SAML assertion and response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.features">
<code class="sig-name descname">features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.features" title="Permalink to this definition">¶</a></dt>
<dd><p>features enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.honor_force_authn">
<code class="sig-name descname">honor_force_authn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.honor_force_authn" title="Permalink to this definition">¶</a></dt>
<dd><p>Prompt user to re-authenticate if SP asks for it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.idp_issuer">
<code class="sig-name descname">idp_issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.idp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML issuer ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate key ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.label" title="Permalink to this definition">¶</a></dt>
<dd><p>label of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.recipient">
<code class="sig-name descname">recipient</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.recipient" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the app may present the SAML assertion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.request_compressed">
<code class="sig-name descname">request_compressed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.request_compressed" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether the request is compressed or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.response_signed">
<code class="sig-name descname">response_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.response_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML auth response message is digitally signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.signature_algorithm">
<code class="sig-name descname">signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Signature algorithm used ot digitally sign the assertion and response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.sp_issuer">
<code class="sig-name descname">sp_issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.sp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML service provider issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.sso_url">
<code class="sig-name descname">sso_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.sso_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Single Sign on Url.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>status of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.subject_name_id_format">
<code class="sig-name descname">subject_name_id_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.subject_name_id_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML processing rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.subject_name_id_template">
<code class="sig-name descname">subject_name_id_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.subject_name_id_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Template for app user’s username when a user is assigned to the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.user_name_template_suffix">
<code class="sig-name descname">user_name_template_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.user_name_template_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template suffix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GetSamlResult.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GetSamlResult.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.app.GroupAssignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">GroupAssignment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GroupAssignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Assigns a group to an application.</p>
<p>This resource allows you to create an App Group assignment.</p>
<p><strong>When using this resource, make sure to add the following ``lifefycle`` argument to the application resource you are assigning to:</strong></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_group_assignment.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_group_assignment.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application to assign a group to.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group to assign the app to.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON document containing <a class="reference external" href="https://developer.okta.com/docs/reference/api/apps/#profile-object">application profile</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.app.GroupAssignment.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application to assign a group to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GroupAssignment.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the group to assign the app to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.GroupAssignment.profile">
<code class="sig-name descname">profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON document containing <a class="reference external" href="https://developer.okta.com/docs/reference/api/apps/#profile-object">application profile</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.GroupAssignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupAssignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application to assign a group to.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group to assign the app to.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON document containing <a class="reference external" href="https://developer.okta.com/docs/reference/api/apps/#profile-object">application profile</a></p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.GroupAssignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.GroupAssignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.GroupAssignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.OAuth">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">OAuth</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_key_rotation=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">client_basic_secret=None</em>, <em class="sig-param">client_uri=None</em>, <em class="sig-param">consent_method=None</em>, <em class="sig-param">custom_client_id=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">login_uri=None</em>, <em class="sig-param">logo_uri=None</em>, <em class="sig-param">omit_secret=None</em>, <em class="sig-param">policy_uri=None</em>, <em class="sig-param">post_logout_redirect_uris=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">redirect_uris=None</em>, <em class="sig-param">response_types=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">token_endpoint_auth_method=None</em>, <em class="sig-param">tos_uri=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuth" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an OIDC Application.</p>
<p>This resource allows you to create and configure an OIDC Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_oauth.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_oauth.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requested key rotation mode.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>client_basic_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.</p></li>
<li><p><strong>client_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a web page providing information about the client.</p></li>
<li><p><strong>consent_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED. Default value is TRUSTED.</p></li>
<li><p><strong>custom_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This property allows you to set the application’s client id.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 grant types. Conditional validation params found here <a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per app type.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The groups assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code>.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a custom domain URL as the issuer of ID token for this client.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>login_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that initiates login.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that references a logo for the client.</p></li>
<li><p><strong>omit_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false your app will be recreated.</p></li>
<li><p><strong>policy_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to web page providing client policy document.</p></li>
<li><p><strong>post_logout_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for redirection after logout.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON that represents an OAuth application’s profile.</p></li>
<li><p><strong>redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for use in the redirect-based flow. This is required for all application types except service.</p></li>
<li><p><strong>response_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 response type strings.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requested authentication method for the token endpoint. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_post&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_jwt&quot;</span></code>.</p></li>
<li><p><strong>tos_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to web page providing client tos (terms of service).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of OAuth application.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.User</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.auto_key_rotation">
<code class="sig-name descname">auto_key_rotation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.auto_key_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>Requested key rotation mode.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.client_basic_secret">
<code class="sig-name descname">client_basic_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.client_basic_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The client ID of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.client_uri">
<code class="sig-name descname">client_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.client_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to a web page providing information about the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.consent_method">
<code class="sig-name descname">consent_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.consent_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED. Default value is TRUSTED.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.custom_client_id">
<code class="sig-name descname">custom_client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.custom_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This property allows you to set the application’s client id.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.grant_types">
<code class="sig-name descname">grant_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.grant_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of OAuth 2.0 grant types. Conditional validation params found here <a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per app type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The groups assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a custom domain URL as the issuer of ID token for this client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.login_uri">
<code class="sig-name descname">login_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.login_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that initiates login.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.logo_uri">
<code class="sig-name descname">logo_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.logo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that references a logo for the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name assigned to the application by Okta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.omit_secret">
<code class="sig-name descname">omit_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.omit_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false your app will be recreated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.policy_uri">
<code class="sig-name descname">policy_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.policy_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to web page providing client policy document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.post_logout_redirect_uris">
<code class="sig-name descname">post_logout_redirect_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.post_logout_redirect_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for redirection after logout.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.profile">
<code class="sig-name descname">profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON that represents an OAuth application’s profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.redirect_uris">
<code class="sig-name descname">redirect_uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.redirect_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for use in the redirect-based flow. This is required for all application types except service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.response_types">
<code class="sig-name descname">response_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.response_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of OAuth 2.0 response type strings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.token_endpoint_auth_method">
<code class="sig-name descname">token_endpoint_auth_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.token_endpoint_auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Requested authentication method for the token endpoint. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_post&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_jwt&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.tos_uri">
<code class="sig-name descname">tos_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.tos_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to web page providing client tos (terms of service).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of OAuth application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.OAuth.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuth.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The users assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.User</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.OAuth.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_key_rotation=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">client_basic_secret=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">client_uri=None</em>, <em class="sig-param">consent_method=None</em>, <em class="sig-param">custom_client_id=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">login_uri=None</em>, <em class="sig-param">logo_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">omit_secret=None</em>, <em class="sig-param">policy_uri=None</em>, <em class="sig-param">post_logout_redirect_uris=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">redirect_uris=None</em>, <em class="sig-param">response_types=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">token_endpoint_auth_method=None</em>, <em class="sig-param">tos_uri=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuth.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OAuth resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requested key rotation mode.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>client_basic_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client ID of the application.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret of the application.</p></li>
<li><p><strong>client_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a web page providing information about the client.</p></li>
<li><p><strong>consent_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED. Default value is TRUSTED.</p></li>
<li><p><strong>custom_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This property allows you to set the application’s client id.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 grant types. Conditional validation params found here <a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per app type.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The groups assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code>.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a custom domain URL as the issuer of ID token for this client.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s display name.</p></li>
<li><p><strong>login_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that initiates login.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that references a logo for the client.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name assigned to the application by Okta.</p></li>
<li><p><strong>omit_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false your app will be recreated.</p></li>
<li><p><strong>policy_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to web page providing client policy document.</p></li>
<li><p><strong>post_logout_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for redirection after logout.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON that represents an OAuth application’s profile.</p></li>
<li><p><strong>redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for use in the redirect-based flow. This is required for all application types except service.</p></li>
<li><p><strong>response_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 response type strings.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the application, by default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requested authentication method for the token endpoint. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_post&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;client_secret_jwt&quot;</span></code>.</p></li>
<li><p><strong>tos_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to web page providing client tos (terms of service).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of OAuth application.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. It is recommended not to use this and instead use <code class="docutils literal notranslate"><span class="pre">app.User</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.OAuth.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuth.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.OAuth.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuth.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.OAuthRedirectUri">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">OAuthRedirectUri</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuthRedirectUri" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OAuthRedirectUri resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] uri: Redirect URI to append to Okta OIDC application.</p>
<dl class="attribute">
<dt id="pulumi_okta.app.OAuthRedirectUri.uri">
<code class="sig-name descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.OAuthRedirectUri.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Redirect URI to append to Okta OIDC application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.OAuthRedirectUri.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuthRedirectUri.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OAuthRedirectUri resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Redirect URI to append to Okta OIDC application.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.OAuthRedirectUri.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuthRedirectUri.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.OAuthRedirectUri.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.OAuthRedirectUri.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Saml">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">Saml</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">key_years_valid=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an SAML Application.</p>
<p>This resource allows you to create and configure an SAML Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_saml.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_saml.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_login_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom login page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service.</p></li>
<li><p><strong>app_settings_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application settings in JSON format.</p></li>
<li><p><strong>assertion_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML assertion is digitally signed.</p></li>
<li><p><strong>attribute_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of SAML Attribute statements.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Audience restriction.</p></li>
<li><p><strong>authn_context_class_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML authentication context class for the assertion’s authentication statement.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>default_relay_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies a specific application resource in an IDP initiated SSO scenario.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.</p></li>
<li><p><strong>digest_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the digest algorithm used to digitally sign the SAML assertion and response.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – features enabled.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>honor_force_authn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prompt user to re-authenticate if SP asks for it.</p></li>
<li><p><strong>idp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML issuer ID.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate name. This modulates the rotation of keys. New name == new key.</p></li>
<li><p><strong>key_years_valid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of years the certificate is valid.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – label of application.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of application from the Okta Integration Network, if not included a custom app will be created.</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the app may present the SAML assertion.</p></li>
<li><p><strong>request_compressed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether the request is compressed or not.</p></li>
<li><p><strong>response_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML auth response message is digitally signed.</p></li>
<li><p><strong>signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signature algorithm used ot digitally sign the assertion and response.</p></li>
<li><p><strong>sp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML service provider issuer.</p></li>
<li><p><strong>sso_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Single Sign on Url.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – status of application.</p></li>
<li><p><strong>subject_name_id_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML processing rules.</p></li>
<li><p><strong>subject_name_id_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Template for app user’s username when a user is assigned to the app.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template.</p></li>
<li><p><strong>user_name_template_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template suffix.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of group attribute filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Filter value to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the attribute statement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The attribute namespace. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:uri&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:basic&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of attribute statement value. Can be <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUP&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of values to use.</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - id of application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.Saml.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.accessibility_login_redirect_url">
<code class="sig-name descname">accessibility_login_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.accessibility_login_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom login page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.app_settings_json">
<code class="sig-name descname">app_settings_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.app_settings_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Application settings in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.assertion_signed">
<code class="sig-name descname">assertion_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.assertion_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML assertion is digitally signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.attribute_statements">
<code class="sig-name descname">attribute_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.attribute_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>List of SAML Attribute statements.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of group attribute filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Filter value to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the attribute statement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The attribute namespace. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:uri&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:basic&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of attribute statement value. Can be <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUP&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of values to use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>Audience restriction.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.authn_context_class_ref">
<code class="sig-name descname">authn_context_class_ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.authn_context_class_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML authentication context class for the assertion’s authentication statement.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw signing certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.default_relay_state">
<code class="sig-name descname">default_relay_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.default_relay_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies a specific application resource in an IDP initiated SSO scenario.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.digest_algorithm">
<code class="sig-name descname">digest_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.digest_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the digest algorithm used to digitally sign the SAML assertion and response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.entity_key">
<code class="sig-name descname">entity_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.entity_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity ID, the ID portion of the <code class="docutils literal notranslate"><span class="pre">entity_url</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.entity_url">
<code class="sig-name descname">entity_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.entity_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity URL for instance <a class="reference external" href="http://www.okta.com/exk1fcia6d6EMsf331d8">http://www.okta.com/exk1fcia6d6EMsf331d8</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.features">
<code class="sig-name descname">features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.features" title="Permalink to this definition">¶</a></dt>
<dd><p>features enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.honor_force_authn">
<code class="sig-name descname">honor_force_authn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.honor_force_authn" title="Permalink to this definition">¶</a></dt>
<dd><p>Prompt user to re-authenticate if SP asks for it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.http_post_binding">
<code class="sig-name descname">http_post_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.http_post_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</span></code> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.http_redirect_binding">
<code class="sig-name descname">http_redirect_binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.http_redirect_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</span></code> location from the SAML metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.idp_issuer">
<code class="sig-name descname">idp_issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.idp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML issuer ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate key ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.key_name">
<code class="sig-name descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate name. This modulates the rotation of keys. New name == new key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.key_years_valid">
<code class="sig-name descname">key_years_valid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.key_years_valid" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of years the certificate is valid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.label" title="Permalink to this definition">¶</a></dt>
<dd><p>label of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw SAML metadata in XML.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the attribute statement.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>name of application from the Okta Integration Network, if not included a custom app will be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.recipient">
<code class="sig-name descname">recipient</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.recipient" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the app may present the SAML assertion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.request_compressed">
<code class="sig-name descname">request_compressed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.request_compressed" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether the request is compressed or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.response_signed">
<code class="sig-name descname">response_signed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.response_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML auth response message is digitally signed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.signature_algorithm">
<code class="sig-name descname">signature_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Signature algorithm used ot digitally sign the assertion and response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.sp_issuer">
<code class="sig-name descname">sp_issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.sp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML service provider issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.sso_url">
<code class="sig-name descname">sso_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.sso_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Single Sign on Url.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.status" title="Permalink to this definition">¶</a></dt>
<dd><p>status of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.subject_name_id_format">
<code class="sig-name descname">subject_name_id_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.subject_name_id_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML processing rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.subject_name_id_template">
<code class="sig-name descname">subject_name_id_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.subject_name_id_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Template for app user’s username when a user is assigned to the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.user_name_template_suffix">
<code class="sig-name descname">user_name_template_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.user_name_template_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template suffix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Saml.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Saml.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - id of application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Saml.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">entity_key=None</em>, <em class="sig-param">entity_url=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">key_years_valid=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Saml.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Saml resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_login_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom login page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service.</p></li>
<li><p><strong>app_settings_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application settings in JSON format.</p></li>
<li><p><strong>assertion_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML assertion is digitally signed.</p></li>
<li><p><strong>attribute_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of SAML Attribute statements.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Audience restriction.</p></li>
<li><p><strong>authn_context_class_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML authentication context class for the assertion’s authentication statement.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The raw signing certificate.</p></li>
<li><p><strong>default_relay_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies a specific application resource in an IDP initiated SSO scenario.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.</p></li>
<li><p><strong>digest_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the digest algorithm used to digitally sign the SAML assertion and response.</p></li>
<li><p><strong>entity_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity ID, the ID portion of the <code class="docutils literal notranslate"><span class="pre">entity_url</span></code>.</p></li>
<li><p><strong>entity_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity URL for instance <a class="reference external" href="http://www.okta.com/exk1fcia6d6EMsf331d8">http://www.okta.com/exk1fcia6d6EMsf331d8</a>.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – features enabled.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>honor_force_authn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prompt user to re-authenticate if SP asks for it.</p></li>
<li><p><strong>http_post_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</span></code> location from the SAML metadata.</p></li>
<li><p><strong>http_redirect_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</span></code> location from the SAML metadata.</p></li>
<li><p><strong>idp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML issuer ID.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate key ID.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate name. This modulates the rotation of keys. New name == new key.</p></li>
<li><p><strong>key_years_valid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of years the certificate is valid.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – label of application.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The raw SAML metadata in XML.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the attribute statement.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of application from the Okta Integration Network, if not included a custom app will be created.</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the app may present the SAML assertion.</p></li>
<li><p><strong>request_compressed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether the request is compressed or not.</p></li>
<li><p><strong>response_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML auth response message is digitally signed.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signature algorithm used ot digitally sign the assertion and response.</p></li>
<li><p><strong>sp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML service provider issuer.</p></li>
<li><p><strong>sso_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Single Sign on Url.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – status of application.</p></li>
<li><p><strong>subject_name_id_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML processing rules.</p></li>
<li><p><strong>subject_name_id_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Template for app user’s username when a user is assigned to the app.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template.</p></li>
<li><p><strong>user_name_template_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template suffix.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of group attribute filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Filter value to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the attribute statement.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The attribute namespace. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:uri&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;urn:oasis:names:tc:SAML:2.0:attrname-format:basic&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of attribute statement value. Can be <code class="docutils literal notranslate"><span class="pre">&quot;EXPRESSION&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;GROUP&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of values to use.</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - id of application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Saml.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Saml.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Saml.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Saml.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.SecurePasswordStore">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">SecurePasswordStore</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">optional_field1=None</em>, <em class="sig-param">optional_field1_value=None</em>, <em class="sig-param">optional_field2=None</em>, <em class="sig-param">optional_field2_value=None</em>, <em class="sig-param">optional_field3=None</em>, <em class="sig-param">optional_field3_value=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Secure Password Store Application.</p>
<p>This resource allows you to create and configure a Secure Password Store Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_secure_password_store.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_secure_password_store.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>credentials_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application credentials scheme. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_USERNAME_AND_PASSWORD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ADMIN_SETS_CREDENTIALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_PASSWORD_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EXTERNAL_PASSWORD_SYNC&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;SHARED_USERNAME_AND_PASSWORD&quot;</span></code>.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>optional_field1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field1_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>optional_field2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field2_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>optional_field3</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field3_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field.</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password.</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.credentials_scheme">
<code class="sig-name descname">credentials_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.credentials_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Application credentials scheme. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_USERNAME_AND_PASSWORD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ADMIN_SETS_CREDENTIALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_PASSWORD_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EXTERNAL_PASSWORD_SYNC&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;SHARED_USERNAME_AND_PASSWORD&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name assigned to the application by Okta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field1">
<code class="sig-name descname">optional_field1</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field1" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field1_value">
<code class="sig-name descname">optional_field1_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field1_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field2">
<code class="sig-name descname">optional_field2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field2" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field2_value">
<code class="sig-name descname">optional_field2_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field2_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field3">
<code class="sig-name descname">optional_field3</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field3" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.optional_field3_value">
<code class="sig-name descname">optional_field3_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.optional_field3_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in the login form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.password_field">
<code class="sig-name descname">password_field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.password_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.reveal_password">
<code class="sig-name descname">reveal_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.reveal_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow user to reveal password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.shared_password">
<code class="sig-name descname">shared_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.shared_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared password, required for certain schemes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.shared_username">
<code class="sig-name descname">shared_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.shared_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared username, required for certain schemes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The default username assigned to each user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username template type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.username_field">
<code class="sig-name descname">username_field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.username_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.SecurePasswordStore.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.SecurePasswordStore.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">optional_field1=None</em>, <em class="sig-param">optional_field1_value=None</em>, <em class="sig-param">optional_field2=None</em>, <em class="sig-param">optional_field2_value=None</em>, <em class="sig-param">optional_field3=None</em>, <em class="sig-param">optional_field3_value=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurePasswordStore resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>credentials_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application credentials scheme. Can be set to <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_USERNAME_AND_PASSWORD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ADMIN_SETS_CREDENTIALS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EDIT_PASSWORD_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EXTERNAL_PASSWORD_SYNC&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;SHARED_USERNAME_AND_PASSWORD&quot;</span></code>.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name assigned to the application by Okta.</p></li>
<li><p><strong>optional_field1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field1_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>optional_field2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field2_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>optional_field3</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form.</p></li>
<li><p><strong>optional_field3_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in the login form.</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field.</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password.</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default username assigned to each user.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username template type.</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.SecurePasswordStore.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.SecurePasswordStore.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.SecurePasswordStore.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Swa">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">Swa</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_field=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Swa" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an SWA Application.</p>
<p>This resource allows you to create and configure an SWA Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_swa.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_swa.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>button_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of application from the Okta Integration Network, if not included a custom app will be created.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex.</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.Swa.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.button_field">
<code class="sig-name descname">button_field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.button_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login button field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name assigned to the application by Okta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.password_field">
<code class="sig-name descname">password_field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.password_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>name of application from the Okta Integration Network, if not included a custom app will be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.url_regex">
<code class="sig-name descname">url_regex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.url_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regex that further restricts URL to the specified regex.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The default username assigned to each user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username template type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.username_field">
<code class="sig-name descname">username_field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.username_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.Swa.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.Swa.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Swa.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_field=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Swa.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Swa resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>button_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name assigned to the application by Okta.</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of application from the Okta Integration Network, if not included a custom app will be created.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default username assigned to each user.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username template type.</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.Swa.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Swa.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.Swa.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.Swa.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.ThreeField">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">ThreeField</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_selector=None</em>, <em class="sig-param">extra_field_selector=None</em>, <em class="sig-param">extra_field_value=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">password_selector=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">username_selector=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.ThreeField" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Three Field Application.</p>
<p>This resource allows you to create and configure an Three Field Application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_three_field.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_three_field.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>button_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field CSS selector.</p></li>
<li><p><strong>extra_field_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Extra field CSS selector.</p></li>
<li><p><strong>extra_field_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value for extra form field.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>password_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field CSS selector.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex.</p></li>
<li><p><strong>username_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field CSS selector.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.button_selector">
<code class="sig-name descname">button_selector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.button_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login button field CSS selector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.extra_field_selector">
<code class="sig-name descname">extra_field_selector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.extra_field_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra field CSS selector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.extra_field_value">
<code class="sig-name descname">extra_field_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.extra_field_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Value for extra form field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.hide_web">
<code class="sig-name descname">hide_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name assigned to the application by Okta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.password_selector">
<code class="sig-name descname">password_selector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.password_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field CSS selector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.url_regex">
<code class="sig-name descname">url_regex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.url_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regex that further restricts URL to the specified regex.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The default username assigned to each user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username template type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.username_selector">
<code class="sig-name descname">username_selector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.username_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field CSS selector.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.ThreeField.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.ThreeField.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.ThreeField.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_selector=None</em>, <em class="sig-param">extra_field_selector=None</em>, <em class="sig-param">extra_field_value=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_selector=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_selector=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.ThreeField.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThreeField resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service. By default it is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>button_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field CSS selector.</p></li>
<li><p><strong>extra_field_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Extra field CSS selector.</p></li>
<li><p><strong>extra_field_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value for extra form field.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application. See <code class="docutils literal notranslate"><span class="pre">app.GroupAssignment</span></code> for a more flexible approach.</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the Application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name assigned to the application by Okta.</p></li>
<li><p><strong>password_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field CSS selector.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application. By default it is <code class="docutils literal notranslate"><span class="pre">&quot;ACTIVE&quot;</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL.</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex.</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default username assigned to each user.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username template type.</p></li>
<li><p><strong>username_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field CSS selector.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The users assigned to the application. See <code class="docutils literal notranslate"><span class="pre">app.User</span></code> for a more flexible approach.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.ThreeField.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.ThreeField.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.ThreeField.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.ThreeField.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Application User.</p>
<p>This resource allows you to create and configure an Application User.</p>
<p><strong>When using this resource, make sure to add the following ``lifefycle`` argument to the application resource you are assigning to:</strong></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App to associate user with.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON profile of the App User.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User to associate the application with.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for the app user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.app.User.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.User.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>App to associate user with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.User.profile">
<code class="sig-name descname">profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.User.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON profile of the App User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.User.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.User.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User to associate the application with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.User.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username to use for the app user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App to associate user with.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to use.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON profile of the App User.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User to associate the application with.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username to use for the app user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.UserBaseSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">UserBaseSchema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application User Base Schema property.</p>
<p>This resource allows you to configure a base app user schema property.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user_base_schema.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user_base_schema.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s ID the user schema property should be assigned to.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s ID the user schema property should be assigned to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.index">
<code class="sig-name descname">index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.index" title="Permalink to this definition">¶</a></dt>
<dd><p>The property name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.master">
<code class="sig-name descname">master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.master" title="Permalink to this definition">¶</a></dt>
<dd><p>Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.required">
<code class="sig-name descname">required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the property is required for this application’s users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The property display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserBaseSchema.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.UserBaseSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserBaseSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s ID the user schema property should be assigned to.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.UserBaseSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.UserBaseSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserBaseSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.UserSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">UserSchema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">array_enums=None</em>, <em class="sig-param">array_one_ofs=None</em>, <em class="sig-param">array_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enums=None</em>, <em class="sig-param">external_name=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">max_length=None</em>, <em class="sig-param">min_length=None</em>, <em class="sig-param">one_ofs=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Application User Schema property.</p>
<p>This resource allows you to create and configure a custom user schema property and associate it with an application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user_schema.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/app_user_schema.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s ID the user custom schema property should be assigned to.</p></li>
<li><p><strong>array_enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values that an array property’s items can be set to.</p></li>
<li><p><strong>array_one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Display name and value an enum array can be set to.</p></li>
<li><p><strong>array_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user schema property.</p></li>
<li><p><strong>enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p></li>
<li><p><strong>external_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – External name of the user schema property.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>max_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of maps containing a mapping for display name to enum value.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – determines whether an app user attribute can be set at the Individual or Group Level.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – display name for the enum value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>array_one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<p>The <strong>one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Application’s ID the user custom schema property should be assigned to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.array_enums">
<code class="sig-name descname">array_enums</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.array_enums" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values that an array property’s items can be set to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.array_one_ofs">
<code class="sig-name descname">array_one_ofs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.array_one_ofs" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name and value an enum array can be set to.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.array_type">
<code class="sig-name descname">array_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.array_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the user schema property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.enums">
<code class="sig-name descname">enums</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.enums" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.external_name">
<code class="sig-name descname">external_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.external_name" title="Permalink to this definition">¶</a></dt>
<dd><p>External name of the user schema property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.index">
<code class="sig-name descname">index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.index" title="Permalink to this definition">¶</a></dt>
<dd><p>The property name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.master">
<code class="sig-name descname">master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.master" title="Permalink to this definition">¶</a></dt>
<dd><p>Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.max_length">
<code class="sig-name descname">max_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.max_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.min_length">
<code class="sig-name descname">min_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.one_ofs">
<code class="sig-name descname">one_ofs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.one_ofs" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of maps containing a mapping for display name to enum value.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.required">
<code class="sig-name descname">required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the property is required for this application’s users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>determines whether an app user attribute can be set at the Individual or Group Level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.title" title="Permalink to this definition">¶</a></dt>
<dd><p>display name for the enum value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.app.UserSchema.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.app.UserSchema.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.UserSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">array_enums=None</em>, <em class="sig-param">array_one_ofs=None</em>, <em class="sig-param">array_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enums=None</em>, <em class="sig-param">external_name=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">max_length=None</em>, <em class="sig-param">min_length=None</em>, <em class="sig-param">one_ofs=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Application’s ID the user custom schema property should be assigned to.</p></li>
<li><p><strong>array_enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values that an array property’s items can be set to.</p></li>
<li><p><strong>array_one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Display name and value an enum array can be set to.</p></li>
<li><p><strong>array_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user schema property.</p></li>
<li><p><strong>enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p></li>
<li><p><strong>external_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – External name of the user schema property.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>max_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of maps containing a mapping for display name to enum value.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – determines whether an app user attribute can be set at the Individual or Group Level.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – display name for the enum value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>array_one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<p>The <strong>one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.app.UserSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.UserSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.UserSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.app.get_app">
<code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">get_app</code><span class="sig-paren">(</span><em class="sig-param">active_only=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.get_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the collaborators for a given repository.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>active_only</strong> (<em>bool</em>) – tells the provider to query for only <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> applications.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – <code class="docutils literal notranslate"><span class="pre">id</span></code> of application to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label</span></code> and <code class="docutils literal notranslate"><span class="pre">label_prefix</span></code>.</p></li>
<li><p><strong>label</strong> (<em>str</em>) – The label of the app to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label_prefix</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>.</p></li>
<li><p><strong>label_prefix</strong> (<em>str</em>) – Label prefix of the app to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>. This will tell the provider to do a <code class="docutils literal notranslate"><span class="pre">starts</span> <span class="pre">with</span></code> query as opposed to an <code class="docutils literal notranslate"><span class="pre">equals</span></code> query.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.app.get_metadata_saml">
<code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">get_metadata_saml</code><span class="sig-paren">(</span><em class="sig-param">app_id=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.get_metadata_saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the collaborators for a given repository.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app_metadata_saml.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app_metadata_saml.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>app_id</strong> (<em>str</em>) – The application ID.</p></li>
<li><p><strong>key_id</strong> (<em>str</em>) – Certificate Key ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.app.get_saml">
<code class="sig-prename descclassname">pulumi_okta.app.</code><code class="sig-name descname">get_saml</code><span class="sig-paren">(</span><em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">active_only=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">label_prefix=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.app.get_saml" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the collaborators for a given repository.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app_saml.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/app_saml.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>accessibility_error_redirect_url</strong> (<em>str</em>) – Custom error page URL.</p></li>
<li><p><strong>accessibility_login_redirect_url</strong> (<em>str</em>) – Custom login page URL.</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>bool</em>) – Enable self service.</p></li>
<li><p><strong>active_only</strong> (<em>bool</em>) – tells the provider to query for only <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> applications.</p></li>
<li><p><strong>app_settings_json</strong> (<em>str</em>) – Application settings in JSON format.</p></li>
<li><p><strong>assertion_signed</strong> (<em>bool</em>) – Determines whether the SAML assertion is digitally signed.</p></li>
<li><p><strong>attribute_statements</strong> (<em>list</em>) – SAML Attribute statements.</p></li>
<li><p><strong>audience</strong> (<em>str</em>) – Audience restriction.</p></li>
<li><p><strong>authn_context_class_ref</strong> (<em>str</em>) – Identifies the SAML authentication context class for the assertion’s authentication statement.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>bool</em>) – Display auto submit toolbar.</p></li>
<li><p><strong>default_relay_state</strong> (<em>str</em>) – Identifies a specific application resource in an IDP initiated SSO scenario.</p></li>
<li><p><strong>destination</strong> (<em>str</em>) – Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.</p></li>
<li><p><strong>digest_algorithm</strong> (<em>str</em>) – Determines the digest algorithm used to digitally sign the SAML assertion and response.</p></li>
<li><p><strong>features</strong> (<em>list</em>) – features enabled.</p></li>
<li><p><strong>hide_ios</strong> (<em>bool</em>) – Do not display application icon on mobile app.</p></li>
<li><p><strong>hide_web</strong> (<em>bool</em>) – Do not display application icon to users</p></li>
<li><p><strong>honor_force_authn</strong> (<em>bool</em>) – Prompt user to re-authenticate if SP asks for it.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – <code class="docutils literal notranslate"><span class="pre">id</span></code> of application to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label</span></code> and <code class="docutils literal notranslate"><span class="pre">label_prefix</span></code>.</p></li>
<li><p><strong>idp_issuer</strong> (<em>str</em>) – SAML issuer ID.</p></li>
<li><p><strong>label</strong> (<em>str</em>) – The label of the app to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label_prefix</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>.</p></li>
<li><p><strong>label_prefix</strong> (<em>str</em>) – Label prefix of the app to retrieve, conflicts with <code class="docutils literal notranslate"><span class="pre">label</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>. This will tell the provider to do a <code class="docutils literal notranslate"><span class="pre">starts</span> <span class="pre">with</span></code> query as opposed to an <code class="docutils literal notranslate"><span class="pre">equals</span></code> query.</p></li>
<li><p><strong>recipient</strong> (<em>str</em>) – The location where the app may present the SAML assertion.</p></li>
<li><p><strong>request_compressed</strong> (<em>bool</em>) – Denotes whether the request is compressed or not.</p></li>
<li><p><strong>response_signed</strong> (<em>bool</em>) – Determines whether the SAML auth response message is digitally signed.</p></li>
<li><p><strong>signature_algorithm</strong> (<em>str</em>) – Signature algorithm used ot digitally sign the assertion and response.</p></li>
<li><p><strong>sp_issuer</strong> (<em>str</em>) – SAML service provider issuer.</p></li>
<li><p><strong>sso_url</strong> (<em>str</em>) – Single Sign on Url.</p></li>
<li><p><strong>subject_name_id_format</strong> (<em>str</em>) – Identifies the SAML processing rules.</p></li>
<li><p><strong>subject_name_id_template</strong> (<em>str</em>) – Template for app user’s username when a user is assigned to the app.</p></li>
<li><p><strong>user_name_template</strong> (<em>str</em>) – Username template.</p></li>
<li><p><strong>user_name_template_suffix</strong> (<em>str</em>) – Username template suffix.</p></li>
<li><p><strong>user_name_template_type</strong> (<em>str</em>) – Username template type.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - name of application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

</div>
