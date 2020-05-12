---
title: Module okta
title_tag: Module okta | Package pulumi_vault | Python SDK
linktitle: okta
notitle: true
---

<div class="section" id="okta">
<h1>okta<a class="headerlink" href="#okta" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.okta"></span><dl class="py class">
<dt id="pulumi_vault.okta.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.okta.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_okta_mfa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackend resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] base_url: The Okta url. Examples: oktapreview.com, okta.com
:param pulumi.Input[bool] bypass_okta_mfa: When true, requests by Okta for a MFA check will be bypassed. This also disallows certain status checks on the account, such as whether the password is expired.
:param pulumi.Input[str] description: The description of the auth backend
:param pulumi.Input[list] groups: Associate Okta groups with policies within Vault.</p>
<blockquote>
<div><p>See below for more details.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maximum duration after which authentication will be expired
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta organization. This will be the first part of the url <code class="docutils literal notranslate"><span class="pre">https://XXX.okta.com</span></code></p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the Okta auth backend</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta API token. This is required to query Okta for user group membership.
If this is not supplied only locally configured groups will be enabled.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Duration after which authentication will be expired.
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p>
</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Associate Okta users with groups or policies within Vault.
See below for more details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the group within the Okta</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Vault policies to associate with this user</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Okta groups to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Vault policies to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the user within Okta</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.accessor">
<code class="sig-name descname">accessor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The mount accessor related to the auth mount. It is useful for integration with <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity Secrets Engine</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.base_url">
<code class="sig-name descname">base_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.base_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Okta url. Examples: oktapreview.com, okta.com</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.bypass_okta_mfa">
<code class="sig-name descname">bypass_okta_mfa</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.bypass_okta_mfa" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, requests by Okta for a MFA check will be bypassed. This also disallows certain status checks on the account, such as whether the password is expired.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the auth backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate Okta groups with policies within Vault.
See below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the group within the Okta</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Vault policies to associate with this user</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum duration after which authentication will be expired
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The Okta organization. This will be the first part of the url <code class="docutils literal notranslate"><span class="pre">https://XXX.okta.com</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to mount the Okta auth backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The Okta API token. This is required to query Okta for user group membership.
If this is not supplied only locally configured groups will be enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration after which authentication will be expired.
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackend.users">
<code class="sig-name descname">users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate Okta users with groups or policies within Vault.
See below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Okta groups to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Vault policies to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the user within Okta</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_okta_mfa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The mount accessor related to the auth mount. It is useful for integration with <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity Secrets Engine</a>.</p>
</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta url. Examples: oktapreview.com, okta.com</p></li>
<li><p><strong>bypass_okta_mfa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, requests by Okta for a MFA check will be bypassed. This also disallows certain status checks on the account, such as whether the password is expired.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the auth backend</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Associate Okta groups with policies within Vault.
See below for more details.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Maximum duration after which authentication will be expired
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p>
</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta organization. This will be the first part of the url <code class="docutils literal notranslate"><span class="pre">https://XXX.okta.com</span></code></p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the Okta auth backend</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta API token. This is required to query Okta for user group membership.
If this is not supplied only locally configured groups will be enabled.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Duration after which authentication will be expired.
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">See the documentation for info on valid duration formats</a>.</p>
</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Associate Okta users with groups or policies within Vault.
See below for more details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the group within the Okta</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Vault policies to associate with this user</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Okta groups to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Vault policies to associate with this user</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the user within Okta</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.okta.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.okta.AuthBackendGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.okta.</code><code class="sig-name descname">AuthBackendGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a group in an
<a class="reference external" href="https://www.vaultproject.io/docs/auth/okta.html">Okta auth backend within Vault</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">okta</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">organization</span><span class="o">=</span><span class="s2">&quot;dummy&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;group_okta&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">okta</span><span class="o">.</span><span class="n">AuthBackendGroup</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">group_name</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;one&quot;</span><span class="p">,</span>
        <span class="s2">&quot;two&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group within the Okta</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the Okta auth backend is mounted</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Vault policies to associate with this group</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendGroup.group_name">
<code class="sig-name descname">group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the group within the Okta</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendGroup.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path where the Okta auth backend is mounted</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendGroup.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Vault policies to associate with this group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackendGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group within the Okta</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the Okta auth backend is mounted</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Vault policies to associate with this group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackendGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.okta.AuthBackendGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.okta.AuthBackendUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.okta.</code><code class="sig-name descname">AuthBackendUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a user in an
<a class="reference external" href="https://www.vaultproject.io/docs/auth/okta.html">Okta auth backend within Vault</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">okta</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">organization</span><span class="o">=</span><span class="s2">&quot;dummy&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;user_okta&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">okta</span><span class="o">.</span><span class="n">AuthBackendUser</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">groups</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;one&quot;</span><span class="p">,</span>
        <span class="s2">&quot;two&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">path</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta groups to associate with this user</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the Okta auth backend is mounted</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Vault policies to associate with this user</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user within Okta</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendUser.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Okta groups to associate with this user</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendUser.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path where the Okta auth backend is mounted</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendUser.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Vault policies to associate with this user</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.okta.AuthBackendUser.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the user within Okta</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackendUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Okta groups to associate with this user</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the Okta auth backend is mounted</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Vault policies to associate with this user</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user within Okta</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.okta.AuthBackendUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.okta.AuthBackendUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.okta.AuthBackendUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
