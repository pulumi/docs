---
title: Module consul
title_tag: Module consul | Package pulumi_vault | Python SDK
linktitle: consul
notitle: true
---

<div class="section" id="consul">
<h1>consul<a class="headerlink" href="#consul" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.consul"></span><dl class="class">
<dt id="pulumi_vault.consul.SecretBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.consul.</code><code class="sig-name descname">SecretBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">scheme=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackend resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] address: Specifies the address of the Consul instance, provided as “host:port” like “127.0.0.1:8500”.
:param pulumi.Input[float] default_lease_ttl_seconds: The default TTL for credentials issued by this backend.
:param pulumi.Input[str] description: A human-friendly description for this backend.
:param pulumi.Input[float] max_lease_ttl_seconds: The maximum TTL that can be requested</p>
<blockquote>
<div><p>for credentials issued by this backend.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique location this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">consul</span></code>.</p></li>
<li><p><strong>scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URL scheme to use. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Consul management token this backend should use to issue new tokens.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the address of the Consul instance, provided as “host:port” like “127.0.0.1:8500”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.default_lease_ttl_seconds">
<code class="sig-name descname">default_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL for credentials issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly description for this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.max_lease_ttl_seconds">
<code class="sig-name descname">max_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL that can be requested
for credentials issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique location this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">consul</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.scheme">
<code class="sig-name descname">scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URL scheme to use. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackend.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The Consul management token this backend should use to issue new tokens.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.consul.SecretBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">scheme=None</em>, <em class="sig-param">token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the address of the Consul instance, provided as “host:port” like “127.0.0.1:8500”.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique location this backend should be mounted at. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">consul</span></code>.</p></li>
<li><p><strong>scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URL scheme to use. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Consul management token this backend should use to issue new tokens.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.consul.SecretBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.consul.SecretBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.consul.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.consul.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">local=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Consul secrets role for a Consul secrets engine in Vault. Consul secret backends can then issue Consul tokens.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/consul_secret_backend_role.html.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/consul_secret_backend_role.html.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. One of <code class="docutils literal notranslate"><span class="pre">path</span></code> or <code class="docutils literal notranslate"><span class="pre">backend</span></code> is required.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that the token should not be replicated globally and instead be local to the current datacenter.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum TTL for leases associated with this role, in seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Consul secrets engine role to create.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. <strong>Deprecated</strong></p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of Consul ACL policies to associate with these roles.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of token to create when using this role. Valid values are “client” or “management”.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the TTL for this role.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. One of <code class="docutils literal notranslate"><span class="pre">path</span></code> or <code class="docutils literal notranslate"><span class="pre">backend</span></code> is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.local">
<code class="sig-name descname">local</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.local" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that the token should not be replicated globally and instead be local to the current datacenter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum TTL for leases associated with this role, in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Consul secrets engine role to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. <strong>Deprecated</strong></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Consul ACL policies to associate with these roles.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of token to create when using this role. Valid values are “client” or “management”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.consul.SecretBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the TTL for this role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.consul.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">local=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. One of <code class="docutils literal notranslate"><span class="pre">path</span></code> or <code class="docutils literal notranslate"><span class="pre">backend</span></code> is required.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that the token should not be replicated globally and instead be local to the current datacenter.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum TTL for leases associated with this role, in seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Consul secrets engine role to create.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of an existing Consul secrets backend mount. Must not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. <strong>Deprecated</strong></p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of Consul ACL policies to associate with these roles.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of token to create when using this role. Valid values are “client” or “management”.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the TTL for this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.consul.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.consul.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.consul.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
