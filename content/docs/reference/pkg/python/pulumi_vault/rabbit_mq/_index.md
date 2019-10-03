---
title: Module rabbit_mq
linktitle: rabbit_mq
notitle: true
---

<div class="section" id="rabbit-mq">
<h1>rabbit_mq<a class="headerlink" href="#rabbit-mq" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.rabbit_mq"></span><dl class="class">
<dt id="pulumi_vault.rabbit_mq.SecretBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.rabbit_mq.</code><code class="sig-name descname">SecretBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_uri=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">verify_connection=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackend resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ connection URI.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials
issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ management administrator password.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ management administrator username.</p></li>
<li><p><strong>verify_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to verify connection URI, username, and password.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.connection_uri">
<code class="sig-name descname">connection_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.connection_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the RabbitMQ connection URI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.default_lease_ttl_seconds">
<code class="sig-name descname">default_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL for credentials
issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly description for this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.max_lease_ttl_seconds">
<code class="sig-name descname">max_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL that can be requested
for credentials issued by this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the RabbitMQ management administrator password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the RabbitMQ management administrator username.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.verify_connection">
<code class="sig-name descname">verify_connection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.verify_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to verify connection URI, username, and password.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_uri=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">verify_connection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ connection URI.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials
issued by this backend.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ management administrator password.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">aws</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the RabbitMQ management administrator username.</p></li>
<li><p><strong>verify_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to verify connection URI, username, and password.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.rabbit_mq.SecretBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.rabbit_mq.SecretBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.rabbit_mq.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vhosts=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the RabbitMQ secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend.
Must be unique within the backend.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated RabbitMQ management tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vhosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the RabbitMQ secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to identify this role within the backend.
Must be unique within the backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a comma-separated RabbitMQ management tags.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vhosts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the RabbitMQ secret backend is mounted at,
with no leading or trailing <code class="docutils literal notranslate"><span class="pre">/</span></code>s.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to identify this role within the backend.
Must be unique within the backend.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a comma-separated RabbitMQ management tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vhosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/rabbitmq_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.rabbit_mq.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.rabbit_mq.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
