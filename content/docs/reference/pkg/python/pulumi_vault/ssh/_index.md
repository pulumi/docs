---
title: Module ssh
title_tag: Module ssh | Package pulumi_vault | Python SDK
linktitle: ssh
notitle: true
---

<div class="section" id="ssh">
<h1>ssh<a class="headerlink" href="#ssh" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.ssh"></span><dl class="py class">
<dt id="pulumi_vault.ssh.SecretBackendCa">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.ssh.</code><code class="sig-name descname">SecretBackendCa</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generate_signing_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage CA information in an SSH secret backend
<a class="reference external" href="https://www.vaultproject.io/docs/secrets/ssh/index.html">SSH secret backend within Vault</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Mount</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ssh&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">ssh</span><span class="o">.</span><span class="n">SecretBackendCa</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">backend</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the SSH secret backend is mounted. Defaults to ‘ssh’</p></li>
<li><p><strong>generate_signing_key</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Vault should generate the signing key pair internally. Defaults to true</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key part the SSH CA key pair; required if generate_signing_key is false.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key part the SSH CA key pair; required if generate_signing_key is false.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendCa.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path where the SSH secret backend is mounted. Defaults to ‘ssh’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendCa.generate_signing_key">
<code class="sig-name descname">generate_signing_key</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.generate_signing_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Vault should generate the signing key pair internally. Defaults to true</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendCa.private_key">
<code class="sig-name descname">private_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key part the SSH CA key pair; required if generate_signing_key is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendCa.public_key">
<code class="sig-name descname">public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key part the SSH CA key pair; required if generate_signing_key is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.ssh.SecretBackendCa.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generate_signing_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendCa resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the SSH secret backend is mounted. Defaults to ‘ssh’</p></li>
<li><p><strong>generate_signing_key</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Vault should generate the signing key pair internally. Defaults to true</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key part the SSH CA key pair; required if generate_signing_key is false.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key part the SSH CA key pair; required if generate_signing_key is false.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.ssh.SecretBackendCa.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.ssh.SecretBackendCa.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendCa.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.ssh.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.ssh.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_bare_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_host_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_subdomains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_user_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_user_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_critical_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_user_key_lengths</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_critical_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage roles in an SSH secret backend
<a class="reference external" href="https://www.vaultproject.io/docs/secrets/ssh/index.html">SSH secret backend within Vault</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Mount</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ssh&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">ssh</span><span class="o">.</span><span class="n">SecretBackendRole</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">allow_user_certificates</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">backend</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
    <span class="n">key_type</span><span class="o">=</span><span class="s2">&quot;ca&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">ssh</span><span class="o">.</span><span class="n">SecretBackendRole</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">allowed_users</span><span class="o">=</span><span class="s2">&quot;default,baz&quot;</span><span class="p">,</span>
    <span class="n">backend</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
    <span class="n">cidr_list</span><span class="o">=</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">,</span>
    <span class="n">default_user</span><span class="o">=</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">key_type</span><span class="o">=</span><span class="s2">&quot;otp&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_bare_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if host certificates that are requested are allowed to use the base domains listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p></li>
<li><p><strong>allow_host_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if certificates are allowed to be signed for use as a ‘host’.</p></li>
<li><p><strong>allow_subdomains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if host certificates that are requested are allowed to be subdomains of those listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p></li>
<li><p><strong>allow_user_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if certificates are allowed to be signed for use as a ‘user’.</p></li>
<li><p><strong>allow_user_key_ids</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if users can override the key ID for a signed certificate with the <code class="docutils literal notranslate"><span class="pre">key_id</span></code> field.</p></li>
<li><p><strong>allowed_critical_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of critical options that certificates can have when signed.</p></li>
<li><p><strong>allowed_domains</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of domains for which a client can request a host certificate.</p></li>
<li><p><strong>allowed_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of extensions that certificates can have when signed.</p></li>
<li><p><strong>allowed_user_key_lengths</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of ssh key types and their expected sizes which are allowed to be signed by the CA type.</p></li>
<li><p><strong>allowed_users</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of usernames that are to be allowed, only if certain usernames are to be allowed.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the SSH secret backend is mounted.</p></li>
<li><p><strong>cidr_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The comma-separated string of CIDR blocks for which this role is applicable.</p></li>
<li><p><strong>default_critical_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of critical options that certificates have when signed.</p></li>
<li><p><strong>default_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of extensions that certificates have when signed.</p></li>
<li><p><strong>default_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default username for which a credential will be generated.</p></li>
<li><p><strong>key_id_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom format for the key id of a signed certificate.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of credentials generated by this role. This can be either <code class="docutils literal notranslate"><span class="pre">otp</span></code>, <code class="docutils literal notranslate"><span class="pre">dynamic</span></code> or <code class="docutils literal notranslate"><span class="pre">ca</span></code>.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum Time To Live value.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the role to create.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Time To Live value.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allow_bare_domains">
<code class="sig-name descname">allow_bare_domains</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allow_bare_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if host certificates that are requested are allowed to use the base domains listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allow_host_certificates">
<code class="sig-name descname">allow_host_certificates</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allow_host_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if certificates are allowed to be signed for use as a ‘host’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allow_subdomains">
<code class="sig-name descname">allow_subdomains</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allow_subdomains" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if host certificates that are requested are allowed to be subdomains of those listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allow_user_certificates">
<code class="sig-name descname">allow_user_certificates</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allow_user_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if certificates are allowed to be signed for use as a ‘user’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allow_user_key_ids">
<code class="sig-name descname">allow_user_key_ids</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allow_user_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if users can override the key ID for a signed certificate with the <code class="docutils literal notranslate"><span class="pre">key_id</span></code> field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allowed_critical_options">
<code class="sig-name descname">allowed_critical_options</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allowed_critical_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a comma-separated list of critical options that certificates can have when signed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allowed_domains">
<code class="sig-name descname">allowed_domains</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allowed_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of domains for which a client can request a host certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allowed_extensions">
<code class="sig-name descname">allowed_extensions</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allowed_extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a comma-separated list of extensions that certificates can have when signed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allowed_user_key_lengths">
<code class="sig-name descname">allowed_user_key_lengths</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allowed_user_key_lengths" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a map of ssh key types and their expected sizes which are allowed to be signed by the CA type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.allowed_users">
<code class="sig-name descname">allowed_users</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.allowed_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a comma-separated list of usernames that are to be allowed, only if certain usernames are to be allowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path where the SSH secret backend is mounted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.cidr_list">
<code class="sig-name descname">cidr_list</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.cidr_list" title="Permalink to this definition">¶</a></dt>
<dd><p>The comma-separated string of CIDR blocks for which this role is applicable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.default_critical_options">
<code class="sig-name descname">default_critical_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.default_critical_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a map of critical options that certificates have when signed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.default_extensions">
<code class="sig-name descname">default_extensions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.default_extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a map of extensions that certificates have when signed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.default_user">
<code class="sig-name descname">default_user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.default_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the default username for which a credential will be generated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.key_id_format">
<code class="sig-name descname">key_id_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.key_id_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a custom format for the key id of a signed certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.key_type">
<code class="sig-name descname">key_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of credentials generated by this role. This can be either <code class="docutils literal notranslate"><span class="pre">otp</span></code>, <code class="docutils literal notranslate"><span class="pre">dynamic</span></code> or <code class="docutils literal notranslate"><span class="pre">ca</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum Time To Live value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the role to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.ssh.SecretBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Time To Live value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.ssh.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_bare_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_host_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_subdomains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_user_certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_user_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_critical_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_user_key_lengths</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_critical_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_bare_domains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if host certificates that are requested are allowed to use the base domains listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p></li>
<li><p><strong>allow_host_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if certificates are allowed to be signed for use as a ‘host’.</p></li>
<li><p><strong>allow_subdomains</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if host certificates that are requested are allowed to be subdomains of those listed in <code class="docutils literal notranslate"><span class="pre">allowed_domains</span></code>.</p></li>
<li><p><strong>allow_user_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if certificates are allowed to be signed for use as a ‘user’.</p></li>
<li><p><strong>allow_user_key_ids</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if users can override the key ID for a signed certificate with the <code class="docutils literal notranslate"><span class="pre">key_id</span></code> field.</p></li>
<li><p><strong>allowed_critical_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of critical options that certificates can have when signed.</p></li>
<li><p><strong>allowed_domains</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of domains for which a client can request a host certificate.</p></li>
<li><p><strong>allowed_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of extensions that certificates can have when signed.</p></li>
<li><p><strong>allowed_user_key_lengths</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of ssh key types and their expected sizes which are allowed to be signed by the CA type.</p></li>
<li><p><strong>allowed_users</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated list of usernames that are to be allowed, only if certain usernames are to be allowed.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path where the SSH secret backend is mounted.</p></li>
<li><p><strong>cidr_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The comma-separated string of CIDR blocks for which this role is applicable.</p></li>
<li><p><strong>default_critical_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of critical options that certificates have when signed.</p></li>
<li><p><strong>default_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a map of extensions that certificates have when signed.</p></li>
<li><p><strong>default_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default username for which a credential will be generated.</p></li>
<li><p><strong>key_id_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a custom format for the key id of a signed certificate.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of credentials generated by this role. This can be either <code class="docutils literal notranslate"><span class="pre">otp</span></code>, <code class="docutils literal notranslate"><span class="pre">dynamic</span></code> or <code class="docutils literal notranslate"><span class="pre">ca</span></code>.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum Time To Live value.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the role to create.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Time To Live value.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.ssh.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.ssh.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.ssh.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
