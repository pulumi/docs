---
title: Package pulumi_vault
title_tag: Package pulumi_vault | Python SDK
linktitle: pulumi_vault
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "vault" >}}

<div class="section" id="pulumi-vault">
<h1>Pulumi Vault<a class="headerlink" href="#pulumi-vault" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault"></span><dl class="py class">
<dt id="pulumi_vault.Audit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Audit</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Audit" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Audit</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;file_path&quot;</span><span class="p">:</span> <span class="s2">&quot;C:/temp/audit.txt&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;file&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Audit</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.1:8000&quot;</span><span class="p">,</span>
        <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;application x socket&quot;</span><span class="p">,</span>
        <span class="s2">&quot;socket_type&quot;</span><span class="p">:</span> <span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;app_socket&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;socket&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Audit devices can be imported using the <code class="docutils literal notranslate"><span class="pre">path</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/audit:Audit <span class="nb">test</span> syslog
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-friendly description of the audit device.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Configuration options to pass to the audit device itself.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to mount the audit device. This defaults to the type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the audit device, such as ‘file’.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Audit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.audit.Audit<a class="headerlink" href="#pulumi_vault.Audit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Audit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-friendly description of the audit device.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Configuration options to pass to the audit device itself.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to mount the audit device. This defaults to the type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the audit device, such as ‘file’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Audit.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_vault.Audit.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-friendly description of the audit device.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Audit.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_vault.Audit.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options to pass to the audit device itself.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Audit.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_vault.Audit.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to mount the audit device. This defaults to the type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Audit.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_vault.Audit.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the audit device, such as ‘file’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Audit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Audit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Audit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Audit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listing_visibility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="p">:</span> <span class="n">Union[AuthBackendTuneArgs, Mapping[str, Any], Awaitable[Union[AuthBackendTuneArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">tune</span><span class="o">=</span><span class="n">vault</span><span class="o">.</span><span class="n">AuthBackendTuneArgs</span><span class="p">(</span>
        <span class="n">listing_visibility</span><span class="o">=</span><span class="s2">&quot;unauth&quot;</span><span class="p">,</span>
        <span class="n">max_lease_ttl</span><span class="o">=</span><span class="s2">&quot;90000s&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;github&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Auth methods can be imported using the <code class="docutils literal notranslate"><span class="pre">path</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/authBackend:AuthBackend example github
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.default_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The default lease duration in seconds.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the auth method</p></li>
<li><p><strong>listing_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are “unauth” or “hidden”.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the auth method is local only.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.max_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The maximum lease duration in seconds.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to mount the auth method — this defaults to the name of the type</p></li>
<li><p><strong>tune</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AuthBackendTuneArgs'</em><em>]</em><em>]</em>) – Extra configuration block. Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the auth method type</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listing_visibility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="p">:</span> <span class="n">Union[AuthBackendTuneArgs, Mapping[str, Any], Awaitable[Union[AuthBackendTuneArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.auth_backend.AuthBackend<a class="headerlink" href="#pulumi_vault.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The accessor for this auth method</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.default_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The default lease duration in seconds.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the auth method</p></li>
<li><p><strong>listing_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are “unauth” or “hidden”.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the auth method is local only.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.max_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The maximum lease duration in seconds.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to mount the auth method — this defaults to the name of the type</p></li>
<li><p><strong>tune</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AuthBackendTuneArgs'</em><em>]</em><em>]</em>) – Extra configuration block. Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the auth method type</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.accessor">
<em class="property">property </em><code class="sig-name descname">accessor</code><a class="headerlink" href="#pulumi_vault.AuthBackend.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor for this auth method</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.default_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">default_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.AuthBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.default_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The default lease duration in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_vault.AuthBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the auth method</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.listing_visibility">
<em class="property">property </em><code class="sig-name descname">listing_visibility</code><a class="headerlink" href="#pulumi_vault.AuthBackend.listing_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are “unauth” or “hidden”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.local">
<em class="property">property </em><code class="sig-name descname">local</code><a class="headerlink" href="#pulumi_vault.AuthBackend.local" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the auth method is local only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.max_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">max_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.AuthBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">tune.max_lease_ttl</span></code> if you are using Vault provider version &gt;= 1.8) The maximum lease duration in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_vault.AuthBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to mount the auth method — this defaults to the name of the type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.tune">
<em class="property">property </em><code class="sig-name descname">tune</code><a class="headerlink" href="#pulumi_vault.AuthBackend.tune" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra configuration block. Structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_vault.AuthBackend.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the auth method type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.AwaitableGetAuthBackendResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">AwaitableGetAuthBackendResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listing_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.AwaitableGetAuthBackendResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_vault.AwaitableGetPolicyDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">AwaitableGetPolicyDocumentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hcl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.AwaitableGetPolicyDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_vault.CertAuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">CertAuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_common_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_dns_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_email_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_organization_units</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_uri_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_cidrs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_extensions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a role in an <a class="reference external" href="https://www.vaultproject.io/docs/auth/cert.html">Cert auth backend within Vault</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">cert_auth_backend</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;certAuthBackend&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;cert&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cert&quot;</span><span class="p">)</span>
<span class="n">cert_cert_auth_backend_role</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">CertAuthBackendRole</span><span class="p">(</span><span class="s2">&quot;certCertAuthBackendRole&quot;</span><span class="p">,</span>
    <span class="n">certificate</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;/path/to/certs/ca-cert.pem&quot;</span><span class="p">),</span>
    <span class="n">backend</span><span class="o">=</span><span class="n">cert_auth_backend</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
    <span class="n">allowed_names</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo.example.org&quot;</span><span class="p">,</span>
        <span class="s2">&quot;baz.example.org&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">token_ttl</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">token_max_ttl</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="n">token_policies</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_common_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed the common names for authenticated client certificates</p></li>
<li><p><strong>allowed_dns_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed alternative dns names for authenticated client certificates</p></li>
<li><p><strong>allowed_email_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed emails for authenticated client certificates</p></li>
<li><p><strong>allowed_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed subject names for authenticated client certificates</p></li>
<li><p><strong>allowed_organization_units</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed organization units for authenticated client certificates</p></li>
<li><p><strong>allowed_uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed URIs for authenticated client certificates</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted Cert auth backend</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Restriction usage of the
certificates to client IPs falling within the range of the specified CIDRs</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CA certificate used to validate client certificates</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display on tokens issued under this role.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>required_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – TLS extensions required on client certificates</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_common_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_dns_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_email_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_organization_units</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_uri_sans</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bound_cidrs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_extensions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.cert_auth_backend_role.CertAuthBackendRole<a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertAuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_common_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed the common names for authenticated client certificates</p></li>
<li><p><strong>allowed_dns_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed alternative dns names for authenticated client certificates</p></li>
<li><p><strong>allowed_email_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed emails for authenticated client certificates</p></li>
<li><p><strong>allowed_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed subject names for authenticated client certificates</p></li>
<li><p><strong>allowed_organization_units</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed organization units for authenticated client certificates</p></li>
<li><p><strong>allowed_uri_sans</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Allowed URIs for authenticated client certificates</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted Cert auth backend</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Restriction usage of the
certificates to client IPs falling within the range of the specified CIDRs</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CA certificate used to validate client certificates</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to display on tokens issued under this role.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>required_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – TLS extensions required on client certificates</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_common_names">
<em class="property">property </em><code class="sig-name descname">allowed_common_names</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_common_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed the common names for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_dns_sans">
<em class="property">property </em><code class="sig-name descname">allowed_dns_sans</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_dns_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed alternative dns names for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_email_sans">
<em class="property">property </em><code class="sig-name descname">allowed_email_sans</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_email_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed emails for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_names">
<em class="property">property </em><code class="sig-name descname">allowed_names</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed subject names for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_organization_units">
<em class="property">property </em><code class="sig-name descname">allowed_organization_units</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_organization_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed organization units for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.allowed_uri_sans">
<em class="property">property </em><code class="sig-name descname">allowed_uri_sans</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.allowed_uri_sans" title="Permalink to this definition">¶</a></dt>
<dd><p>Allowed URIs for authenticated client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.backend">
<em class="property">property </em><code class="sig-name descname">backend</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to the mounted Cert auth backend</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.bound_cidrs">
<em class="property">property </em><code class="sig-name descname">bound_cidrs</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>Restriction usage of the
certificates to client IPs falling within the range of the specified CIDRs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>CA certificate used to validate client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to display on tokens issued under this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.max_ttl">
<em class="property">property </em><code class="sig-name descname">max_ttl</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.period">
<em class="property">property </em><code class="sig-name descname">period</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.required_extensions">
<em class="property">property </em><code class="sig-name descname">required_extensions</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.required_extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS extensions required on client certificates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_bound_cidrs">
<em class="property">property </em><code class="sig-name descname">token_bound_cidrs</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_explicit_max_ttl">
<em class="property">property </em><code class="sig-name descname">token_explicit_max_ttl</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_max_ttl">
<em class="property">property </em><code class="sig-name descname">token_max_ttl</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_no_default_policy">
<em class="property">property </em><code class="sig-name descname">token_no_default_policy</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_num_uses">
<em class="property">property </em><code class="sig-name descname">token_num_uses</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_period">
<em class="property">property </em><code class="sig-name descname">token_period</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_policies">
<em class="property">property </em><code class="sig-name descname">token_policies</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_ttl">
<em class="property">property </em><code class="sig-name descname">token_ttl</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.token_type">
<em class="property">property </em><code class="sig-name descname">token_type</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.CertAuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.CertAuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.CertAuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.EgpPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">EgpPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paths</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.EgpPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage Endpoint Governing Policy (EGP) via <a class="reference external" href="https://www.vaultproject.io/docs/enterprise/sentinel/index.html">Sentinel</a>.</p>
<p><strong>Note</strong> this feature is available only with Vault Enterprise.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">allow_all</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">EgpPolicy</span><span class="p">(</span><span class="s2">&quot;allow-all&quot;</span><span class="p">,</span>
    <span class="n">enforcement_level</span><span class="o">=</span><span class="s2">&quot;soft-mandatory&quot;</span><span class="p">,</span>
    <span class="n">paths</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*&quot;</span><span class="p">],</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;main = rule {</span>
<span class="s2">  true</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enforcement_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>paths</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of paths to which the policy will be applied to</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Sentinel policy</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paths</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.egp_policy.EgpPolicy<a class="headerlink" href="#pulumi_vault.EgpPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EgpPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enforcement_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>paths</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of paths to which the policy will be applied to</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Sentinel policy</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.enforcement_level">
<em class="property">property </em><code class="sig-name descname">enforcement_level</code><a class="headerlink" href="#pulumi_vault.EgpPolicy.enforcement_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.EgpPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.paths">
<em class="property">property </em><code class="sig-name descname">paths</code><a class="headerlink" href="#pulumi_vault.EgpPolicy.paths" title="Permalink to this definition">¶</a></dt>
<dd><p>List of paths to which the policy will be applied to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_vault.EgpPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing a Sentinel policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.EgpPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.EgpPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.EgpPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.EgpPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.GetAuthBackendResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">GetAuthBackendResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listing_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthBackend.</p>
<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.accessor">
<em class="property">property </em><code class="sig-name descname">accessor</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor for this auth method</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.default_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">default_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default lease duration in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the auth method.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.listing_visibility">
<em class="property">property </em><code class="sig-name descname">listing_visibility</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.listing_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Speficies whether to show this mount in the UI-specific listing endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.local">
<em class="property">property </em><code class="sig-name descname">local</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.local" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the auth method is local only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.max_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">max_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lease duration in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetAuthBackendResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_vault.GetAuthBackendResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the auth method type.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_vault.GetPolicyDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">GetPolicyDocumentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hcl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.GetPolicyDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyDocument.</p>
<dl class="py method">
<dt id="pulumi_vault.GetPolicyDocumentResult.hcl">
<em class="property">property </em><code class="sig-name descname">hcl</code><a class="headerlink" href="#pulumi_vault.GetPolicyDocumentResult.hcl" title="Permalink to this definition">¶</a></dt>
<dd><p>The above arguments serialized as a standard Vault HCL policy document.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.GetPolicyDocumentResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_vault.GetPolicyDocumentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_vault.MfaDuo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">MfaDuo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_accessor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_info</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.MfaDuo" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage <a class="reference external" href="https://www.vaultproject.io/docs/enterprise/mfa/mfa-duo.html">Duo MFA</a>.</p>
<p><strong>Note</strong> this feature is available only with Vault Enterprise.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">userpass</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;userpass&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;userpass&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;userpass&quot;</span><span class="p">)</span>
<span class="n">my_duo</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">MfaDuo</span><span class="p">(</span><span class="s2">&quot;myDuo&quot;</span><span class="p">,</span>
    <span class="n">api_hostname</span><span class="o">=</span><span class="s2">&quot;api-2b5c39f5.duosecurity.com&quot;</span><span class="p">,</span>
    <span class="n">integration_key</span><span class="o">=</span><span class="s2">&quot;BIACEUEAXI20BNWTEYXT&quot;</span><span class="p">,</span>
    <span class="n">mount_accessor</span><span class="o">=</span><span class="n">userpass</span><span class="o">.</span><span class="n">accessor</span><span class="p">,</span>
    <span class="n">secret_key</span><span class="o">=</span><span class="s2">&quot;8C7THtrIigh2rPZQMbguugt8IUftWhMRCOBzbuyz&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Mounts can be imported using the <code class="docutils literal notranslate"><span class="pre">path</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/mfaDuo:MfaDuo my_duo my_duo
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - API hostname for Duo.</p></li>
<li><p><strong>integration_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Integration key for Duo.</p></li>
<li><p><strong>mount_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> – Name of the MFA method.</p></li>
<li><p><strong>push_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string)</span></code> - Push information for Duo.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Secret key for Duo.</p></li>
<li><p><strong>username_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string)</span></code> - A format string for mapping Identity names to MFA method names. Values to substitute should be placed in <code class="docutils literal notranslate"><span class="pre">{{}}</span></code>. For example, <code class="docutils literal notranslate"><span class="pre">&quot;{{alias.name}}&#64;example.com&quot;</span></code>. If blank, the Alias’s Name field will be used as-is. Currently-supported mappings:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- alias.name: The name returned by the mount configured via the `mount_accessor` parameter
- entity.name: The name configured for the Entity
- alias.metadata.`&lt;key&gt;`: The value of the Alias&#39;s metadata parameter
- entity.metadata.`&lt;key&gt;`: The value of the Entity&#39;s metadata parameter
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_vault.MfaDuo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_accessor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_info</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username_format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.mfa_duo.MfaDuo<a class="headerlink" href="#pulumi_vault.MfaDuo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MfaDuo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - API hostname for Duo.</p></li>
<li><p><strong>integration_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Integration key for Duo.</p></li>
<li><p><strong>mount_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> – Name of the MFA method.</p></li>
<li><p><strong>push_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string)</span></code> - Push information for Duo.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Secret key for Duo.</p></li>
<li><p><strong>username_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">(string)</span></code> - A format string for mapping Identity names to MFA method names. Values to substitute should be placed in <code class="docutils literal notranslate"><span class="pre">{{}}</span></code>. For example, <code class="docutils literal notranslate"><span class="pre">&quot;{{alias.name}}&#64;example.com&quot;</span></code>. If blank, the Alias’s Name field will be used as-is. Currently-supported mappings:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- alias.name: The name returned by the mount configured via the `mount_accessor` parameter
- entity.name: The name configured for the Entity
- alias.metadata.`&lt;key&gt;`: The value of the Alias&#39;s metadata parameter
- entity.metadata.`&lt;key&gt;`: The value of the Entity&#39;s metadata parameter
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.api_hostname">
<em class="property">property </em><code class="sig-name descname">api_hostname</code><a class="headerlink" href="#pulumi_vault.MfaDuo.api_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - API hostname for Duo.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.integration_key">
<em class="property">property </em><code class="sig-name descname">integration_key</code><a class="headerlink" href="#pulumi_vault.MfaDuo.integration_key" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Integration key for Duo.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.mount_accessor">
<em class="property">property </em><code class="sig-name descname">mount_accessor</code><a class="headerlink" href="#pulumi_vault.MfaDuo.mount_accessor" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.MfaDuo.name" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> – Name of the MFA method.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.push_info">
<em class="property">property </em><code class="sig-name descname">push_info</code><a class="headerlink" href="#pulumi_vault.MfaDuo.push_info" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string)</span></code> - Push information for Duo.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.secret_key">
<em class="property">property </em><code class="sig-name descname">secret_key</code><a class="headerlink" href="#pulumi_vault.MfaDuo.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string:</span> <span class="pre">&lt;required&gt;)</span></code> - Secret key for Duo.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.username_format">
<em class="property">property </em><code class="sig-name descname">username_format</code><a class="headerlink" href="#pulumi_vault.MfaDuo.username_format" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">(string)</span></code> - A format string for mapping Identity names to MFA method names. Values to substitute should be placed in <code class="docutils literal notranslate"><span class="pre">{{}}</span></code>. For example, <code class="docutils literal notranslate"><span class="pre">&quot;{{alias.name}}&#64;example.com&quot;</span></code>. If blank, the Alias’s Name field will be used as-is. Currently-supported mappings:</p>
<ul class="simple">
<li><p>alias.name: The name returned by the mount configured via the <code class="docutils literal notranslate"><span class="pre">mount_accessor</span></code> parameter</p></li>
<li><p>entity.name: The name configured for the Entity</p></li>
<li><p>alias.metadata.<code class="docutils literal notranslate"><span class="pre">&lt;key&gt;</span></code>: The value of the Alias’s metadata parameter</p></li>
<li><p>entity.metadata.<code class="docutils literal notranslate"><span class="pre">&lt;key&gt;</span></code>: The value of the Entity’s metadata parameter</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.MfaDuo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.MfaDuo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.MfaDuo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.MfaDuo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Mount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Mount</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_entropy_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">seal_wrap</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Mount" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Mount</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This is an example mount&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;dummy&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;generic&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Mounts can be imported using the <code class="docutils literal notranslate"><span class="pre">path</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/mount:Mount example dummy
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Default lease duration for tokens and secrets in seconds</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-friendly description of the mount</p></li>
<li><p><strong>external_entropy_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enable the secrets engine to access Vault’s external entropy source</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enforce local mount in HA environment</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum possible lease duration for tokens and secrets in seconds</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Specifies mount type specific options that are passed to the backend</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Where the secret backend will be mounted</p></li>
<li><p><strong>seal_wrap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal’s encryption capability</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the backend, such as “aws”</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Mount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_entropy_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">seal_wrap</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.mount.Mount<a class="headerlink" href="#pulumi_vault.Mount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Mount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The accessor for this mount.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Default lease duration for tokens and secrets in seconds</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-friendly description of the mount</p></li>
<li><p><strong>external_entropy_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enable the secrets engine to access Vault’s external entropy source</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enforce local mount in HA environment</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum possible lease duration for tokens and secrets in seconds</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Specifies mount type specific options that are passed to the backend</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Where the secret backend will be mounted</p></li>
<li><p><strong>seal_wrap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag that can be explicitly set to true to enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal’s encryption capability</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the backend, such as “aws”</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.accessor">
<em class="property">property </em><code class="sig-name descname">accessor</code><a class="headerlink" href="#pulumi_vault.Mount.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor for this mount.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.default_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">default_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.Mount.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Default lease duration for tokens and secrets in seconds</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_vault.Mount.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-friendly description of the mount</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.external_entropy_access">
<em class="property">property </em><code class="sig-name descname">external_entropy_access</code><a class="headerlink" href="#pulumi_vault.Mount.external_entropy_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag that can be explicitly set to true to enable the secrets engine to access Vault’s external entropy source</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.local">
<em class="property">property </em><code class="sig-name descname">local</code><a class="headerlink" href="#pulumi_vault.Mount.local" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag that can be explicitly set to true to enforce local mount in HA environment</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.max_lease_ttl_seconds">
<em class="property">property </em><code class="sig-name descname">max_lease_ttl_seconds</code><a class="headerlink" href="#pulumi_vault.Mount.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum possible lease duration for tokens and secrets in seconds</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_vault.Mount.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies mount type specific options that are passed to the backend</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_vault.Mount.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Where the secret backend will be mounted</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.seal_wrap">
<em class="property">property </em><code class="sig-name descname">seal_wrap</code><a class="headerlink" href="#pulumi_vault.Mount.seal_wrap" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag that can be explicitly set to true to enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal’s encryption capability</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_vault.Mount.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the backend, such as “aws”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Mount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Mount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Mount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Mount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage <a class="reference external" href="https://www.vaultproject.io/docs/enterprise/namespaces/index.html">Namespaces</a>.</p>
<p><strong>Note</strong> this feature is available only with Vault Enterprise.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">ns1</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Namespace</span><span class="p">(</span><span class="s2">&quot;ns1&quot;</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="s2">&quot;ns1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the namespace. Must not have a trailing <code class="docutils literal notranslate"><span class="pre">/</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.namespace.Namespace<a class="headerlink" href="#pulumi_vault.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the namepsace.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the namespace. Must not have a trailing <code class="docutils literal notranslate"><span class="pre">/</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Namespace.namespace_id">
<em class="property">property </em><code class="sig-name descname">namespace_id</code><a class="headerlink" href="#pulumi_vault.Namespace.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the namepsace.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Namespace.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_vault.Namespace.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the namespace. Must not have a trailing <code class="docutils literal notranslate"><span class="pre">/</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Policy" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;path &quot;secret/my_app&quot; {</span>
<span class="s2">  capabilities = [&quot;update&quot;]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Policies can be imported using the <code class="docutils literal notranslate"><span class="pre">name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/policy:Policy example dev-team
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Vault policy</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.policy.Policy<a class="headerlink" href="#pulumi_vault.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Vault policy</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Policy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Policy.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_vault.Policy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing a Vault policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">add_address_to_env</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_logins</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProviderAuthLoginArgs, Mapping[str, Any], Awaitable[Union[ProviderAuthLoginArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProviderAuthLoginArgs, Mapping[str, Any], Awaitable[Union[ProviderAuthLoginArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert_dir</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_auths</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProviderClientAuthArgs, Mapping[str, Any], Awaitable[Union[ProviderClientAuthArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProviderClientAuthArgs, Mapping[str, Any], Awaitable[Union[ProviderClientAuthArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProviderHeaderArgs, Mapping[str, Any], Awaitable[Union[ProviderHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProviderHeaderArgs, Mapping[str, Any], Awaitable[Union[ProviderHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_lease_ttl_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_tls_verify</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the vault package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_address_to_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If true, adds the value of the <code class="docutils literal notranslate"><span class="pre">address</span></code> argument to the Terraform process environment.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the root of the target Vault server.</p></li>
<li><p><strong>auth_logins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProviderAuthLoginArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Login to vault with an existing auth method using auth/<span class="raw-html-m2r"><mount></span>/login</p></li>
<li><p><strong>ca_cert_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to directory containing CA certificate files to validate the server’s certificate.</p></li>
<li><p><strong>ca_cert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a CA certificate file to validate the server’s certificate.</p></li>
<li><p><strong>client_auths</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProviderClientAuthArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Client authentication credentials.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProviderHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The headers to send with each Vault request.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum TTL for secret leases requested by this provider</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of retries when a 5xx error code is encountered.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to use. Available only for Vault Enterprise</p></li>
<li><p><strong>skip_tls_verify</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to true only if the target Vault server is an insecure development instance.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token to use to authenticate to Vault.</p></li>
<li><p><strong>token_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token name to use for creating the Vault child token.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.QuotaRateLimit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">QuotaRateLimit</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.QuotaRateLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage rate limit quotas which enforce API rate limiting using a token bucket algorithm.
A rate limit quota can be created at the root level or defined on a namespace or mount by
specifying a path when creating the quota.</p>
<p>See <a class="reference external" href="https://www.vaultproject.io/docs/concepts/resource-quotas">Vault’s Documentation</a> for more
information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">global_</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">QuotaRateLimit</span><span class="p">(</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">rate</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
</pre></div>
</div>
<p>Rate limit quotas can be imported using their names</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/quotaRateLimit:QuotaRateLimit global global
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the rate limit quota</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path of the mount or namespace to apply the quota. A blank path configures a
global rate limit quota. For example <code class="docutils literal notranslate"><span class="pre">namespace1/</span></code> adds a quota to a full namespace,
<code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> adds a <code class="docutils literal notranslate"><span class="pre">quota</span></code> to <code class="docutils literal notranslate"><span class="pre">userpass</span></code> in <code class="docutils literal notranslate"><span class="pre">namespace1</span></code>.
Updating this field on an existing quota can have “moving” effects. For example, updating
<code class="docutils literal notranslate"><span class="pre">auth/userpass</span></code> to <code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> moves this quota from being a global mount quota to
a namespace specific mount quota. <strong>Note, namespaces are supported in Enterprise only.</strong></p></li>
<li><p><strong>rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests at any given second to be allowed by the quota
rule. The <code class="docutils literal notranslate"><span class="pre">rate</span></code> must be positive.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.QuotaRateLimit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.quota_rate_limit.QuotaRateLimit<a class="headerlink" href="#pulumi_vault.QuotaRateLimit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QuotaRateLimit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the rate limit quota</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path of the mount or namespace to apply the quota. A blank path configures a
global rate limit quota. For example <code class="docutils literal notranslate"><span class="pre">namespace1/</span></code> adds a quota to a full namespace,
<code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> adds a <code class="docutils literal notranslate"><span class="pre">quota</span></code> to <code class="docutils literal notranslate"><span class="pre">userpass</span></code> in <code class="docutils literal notranslate"><span class="pre">namespace1</span></code>.
Updating this field on an existing quota can have “moving” effects. For example, updating
<code class="docutils literal notranslate"><span class="pre">auth/userpass</span></code> to <code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> moves this quota from being a global mount quota to
a namespace specific mount quota. <strong>Note, namespaces are supported in Enterprise only.</strong></p></li>
<li><p><strong>rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of requests at any given second to be allowed by the quota
rule. The <code class="docutils literal notranslate"><span class="pre">rate</span></code> must be positive.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.QuotaRateLimit.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.QuotaRateLimit.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the rate limit quota</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.QuotaRateLimit.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_vault.QuotaRateLimit.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path of the mount or namespace to apply the quota. A blank path configures a
global rate limit quota. For example <code class="docutils literal notranslate"><span class="pre">namespace1/</span></code> adds a quota to a full namespace,
<code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> adds a <code class="docutils literal notranslate"><span class="pre">quota</span></code> to <code class="docutils literal notranslate"><span class="pre">userpass</span></code> in <code class="docutils literal notranslate"><span class="pre">namespace1</span></code>.
Updating this field on an existing quota can have “moving” effects. For example, updating
<code class="docutils literal notranslate"><span class="pre">auth/userpass</span></code> to <code class="docutils literal notranslate"><span class="pre">namespace1/auth/userpass</span></code> moves this quota from being a global mount quota to
a namespace specific mount quota. <strong>Note, namespaces are supported in Enterprise only.</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.QuotaRateLimit.rate">
<em class="property">property </em><code class="sig-name descname">rate</code><a class="headerlink" href="#pulumi_vault.QuotaRateLimit.rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of requests at any given second to be allowed by the quota
rule. The <code class="docutils literal notranslate"><span class="pre">rate</span></code> must be positive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.QuotaRateLimit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.QuotaRateLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.QuotaRateLimit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.QuotaRateLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.RgpPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">RgpPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.RgpPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage Role Governing Policy (RGP) via <a class="reference external" href="https://www.vaultproject.io/docs/enterprise/sentinel/index.html">Sentinel</a>.</p>
<p><strong>Note</strong> this feature is available only with Vault Enterprise.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">allow_all</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">RgpPolicy</span><span class="p">(</span><span class="s2">&quot;allow-all&quot;</span><span class="p">,</span>
    <span class="n">enforcement_level</span><span class="o">=</span><span class="s2">&quot;soft-mandatory&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;main = rule {</span>
<span class="s2">  true</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enforcement_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Sentinel policy</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.RgpPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforcement_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.rgp_policy.RgpPolicy<a class="headerlink" href="#pulumi_vault.RgpPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RgpPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enforcement_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a Sentinel policy</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.RgpPolicy.enforcement_level">
<em class="property">property </em><code class="sig-name descname">enforcement_level</code><a class="headerlink" href="#pulumi_vault.RgpPolicy.enforcement_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforcement level of Sentinel policy. Can be either <code class="docutils literal notranslate"><span class="pre">advisory</span></code> or <code class="docutils literal notranslate"><span class="pre">soft-mandatory</span></code> or <code class="docutils literal notranslate"><span class="pre">hard-mandatory</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.RgpPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_vault.RgpPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.RgpPolicy.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_vault.RgpPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing a Sentinel policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.RgpPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.RgpPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.RgpPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.RgpPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Token">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">Token</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">explicit_max_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_default_policy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_parent</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_uses</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_increment</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_min_lease</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wrapping_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Token" title="Permalink to this definition">¶</a></dt>
<dd><p>Tokens can be imported using its <code class="docutils literal notranslate"><span class="pre">id</span></code> as accessor id, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import vault:index/token:Token example &lt;accessor_id&gt;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the token display name</p></li>
<li><p><strong>explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The explicit max TTL of this token</p></li>
<li><p><strong>no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to not attach the default policy to this token</p></li>
<li><p><strong>no_parent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to create a token without parent</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of allowed uses of this token</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of this token</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PGP key (base64 encoded) to encrypt the token.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of policies to attach to this token</p></li>
<li><p><strong>renew_increment</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The renew increment</p></li>
<li><p><strong>renew_min_lease</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimal lease to renew this token</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow to renew this token</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token role name</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of this token</p></li>
<li><p><strong>wrapping_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of the wrapped token.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_vault.Token.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_client_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">explicit_max_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lease_duration</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lease_started</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_default_policy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_parent</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_uses</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_increment</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_min_lease</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wrapped_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wrapping_accessor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wrapping_ttl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.token.Token<a class="headerlink" href="#pulumi_vault.Token.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Token resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the client token if stored in present file</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the token display name</p></li>
<li><p><strong>encrypted_client_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the client token encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> if stored in present file</p></li>
<li><p><strong>explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The explicit max TTL of this token</p></li>
<li><p><strong>lease_duration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – String containing the token lease duration if present in state file</p></li>
<li><p><strong>lease_started</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the token lease started time if present in state file</p></li>
<li><p><strong>no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to not attach the default policy to this token</p></li>
<li><p><strong>no_parent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to create a token without parent</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of allowed uses of this token</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of this token</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PGP key (base64 encoded) to encrypt the token.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of policies to attach to this token</p></li>
<li><p><strong>renew_increment</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The renew increment</p></li>
<li><p><strong>renew_min_lease</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimal lease to renew this token</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag to allow to renew this token</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token role name</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of this token</p></li>
<li><p><strong>wrapped_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client wrapped token.</p></li>
<li><p><strong>wrapping_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client wrapping accessor.</p></li>
<li><p><strong>wrapping_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of the wrapped token.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.client_token">
<em class="property">property </em><code class="sig-name descname">client_token</code><a class="headerlink" href="#pulumi_vault.Token.client_token" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the client token if stored in present file</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_vault.Token.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the token display name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.encrypted_client_token">
<em class="property">property </em><code class="sig-name descname">encrypted_client_token</code><a class="headerlink" href="#pulumi_vault.Token.encrypted_client_token" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the client token encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> if stored in present file</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.explicit_max_ttl">
<em class="property">property </em><code class="sig-name descname">explicit_max_ttl</code><a class="headerlink" href="#pulumi_vault.Token.explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The explicit max TTL of this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.lease_duration">
<em class="property">property </em><code class="sig-name descname">lease_duration</code><a class="headerlink" href="#pulumi_vault.Token.lease_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the token lease duration if present in state file</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.lease_started">
<em class="property">property </em><code class="sig-name descname">lease_started</code><a class="headerlink" href="#pulumi_vault.Token.lease_started" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the token lease started time if present in state file</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.no_default_policy">
<em class="property">property </em><code class="sig-name descname">no_default_policy</code><a class="headerlink" href="#pulumi_vault.Token.no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to not attach the default policy to this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.no_parent">
<em class="property">property </em><code class="sig-name descname">no_parent</code><a class="headerlink" href="#pulumi_vault.Token.no_parent" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to create a token without parent</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.num_uses">
<em class="property">property </em><code class="sig-name descname">num_uses</code><a class="headerlink" href="#pulumi_vault.Token.num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of allowed uses of this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.period">
<em class="property">property </em><code class="sig-name descname">period</code><a class="headerlink" href="#pulumi_vault.Token.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.pgp_key">
<em class="property">property </em><code class="sig-name descname">pgp_key</code><a class="headerlink" href="#pulumi_vault.Token.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The PGP key (base64 encoded) to encrypt the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_vault.Token.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to attach to this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.renew_increment">
<em class="property">property </em><code class="sig-name descname">renew_increment</code><a class="headerlink" href="#pulumi_vault.Token.renew_increment" title="Permalink to this definition">¶</a></dt>
<dd><p>The renew increment</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.renew_min_lease">
<em class="property">property </em><code class="sig-name descname">renew_min_lease</code><a class="headerlink" href="#pulumi_vault.Token.renew_min_lease" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimal lease to renew this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.renewable">
<em class="property">property </em><code class="sig-name descname">renewable</code><a class="headerlink" href="#pulumi_vault.Token.renewable" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag to allow to renew this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.role_name">
<em class="property">property </em><code class="sig-name descname">role_name</code><a class="headerlink" href="#pulumi_vault.Token.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The token role name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_vault.Token.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.wrapped_token">
<em class="property">property </em><code class="sig-name descname">wrapped_token</code><a class="headerlink" href="#pulumi_vault.Token.wrapped_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The client wrapped token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.wrapping_accessor">
<em class="property">property </em><code class="sig-name descname">wrapping_accessor</code><a class="headerlink" href="#pulumi_vault.Token.wrapping_accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The client wrapping accessor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.wrapping_ttl">
<em class="property">property </em><code class="sig-name descname">wrapping_ttl</code><a class="headerlink" href="#pulumi_vault.Token.wrapping_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of the wrapped token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.Token.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Token.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.Token.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.Token.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.get_auth_backend">
<code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">get_auth_backend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.get_auth_backend.AwaitableGetAuthBackendResult<a class="headerlink" href="#pulumi_vault.get_auth_backend" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">get_auth_backend</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="s2">&quot;userpass&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>path</strong> (<em>str</em>) – The auth backend mount point.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_vault.get_policy_document">
<code class="sig-prename descclassname">pulumi_vault.</code><code class="sig-name descname">get_policy_document</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetPolicyDocumentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_vault.get_policy_document.AwaitableGetPolicyDocumentResult<a class="headerlink" href="#pulumi_vault.get_policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a data source which can be used to construct a HCL representation of an Vault policy document, for use with resources which expect policy documents, such as the <code class="docutils literal notranslate"><span class="pre">Policy</span></code> resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example_policy_document</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">get_policy_document</span><span class="p">(</span><span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">vault</span><span class="o">.</span><span class="n">GetPolicyDocumentRuleArgs</span><span class="p">(</span>
    <span class="n">capabilities</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;create&quot;</span><span class="p">,</span>
        <span class="s2">&quot;read&quot;</span><span class="p">,</span>
        <span class="s2">&quot;update&quot;</span><span class="p">,</span>
        <span class="s2">&quot;delete&quot;</span><span class="p">,</span>
        <span class="s2">&quot;list&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;allow all on secrets&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;secret/*&quot;</span><span class="p">,</span>
<span class="p">)])</span>
<span class="n">example_policy</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;examplePolicy&quot;</span><span class="p">,</span> <span class="n">policy</span><span class="o">=</span><span class="n">example_policy_document</span><span class="o">.</span><span class="n">hcl</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

</div>
