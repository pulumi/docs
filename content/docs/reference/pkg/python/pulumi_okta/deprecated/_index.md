---
title: Module deprecated
title_tag: Module deprecated | Package pulumi_okta | Python SDK
linktitle: deprecated
notitle: true
---

<div class="section" id="deprecated">
<h1>deprecated<a class="headerlink" href="#deprecated" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.deprecated"></span><dl class="py class">
<dt id="pulumi_okta.deprecated.AuthLoginApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">AuthLoginApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reveal_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthLoginApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
:param pulumi.Input[bool] accessibility_self_service: Enable self service
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] credentials_scheme: Application credentials scheme
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] preconfigured_app: Preconfigured app name
:param pulumi.Input[bool] reveal_password: Allow user to reveal password
:param pulumi.Input[str] shared_password: Shared password, required for certain schemes.
:param pulumi.Input[str] shared_username: Shared username, required for certain schemes.
:param pulumi.Input[str] sign_on_redirect_url: Post login redirect URL
:param pulumi.Input[str] sign_on_url: Login URL
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.credentials_scheme">
<code class="sig-name descname">credentials_scheme</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.credentials_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Application credentials scheme</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Preconfigured app name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.reveal_password">
<code class="sig-name descname">reveal_password</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.reveal_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow user to reveal password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.shared_password">
<code class="sig-name descname">shared_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.shared_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared password, required for certain schemes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.shared_username">
<code class="sig-name descname">shared_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.shared_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared username, required for certain schemes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.sign_on_redirect_url">
<code class="sig-name descname">sign_on_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.sign_on_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Post login redirect URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.sign_on_url">
<code class="sig-name descname">sign_on_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.sign_on_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.AuthLoginApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.AuthLoginApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reveal_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthLoginApp resource’s state with the given name, id, and optional extra
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
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Preconfigured app name</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>sign_on_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Post login redirect URL</p></li>
<li><p><strong>sign_on_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.AuthLoginApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.AuthLoginApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.AwaitableGetDefaultPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">AwaitableGetDefaultPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AwaitableGetDefaultPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_okta.deprecated.BookmarkApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">BookmarkApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_integration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BookmarkApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.BookmarkApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.BookmarkApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_integration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BookmarkApp resource’s state with the given name, id, and optional extra
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
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.BookmarkApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.BookmarkApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.GetDefaultPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">GetDefaultPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.GetDefaultPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultPolicies.</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.GetDefaultPoliciesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.GetDefaultPoliciesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_okta.deprecated.Idp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">Idp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_clock_skew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_info_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_info_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Idp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] issuer_mode: Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL
:param pulumi.Input[str] name: name of idp
:param pulumi.Input[str] request_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] request_signature_scope: algorithm to use to sign response
:param pulumi.Input[str] response_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] response_signature_scope: algorithm to use to sign response</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of idp</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.Idp.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.Idp.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.Idp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwks_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_clock_skew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_info_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_info_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Idp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of idp</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.Idp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.Idp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.MfaPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">MfaPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_u2f</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_webauthn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_call</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_push</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_question</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_sms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">symantec_vip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">yubikey_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MfaPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Policy Description
:param pulumi.Input[list] groups_includeds: List of Group IDs to Include
:param pulumi.Input[str] name: Policy Name
:param pulumi.Input[float] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid</p>
<blockquote>
<div><p>priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p>
</dd>
</dl>
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicy.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicy.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicy.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_u2f</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fido_webauthn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_call</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_otp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_push</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_question</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">okta_sms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsa_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">symantec_vip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">yubikey_token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MfaPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.MfaPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">MfaPolicyRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enroll</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MfaPolicyRule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] enroll: Should the user be enrolled the first time they LOGIN, the next time they are CHALLENGEd, or NEVER?
:param pulumi.Input[str] name: Policy Rule Name
:param pulumi.Input[str] network_connection: Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.
:param pulumi.Input[list] network_excludes: The zones to exclude
:param pulumi.Input[list] network_includes: The zones to include
:param pulumi.Input[str] policyid: Policy ID of the Rule
:param pulumi.Input[float] priority: Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an</p>
<blockquote>
<div><p>invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.enroll">
<code class="sig-name descname">enroll</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.enroll" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the user be enrolled the first time they LOGIN, the next time they are CHALLENGEd, or NEVER?</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to exclude</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID of the Rule</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enroll</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MfaPolicyRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enroll</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Should the user be enrolled the first time they LOGIN, the next time they are CHALLENGEd, or NEVER?</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to exclude</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to include</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID of the Rule</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.OauthApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">OauthApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_key_rotation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_basic_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consent_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">omit_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">post_logout_redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tos_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OauthApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] auto_key_rotation: Requested key rotation mode.
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] client_basic_secret: OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.
:param pulumi.Input[str] client_uri: URI to a web page providing information about the client.
:param pulumi.Input[str] consent_method: <em>Early Access Property</em>. Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED.</p>
<blockquote>
<div><p>Default value is TRUSTED</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>custom_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This property allows you to set your client_id.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 grant types. Conditional validation params found here
<a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per
app type.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a
custom domain URL as the issuer of ID token for this client.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>login_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that initiates login.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that references a logo for the client.</p></li>
<li><p><strong>omit_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false
your app will be recreated.</p></li>
<li><p><strong>policy_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. URI to web page providing client policy document.</p></li>
<li><p><strong>post_logout_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for redirection after logout</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON that represents an OAuth application’s profile</p></li>
<li><p><strong>redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for use in the redirect-based flow. This is required for all application types except service. Note: see
okta_app_oauth_redirect_uri for appending to this list in a decentralized way.</p></li>
<li><p><strong>response_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 response type strings.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requested authentication method for the token endpoint.</p></li>
<li><p><strong>tos_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. URI to web page providing client tos (terms of service).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of client application.</p></li>
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
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.auto_key_rotation">
<code class="sig-name descname">auto_key_rotation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.auto_key_rotation" title="Permalink to this definition">¶</a></dt>
<dd><p>Requested key rotation mode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.client_basic_secret">
<code class="sig-name descname">client_basic_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.client_basic_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.client_secret">
<code class="sig-name descname">client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>OAuth client secret key. This will be in plain text in your statefile unless you set omit_secret above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.client_uri">
<code class="sig-name descname">client_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.client_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to a web page providing information about the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.consent_method">
<code class="sig-name descname">consent_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.consent_method" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Early Access Property</em>. Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED.
Default value is TRUSTED</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.custom_client_id">
<code class="sig-name descname">custom_client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.custom_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This property allows you to set your client_id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.grant_types">
<code class="sig-name descname">grant_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.grant_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of OAuth 2.0 grant types. Conditional validation params found here
<a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per
app type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Early Access Property</em>. Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a
custom domain URL as the issuer of ID token for this client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.login_uri">
<code class="sig-name descname">login_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.login_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that initiates login.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.logo_uri">
<code class="sig-name descname">logo_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.logo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI that references a logo for the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.omit_secret">
<code class="sig-name descname">omit_secret</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.omit_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false
your app will be recreated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.policy_uri">
<code class="sig-name descname">policy_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.policy_uri" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Early Access Property</em>. URI to web page providing client policy document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.post_logout_redirect_uris">
<code class="sig-name descname">post_logout_redirect_uris</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.post_logout_redirect_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for redirection after logout</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.profile">
<code class="sig-name descname">profile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON that represents an OAuth application’s profile</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.redirect_uris">
<code class="sig-name descname">redirect_uris</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.redirect_uris" title="Permalink to this definition">¶</a></dt>
<dd><p>List of URIs for use in the redirect-based flow. This is required for all application types except service. Note: see
okta_app_oauth_redirect_uri for appending to this list in a decentralized way.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.response_types">
<code class="sig-name descname">response_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.response_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of OAuth 2.0 response type strings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.token_endpoint_auth_method">
<code class="sig-name descname">token_endpoint_auth_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.token_endpoint_auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Requested authentication method for the token endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.tos_uri">
<code class="sig-name descname">tos_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.tos_uri" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Early Access Property</em>. URI to web page providing client tos (terms of service).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of client application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_key_rotation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_basic_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consent_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">omit_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">post_logout_redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_uris</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_endpoint_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tos_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OauthApp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_key_rotation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requested key rotation mode.</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>client_basic_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client ID.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OAuth client secret key. This will be in plain text in your statefile unless you set omit_secret above.</p></li>
<li><p><strong>client_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a web page providing information about the client.</p></li>
<li><p><strong>consent_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. Indicates whether user consent is required or implicit. Valid values: REQUIRED, TRUSTED.
Default value is TRUSTED</p></li>
<li><p><strong>custom_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This property allows you to set your client_id.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 grant types. Conditional validation params found here
<a class="reference external" href="https://developer.okta.com/docs/api/resources/apps#credentials-settings-details">https://developer.okta.com/docs/api/resources/apps#credentials-settings-details</a>. Defaults to minimum requirements per
app type.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a
custom domain URL as the issuer of ID token for this client.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>login_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that initiates login.</p></li>
<li><p><strong>logo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI that references a logo for the client.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>omit_secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This tells the provider not to persist the application’s secret to state. If this is ever changes from true =&gt; false
your app will be recreated.</p></li>
<li><p><strong>policy_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. URI to web page providing client policy document.</p></li>
<li><p><strong>post_logout_redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for redirection after logout</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON that represents an OAuth application’s profile</p></li>
<li><p><strong>redirect_uris</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of URIs for use in the redirect-based flow. This is required for all application types except service. Note: see
okta_app_oauth_redirect_uri for appending to this list in a decentralized way.</p></li>
<li><p><strong>response_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth 2.0 response type strings.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>token_endpoint_auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requested authentication method for the token endpoint.</p></li>
<li><p><strong>tos_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Early Access Property</em>. URI to web page providing client tos (terms of service).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of client application.</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">OauthAppRedirectUri</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OauthAppRedirectUri resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] uri: Redirect URI to append to Okta OIDC application.</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.uri">
<code class="sig-name descname">uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Redirect URI to append to Okta OIDC application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OauthAppRedirectUri resource’s state with the given name, id, and optional extra
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.PasswordPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">PasswordPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_auto_unlock_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_dictionary_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_expire_warn_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_history_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_age_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_lockout_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_age_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_lowercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_symbol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_uppercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_show_lockout_failures</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_email_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PasswordPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] auth_provider: Authentication Provider: OKTA or ACTIVE_DIRECTORY.
:param pulumi.Input[str] description: Policy Description
:param pulumi.Input[str] email_recovery: Enable or disable email password recovery: ACTIVE or INACTIVE.
:param pulumi.Input[list] groups_includeds: List of Group IDs to Include
:param pulumi.Input[str] name: Policy Name
:param pulumi.Input[float] password_auto_unlock_minutes: Number of minutes before a locked account is unlocked: 0 = no limit.
:param pulumi.Input[bool] password_dictionary_lookup: Check Passwords Against Common Password Dictionary.
:param pulumi.Input[bool] password_exclude_first_name: User firstName attribute must be excluded from the password
:param pulumi.Input[bool] password_exclude_last_name: User lastName attribute must be excluded from the password
:param pulumi.Input[bool] password_exclude_username: If the user name must be excluded from the password.
:param pulumi.Input[float] password_expire_warn_days: Length in days a user will be warned before password expiry: 0 = no warning.
:param pulumi.Input[float] password_history_count: Number of distinct passwords that must be created before they can be reused: 0 = none.
:param pulumi.Input[float] password_max_age_days: Length in days a password is valid before expiry: 0 = no limit.
:param pulumi.Input[float] password_max_lockout_attempts: Number of unsuccessful login attempts allowed before lockout: 0 = no limit.
:param pulumi.Input[float] password_min_age_minutes: Minimum time interval in minutes between password changes: 0 = no limit.
:param pulumi.Input[float] password_min_length: Minimum password length.
:param pulumi.Input[float] password_min_lowercase: If a password must contain at least one lower case letter: 0 = no, 1 = yes. Default = 1
:param pulumi.Input[float] password_min_number: If a password must contain at least one number: 0 = no, 1 = yes. Default = 1
:param pulumi.Input[float] password_min_symbol: If a password must contain at least one symbol (<a class="reference external" href="mailto:!&#37;&#52;&#48;#$%^&amp;*">!<span>&#64;</span>#$%^&amp;*</a>): 0 = no, 1 = yes. Default = 1
:param pulumi.Input[float] password_min_uppercase: If a password must contain at least one upper case letter: 0 = no, 1 = yes. Default = 1
:param pulumi.Input[bool] password_show_lockout_failures: If a user should be informed when their account is locked.
:param pulumi.Input[float] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid</p>
<blockquote>
<div><p>priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>question_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Min length of the password recovery question answer.</p></li>
<li><p><strong>question_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable security question password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>recovery_email_token</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime in minutes of the recovery email token.</p></li>
<li><p><strong>skip_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s
Windows account.</p></li>
<li><p><strong>sms_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.auth_provider">
<code class="sig-name descname">auth_provider</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.auth_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication Provider: OKTA or ACTIVE_DIRECTORY.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.email_recovery">
<code class="sig-name descname">email_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.email_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable email password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_auto_unlock_minutes">
<code class="sig-name descname">password_auto_unlock_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_auto_unlock_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of minutes before a locked account is unlocked: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_dictionary_lookup">
<code class="sig-name descname">password_dictionary_lookup</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_dictionary_lookup" title="Permalink to this definition">¶</a></dt>
<dd><p>Check Passwords Against Common Password Dictionary.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_exclude_first_name">
<code class="sig-name descname">password_exclude_first_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_exclude_first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User firstName attribute must be excluded from the password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_exclude_last_name">
<code class="sig-name descname">password_exclude_last_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_exclude_last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User lastName attribute must be excluded from the password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_exclude_username">
<code class="sig-name descname">password_exclude_username</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_exclude_username" title="Permalink to this definition">¶</a></dt>
<dd><p>If the user name must be excluded from the password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_expire_warn_days">
<code class="sig-name descname">password_expire_warn_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_expire_warn_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length in days a user will be warned before password expiry: 0 = no warning.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_history_count">
<code class="sig-name descname">password_history_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_history_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of distinct passwords that must be created before they can be reused: 0 = none.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_max_age_days">
<code class="sig-name descname">password_max_age_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_max_age_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length in days a password is valid before expiry: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_max_lockout_attempts">
<code class="sig-name descname">password_max_lockout_attempts</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_max_lockout_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of unsuccessful login attempts allowed before lockout: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_age_minutes">
<code class="sig-name descname">password_min_age_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_age_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum time interval in minutes between password changes: 0 = no limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_length">
<code class="sig-name descname">password_min_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum password length.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_lowercase">
<code class="sig-name descname">password_min_lowercase</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_lowercase" title="Permalink to this definition">¶</a></dt>
<dd><p>If a password must contain at least one lower case letter: 0 = no, 1 = yes. Default = 1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_number">
<code class="sig-name descname">password_min_number</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_number" title="Permalink to this definition">¶</a></dt>
<dd><p>If a password must contain at least one number: 0 = no, 1 = yes. Default = 1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_symbol">
<code class="sig-name descname">password_min_symbol</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_symbol" title="Permalink to this definition">¶</a></dt>
<dd><p>If a password must contain at least one symbol (<a class="reference external" href="mailto:!&#37;&#52;&#48;#$%^&amp;*">!<span>&#64;</span>#$%^&amp;*</a>): 0 = no, 1 = yes. Default = 1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_min_uppercase">
<code class="sig-name descname">password_min_uppercase</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_min_uppercase" title="Permalink to this definition">¶</a></dt>
<dd><p>If a password must contain at least one upper case letter: 0 = no, 1 = yes. Default = 1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.password_show_lockout_failures">
<code class="sig-name descname">password_show_lockout_failures</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.password_show_lockout_failures" title="Permalink to this definition">¶</a></dt>
<dd><p>If a user should be informed when their account is locked.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.question_min_length">
<code class="sig-name descname">question_min_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.question_min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Min length of the password recovery question answer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.question_recovery">
<code class="sig-name descname">question_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.question_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable security question password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.recovery_email_token">
<code class="sig-name descname">recovery_email_token</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.recovery_email_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Lifetime in minutes of the recovery email token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.skip_unlock">
<code class="sig-name descname">skip_unlock</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.skip_unlock" title="Permalink to this definition">¶</a></dt>
<dd><p>When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s
Windows account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.sms_recovery">
<code class="sig-name descname">sms_recovery</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.sms_recovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicy.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_auto_unlock_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_dictionary_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_exclude_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_expire_warn_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_history_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_age_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_max_lockout_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_age_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_lowercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_symbol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_min_uppercase</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_show_lockout_failures</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_min_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">question_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recovery_email_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_recovery</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PasswordPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication Provider: OKTA or ACTIVE_DIRECTORY.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description</p></li>
<li><p><strong>email_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable email password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name</p></li>
<li><p><strong>password_auto_unlock_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of minutes before a locked account is unlocked: 0 = no limit.</p></li>
<li><p><strong>password_dictionary_lookup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Check Passwords Against Common Password Dictionary.</p></li>
<li><p><strong>password_exclude_first_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User firstName attribute must be excluded from the password</p></li>
<li><p><strong>password_exclude_last_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User lastName attribute must be excluded from the password</p></li>
<li><p><strong>password_exclude_username</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the user name must be excluded from the password.</p></li>
<li><p><strong>password_expire_warn_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a user will be warned before password expiry: 0 = no warning.</p></li>
<li><p><strong>password_history_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of distinct passwords that must be created before they can be reused: 0 = none.</p></li>
<li><p><strong>password_max_age_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length in days a password is valid before expiry: 0 = no limit.</p></li>
<li><p><strong>password_max_lockout_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of unsuccessful login attempts allowed before lockout: 0 = no limit.</p></li>
<li><p><strong>password_min_age_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum time interval in minutes between password changes: 0 = no limit.</p></li>
<li><p><strong>password_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum password length.</p></li>
<li><p><strong>password_min_lowercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a password must contain at least one lower case letter: 0 = no, 1 = yes. Default = 1</p></li>
<li><p><strong>password_min_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a password must contain at least one number: 0 = no, 1 = yes. Default = 1</p></li>
<li><p><strong>password_min_symbol</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a password must contain at least one symbol (<a class="reference external" href="mailto:!&#37;&#52;&#48;#$%^&amp;*">!<span>&#64;</span>#$%^&amp;*</a>): 0 = no, 1 = yes. Default = 1</p></li>
<li><p><strong>password_min_uppercase</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a password must contain at least one upper case letter: 0 = no, 1 = yes. Default = 1</p></li>
<li><p><strong>password_show_lockout_failures</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If a user should be informed when their account is locked.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>question_min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Min length of the password recovery question answer.</p></li>
<li><p><strong>question_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable security question password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>recovery_email_token</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Lifetime in minutes of the recovery email token.</p></li>
<li><p><strong>skip_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When an Active Directory user is locked out of Okta, the Okta unlock operation should also attempt to unlock the user’s
Windows account.</p></li>
<li><p><strong>sms_recovery</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable or disable SMS password recovery: ACTIVE or INACTIVE.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">PasswordPolicyRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_change</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PasswordPolicyRule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: Policy Rule Name
:param pulumi.Input[str] network_connection: Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.
:param pulumi.Input[list] network_excludes: The zones to exclude
:param pulumi.Input[list] network_includes: The zones to include
:param pulumi.Input[str] password_change: Allow or deny a user to change their password: ALLOW or DENY. Default = ALLOW
:param pulumi.Input[str] password_reset: Allow or deny a user to reset their password: ALLOW or DENY. Default = ALLOW
:param pulumi.Input[str] password_unlock: Allow or deny a user to unlock. Default = DENY
:param pulumi.Input[str] policyid: Policy ID of the Rule
:param pulumi.Input[float] priority: Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an</p>
<blockquote>
<div><p>invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to exclude</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.password_change">
<code class="sig-name descname">password_change</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.password_change" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to change their password: ALLOW or DENY. Default = ALLOW</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.password_reset">
<code class="sig-name descname">password_reset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.password_reset" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to reset their password: ALLOW or DENY. Default = ALLOW</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.password_unlock">
<code class="sig-name descname">password_unlock</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.password_unlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny a user to unlock. Default = DENY</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID of the Rule</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_change</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_reset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_unlock</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PasswordPolicyRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to exclude</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to include</p></li>
<li><p><strong>password_change</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to change their password: ALLOW or DENY. Default = ALLOW</p></li>
<li><p><strong>password_reset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to reset their password: ALLOW or DENY. Default = ALLOW</p></li>
<li><p><strong>password_unlock</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny a user to unlock. Default = DENY</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID of the Rule</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SamlApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_login_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_settings_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertion_signed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_statements</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authn_context_class_ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_relay_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">honor_force_authn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_years_valid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_compressed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sp_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name_id_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name_id_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
:param pulumi.Input[str] accessibility_login_redirect_url: Custom login page URL
:param pulumi.Input[bool] accessibility_self_service: Enable self service
:param pulumi.Input[str] app_settings_json: Application settings in JSON format
:param pulumi.Input[bool] assertion_signed: Determines whether the SAML assertion is digitally signed
:param pulumi.Input[str] audience: Audience Restriction
:param pulumi.Input[str] authn_context_class_ref: Identifies the SAML authentication context class for the assertion’s authentication statement
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] default_relay_state: Identifies a specific application resource in an IDP initiated SSO scenario.
:param pulumi.Input[str] destination: Identifies the location where the SAML response is intended to be sent inside of the SAML assertion
:param pulumi.Input[str] digest_algorithm: Determines the digest algorithm used to digitally sign the SAML assertion and response
:param pulumi.Input[list] features: features to enable
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[bool] honor_force_authn: Prompt user to re-authenticate if SP asks for it
:param pulumi.Input[str] idp_issuer: SAML issuer ID
:param pulumi.Input[str] key_name: Certificate name. This modulates the rotation of keys. New name == new key.
:param pulumi.Input[float] key_years_valid: Number of years the certificate is valid.
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] preconfigured_app: Name of preexisting SAML application. For instance ‘slack’
:param pulumi.Input[str] recipient: The location where the app may present the SAML assertion
:param pulumi.Input[bool] request_compressed: Denotes whether the request is compressed or not.
:param pulumi.Input[bool] response_signed: Determines whether the SAML auth response message is digitally signed
:param pulumi.Input[str] signature_algorithm: Signature algorithm used ot digitally sign the assertion and response
:param pulumi.Input[str] sp_issuer: SAML SP issuer ID
:param pulumi.Input[str] sso_url: Single Sign On URL
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[str] subject_name_id_format: Identifies the SAML processing rules.
:param pulumi.Input[str] subject_name_id_template: Template for app user’s username when a user is assigned to the app
:param pulumi.Input[str] user_name_template: Username template
:param pulumi.Input[str] user_name_template_suffix: Username template suffix
:param pulumi.Input[str] user_name_template_type: Username template type
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.accessibility_login_redirect_url">
<code class="sig-name descname">accessibility_login_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.accessibility_login_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom login page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.app_settings_json">
<code class="sig-name descname">app_settings_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.app_settings_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Application settings in JSON format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.assertion_signed">
<code class="sig-name descname">assertion_signed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.assertion_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML assertion is digitally signed</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.audience">
<code class="sig-name descname">audience</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>Audience Restriction</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.authn_context_class_ref">
<code class="sig-name descname">authn_context_class_ref</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.authn_context_class_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML authentication context class for the assertion’s authentication statement</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>cert from SAML XML metadata payload</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.default_relay_state">
<code class="sig-name descname">default_relay_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.default_relay_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies a specific application resource in an IDP initiated SSO scenario.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the location where the SAML response is intended to be sent inside of the SAML assertion</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.digest_algorithm">
<code class="sig-name descname">digest_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.digest_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the digest algorithm used to digitally sign the SAML assertion and response</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.entity_key">
<code class="sig-name descname">entity_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.entity_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity ID, the ID portion of the entity_url</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.entity_url">
<code class="sig-name descname">entity_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.entity_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity URL for instance <a class="reference external" href="http://www.okta.com/exk1fcia6d6EMsf331d8">http://www.okta.com/exk1fcia6d6EMsf331d8</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.features">
<code class="sig-name descname">features</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.features" title="Permalink to this definition">¶</a></dt>
<dd><p>features to enable</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.honor_force_authn">
<code class="sig-name descname">honor_force_authn</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.honor_force_authn" title="Permalink to this definition">¶</a></dt>
<dd><p>Prompt user to re-authenticate if SP asks for it</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.http_post_binding">
<code class="sig-name descname">http_post_binding</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.http_post_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.http_redirect_binding">
<code class="sig-name descname">http_redirect_binding</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.http_redirect_binding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</a> location from the SAML metadata.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.idp_issuer">
<code class="sig-name descname">idp_issuer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.idp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML issuer ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate name. This modulates the rotation of keys. New name == new key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.key_years_valid">
<code class="sig-name descname">key_years_valid</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.key_years_valid" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of years the certificate is valid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML xml metadata payload</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of preexisting SAML application. For instance ‘slack’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.recipient">
<code class="sig-name descname">recipient</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.recipient" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the app may present the SAML assertion</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.request_compressed">
<code class="sig-name descname">request_compressed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.request_compressed" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether the request is compressed or not.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.response_signed">
<code class="sig-name descname">response_signed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.response_signed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether the SAML auth response message is digitally signed</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.signature_algorithm">
<code class="sig-name descname">signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Signature algorithm used ot digitally sign the assertion and response</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.sp_issuer">
<code class="sig-name descname">sp_issuer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.sp_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML SP issuer ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.sso_url">
<code class="sig-name descname">sso_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.sso_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Single Sign On URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.subject_name_id_format">
<code class="sig-name descname">subject_name_id_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.subject_name_id_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the SAML processing rules.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.subject_name_id_template">
<code class="sig-name descname">subject_name_id_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.subject_name_id_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Template for app user’s username when a user is assigned to the app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.user_name_template_suffix">
<code class="sig-name descname">user_name_template_suffix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.user_name_template_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template suffix</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_login_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_settings_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertion_signed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_statements</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authn_context_class_ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_relay_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">honor_force_authn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_post_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_redirect_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idp_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_years_valid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_compressed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sp_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name_id_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name_id_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlApp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessibility_error_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom error page URL</p></li>
<li><p><strong>accessibility_login_redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom login page URL</p></li>
<li><p><strong>accessibility_self_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable self service</p></li>
<li><p><strong>app_settings_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application settings in JSON format</p></li>
<li><p><strong>assertion_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML assertion is digitally signed</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Audience Restriction</p></li>
<li><p><strong>authn_context_class_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML authentication context class for the assertion’s authentication statement</p></li>
<li><p><strong>auto_submit_toolbar</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Display auto submit toolbar</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – cert from SAML XML metadata payload</p></li>
<li><p><strong>default_relay_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies a specific application resource in an IDP initiated SSO scenario.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the location where the SAML response is intended to be sent inside of the SAML assertion</p></li>
<li><p><strong>digest_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines the digest algorithm used to digitally sign the SAML assertion and response</p></li>
<li><p><strong>entity_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity ID, the ID portion of the entity_url</p></li>
<li><p><strong>entity_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity URL for instance <a class="reference external" href="http://www.okta.com/exk1fcia6d6EMsf331d8">http://www.okta.com/exk1fcia6d6EMsf331d8</a></p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – features to enable</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>honor_force_authn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prompt user to re-authenticate if SP asks for it</p></li>
<li><p><strong>http_post_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post</a> location from the SAML metadata.</p></li>
<li><p><strong>http_redirect_binding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect">urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</a> location from the SAML metadata.</p></li>
<li><p><strong>idp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML issuer ID</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate ID</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate name. This modulates the rotation of keys. New name == new key.</p></li>
<li><p><strong>key_years_valid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of years the certificate is valid.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML xml metadata payload</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of preexisting SAML application. For instance ‘slack’</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the app may present the SAML assertion</p></li>
<li><p><strong>request_compressed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether the request is compressed or not.</p></li>
<li><p><strong>response_signed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether the SAML auth response message is digitally signed</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signature algorithm used ot digitally sign the assertion and response</p></li>
<li><p><strong>sp_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML SP issuer ID</p></li>
<li><p><strong>sso_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Single Sign On URL</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>subject_name_id_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the SAML processing rules.</p></li>
<li><p><strong>subject_name_id_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Template for app user’s username when a user is assigned to the app</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template</p></li>
<li><p><strong>user_name_template_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template suffix</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the application</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SamlIdp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlIdp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_formats</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlIdp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] issuer_mode: Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL
:param pulumi.Input[str] name: name of idp
:param pulumi.Input[str] request_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] request_signature_scope: algorithm to use to sign response
:param pulumi.Input[str] response_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] response_signature_scope: algorithm to use to sign response</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of idp</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdp.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acs_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audience</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_formats</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlIdp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of idp</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlIdpSigningKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x5cs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlIdpSigningKey resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] x5cs: base64-encoded X.509 certificate chain with DER encoding</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.x5cs">
<code class="sig-name descname">x5cs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.x5cs" title="Permalink to this definition">¶</a></dt>
<dd><p>base64-encoded X.509 certificate chain with DER encoding</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kty</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x5cs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x5t_s256</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlIdpSigningKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>x5cs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – base64-encoded X.509 certificate chain with DER encoding</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SecurePasswordStoreApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field1_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field2_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field3</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field3_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reveal_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurePasswordStoreApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
:param pulumi.Input[bool] accessibility_self_service: Enable self service
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] credentials_scheme: Application credentials scheme
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] optional_field1: Name of optional param in the login form
:param pulumi.Input[str] optional_field1_value: Name of optional value in login form
:param pulumi.Input[str] optional_field2: Name of optional param in the login form
:param pulumi.Input[str] optional_field2_value: Name of optional value in login form
:param pulumi.Input[str] optional_field3: Name of optional param in the login form
:param pulumi.Input[str] optional_field3_value: Name of optional value in login form
:param pulumi.Input[str] password_field: Login password field
:param pulumi.Input[bool] reveal_password: Allow user to reveal password
:param pulumi.Input[str] shared_password: Shared password, required for certain schemes.
:param pulumi.Input[str] shared_username: Shared username, required for certain schemes.
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[str] url: Login URL
:param pulumi.Input[str] username_field: Login username field
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.credentials_scheme">
<code class="sig-name descname">credentials_scheme</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.credentials_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Application credentials scheme</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field1">
<code class="sig-name descname">optional_field1</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field1" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field1_value">
<code class="sig-name descname">optional_field1_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field1_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field2">
<code class="sig-name descname">optional_field2</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field2" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field2_value">
<code class="sig-name descname">optional_field2_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field2_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field3">
<code class="sig-name descname">optional_field3</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field3" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional param in the login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field3_value">
<code class="sig-name descname">optional_field3_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.optional_field3_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of optional value in login form</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.password_field">
<code class="sig-name descname">password_field</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.password_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.reveal_password">
<code class="sig-name descname">reveal_password</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.reveal_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow user to reveal password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.shared_password">
<code class="sig-name descname">shared_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.shared_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared password, required for certain schemes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.shared_username">
<code class="sig-name descname">shared_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.shared_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Shared username, required for certain schemes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.username_field">
<code class="sig-name descname">username_field</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.username_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field1_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field2_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field3</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optional_field3_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reveal_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurePasswordStoreApp resource’s state with the given name, id, and optional extra
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
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>optional_field1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form</p></li>
<li><p><strong>optional_field1_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in login form</p></li>
<li><p><strong>optional_field2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form</p></li>
<li><p><strong>optional_field2_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in login form</p></li>
<li><p><strong>optional_field3</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional param in the login form</p></li>
<li><p><strong>optional_field3_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of optional value in login form</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field</p></li>
<li><p><strong>reveal_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow user to reveal password</p></li>
<li><p><strong>shared_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared password, required for certain schemes.</p></li>
<li><p><strong>shared_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shared username, required for certain schemes.</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SignonPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SignonPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SignonPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Policy Description
:param pulumi.Input[list] groups_includeds: List of Group IDs to Include
:param pulumi.Input[str] name: Policy Name
:param pulumi.Input[float] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid</p>
<blockquote>
<div><p>priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Description</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicy.groups_includeds">
<code class="sig-name descname">groups_includeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.groups_includeds" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs to Include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicy.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicy.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_includeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SignonPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Description</p></li>
<li><p><strong>groups_includeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Group IDs to Include</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Name</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Status: ACTIVE or INACTIVE.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SignonPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SignonPolicyRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authtype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_prompt</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_remember_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_idle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_persistent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SignonPolicyRule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access: Allow or deny access based on the rule conditions: ALLOW or DENY.
:param pulumi.Input[str] authtype: Authentication entrypoint: ANY or RADIUS.
:param pulumi.Input[float] mfa_lifetime: Elapsed time before the next MFA challenge
:param pulumi.Input[str] mfa_prompt: Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: DEVICE, SESSION or ALWAYS
:param pulumi.Input[bool] mfa_remember_device: Remember MFA device.
:param pulumi.Input[bool] mfa_required: Require MFA.
:param pulumi.Input[str] name: Policy Rule Name
:param pulumi.Input[str] network_connection: Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.
:param pulumi.Input[list] network_excludes: The zones to exclude
:param pulumi.Input[list] network_includes: The zones to include
:param pulumi.Input[str] policyid: Policy ID of the Rule
:param pulumi.Input[float] priority: Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an</p>
<blockquote>
<div><p>invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>session_idle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session can be idle.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session is active: Disable = 0.</p></li>
<li><p><strong>session_persistent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session
cookies.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.access">
<code class="sig-name descname">access</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.access" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow or deny access based on the rule conditions: ALLOW or DENY.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.authtype">
<code class="sig-name descname">authtype</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.authtype" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication entrypoint: ANY or RADIUS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.mfa_lifetime">
<code class="sig-name descname">mfa_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.mfa_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Elapsed time before the next MFA challenge</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.mfa_prompt">
<code class="sig-name descname">mfa_prompt</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.mfa_prompt" title="Permalink to this definition">¶</a></dt>
<dd><p>Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: DEVICE, SESSION or ALWAYS</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.mfa_remember_device">
<code class="sig-name descname">mfa_remember_device</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.mfa_remember_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Remember MFA device.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.mfa_required">
<code class="sig-name descname">mfa_required</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.mfa_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Require MFA.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.network_connection">
<code class="sig-name descname">network_connection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.network_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.network_excludes">
<code class="sig-name descname">network_excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.network_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to exclude</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.network_includes">
<code class="sig-name descname">network_includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.network_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>The zones to include</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.policyid">
<code class="sig-name descname">policyid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.policyid" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy ID of the Rule</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.session_idle">
<code class="sig-name descname">session_idle</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.session_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>Max minutes a session can be idle.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.session_lifetime">
<code class="sig-name descname">session_lifetime</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.session_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>Max minutes a session is active: Disable = 0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.session_persistent">
<code class="sig-name descname">session_persistent</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.session_persistent" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session
cookies.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy Rule Status: ACTIVE or INACTIVE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.users_excludeds">
<code class="sig-name descname">users_excludeds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.users_excludeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of User IDs to Exclude</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authtype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_prompt</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_remember_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mfa_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policyid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_idle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_lifetime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_persistent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users_excludeds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SignonPolicyRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow or deny access based on the rule conditions: ALLOW or DENY.</p></li>
<li><p><strong>authtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication entrypoint: ANY or RADIUS.</p></li>
<li><p><strong>mfa_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Elapsed time before the next MFA challenge</p></li>
<li><p><strong>mfa_prompt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: DEVICE, SESSION or ALWAYS</p></li>
<li><p><strong>mfa_remember_device</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Remember MFA device.</p></li>
<li><p><strong>mfa_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Require MFA.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Name</p></li>
<li><p><strong>network_connection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network selection mode: ANYWHERE, ZONE, ON_NETWORK, or OFF_NETWORK.</p></li>
<li><p><strong>network_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to exclude</p></li>
<li><p><strong>network_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The zones to include</p></li>
<li><p><strong>policyid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy ID of the Rule</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an
invalid priority is provided. API defaults it to the last/lowest if not there.</p></li>
<li><p><strong>session_idle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session can be idle.</p></li>
<li><p><strong>session_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max minutes a session is active: Disable = 0.</p></li>
<li><p><strong>session_persistent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session
cookies.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy Rule Status: ACTIVE or INACTIVE.</p></li>
<li><p><strong>users_excludeds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of User IDs to Exclude</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SocialIdp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SocialIdp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_clock_skew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SocialIdp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] issuer_mode: Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL
:param pulumi.Input[str] name: name of idp
:param pulumi.Input[str] request_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] request_signature_scope: algorithm to use to sign response
:param pulumi.Input[str] response_signature_algorithm: algorithm to use to sign requests
:param pulumi.Input[str] response_signature_scope: algorithm to use to sign response</p>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.issuer_mode">
<code class="sig-name descname">issuer_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.issuer_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of idp</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.request_signature_algorithm">
<code class="sig-name descname">request_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.request_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.request_signature_scope">
<code class="sig-name descname">request_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.request_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.response_signature_algorithm">
<code class="sig-name descname">response_signature_algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.response_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign requests</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SocialIdp.response_signature_scope">
<code class="sig-name descname">response_signature_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.response_signature_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>algorithm to use to sign response</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SocialIdp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_link_group_includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprovisioned_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_assignments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_clock_skew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_master</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_signature_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_attribute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_match_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_binding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SocialIdp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>issuer_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of idp</p></li>
<li><p><strong>request_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>request_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
<li><p><strong>response_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign requests</p></li>
<li><p><strong>response_signature_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – algorithm to use to sign response</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SocialIdp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SocialIdp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.SwaApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SwaApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">button_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SwaApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
:param pulumi.Input[bool] accessibility_self_service: Enable self service
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] button_field: Login button field
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] password_field: Login password field
:param pulumi.Input[str] preconfigured_app: Preconfigured app name
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[str] url: Login URL
:param pulumi.Input[str] url_regex: A regex that further restricts URL to the specified regex
:param pulumi.Input[str] username_field: Login username field
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.button_field">
<code class="sig-name descname">button_field</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.button_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login button field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.password_field">
<code class="sig-name descname">password_field</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.password_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.preconfigured_app">
<code class="sig-name descname">preconfigured_app</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.preconfigured_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Preconfigured app name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.url_regex">
<code class="sig-name descname">url_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.url_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regex that further restricts URL to the specified regex</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.username_field">
<code class="sig-name descname">username_field</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.username_field" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.SwaApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.SwaApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">button_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preconfigured_app</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SwaApp resource’s state with the given name, id, and optional extra
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
<li><p><strong>button_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>password_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field</p></li>
<li><p><strong>preconfigured_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Preconfigured app name</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type</p></li>
<li><p><strong>username_field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SwaApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.SwaApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_okta.deprecated.ThreeFieldApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">ThreeFieldApp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">button_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_field_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_field_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ThreeFieldApp resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
:param pulumi.Input[bool] accessibility_self_service: Enable self service
:param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
:param pulumi.Input[str] button_selector: Login button field CSS selector
:param pulumi.Input[str] extra_field_selector: Extra field CSS selector
:param pulumi.Input[str] extra_field_value: Value for extra form field
:param pulumi.Input[list] groups: Groups associated with the application
:param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
:param pulumi.Input[bool] hide_web: Do not display application icon to users
:param pulumi.Input[str] label: Pretty name of app.
:param pulumi.Input[str] password_selector: Login password field CSS selector
:param pulumi.Input[str] status: Status of application.
:param pulumi.Input[str] url: Login URL
:param pulumi.Input[str] url_regex: A regex that further restricts URL to the specified regex
:param pulumi.Input[str] username_selector: Login username field CSS selector
:param pulumi.Input[list] users: Users associated with the application</p>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.accessibility_error_redirect_url">
<code class="sig-name descname">accessibility_error_redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.accessibility_error_redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom error page URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.accessibility_self_service">
<code class="sig-name descname">accessibility_self_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.accessibility_self_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable self service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.auto_submit_toolbar">
<code class="sig-name descname">auto_submit_toolbar</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.auto_submit_toolbar" title="Permalink to this definition">¶</a></dt>
<dd><p>Display auto submit toolbar</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.button_selector">
<code class="sig-name descname">button_selector</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.button_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login button field CSS selector</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.extra_field_selector">
<code class="sig-name descname">extra_field_selector</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.extra_field_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra field CSS selector</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.extra_field_value">
<code class="sig-name descname">extra_field_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.extra_field_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Value for extra form field</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups associated with the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.hide_ios">
<code class="sig-name descname">hide_ios</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.hide_ios" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon on mobile app</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.hide_web">
<code class="sig-name descname">hide_web</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.hide_web" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not display application icon to users</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.label" title="Permalink to this definition">¶</a></dt>
<dd><p>Pretty name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of app.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.password_selector">
<code class="sig-name descname">password_selector</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.password_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login password field CSS selector</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.sign_on_mode">
<code class="sig-name descname">sign_on_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.sign_on_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sign on mode of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Login URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.url_regex">
<code class="sig-name descname">url_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.url_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regex that further restricts URL to the specified regex</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.user_name_template">
<code class="sig-name descname">user_name_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.user_name_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.user_name_template_type">
<code class="sig-name descname">user_name_template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.user_name_template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Username template type</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.username_selector">
<code class="sig-name descname">username_selector</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.username_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Login username field CSS selector</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the application</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_error_redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessibility_self_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_submit_toolbar</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">button_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_field_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_field_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_ios</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_web</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_on_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name_template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThreeFieldApp resource’s state with the given name, id, and optional extra
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
<li><p><strong>button_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login button field CSS selector</p></li>
<li><p><strong>extra_field_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Extra field CSS selector</p></li>
<li><p><strong>extra_field_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value for extra form field</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups associated with the application</p></li>
<li><p><strong>hide_ios</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon on mobile app</p></li>
<li><p><strong>hide_web</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not display application icon to users</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Pretty name of app.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of app.</p></li>
<li><p><strong>password_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login password field CSS selector</p></li>
<li><p><strong>sign_on_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sign on mode of application.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of application.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login URL</p></li>
<li><p><strong>url_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regex that further restricts URL to the specified regex</p></li>
<li><p><strong>user_name_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template</p></li>
<li><p><strong>user_name_template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username template type</p></li>
<li><p><strong>username_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login username field CSS selector</p></li>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_okta.deprecated.get_default_policies">
<code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">get_default_policies</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.get_default_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
