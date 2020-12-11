---
title: Package pulumi_cloudflare
title_tag: Package pulumi_cloudflare | Python SDK
linktitle: pulumi_cloudflare
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "cloudflare" >}}

<div class="section" id="pulumi-cloudflare">
<h1>Pulumi Cloudflare<a class="headerlink" href="#pulumi-cloudflare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-cloudflare/issues">pulumi/pulumi-cloudflare repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/issues">terraform-providers/terraform-provider-cloudflare repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_cloudflare"></span><dl class="py class">
<dt id="pulumi_cloudflare.AccessApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessApplication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_idps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_redirect_to_identity</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any], Awaitable[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any], Awaitable[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binding_cookie</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_duration</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># With CORS configuration</span>
<span class="n">staging_app</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessApplication</span><span class="p">(</span><span class="s2">&quot;stagingApp&quot;</span><span class="p">,</span>
    <span class="n">cors_headers</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessApplicationCorsHeaderArgs</span><span class="p">(</span>
        <span class="n">allow_credentials</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">allowed_methods</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;GET&quot;</span><span class="p">,</span>
            <span class="s2">&quot;POST&quot;</span><span class="p">,</span>
            <span class="s2">&quot;OPTIONS&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">allowed_origins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;https://example.com&quot;</span><span class="p">],</span>
        <span class="n">max_age</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;staging.example.com&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging application&quot;</span><span class="p">,</span>
    <span class="n">session_duration</span><span class="o">=</span><span class="s2">&quot;24h&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Access Applications can be imported using a composite ID formed of zone ID and application ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/accessApplication:AccessApplication staging cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>allowed_idps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The identity providers selected for the application.</p></li>
<li><p><strong>auto_redirect_to_identity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Option to skip identity provider
selection if only one is configured in allowed_idps. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>
(disabled).</p></li>
<li><p><strong>cors_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessApplicationCorsHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – CORS configuration for the Access Application. See
below for reference structure.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>enable_binding_cookie</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional “binding” cookie on requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">0s</span></code>, <code class="docutils literal notranslate"><span class="pre">15m</span></code>, <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_idps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aud</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_redirect_to_identity</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any], Awaitable[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any], Awaitable[Union[AccessApplicationCorsHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binding_cookie</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_duration</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_application.AccessApplication<a class="headerlink" href="#pulumi_cloudflare.AccessApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>allowed_idps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The identity providers selected for the application.</p></li>
<li><p><strong>aud</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Audience (AUD) Tag of the application</p></li>
<li><p><strong>auto_redirect_to_identity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Option to skip identity provider
selection if only one is configured in allowed_idps. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>
(disabled).</p></li>
<li><p><strong>cors_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessApplicationCorsHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – CORS configuration for the Access Application. See
below for reference structure.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>enable_binding_cookie</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional “binding” cookie on requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">0s</span></code>, <code class="docutils literal notranslate"><span class="pre">15m</span></code>, <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.allowed_idps">
<em class="property">property </em><code class="sig-name descname">allowed_idps</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.allowed_idps" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity providers selected for the application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.aud">
<em class="property">property </em><code class="sig-name descname">aud</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.aud" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Audience (AUD) Tag of the application</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.auto_redirect_to_identity">
<em class="property">property </em><code class="sig-name descname">auto_redirect_to_identity</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.auto_redirect_to_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Option to skip identity provider
selection if only one is configured in allowed_idps. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>
(disabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.cors_headers">
<em class="property">property </em><code class="sig-name descname">cors_headers</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.cors_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>CORS configuration for the Access Application. See
below for reference structure.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.enable_binding_cookie">
<em class="property">property </em><code class="sig-name descname">enable_binding_cookie</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.enable_binding_cookie" title="Permalink to this definition">¶</a></dt>
<dd><p>Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional “binding” cookie on requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.session_duration">
<em class="property">property </em><code class="sig-name descname">session_duration</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">0s</span></code>, <code class="docutils literal notranslate"><span class="pre">15m</span></code>, <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access application should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupExcludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupExcludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupIncludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupIncludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupRequireArgs, Mapping[str, Any], Awaitable[Union[AccessGroupRequireArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupRequireArgs, Mapping[str, Any], Awaitable[Union[AccessGroupRequireArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Group resource. Access Groups are used
in conjunction with Access Policies to restrict access to a
particular resource based on group membership.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Allowing access to `test@example.com` email address only</span>
<span class="n">test_group_access_group</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroup</span><span class="p">(</span><span class="s2">&quot;testGroupAccessGroup&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;975ecf5a45e3bcb680dba0722a420ad9&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging group&quot;</span><span class="p">,</span>
    <span class="n">includes</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroupIncludeArgs</span><span class="p">(</span>
        <span class="n">emails</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">)])</span>
<span class="c1"># Allowing `test@example.com` to access but only when coming from a</span>
<span class="c1"># specific IP.</span>
<span class="n">test_group_index_access_group_access_group</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroup</span><span class="p">(</span><span class="s2">&quot;testGroupIndex/accessGroupAccessGroup&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;975ecf5a45e3bcb680dba0722a420ad9&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging group&quot;</span><span class="p">,</span>
    <span class="n">includes</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroupIncludeArgs</span><span class="p">(</span>
        <span class="n">emails</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">requires</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ips&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;office_ip&quot;</span><span class="p">]],</span>
    <span class="p">})</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">require</span></code>, <code class="docutils literal notranslate"><span class="pre">exclude</span></code> and <code class="docutils literal notranslate"><span class="pre">include</span></code> arguments share the available
conditions which can be applied. The conditions are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> - (Optional) A list of IP addresses or ranges. Example:
<code class="docutils literal notranslate"><span class="pre">ip</span> <span class="pre">=</span> <span class="pre">[&quot;1.2.3.4&quot;,</span> <span class="pre">&quot;10.0.0.0/2&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) A list of email addresses. Example:
<code class="docutils literal notranslate"><span class="pre">email</span> <span class="pre">=</span> <span class="pre">[&quot;test&#64;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_domain</span></code> - (Optional) A list of email domains. Example:
<code class="docutils literal notranslate"><span class="pre">email_domain</span> <span class="pre">=</span> <span class="pre">[&quot;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_token</span></code> - (Optional) A list of service token ids. Example:
<code class="docutils literal notranslate"><span class="pre">service_token</span> <span class="pre">=</span> <span class="pre">[cloudflare_access_service_token.demo.id]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">any_valid_service_token</span></code> - (Optional) Boolean indicating if allow
all tokens to be granted. Example: <code class="docutils literal notranslate"><span class="pre">any_valid_service_token</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> - (Optional) A list of access group ids. Example:
<code class="docutils literal notranslate"><span class="pre">group</span> <span class="pre">=</span> <span class="pre">[cloudflare_access_group.demo.id]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> - (Optional) Boolean indicating permitting access for all
requests. Example: <code class="docutils literal notranslate"><span class="pre">everyone</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> - (Optional) Whether to use mTLS certificate authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">common_name</span></code> - (Optional) Use a certificate common name to authenticate with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auth_method</span></code> - (Optional) A string identifying the authentication
method code. The list of codes are listed here: <a class="reference external" href="https://tools.ietf.org/html/rfc8176#section-2">https://tools.ietf.org/html/rfc8176#section-2</a>.
Custom values are also supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo</span></code> - (Optional) A list of country codes. Example: <code class="docutils literal notranslate"><span class="pre">geo</span> <span class="pre">=</span> <span class="pre">[&quot;US&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuite</span></code> - (Optional) Use GSuite as the authentication mechanism. Example:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">github</span></code> - (Optional) Use a GitHub organization as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azure</span></code> - (Optional) Use Azure AD as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">okta</span></code> - (Optional) Use Okta as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml</span></code> - (Optional) Use an external SAML setup as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition.
Example:</p></li>
</ul>
<p>Access Groups can be imported using a composite ID formed of account ID and group ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accessGroup:AccessGroup staging 975ecf5a45e3bcb680dba0722a420ad9/67ea780ce4982c1cfbe6b7293afc765d

where * <span class="sb">``</span>975ecf5a45e3bcb680dba0722a420ad9<span class="sb">``</span> - Account ID * <span class="sb">``</span>67ea780ce4982c1cfbe6b7293afc765d<span class="sb">``</span> - Access Group ID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupExcludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupIncludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupRequireArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupExcludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupExcludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupIncludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessGroupIncludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessGroupRequireArgs, Mapping[str, Any], Awaitable[Union[AccessGroupRequireArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessGroupRequireArgs, Mapping[str, Any], Awaitable[Union[AccessGroupRequireArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_group.AccessGroup<a class="headerlink" href="#pulumi_cloudflare.AccessGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupExcludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupIncludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessGroupRequireArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.excludes">
<em class="property">property </em><code class="sig-name descname">excludes</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.includes">
<em class="property">property </em><code class="sig-name descname">includes</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.requires">
<em class="property">property </em><code class="sig-name descname">requires</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the zone the group is associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessIdentityProvider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any], Awaitable[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any], Awaitable[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Identity Provider resource. Identity Providers are
used as an authentication or authorisation source within Access.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># one time pin</span>
<span class="n">pin_login</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;pinLogin&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;PIN login&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;onetimepin&quot;</span><span class="p">)</span>
<span class="c1"># oauth</span>
<span class="n">github_oauth</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;githubOauth&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProviderConfigArgs</span><span class="p">(</span>
        <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
        <span class="n">client_secret</span><span class="o">=</span><span class="s2">&quot;secret_key&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;GitHub OAuth&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;github&quot;</span><span class="p">)</span>
<span class="c1"># saml</span>
<span class="n">jumpcloud_saml</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;jumpcloudSaml&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProviderConfigArgs</span><span class="p">(</span>
        <span class="n">attributes</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;email&quot;</span><span class="p">,</span>
            <span class="s2">&quot;username&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">idp_public_cert</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQ...GF/Q2/MHadws97cZg</span>
<span class="s2">uTnQyuOqPuHbnN83d/2l1NSYKCbHt24o</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="n">issuer_url</span><span class="o">=</span><span class="s2">&quot;jumpcloud&quot;</span><span class="p">,</span>
        <span class="n">sign_request</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">sso_target_url</span><span class="o">=</span><span class="s2">&quot;https://sso.myexample.jumpcloud.com/saml2/cloudflareaccess&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;JumpCloud SAML&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;saml&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Please refer to the [developers.cloudflare.com Access documentation][access_identity_provider_guide]
for full reference on what is available and how to configure your provider.</p>
<p>Access Identity Providers can be imported using a composite ID formed of account ID and Access Identity Provider ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accessIdentityProvider:AccessIdentityProvider my_idp cb029e245cfdd66dc8d2e570d5dd3322/e00e1c13-e350-44fe-96c5-fb75c954871c

<span class="o">[</span>access_identity_provider_guide<span class="o">]</span>https://developers.cloudflare.com/access/configuring-identity-providers/
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessIdentityProviderConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any], Awaitable[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any], Awaitable[Union[AccessIdentityProviderConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_identity_provider.AccessIdentityProvider<a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessIdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessIdentityProviderConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.configs">
<em class="property">property </em><code class="sig-name descname">configs</code><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Provider configuration from the [developer documentation][access_identity_provider_guide].</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Identity Provider configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID the provider should be associated with. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decision</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyExcludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyExcludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyIncludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyIncludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">precedence</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyRequireArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyRequireArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyRequireArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyRequireArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Allowing access to `test@example.com` email address only</span>
<span class="n">test_policy_access_policy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicy</span><span class="p">(</span><span class="s2">&quot;testPolicyAccessPolicy&quot;</span><span class="p">,</span>
    <span class="n">application_id</span><span class="o">=</span><span class="s2">&quot;cb029e245cfdd66dc8d2e570d5dd3322&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging policy&quot;</span><span class="p">,</span>
    <span class="n">precedence</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">decision</span><span class="o">=</span><span class="s2">&quot;allow&quot;</span><span class="p">,</span>
    <span class="n">includes</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicyIncludeArgs</span><span class="p">(</span>
        <span class="n">emails</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">)])</span>
<span class="c1"># Allowing `test@example.com` to access but only when coming from a</span>
<span class="c1"># specific IP.</span>
<span class="n">test_policy_index_access_policy_access_policy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicy</span><span class="p">(</span><span class="s2">&quot;testPolicyIndex/accessPolicyAccessPolicy&quot;</span><span class="p">,</span>
    <span class="n">application_id</span><span class="o">=</span><span class="s2">&quot;cb029e245cfdd66dc8d2e570d5dd3322&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging policy&quot;</span><span class="p">,</span>
    <span class="n">precedence</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">decision</span><span class="o">=</span><span class="s2">&quot;allow&quot;</span><span class="p">,</span>
    <span class="n">includes</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicyIncludeArgs</span><span class="p">(</span>
        <span class="n">emails</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">requires</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ips&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;office_ip&quot;</span><span class="p">]],</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Access Policies can be imported using a composite ID formed of zone ID, application ID and policy ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accessPolicy:AccessPolicy staging cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d

where * <span class="sb">``</span>cb029e245cfdd66dc8d2e570d5dd3322<span class="sb">``</span> - Zone ID * <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - Access Application ID * <span class="sb">``</span>67ea780ce4982c1cfbe6b7293afc765d<span class="sb">``</span> - Access Policy ID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyExcludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyIncludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyRequireArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decision</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyExcludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyExcludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyExcludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyIncludeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyIncludeArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyIncludeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">precedence</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AccessPolicyRequireArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyRequireArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AccessPolicyRequireArgs, Mapping[str, Any], Awaitable[Union[AccessPolicyRequireArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_policy.AccessPolicy<a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyExcludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyIncludeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessPolicyRequireArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.application_id">
<em class="property">property </em><code class="sig-name descname">application_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application the policy is associated with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.decision">
<em class="property">property </em><code class="sig-name descname">decision</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.decision" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.excludes">
<em class="property">property </em><code class="sig-name descname">excludes</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.includes">
<em class="property">property </em><code class="sig-name descname">includes</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.precedence">
<em class="property">property </em><code class="sig-name descname">precedence</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique precedence for policies on a single application. Integer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.requires">
<em class="property">property </em><code class="sig-name descname">requires</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions">Access Groups</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="p">:</span> <span class="n">Union[AccessRuleConfigurationArgs, Mapping[str, Any], Awaitable[Union[AccessRuleConfigurationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.</p>
<p>Records can be imported using a composite ID formed of access rule type, access rule type identifier and identifer value, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accessRule:AccessRule default zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e

where<span class="se">\ </span>* <span class="sb">``</span>zone<span class="sb">``</span> - access rule <span class="nb">type</span> <span class="o">(</span><span class="se">\ </span><span class="sb">``</span>account<span class="sb">``</span><span class="se">\ </span>, <span class="sb">``</span>zone<span class="sb">``</span> or <span class="sb">``</span>user<span class="sb">``</span><span class="se">\ </span><span class="o">)</span> * <span class="sb">``</span>cb029e245cfdd66dc8d2e570d5dd3322<span class="sb">``</span> - access rule <span class="nb">type</span> ID <span class="o">(</span>i.e the zone ID

or account ID you wish to target<span class="o">)</span> * <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - access rule ID as returned by

respective API endpoint <span class="k">for</span> the <span class="nb">type</span> you are attempting to import.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessRuleConfigurationArgs'</em><em>]</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="p">:</span> <span class="n">Union[AccessRuleConfigurationArgs, Mapping[str, Any], Awaitable[Union[AccessRuleConfigurationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_rule.AccessRule<a class="headerlink" href="#pulumi_cloudflare.AccessRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AccessRuleConfigurationArgs'</em><em>]</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.configuration">
<em class="property">property </em><code class="sig-name descname">configuration</code><a class="headerlink" href="#pulumi_cloudflare.AccessRule.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule configuration to apply to a matched request. It’s a complex value. See description below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_cloudflare.AccessRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.notes">
<em class="property">property </em><code class="sig-name descname">notes</code><a class="headerlink" href="#pulumi_cloudflare.AccessRule.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>A personal note about the rule. Typically used as a reminder or explanation for the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessServiceToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Service Tokens are used for service-to-service communication
when an application is behind Cloudflare Access.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">my_app</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessServiceToken</span><span class="p">(</span><span class="s2">&quot;myApp&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;CI/CD app&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>~&gt; <strong>Important:</strong> If you are importing an Access Service Token you will not have the <code class="docutils literal notranslate"><span class="pre">client_secret</span></code> available in the state for use. The <code class="docutils literal notranslate"><span class="pre">client_secret</span></code> is only available once, at creation. In most cases, it is better to just create a new resource should you need to reference it in other resources. Access Service Tokens can be imported using a composite ID formed of account ID and Service Token ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accessServiceToken:AccessServiceToken my_app cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e

where * <span class="sb">``</span>cb029e245cfdd66dc8d2e570d5dd3322<span class="sb">``</span> - Account ID * <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - Access Service Token ID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.access_service_token.AccessServiceToken<a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessServiceToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UUID client ID associated with the Service Token.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A secret for interacting with Access protocols.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">zone_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID client ID associated with the Service Token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.client_secret">
<em class="property">property </em><code class="sig-name descname">client_secret</code><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>A secret for interacting with Access protocols.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the token’s intent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the zone where the Access Service is being created. Conflicts with <code class="docutils literal notranslate"><span class="pre">account_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccountMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare account members.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccountMember</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email_address</span><span class="o">=</span><span class="s2">&quot;user@example.com&quot;</span><span class="p">,</span>
    <span class="n">role_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;68b329da9893e34099c7d8ad5cb9c940&quot;</span><span class="p">,</span>
        <span class="s2">&quot;d784fa8b6d98d27699781bd9a7cf19f0&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Account members can be imported using a composite ID formed of account ID and account member ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/accountMember:AccountMember example_user d41d8cd98f00b204e9800998ecf8427e/b58c6f14d292556214bd64909bcdb118

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - account ID as returned by the <span class="sb">`</span>API &lt;https://api.cloudflare.com/#accounts-account-details&gt;<span class="sb">`</span>_ * <span class="sb">``</span>b58c6f14d292556214bd64909bcdb118<span class="sb">``</span> - account member ID as returned by the <span class="sb">`</span>API &lt;https://api.cloudflare.com/#account-members-member-details&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.account_member.AccountMember<a class="headerlink" href="#pulumi_cloudflare.AccountMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.email_address">
<em class="property">property </em><code class="sig-name descname">email_address</code><a class="headerlink" href="#pulumi_cloudflare.AccountMember.email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.role_ids">
<em class="property">property </em><code class="sig-name descname">role_ids</code><a class="headerlink" href="#pulumi_cloudflare.AccountMember.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of account role IDs that you want to assign to a member.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ApiToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ApiToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Union[ApiTokenConditionArgs, Mapping[str, Any], Awaitable[Union[ApiTokenConditionArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApiTokenPolicyArgs, Mapping[str, Any], Awaitable[Union[ApiTokenPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApiTokenPolicyArgs, Mapping[str, Any], Awaitable[Union[ApiTokenPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ApiToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare API tokens.</p>
<p>Read more about permission groups and their applicable scopes in
<a class="reference external" href="https://developers.cloudflare.com/api/tokens/create/permissions">the official documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="nb">all</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_api_token_permission_groups</span><span class="p">()</span>
<span class="c1"># Token allowed to create new tokens.</span>
<span class="c1"># Can only be used from specific ip range.</span>
<span class="n">api_token_create</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;apiTokenCreate&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;api_token_create&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
        <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;API Tokens Write&quot;</span><span class="p">]],</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
            <span class="sa">f</span><span class="s2">&quot;com.cloudflare.api.user.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;user_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)],</span>
    <span class="n">condition</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenConditionArgs</span><span class="p">(</span>
        <span class="n">request_ip</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenConditionRequestIpArgs</span><span class="p">(</span>
            <span class="n">ins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;192.0.2.1/32&quot;</span><span class="p">],</span>
            <span class="n">not_ins</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;198.51.100.1/32&quot;</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="nb">all</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_api_token_permission_groups</span><span class="p">()</span>
<span class="c1"># Token allowed to read audit logs from all accounts.</span>
<span class="n">logs_account_all</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;logsAccountAll&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;logs_account_all&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
        <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;Access: Audit Logs Read&quot;</span><span class="p">]],</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;com.cloudflare.api.account.*&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)])</span>
<span class="c1"># Token allowed to read audit logs from specific account.</span>
<span class="n">logs_account</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;logsAccount&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;logs_account&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
        <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;Access: Audit Logs Read&quot;</span><span class="p">]],</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
            <span class="sa">f</span><span class="s2">&quot;com.cloudflare.api.account.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;account_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="nb">all</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_api_token_permission_groups</span><span class="p">()</span>
<span class="c1"># Token allowed to edit DNS entries and TLS certs for specific zone.</span>
<span class="n">dns_tls_edit</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;dnsTlsEdit&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;dns_tls_edit&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
        <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span>
            <span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;DNS Write&quot;</span><span class="p">],</span>
            <span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;SSL and Certificates Write&quot;</span><span class="p">],</span>
        <span class="p">],</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
            <span class="sa">f</span><span class="s2">&quot;com.cloudflare.api.account.zone.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;zone_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)])</span>
<span class="c1"># Token allowed to edit DNS entries for all zones except one.</span>
<span class="n">dns_tls_edit_all_except_one</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;dnsTlsEditAllExceptOne&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;dns_tls_edit_all_except_one&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
            <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;DNS Write&quot;</span><span class="p">]],</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;com.cloudflare.api.account.zone.*&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
            <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;DNS Write&quot;</span><span class="p">]],</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
                <span class="sa">f</span><span class="s2">&quot;com.cloudflare.api.account.zone.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;zone_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">effect</span><span class="o">=</span><span class="s2">&quot;deny&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="c1"># Token allowed to edit DNS entries for all zones from specific account.</span>
<span class="n">dns_edit_all_account</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiToken</span><span class="p">(</span><span class="s2">&quot;dnsEditAllAccount&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;dns_edit_all_account&quot;</span><span class="p">,</span>
    <span class="n">policies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ApiTokenPolicyArgs</span><span class="p">(</span>
        <span class="n">permission_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">all</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;DNS Write&quot;</span><span class="p">]],</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">{</span>
            <span class="sa">f</span><span class="s2">&quot;com.cloudflare.api.account.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;account_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
                <span class="s2">&quot;com.cloudflare.api.account.zone.*&quot;</span><span class="p">:</span> <span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="p">}),</span>
        <span class="p">},</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiTokenConditionArgs'</em><em>]</em><em>]</em>) – Condition block. See the definition below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the APIToken.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiTokenPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Permissions policy. Multiple policy blocks can be defined.
See the definition below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Union[ApiTokenConditionArgs, Mapping[str, Any], Awaitable[Union[ApiTokenConditionArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issued_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ApiTokenPolicyArgs, Mapping[str, Any], Awaitable[Union[ApiTokenPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ApiTokenPolicyArgs, Mapping[str, Any], Awaitable[Union[ApiTokenPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.api_token.ApiToken<a class="headerlink" href="#pulumi_cloudflare.ApiToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiTokenConditionArgs'</em><em>]</em><em>]</em>) – Condition block. See the definition below.</p></li>
<li><p><strong>issued_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the API Token was issued.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the API Token was last modified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the APIToken.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiTokenPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Permissions policy. Multiple policy blocks can be defined.
See the definition below.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the API Token.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.condition">
<em class="property">property </em><code class="sig-name descname">condition</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>Condition block. See the definition below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.issued_on">
<em class="property">property </em><code class="sig-name descname">issued_on</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.issued_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the API Token was issued.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the API Token was last modified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the APIToken.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Permissions policy. Multiple policy blocks can be defined.
See the definition below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_cloudflare.ApiToken.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the API Token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ApiToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ApiToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ApiToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ApiToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Argo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smart_routing</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tiered_caching</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare Argo controls the routing to your origin and tiered caching options to speed up your website browsing experience.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Argo</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">smart_routing</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">tiered_caching</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Argo settings can be imported the zone ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/argo:Argo example d41d8cd98f00b204e9800998ecf8427e

where <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> is the zone ID.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Argo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smart_routing</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tiered_caching</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.argo.Argo<a class="headerlink" href="#pulumi_cloudflare.Argo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Argo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.smart_routing">
<em class="property">property </em><code class="sig-name descname">smart_routing</code><a class="headerlink" href="#pulumi_cloudflare.Argo.smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.tiered_caching">
<em class="property">property </em><code class="sig-name descname">tiered_caching</code><a class="headerlink" href="#pulumi_cloudflare.Argo.tiered_caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.Argo.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID that you wish to manage Argo on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AuthenticatedOriginPulls</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticated_origin_pulls_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Authenticated Origin Pulls resource. An <code class="docutils literal notranslate"><span class="pre">AuthenticatedOriginPulls</span></code> resource is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.</p>
<p>The arguments that you provide determine which form of Authenticated Origin Pulls to use:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Authenticated Origin Pulls</span>
<span class="n">my_aop</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPulls</span><span class="p">(</span><span class="s2">&quot;myAop&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="c1"># Per-Zone Authenticated Origin Pulls</span>
<span class="n">my_per_zone_aop_cert</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPullsCertificate</span><span class="p">(</span><span class="s2">&quot;myPerZoneAopCert&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">certificate</span><span class="o">=</span><span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
    <span class="n">private_key</span><span class="o">=</span><span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;per-zone&quot;</span><span class="p">)</span>
<span class="n">my_per_zone_aop</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPulls</span><span class="p">(</span><span class="s2">&quot;myPerZoneAop&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">authenticated_origin_pulls_certificate</span><span class="o">=</span><span class="n">my_per_zone_aop_cert</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="c1"># Per-Hostname Authenticated Origin Pulls</span>
<span class="n">my_per_hostname_aop_cert</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPullsCertificate</span><span class="p">(</span><span class="s2">&quot;myPerHostnameAopCert&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">certificate</span><span class="o">=</span><span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
    <span class="n">private_key</span><span class="o">=</span><span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;per-hostname&quot;</span><span class="p">)</span>
<span class="n">my_per_hostname_aop</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPulls</span><span class="p">(</span><span class="s2">&quot;myPerHostnameAop&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">authenticated_origin_pulls_certificate</span><span class="o">=</span><span class="n">my_per_hostname_aop_cert</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;aop.example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p>Authenticated Origin Pull configuration can be imported using a composite ID formed of the zone ID, the form of Authenticated Origin Pulls, and the certificate ID, with each section filled or left blank e.g. # Import Authenticated Origin Pull configuration</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_aop 023e105f4ecef8ad9ca31a8372d0c353//
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_zone_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_hostname_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/aop.example.com
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authenticated_origin_pulls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to upload the certificate to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticated_origin_pulls_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.authenticated_origin_pulls.AuthenticatedOriginPulls<a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthenticatedOriginPulls resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authenticated_origin_pulls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to upload the certificate to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.authenticated_origin_pulls_certificate">
<em class="property">property </em><code class="sig-name descname">authenticated_origin_pulls_certificate</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.authenticated_origin_pulls_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to upload the certificate to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AuthenticatedOriginPulls.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPulls.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AuthenticatedOriginPullsCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Authenticated Origin Pulls certificate resource. An uploaded client certificate is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Per-Zone Authenticated Origin Pulls certificate</span>
<span class="n">my_per_zone_aop_cert</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPullsCertificate</span><span class="p">(</span><span class="s2">&quot;myPerZoneAopCert&quot;</span><span class="p">,</span>
    <span class="n">certificate</span><span class="o">=</span><span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
    <span class="n">private_key</span><span class="o">=</span><span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;per-zone&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">])</span>
<span class="c1"># Per-Hostname Authenticated Origin Pulls certificate</span>
<span class="n">my_per_hostname_aop_cert</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AuthenticatedOriginPullsCertificate</span><span class="p">(</span><span class="s2">&quot;myPerHostnameAopCert&quot;</span><span class="p">,</span>
    <span class="n">certificate</span><span class="o">=</span><span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
    <span class="n">private_key</span><span class="o">=</span><span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;per-hostname&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Authenticated Origin Pull certificates can be imported using a composite ID formed of the zone ID, the form of Authenticated Origin Pulls, and the certificate ID, e.g. # Import Per-Zone Authenticated Origin Pull certificate</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/authenticatedOriginPullsCertificate:AuthenticatedOriginPullsCertificate 2458ce5a-0c35-4c7f-82c7-8e9487d3ff60 023e105f4ecef8ad9ca31a8372d0c353/per-zone/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/authenticatedOriginPullsCertificate:AuthenticatedOriginPullsCertificate 2458ce5a-0c35-4c7f-82c7-8e9487d3ff60 023e105f4ecef8ad9ca31a8372d0c353/per-hostname/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public client certificate.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key of the client certificate.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The form of Authenticated Origin Pulls to upload the certificate to.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to upload the certificate to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial_number</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploaded_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.authenticated_origin_pulls_certificate.AuthenticatedOriginPullsCertificate<a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthenticatedOriginPullsCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public client certificate.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key of the client certificate.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The form of Authenticated Origin Pulls to upload the certificate to.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to upload the certificate to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The public client certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.private_key">
<em class="property">property </em><code class="sig-name descname">private_key</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key of the client certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The form of Authenticated Origin Pulls to upload the certificate to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to upload the certificate to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AuthenticatedOriginPullsCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AuthenticatedOriginPullsCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AwaitableGetApiTokenPermissionGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetApiTokenPermissionGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetApiTokenPermissionGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">china_ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">china_ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetZoneDnssecResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetZoneDnssecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetZoneDnssecResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.ByoIpPrefix">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ByoIpPrefix</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertisement</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the ability to manage Bring-Your-Own-IP prefixes (BYOIP) which are used with or without Magic Transit.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ByoIpPrefix</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">advertisement</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example IP Prefix&quot;</span><span class="p">,</span>
    <span class="n">prefix_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The current settings for Bring-Your-Own-IP prefixes can be imported using the prefix ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/byoIpPrefix:ByoIpPrefix example d41d8cd98f00b204e9800998ecf8427e
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertisement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether or not the prefix shall be announced. A prefix can be activated or deactivated once every 15 minutes (attempting more regular updates will trigger rate limiting). Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the prefix.</p></li>
<li><p><strong>prefix_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The assigned Bring-Your-Own-IP prefix ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.ByoIpPrefix.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertisement</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.byo_ip_prefix.ByoIpPrefix<a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ByoIpPrefix resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertisement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether or not the prefix shall be announced. A prefix can be activated or deactivated once every 15 minutes (attempting more regular updates will trigger rate limiting). Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the prefix.</p></li>
<li><p><strong>prefix_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The assigned Bring-Your-Own-IP prefix ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ByoIpPrefix.advertisement">
<em class="property">property </em><code class="sig-name descname">advertisement</code><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.advertisement" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the prefix shall be announced. A prefix can be activated or deactivated once every 15 minutes (attempting more regular updates will trigger rate limiting). Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ByoIpPrefix.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the prefix.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ByoIpPrefix.prefix_id">
<em class="property">property </em><code class="sig-name descname">prefix_id</code><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.prefix_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The assigned Bring-Your-Own-IP prefix ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ByoIpPrefix.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ByoIpPrefix.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ByoIpPrefix.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CertificatePack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CertificatePack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_authority</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloudflare_branding</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validation_method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validity_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CertificatePack" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate packs can be imported using a composite ID of the zone ID and certificate pack ID. This isn’t recommended and it is advised to replace the certificate entirely instead.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/certificatePack:CertificatePack example cb029e245cfdd66dc8d2e570d5dd3322/8fda82e2-6af9-4eb2-992a-5ab65b792ef1
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_authority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which certificate
authority to issue the certificate pack. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;digicert&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;lets_encrypt&quot;</span></code>.</p></li>
<li><p><strong>cloudflare_branding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include
Cloudflare branding. This will add <code class="docutils literal notranslate"><span class="pre">sni.cloudflaressl.com</span></code> as the Common Name
if set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of hostnames to provision the certificate pack for.
Note: If using Let’s Encrypt, you cannot use individual subdomains and only a
wildcard for subdomain is available.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate pack configuration type.
Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated_custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;advanced&quot;</span></code>.</p></li>
<li><p><strong>validation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which validation method to
use in order to prove domain ownership. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;txt&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>.</p></li>
<li><p><strong>validity_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long the certificate is valid
for. Note: If using Let’s Encrypt, this value can only be 90 days.
Allowed values: 14, 30, 90, 365.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the certificate pack should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_authority</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloudflare_branding</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validation_method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validity_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.certificate_pack.CertificatePack<a class="headerlink" href="#pulumi_cloudflare.CertificatePack.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CertificatePack resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_authority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which certificate
authority to issue the certificate pack. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;digicert&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;lets_encrypt&quot;</span></code>.</p></li>
<li><p><strong>cloudflare_branding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include
Cloudflare branding. This will add <code class="docutils literal notranslate"><span class="pre">sni.cloudflaressl.com</span></code> as the Common Name
if set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of hostnames to provision the certificate pack for.
Note: If using Let’s Encrypt, you cannot use individual subdomains and only a
wildcard for subdomain is available.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate pack configuration type.
Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated_custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;advanced&quot;</span></code>.</p></li>
<li><p><strong>validation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which validation method to
use in order to prove domain ownership. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;txt&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>.</p></li>
<li><p><strong>validity_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long the certificate is valid
for. Note: If using Let’s Encrypt, this value can only be 90 days.
Allowed values: 14, 30, 90, 365.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the certificate pack should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.certificate_authority">
<em class="property">property </em><code class="sig-name descname">certificate_authority</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Which certificate
authority to issue the certificate pack. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;digicert&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;lets_encrypt&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.cloudflare_branding">
<em class="property">property </em><code class="sig-name descname">cloudflare_branding</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.cloudflare_branding" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include
Cloudflare branding. This will add <code class="docutils literal notranslate"><span class="pre">sni.cloudflaressl.com</span></code> as the Common Name
if set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.hosts">
<em class="property">property </em><code class="sig-name descname">hosts</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.hosts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of hostnames to provision the certificate pack for.
Note: If using Let’s Encrypt, you cannot use individual subdomains and only a
wildcard for subdomain is available.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate pack configuration type.
Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dedicated_custom&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;advanced&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.validation_method">
<em class="property">property </em><code class="sig-name descname">validation_method</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.validation_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Which validation method to
use in order to prove domain ownership. Allowed values: <code class="docutils literal notranslate"><span class="pre">&quot;txt&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.validity_days">
<em class="property">property </em><code class="sig-name descname">validity_days</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.validity_days" title="Permalink to this definition">¶</a></dt>
<dd><p>How long the certificate is valid
for. Note: If using Let’s Encrypt, this value can only be 90 days.
Allowed values: 14, 30, 90, 365.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the certificate pack should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CertificatePack.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CertificatePack.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CertificatePack.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomHostname">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomHostname</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_origin_server</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomHostnameSslArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameSslArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomHostnameSslArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameSslArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare custom hostname (also known as SSL for SaaS) resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_hostname</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomHostname</span><span class="p">(</span><span class="s2">&quot;exampleHostname&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;hostname.example.com&quot;</span><span class="p">,</span>
    <span class="n">ssls</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomHostnameSslArgs</span><span class="p">(</span>
        <span class="n">method</span><span class="o">=</span><span class="s2">&quot;txt&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Custom hostname certificates can be imported using a composite ID formed of the zone ID and <a class="reference external" href="https://api.cloudflare.com/#custom-hostname-for-a-zone-properties">hostname ID</a>, separated by a “/” e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/customHostname:CustomHostname example d41d8cd98f00b204e9800998ecf8427e/0d89c70d-ad9f-4843-b99f-6cc0252067e9
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_origin_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The custom origin server used for certificates.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname you intend to request a certificate for.</p></li>
<li><p><strong>ssls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CustomHostnameSslArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – SSL configuration of the certificate. See further notes below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID where the custom hostname should be assigned.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_origin_server</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_verification</span><span class="p">:</span> <span class="n">Union[CustomHostnameOwnershipVerificationArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameOwnershipVerificationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_verification_http</span><span class="p">:</span> <span class="n">Union[CustomHostnameOwnershipVerificationHttpArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameOwnershipVerificationHttpArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomHostnameSslArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameSslArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomHostnameSslArgs, Mapping[str, Any], Awaitable[Union[CustomHostnameSslArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.custom_hostname.CustomHostname<a class="headerlink" href="#pulumi_cloudflare.CustomHostname.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomHostname resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_origin_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The custom origin server used for certificates.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname you intend to request a certificate for.</p></li>
<li><p><strong>ssls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CustomHostnameSslArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – SSL configuration of the certificate. See further notes below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID where the custom hostname should be assigned.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.custom_origin_server">
<em class="property">property </em><code class="sig-name descname">custom_origin_server</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.custom_origin_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The custom origin server used for certificates.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname you intend to request a certificate for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.ssls">
<em class="property">property </em><code class="sig-name descname">ssls</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.ssls" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL configuration of the certificate. See further notes below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID where the custom hostname should be assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostname.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomHostname.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostname.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomHostnameFallbackOrigin</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare custom hostname fallback origin resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">fallback_origin</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomHostnameFallbackOrigin</span><span class="p">(</span><span class="s2">&quot;fallbackOrigin&quot;</span><span class="p">,</span>
    <span class="n">origin</span><span class="o">=</span><span class="s2">&quot;fallback.example.com&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Custom hostname fallback origins can be imported using a composite ID formed of the zone ID and <a class="reference external" href="https://api.cloudflare.com/#custom-hostname-fallback-origin-for-a-zone-properties">fallback origin</a>, separated by a “/” e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/customHostnameFallbackOrigin:CustomHostnameFallbackOrigin example d41d8cd98f00b204e9800998ecf8427e/fallback.example.com
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname you intend to fallback requests to. Origin must be a proxied A/AAAA/CNAME DNS record within Clouldflare.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID where the custom hostname should be assigned.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.custom_hostname_fallback_origin.CustomHostnameFallbackOrigin<a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomHostnameFallbackOrigin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname you intend to fallback requests to. Origin must be a proxied A/AAAA/CNAME DNS record within Clouldflare.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the fallback origin’s activation.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID where the custom hostname should be assigned.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.origin">
<em class="property">property </em><code class="sig-name descname">origin</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname you intend to fallback requests to. Origin must be a proxied A/AAAA/CNAME DNS record within Clouldflare.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the fallback origin’s activation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID where the custom hostname should be assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomHostnameFallbackOrigin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomHostnameFallbackOrigin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomPages</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare custom error pages.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">basic_challenge</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomPages</span><span class="p">(</span><span class="s2">&quot;basicChallenge&quot;</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;customized&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;basic_challenge&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://example.com/challenge.html&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Custom pages can be imported using a composite ID formed of* <code class="docutils literal notranslate"><span class="pre">customPageLevel</span></code> - Either <code class="docutils literal notranslate"><span class="pre">account</span></code> or <code class="docutils literal notranslate"><span class="pre">zone</span></code>. * <code class="docutils literal notranslate"><span class="pre">identifier</span></code> - The ID of the account or zone you intend to manage. * <code class="docutils literal notranslate"><span class="pre">pageType</span></code> - The value from the <code class="docutils literal notranslate"><span class="pre">type</span></code> argument. Example for a zone</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/customPages:CustomPages basic_challenge zone/d41d8cd98f00b204e9800998ecf8427e/basic_challenge

Example <span class="k">for</span> an account
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/customPages:CustomPages basic_challenge account/e268443e43d93dab7ebef303bbe9642f/basic_challenge
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.custom_pages.CustomPages<a class="headerlink" href="#pulumi_cloudflare.CustomPages.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomPages resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.CustomPages.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.CustomPages.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_cloudflare.CustomPages.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of where the custom page source is located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.CustomPages.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomSsl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_options</span><span class="p">:</span> <span class="n">Union[CustomSslCustomSslOptionsArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_priorities</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare custom ssl resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">cloudflare_zone_id</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;cloudflareZoneId&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">cloudflare_zone_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">cloudflare_zone_id</span> <span class="o">=</span> <span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span>
<span class="c1"># Add a custom ssl certificate to the domain</span>
<span class="n">foossl</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomSsl</span><span class="p">(</span><span class="s2">&quot;foossl&quot;</span><span class="p">,</span>
    <span class="n">custom_ssl_options</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomSslCustomSslOptionsArgs</span><span class="p">(</span>
        <span class="n">bundle_method</span><span class="o">=</span><span class="s2">&quot;ubiquitous&quot;</span><span class="p">,</span>
        <span class="n">certificate</span><span class="o">=</span><span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
        <span class="n">geo_restrictions</span><span class="o">=</span><span class="s2">&quot;us&quot;</span><span class="p">,</span>
        <span class="n">private_key</span><span class="o">=</span><span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;legacy_custom&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">cloudflare_zone_id</span><span class="p">)</span>
</pre></div>
</div>
<p>Custom SSL Certs can be imported using a composite ID formed of the zone ID and <a class="reference external" href="https://api.cloudflare.com/#custom-ssl-for-a-zone-properties">certificate ID</a>, separated by a “/” e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/customSsl:CustomSsl default 1d5fdc9e88c8a8c4518b068cd94331fe/0123f0ab-9cde-45b2-80bd-4da3010f1337
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CustomSslCustomSslOptionsArgs'</em><em>]</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_options</span><span class="p">:</span> <span class="n">Union[CustomSslCustomSslOptionsArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_priorities</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any], Awaitable[Union[CustomSslCustomSslPriorityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploaded_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.custom_ssl.CustomSsl<a class="headerlink" href="#pulumi_cloudflare.CustomSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CustomSslCustomSslOptionsArgs'</em><em>]</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.custom_ssl_options">
<em class="property">property </em><code class="sig-name descname">custom_ssl_options</code><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.custom_ssl_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone id to the custom ssl cert should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Filter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Filter expressions that can be referenced across multiple features, e.g. Firewall Rule. The expression format is similar to <a class="reference external" href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark Display Filter</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">wordpress</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Filter</span><span class="p">(</span><span class="s2">&quot;wordpress&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Wordpress break-in attempts that are outside of the office&quot;</span><span class="p">,</span>
    <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;(http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">wp</span><span class="o">-</span><span class="n">login</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot; or http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">xmlrpc</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot;) and ip.src ne 192.0.2.1&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Filter can be imported using a composite ID formed of zone ID and filter ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/filter:Filter default d41d8cd98f00b204e9800998ecf8427e/9e107d9d372bb6826bd81d3542a419d6

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID * <span class="sb">``</span>9e107d9d372bb6826bd81d3542a419d6<span class="sb">``</span> - filter ID as returned by <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-firewall-filters&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Filter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.filter.Filter<a class="headerlink" href="#pulumi_cloudflare.Filter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Filter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.Filter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the purpose of the filter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.expression">
<em class="property">property </em><code class="sig-name descname">expression</code><a class="headerlink" href="#pulumi_cloudflare.Filter.expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter expression to be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_cloudflare.Filter.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter is currently paused. Boolean value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.ref">
<em class="property">property </em><code class="sig-name descname">ref</code><a class="headerlink" href="#pulumi_cloudflare.Filter.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Short reference tag to quickly select related rules.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.Filter.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.</p>
<p>Filter expressions needs to be created first before using Firewall Rule. See Filter.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">wordpress_filter</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Filter</span><span class="p">(</span><span class="s2">&quot;wordpressFilter&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Wordpress break-in attempts that are outside of the office&quot;</span><span class="p">,</span>
    <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;(http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">wp</span><span class="o">-</span><span class="n">login</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot; or http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">xmlrpc</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot;) and ip.src ne 192.0.2.1&quot;</span><span class="p">)</span>
<span class="n">wordpress_firewall_rule</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">FirewallRule</span><span class="p">(</span><span class="s2">&quot;wordpressFirewallRule&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Block wordpress break-in attempts&quot;</span><span class="p">,</span>
    <span class="n">filter_id</span><span class="o">=</span><span class="n">wordpress_filter</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">action</span><span class="o">=</span><span class="s2">&quot;block&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Firewall Rule can be imported using a composite ID formed of zone ID and rule ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/firewallRule:FirewallRule default d41d8cd98f00b204e9800998ecf8427e/9e107d9d372bb6826bd81d3542a419d6

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID * <span class="sb">``</span>9e107d9d372bb6826bd81d3542a419d6<span class="sb">``</span> - rule ID as returned by <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-firewall-filter-rules&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.firewall_rule.FirewallRule<a class="headerlink" href="#pulumi_cloudflare.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.action">
<em class="property">property </em><code class="sig-name descname">action</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule to help identify it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter based firewall rule is currently paused. Boolean value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.products">
<em class="property">property </em><code class="sig-name descname">products</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.products" title="Permalink to this definition">¶</a></dt>
<dd><p>List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.GetApiTokenPermissionGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetApiTokenPermissionGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetApiTokenPermissionGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApiTokenPermissionGroups.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetApiTokenPermissionGroupsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetApiTokenPermissionGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetApiTokenPermissionGroupsResult.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_cloudflare.GetApiTokenPermissionGroupsResult.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of permission groups where keys are human-readable permission names
and values are permission IDs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">china_ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">china_ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.china_ipv4_cidr_blocks">
<em class="property">property </em><code class="sig-name descname">china_ipv4_cidr_blocks</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.china_ipv4_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of only the IPv4 China CIDR blocks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.china_ipv6_cidr_blocks">
<em class="property">property </em><code class="sig-name descname">china_ipv6_cidr_blocks</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.china_ipv6_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of only the IPv6 China CIDR blocks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.cidr_blocks">
<em class="property">property </em><code class="sig-name descname">cidr_blocks</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of all non-China CIDR blocks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.ipv4_cidr_blocks">
<em class="property">property </em><code class="sig-name descname">ipv4_cidr_blocks</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.ipv4_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of only the IPv4 CIDR blocks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetIpRangesResult.ipv6_cidr_blocks">
<em class="property">property </em><code class="sig-name descname">ipv6_cidr_blocks</code><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.ipv6_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of only the IPv6 CIDR blocks.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafGroups.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetWafGroupsResult.groups">
<em class="property">property </em><code class="sig-name descname">groups</code><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of WAF Rule Groups details. Full list below:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetWafGroupsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetWafGroupsResult.package_id">
<em class="property">property </em><code class="sig-name descname">package_id</code><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the WAF Rule Group</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafPackages.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetWafPackagesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetWafPackagesResult.packages">
<em class="property">property </em><code class="sig-name descname">packages</code><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult.packages" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of WAF Rule Packages details. Full list below:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafRules.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetWafRulesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetWafRulesResult.package_id">
<em class="property">property </em><code class="sig-name descname">package_id</code><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the WAF Rule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetWafRulesResult.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of WAF Rules details. Full list below:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetZoneDnssecResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetZoneDnssecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZoneDnssec.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC algorithm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.digest">
<em class="property">property </em><code class="sig-name descname">digest</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.digest" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC digest.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.digest_algorithm">
<em class="property">property </em><code class="sig-name descname">digest_algorithm</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.digest_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Digest algorithm use for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.digest_type">
<em class="property">property </em><code class="sig-name descname">digest_type</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.digest_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Digest Type for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.ds">
<em class="property">property </em><code class="sig-name descname">ds</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.ds" title="Permalink to this definition">¶</a></dt>
<dd><p>DS for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.flags">
<em class="property">property </em><code class="sig-name descname">flags</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.flags" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC flags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.key_tag">
<em class="property">property </em><code class="sig-name descname">key_tag</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.key_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Key Tag for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.key_type">
<em class="property">property </em><code class="sig-name descname">key_type</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Key type used for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Key for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZoneDnssecResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudflare.GetZoneDnssecResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Zone DNSSEC.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.GetZonesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.GetZonesResult.zones">
<em class="property">property </em><code class="sig-name descname">zones</code><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of zone details. Full list below:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.Healthcheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Healthcheck</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consecutive_fails</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consecutive_successes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[HealthcheckHeaderArgs, Mapping[str, Any], Awaitable[Union[HealthcheckHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[HealthcheckHeaderArgs, Mapping[str, Any], Awaitable[Union[HealthcheckHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email_addresses</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_suspended</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Standalone Health Checks provide a way to monitor origin servers without needing a Cloudflare Load Balancer.</p>
<p>The resource supports HTTP, HTTPS and TCP type health checks.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">http_health_check</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Healthcheck</span><span class="p">(</span><span class="s2">&quot;httpHealthCheck&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;http-health-check&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example http health check&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">suspended</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">check_regions</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;WEU&quot;</span><span class="p">,</span>
        <span class="s2">&quot;EEU&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">notification_suspended</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">notification_email_addresses</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;hostmaster@example.com&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;HTTPS&quot;</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/health&quot;</span><span class="p">,</span>
    <span class="n">expected_body</span><span class="o">=</span><span class="s2">&quot;alive&quot;</span><span class="p">,</span>
    <span class="n">expected_codes</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;2xx&quot;</span><span class="p">,</span>
        <span class="s2">&quot;301&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">follow_redirects</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">allow_insecure</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">HealthcheckHeaderArgs</span><span class="p">(</span>
        <span class="n">header</span><span class="o">=</span><span class="s2">&quot;Host&quot;</span><span class="p">,</span>
        <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;example.com&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">consecutive_fails</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">consecutive_successes</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">tcp_health_check</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Healthcheck</span><span class="p">(</span><span class="s2">&quot;tcpHealthCheck&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;tcp-health-check&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example tcp health check&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">suspended</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">check_regions</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;WEU&quot;</span><span class="p">,</span>
        <span class="s2">&quot;EEU&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">notification_suspended</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">notification_email_addresses</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;hostmaster@example.com&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;TCP&quot;</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">22</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;connection_established&quot;</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">consecutive_fails</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">consecutive_successes</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname or IP address of the origin server to run health checks on.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when the health check uses HTTPS. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: <code class="docutils literal notranslate"><span class="pre">WNAM</span></code>, <code class="docutils literal notranslate"><span class="pre">ENAM</span></code>, <code class="docutils literal notranslate"><span class="pre">WEU</span></code>, <code class="docutils literal notranslate"><span class="pre">EEU</span></code>, <code class="docutils literal notranslate"><span class="pre">NSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">SSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">OC</span></code>, <code class="docutils literal notranslate"><span class="pre">ME</span></code>, <code class="docutils literal notranslate"><span class="pre">NAF</span></code>, <code class="docutils literal notranslate"><span class="pre">SAF</span></code>, <code class="docutils literal notranslate"><span class="pre">IN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">NEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL_REGIONS</span></code>.</p></li>
<li><p><strong>consecutive_fails</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p></li>
<li><p><strong>consecutive_successes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive successes required from a health check before changing the health to healthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description of the health check.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check. (Default: <code class="docutils literal notranslate"><span class="pre">[&quot;200&quot;]</span></code>)</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if the origin returns a 3xx status code. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HealthcheckHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: <code class="docutils literal notranslate"><span class="pre">60</span></code>)</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TCP connection method to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code>).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.</p></li>
<li><p><strong>notification_email_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of email addresses we want to send the notifications to.</p></li>
<li><p><strong>notification_suspended</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. (Default: <code class="docutils literal notranslate"><span class="pre">/</span></code>)</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Port number to connect to for the health check.  Valid values are in the rage <code class="docutils literal notranslate"><span class="pre">0-65535</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">80</span></code>).</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>)</p></li>
<li><p><strong>suspended</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If suspended, no health checks are sent to the origin. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. (Default: <code class="docutils literal notranslate"><span class="pre">5</span></code>)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consecutive_fails</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consecutive_successes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[HealthcheckHeaderArgs, Mapping[str, Any], Awaitable[Union[HealthcheckHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[HealthcheckHeaderArgs, Mapping[str, Any], Awaitable[Union[HealthcheckHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email_addresses</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_suspended</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suspended</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.healthcheck.Healthcheck<a class="headerlink" href="#pulumi_cloudflare.Healthcheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Healthcheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname or IP address of the origin server to run health checks on.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when the health check uses HTTPS. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: <code class="docutils literal notranslate"><span class="pre">WNAM</span></code>, <code class="docutils literal notranslate"><span class="pre">ENAM</span></code>, <code class="docutils literal notranslate"><span class="pre">WEU</span></code>, <code class="docutils literal notranslate"><span class="pre">EEU</span></code>, <code class="docutils literal notranslate"><span class="pre">NSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">SSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">OC</span></code>, <code class="docutils literal notranslate"><span class="pre">ME</span></code>, <code class="docutils literal notranslate"><span class="pre">NAF</span></code>, <code class="docutils literal notranslate"><span class="pre">SAF</span></code>, <code class="docutils literal notranslate"><span class="pre">IN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">NEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL_REGIONS</span></code>.</p></li>
<li><p><strong>consecutive_fails</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p></li>
<li><p><strong>consecutive_successes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive successes required from a health check before changing the health to healthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description of the health check.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check. (Default: <code class="docutils literal notranslate"><span class="pre">[&quot;200&quot;]</span></code>)</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if the origin returns a 3xx status code. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HealthcheckHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: <code class="docutils literal notranslate"><span class="pre">60</span></code>)</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TCP connection method to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code>).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.</p></li>
<li><p><strong>notification_email_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of email addresses we want to send the notifications to.</p></li>
<li><p><strong>notification_suspended</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. (Default: <code class="docutils literal notranslate"><span class="pre">/</span></code>)</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Port number to connect to for the health check.  Valid values are in the rage <code class="docutils literal notranslate"><span class="pre">0-65535</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">80</span></code>).</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>)</p></li>
<li><p><strong>suspended</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If suspended, no health checks are sent to the origin. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. (Default: <code class="docutils literal notranslate"><span class="pre">5</span></code>)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.address">
<em class="property">property </em><code class="sig-name descname">address</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname or IP address of the origin server to run health checks on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.allow_insecure">
<em class="property">property </em><code class="sig-name descname">allow_insecure</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.allow_insecure" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not validate the certificate when the health check uses HTTPS. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.check_regions">
<em class="property">property </em><code class="sig-name descname">check_regions</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.check_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: <code class="docutils literal notranslate"><span class="pre">WNAM</span></code>, <code class="docutils literal notranslate"><span class="pre">ENAM</span></code>, <code class="docutils literal notranslate"><span class="pre">WEU</span></code>, <code class="docutils literal notranslate"><span class="pre">EEU</span></code>, <code class="docutils literal notranslate"><span class="pre">NSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">SSAM</span></code>, <code class="docutils literal notranslate"><span class="pre">OC</span></code>, <code class="docutils literal notranslate"><span class="pre">ME</span></code>, <code class="docutils literal notranslate"><span class="pre">NAF</span></code>, <code class="docutils literal notranslate"><span class="pre">SAF</span></code>, <code class="docutils literal notranslate"><span class="pre">IN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">NEAS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL_REGIONS</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.consecutive_fails">
<em class="property">property </em><code class="sig-name descname">consecutive_fails</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.consecutive_fails" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.consecutive_successes">
<em class="property">property </em><code class="sig-name descname">consecutive_successes</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.consecutive_successes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive successes required from a health check before changing the health to healthy. (Default: <code class="docutils literal notranslate"><span class="pre">1</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description of the health check.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.expected_body">
<em class="property">property </em><code class="sig-name descname">expected_body</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.expected_body" title="Permalink to this definition">¶</a></dt>
<dd><p>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.expected_codes">
<em class="property">property </em><code class="sig-name descname">expected_codes</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected HTTP response codes (e.g. “200”) or code ranges (e.g. “2xx” for all codes starting with 2) of the health check. (Default: <code class="docutils literal notranslate"><span class="pre">[&quot;200&quot;]</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.follow_redirects">
<em class="property">property </em><code class="sig-name descname">follow_redirects</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.follow_redirects" title="Permalink to this definition">¶</a></dt>
<dd><p>Follow redirects if the origin returns a 3xx status code. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.headers">
<em class="property">property </em><code class="sig-name descname">headers</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The header name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.interval">
<em class="property">property </em><code class="sig-name descname">interval</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: <code class="docutils literal notranslate"><span class="pre">60</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The TCP connection method to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">connection_established</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.notification_email_addresses">
<em class="property">property </em><code class="sig-name descname">notification_email_addresses</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.notification_email_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of email addresses we want to send the notifications to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.notification_suspended">
<em class="property">property </em><code class="sig-name descname">notification_suspended</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.notification_suspended" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint path to health check against. (Default: <code class="docutils literal notranslate"><span class="pre">/</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port number to connect to for the health check.  Valid values are in the rage <code class="docutils literal notranslate"><span class="pre">0-65535</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">80</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.retries">
<em class="property">property </em><code class="sig-name descname">retries</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.suspended">
<em class="property">property </em><code class="sig-name descname">suspended</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.suspended" title="Permalink to this definition">¶</a></dt>
<dd><p>If suspended, no health checks are sent to the origin. Valid values: <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> (Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.timeout">
<em class="property">property </em><code class="sig-name descname">timeout</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in seconds) before marking the health check as failed. (Default: <code class="docutils literal notranslate"><span class="pre">5</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which apply settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Healthcheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Healthcheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Healthcheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.IpList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">IpList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items</span><span class="p">:</span> <span class="n">Union[Sequence[Union[IpListItemArgs, Mapping[str, Any], Awaitable[Union[IpListItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[IpListItemArgs, Mapping[str, Any], Awaitable[Union[IpListItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.IpList" title="Permalink to this definition">¶</a></dt>
<dd><p>IP Lists are a set of IP addresses or CIDR ranges that are configured on the account level. Once created, IP Lists can be
used in Firewall Rules across all zones within the same account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">IpList</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;list description&quot;</span><span class="p">,</span>
    <span class="n">items</span><span class="o">=</span><span class="p">[</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">IpListItemArgs</span><span class="p">(</span>
            <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;Office IP&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;192.0.2.1&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">IpListItemArgs</span><span class="p">(</span>
            <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;Datacenter range&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;203.0.113.0/24&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;ip&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example_list&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>An existing IP List can be imported using the account ID and list ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/ipList:IpList example d41d8cd98f00b204e9800998ecf8427e/cb029e245cfdd66dc8d2e570d5dd3322
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the account where the IP List is being created.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that can be used to annotate the List. Maximum Length: 500</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of values in the List. Valid values: <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the list (used in filter expressions). Valid pattern: <cite>^[a-zA-Z0-9*]+$</cite>. Maximum Length: 50</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.IpList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items</span><span class="p">:</span> <span class="n">Union[Sequence[Union[IpListItemArgs, Mapping[str, Any], Awaitable[Union[IpListItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[IpListItemArgs, Mapping[str, Any], Awaitable[Union[IpListItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.ip_list.IpList<a class="headerlink" href="#pulumi_cloudflare.IpList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the account where the IP List is being created.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that can be used to annotate the List. Maximum Length: 500</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of values in the List. Valid values: <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the list (used in filter expressions). Valid pattern: <cite>^[a-zA-Z0-9*]+$</cite>. Maximum Length: 50</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.IpList.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_cloudflare.IpList.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account where the IP List is being created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.IpList.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.IpList.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that can be used to annotate the List. Maximum Length: 500</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.IpList.kind">
<em class="property">property </em><code class="sig-name descname">kind</code><a class="headerlink" href="#pulumi_cloudflare.IpList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of values in the List. Valid values: <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.IpList.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.IpList.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the list (used in filter expressions). Valid pattern: <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9_]+$</span></code>. Maximum Length: 50</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.IpList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.IpList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.IpList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.IpList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_pool_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pop_pools</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerPopPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPopPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerPopPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPopPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_pools</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_affinity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steering_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Cloudflare account before you can use this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPool</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-lb-pool&quot;</span><span class="p">,</span>
    <span class="n">origins</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPoolOriginArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-1&quot;</span><span class="p">,</span>
        <span class="n">address</span><span class="o">=</span><span class="s2">&quot;192.0.2.1&quot;</span><span class="p">,</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">)])</span>
<span class="c1"># Define a load balancer which always points to a pool we define below</span>
<span class="c1"># In normal usage, would have different pools set for different pops (cloudflare points-of-presence) and/or for different regions</span>
<span class="c1"># Within each pop or region we can define multiple pools in failover order</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-load-balancer&quot;</span><span class="p">,</span>
    <span class="n">fallback_pool_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">default_pool_ids</span><span class="o">=</span><span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example load balancer using geo-balancing&quot;</span><span class="p">,</span>
    <span class="n">proxied</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">steering_policy</span><span class="o">=</span><span class="s2">&quot;geo&quot;</span><span class="p">,</span>
    <span class="n">pop_pools</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPopPoolArgs</span><span class="p">(</span>
        <span class="n">pop</span><span class="o">=</span><span class="s2">&quot;LAX&quot;</span><span class="p">,</span>
        <span class="n">pool_ids</span><span class="o">=</span><span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">region_pools</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerRegionPoolArgs</span><span class="p">(</span>
        <span class="n">region</span><span class="o">=</span><span class="s2">&quot;WNAM&quot;</span><span class="p">,</span>
        <span class="n">pool_ids</span><span class="o">=</span><span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerPopPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerRegionPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_pool_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pop_pools</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerPopPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPopPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerPopPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPopPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_pools</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerRegionPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_affinity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steering_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.load_balancer.LoadBalancer<a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerPopPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerRegionPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.created_on">
<em class="property">property </em><code class="sig-name descname">created_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.default_pool_ids">
<em class="property">property </em><code class="sig-name descname">default_pool_ids</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.default_pool_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.fallback_pool_id">
<em class="property">property </em><code class="sig-name descname">fallback_pool_id</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.fallback_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool ID to use when all other pools are detected as unhealthy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name (FQDN, including the zone) to associate with the load balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.pop_pools">
<em class="property">property </em><code class="sig-name descname">pop_pools</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.pop_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.proxied">
<em class="property">property </em><code class="sig-name descname">proxied</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.region_pools">
<em class="property">property </em><code class="sig-name descname">region_pools</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.region_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.session_affinity">
<em class="property">property </em><code class="sig-name descname">session_affinity</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.steering_policy">
<em class="property">property </em><code class="sig-name descname">steering_policy</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.steering_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the load balancer to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerMonitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using Cloudflare’s Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S) or TCP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">http_monitor</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerMonitor</span><span class="p">(</span><span class="s2">&quot;httpMonitor&quot;</span><span class="p">,</span>
    <span class="n">allow_insecure</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example http load balancer&quot;</span><span class="p">,</span>
    <span class="n">expected_body</span><span class="o">=</span><span class="s2">&quot;alive&quot;</span><span class="p">,</span>
    <span class="n">expected_codes</span><span class="o">=</span><span class="s2">&quot;2xx&quot;</span><span class="p">,</span>
    <span class="n">follow_redirects</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerMonitorHeaderArgs</span><span class="p">(</span>
        <span class="n">header</span><span class="o">=</span><span class="s2">&quot;Host&quot;</span><span class="p">,</span>
        <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;example.com&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/health&quot;</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">tcp_monitor</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerMonitor</span><span class="p">(</span><span class="s2">&quot;tcpMonitor&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example tcp load balancer&quot;</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;connection_established&quot;</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerMonitorHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerMonitorHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.load_balancer_monitor.LoadBalancerMonitor<a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerMonitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerMonitorHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was last modified.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.allow_insecure">
<em class="property">property </em><code class="sig-name descname">allow_insecure</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.allow_insecure" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.created_on">
<em class="property">property </em><code class="sig-name descname">created_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_body">
<em class="property">property </em><code class="sig-name descname">expected_body</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_body" title="Permalink to this definition">¶</a></dt>
<dd><p>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_codes">
<em class="property">property </em><code class="sig-name descname">expected_codes</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.follow_redirects">
<em class="property">property </em><code class="sig-name descname">follow_redirects</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.follow_redirects" title="Permalink to this definition">¶</a></dt>
<dd><p>Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.headers">
<em class="property">property </em><code class="sig-name descname">headers</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The header name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.interval">
<em class="property">property </em><code class="sig-name descname">interval</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was last modified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.retries">
<em class="property">property </em><code class="sig-name descname">retries</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.timeout">
<em class="property">property </em><code class="sig-name descname">timeout</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in seconds) before marking the health check as failed. Default: 5.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerPool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_origins</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Cloudflare account before you can use this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPool</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example load balancer pool&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">minimum_origins</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-pool&quot;</span><span class="p">,</span>
    <span class="n">notification_email</span><span class="o">=</span><span class="s2">&quot;someone@example.com&quot;</span><span class="p">,</span>
    <span class="n">origins</span><span class="o">=</span><span class="p">[</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPoolOriginArgs</span><span class="p">(</span>
            <span class="n">address</span><span class="o">=</span><span class="s2">&quot;192.0.2.1&quot;</span><span class="p">,</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-1&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPoolOriginArgs</span><span class="p">(</span>
            <span class="n">address</span><span class="o">=</span><span class="s2">&quot;192.0.2.2&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-2&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerPoolOriginArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_origins</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerPoolOriginArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.load_balancer_pool.LoadBalancerPool<a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerPoolOriginArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.check_regions">
<em class="property">property </em><code class="sig-name descname">check_regions</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.check_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.created_on">
<em class="property">property </em><code class="sig-name descname">created_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.minimum_origins">
<em class="property">property </em><code class="sig-name descname">minimum_origins</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.minimum_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.monitor">
<em class="property">property </em><code class="sig-name descname">monitor</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Monitor to use for health checking origins within this pool.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-identifiable name for the origin.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.notification_email">
<em class="property">property </em><code class="sig-name descname">notification_email</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.notification_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.origins">
<em class="property">property </em><code class="sig-name descname">origins</code><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LogPushOwnershipChallenge</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare Logpush ownership challenges to use
in a Logpush Job. On it’s own, doesn’t do much however this resource should
be used in conjunction to create Logpush jobs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LogPushOwnershipChallenge</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">destination_conf</span><span class="o">=</span><span class="s2">&quot;s3://my-bucket-path?region=us-west-2&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush ownership challenge should be created.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_challenge_filename</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.log_push_ownership_challenge.LogPushOwnershipChallenge<a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogPushOwnershipChallenge resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</p></li>
<li><p><strong>ownership_challenge_filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filename of the ownership challenge which
contains the contents required for Logpush Job creation.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush ownership challenge should be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.destination_conf">
<em class="property">property </em><code class="sig-name descname">destination_conf</code><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.destination_conf" title="Permalink to this definition">¶</a></dt>
<dd><p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.ownership_challenge_filename">
<em class="property">property </em><code class="sig-name descname">ownership_challenge_filename</code><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.ownership_challenge_filename" title="Permalink to this definition">¶</a></dt>
<dd><p>The filename of the ownership challenge which
contains the contents required for Logpush Job creation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the logpush ownership challenge should be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogPushOwnershipChallenge.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogPushOwnershipChallenge.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpullRetention">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LogpullRetention</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpullRetention" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of the Logpull Retention settings used to control whether or not to retain HTTP request logs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LogpullRetention</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;fb54f084ca7f7b732d3d3ecbd8ef7bf2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>You can import existing Logpull Retention using the zone ID as the identifier.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/logpullRetention:LogpullRetention example fb54f084ca7f7b732d3d3ecbd8ef7bf2
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether you wish to retain logs or not.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to apply the log retention to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.LogpullRetention.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.logpull_retention.LogpullRetention<a class="headerlink" href="#pulumi_cloudflare.LogpullRetention.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogpullRetention resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether you wish to retain logs or not.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to apply the log retention to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpullRetention.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudflare.LogpullRetention.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether you wish to retain logs or not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpullRetention.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.LogpullRetention.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to apply the log retention to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpullRetention.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpullRetention.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpullRetention.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpullRetention.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LogpushJob</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logpull_options</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_challenge</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LogpushJob resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] dataset: Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.
:param pulumi.Input[str] destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.
:param pulumi.Input[bool] enabled: Whether to enable the job.
:param pulumi.Input[str] logpull_options: Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.
:param pulumi.Input[str] name: The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.
:param pulumi.Input[str] ownership_challenge: Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.
:param pulumi.Input[str] zone_id: The zone ID where the logpush job should be created.</p>
<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logpull_options</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_challenge</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.logpush_job.LogpushJob<a class="headerlink" href="#pulumi_cloudflare.LogpushJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogpushJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable the job.</p></li>
<li><p><strong>logpull_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p></li>
<li><p><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush job should be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.dataset">
<em class="property">property </em><code class="sig-name descname">dataset</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.destination_conf">
<em class="property">property </em><code class="sig-name descname">destination_conf</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.destination_conf" title="Permalink to this definition">¶</a></dt>
<dd><p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable the job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.logpull_options">
<em class="property">property </em><code class="sig-name descname">logpull_options</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.logpull_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.ownership_challenge">
<em class="property">property </em><code class="sig-name descname">ownership_challenge</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.ownership_challenge" title="Permalink to this definition">¶</a></dt>
<dd><p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the logpush job should be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">OriginCaCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_validity</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Origin CA certificate used to protect traffic to your origin without involving a third party Certificate Authority.</p>
<p><strong>This resource requires you use your Origin CA Key as the ``api_user_service_key``, in conjunction with an ``api_token`` or ``email`` and ``api_key``.</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>
<span class="kn">import</span> <span class="nn">pulumi_tls</span> <span class="k">as</span> <span class="nn">tls</span>

<span class="c1"># Create a CSR and generate a CA certificate</span>
<span class="n">example_private_key</span> <span class="o">=</span> <span class="n">tls</span><span class="o">.</span><span class="n">PrivateKey</span><span class="p">(</span><span class="s2">&quot;examplePrivateKey&quot;</span><span class="p">,</span> <span class="n">algorithm</span><span class="o">=</span><span class="s2">&quot;RSA&quot;</span><span class="p">)</span>
<span class="n">example_cert_request</span> <span class="o">=</span> <span class="n">tls</span><span class="o">.</span><span class="n">CertRequest</span><span class="p">(</span><span class="s2">&quot;exampleCertRequest&quot;</span><span class="p">,</span>
    <span class="n">key_algorithm</span><span class="o">=</span><span class="n">example_private_key</span><span class="o">.</span><span class="n">algorithm</span><span class="p">,</span>
    <span class="n">private_key_pem</span><span class="o">=</span><span class="n">example_private_key</span><span class="o">.</span><span class="n">private_key_pem</span><span class="p">,</span>
    <span class="n">subjects</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;commonName&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;organization&quot;</span><span class="p">:</span> <span class="s2">&quot;Terraform Test&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">example_origin_ca_certificate</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">OriginCaCertificate</span><span class="p">(</span><span class="s2">&quot;exampleOriginCaCertificate&quot;</span><span class="p">,</span>
    <span class="n">csr</span><span class="o">=</span><span class="n">example_cert_request</span><span class="o">.</span><span class="n">cert_request_pem</span><span class="p">,</span>
    <span class="n">hostnames</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;example.com&quot;</span><span class="p">],</span>
    <span class="n">request_type</span><span class="o">=</span><span class="s2">&quot;origin-rsa&quot;</span><span class="p">,</span>
    <span class="n">requested_validity</span><span class="o">=</span><span class="mi">7</span><span class="p">)</span>
</pre></div>
</div>
<p>Origin CA certificate resource can be imported using an ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/originCaCertificate:OriginCaCertificate example <span class="m">276266538771611802607153687288146423901027769273</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_validity</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.origin_ca_certificate.OriginCaCertificate<a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OriginCaCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Origin CA certificate</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>expires_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datetime when the certificate will expire.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The Origin CA certificate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.csr">
<em class="property">property </em><code class="sig-name descname">csr</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Signing Request. Must be newline-encoded.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.expires_on">
<em class="property">property </em><code class="sig-name descname">expires_on</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.expires_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The datetime when the certificate will expire.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.hostnames">
<em class="property">property </em><code class="sig-name descname">hostnames</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of hostnames or wildcard names bound to the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.request_type">
<em class="property">property </em><code class="sig-name descname">request_type</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.request_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The signature type desired on the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.requested_validity">
<em class="property">property </em><code class="sig-name descname">requested_validity</code><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.requested_validity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which the certificate should be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">PageRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[PageRuleActionsArgs, Mapping[str, Any], Awaitable[Union[PageRuleActionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare page rule resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Add a page rule to the domain</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">PageRule</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">target</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;sub.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/page&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">PageRuleActionsArgs</span><span class="p">(</span>
        <span class="n">ssl</span><span class="o">=</span><span class="s2">&quot;flexible&quot;</span><span class="p">,</span>
        <span class="n">email_obfuscation</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">minifies</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">PageRuleActionsMinifyArgs</span><span class="p">(</span>
            <span class="n">html</span><span class="o">=</span><span class="s2">&quot;off&quot;</span><span class="p">,</span>
            <span class="n">css</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
            <span class="n">js</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Page rules can be imported using a composite ID formed of zone ID and page rule ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/pageRule:PageRule default d41d8cd98f00b204e9800998ecf8427e/ch8374ftwdghsif43
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PageRuleActionsArgs'</em><em>]</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[PageRuleActionsArgs, Mapping[str, Any], Awaitable[Union[PageRuleActionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.page_rule.PageRule<a class="headerlink" href="#pulumi_cloudflare.PageRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PageRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PageRuleActionsArgs'</em><em>]</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.actions">
<em class="property">property </em><code class="sig-name descname">actions</code><a class="headerlink" href="#pulumi_cloudflare.PageRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The actions taken by the page rule, options given below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_cloudflare.PageRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudflare.PageRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the page rule is active or disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.target">
<em class="property">property </em><code class="sig-name descname">target</code><a class="headerlink" href="#pulumi_cloudflare.PageRule.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL pattern to target with the page rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.PageRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the page rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_client_logging</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_user_service_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_backoff</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_backoff</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rps</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudflare package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configure API client to always use that account.</p></li>
<li><p><strong>api_client_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to print logs from the API client (using the default log library logger)</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key for operations.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API Token for operations.</p></li>
<li><p><strong>api_user_service_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A special Cloudflare API key good for a restricted set of endpoints.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A registered Cloudflare email address.</p></li>
<li><p><strong>max_backoff</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum backoff period in seconds after failed API calls</p></li>
<li><p><strong>min_backoff</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Minimum backoff period in seconds after failed API calls</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of retries to perform when an API request fails</p></li>
<li><p><strong>rps</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – RPS limit to apply when making calls to the API</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">RateLimit</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="p">:</span> <span class="n">Union[RateLimitActionArgs, Mapping[str, Any], Awaitable[Union[RateLimitActionArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_url_patterns</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">correlate</span><span class="p">:</span> <span class="n">Union[RateLimitCorrelateArgs, Mapping[str, Any], Awaitable[Union[RateLimitCorrelateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match</span><span class="p">:</span> <span class="n">Union[RateLimitMatchArgs, Mapping[str, Any], Awaitable[Union[RateLimitMatchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimit</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">threshold</span><span class="o">=</span><span class="mi">2000</span><span class="p">,</span>
    <span class="n">period</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">match</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitMatchArgs</span><span class="p">(</span>
        <span class="n">request</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitMatchRequestArgs</span><span class="p">(</span>
            <span class="n">url_pattern</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/*&quot;</span><span class="p">,</span>
            <span class="n">schemes</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;HTTP&quot;</span><span class="p">,</span>
                <span class="s2">&quot;HTTPS&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">methods</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;GET&quot;</span><span class="p">,</span>
                <span class="s2">&quot;POST&quot;</span><span class="p">,</span>
                <span class="s2">&quot;PUT&quot;</span><span class="p">,</span>
                <span class="s2">&quot;DELETE&quot;</span><span class="p">,</span>
                <span class="s2">&quot;PATCH&quot;</span><span class="p">,</span>
                <span class="s2">&quot;HEAD&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">response</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitMatchResponseArgs</span><span class="p">(</span>
            <span class="n">statuses</span><span class="o">=</span><span class="p">[</span>
                <span class="mi">200</span><span class="p">,</span>
                <span class="mi">201</span><span class="p">,</span>
                <span class="mi">202</span><span class="p">,</span>
                <span class="mi">301</span><span class="p">,</span>
                <span class="mi">429</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">origin_traffic</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">),</span>
    <span class="n">action</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitActionArgs</span><span class="p">(</span>
        <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">43200</span><span class="p">,</span>
        <span class="n">response</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitActionResponseArgs</span><span class="p">(</span>
            <span class="n">content_type</span><span class="o">=</span><span class="s2">&quot;text/plain&quot;</span><span class="p">,</span>
            <span class="n">body</span><span class="o">=</span><span class="s2">&quot;custom response body&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">),</span>
    <span class="n">correlate</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimitCorrelateArgs</span><span class="p">(</span>
        <span class="n">by</span><span class="o">=</span><span class="s2">&quot;nat&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example rate limit for a zone&quot;</span><span class="p">,</span>
    <span class="n">bypass_url_patterns</span><span class="o">=</span><span class="p">[</span>
        <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/bypass1&quot;</span><span class="p">,</span>
        <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/bypass2&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Rate limits can be imported using a composite ID formed of zone name and rate limit ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/rateLimit:RateLimit default d41d8cd98f00b204e9800998ecf8427e/ch8374ftwdghsif43
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitActionArgs'</em><em>]</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitCorrelateArgs'</em><em>]</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitMatchArgs'</em><em>]</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="p">:</span> <span class="n">Union[RateLimitActionArgs, Mapping[str, Any], Awaitable[Union[RateLimitActionArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_url_patterns</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">correlate</span><span class="p">:</span> <span class="n">Union[RateLimitCorrelateArgs, Mapping[str, Any], Awaitable[Union[RateLimitCorrelateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match</span><span class="p">:</span> <span class="n">Union[RateLimitMatchArgs, Mapping[str, Any], Awaitable[Union[RateLimitMatchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.rate_limit.RateLimit<a class="headerlink" href="#pulumi_cloudflare.RateLimit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateLimit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitActionArgs'</em><em>]</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitCorrelateArgs'</em><em>]</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RateLimitMatchArgs'</em><em>]</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.action">
<em class="property">property </em><code class="sig-name descname">action</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.bypass_url_patterns">
<em class="property">property </em><code class="sig-name descname">bypass_url_patterns</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.bypass_url_patterns" title="Permalink to this definition">¶</a></dt>
<dd><p>URLs matching the patterns specified here will be excluded from rate limiting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.correlate">
<em class="property">property </em><code class="sig-name descname">correlate</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.correlate" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.match">
<em class="property">property </em><code class="sig-name descname">match</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.match" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.period">
<em class="property">property </em><code class="sig-name descname">period</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.threshold">
<em class="property">property </em><code class="sig-name descname">threshold</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.RateLimit.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply rate limiting to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[RecordDataArgs, Mapping[str, Any], Awaitable[Union[RecordDataArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare record resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Add a record to the domain</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Record</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;terraform&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;192.168.0.11&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">3600</span><span class="p">)</span>
<span class="c1"># Add a record requiring a data map</span>
<span class="n">_sip_tls</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Record</span><span class="p">(</span><span class="s2">&quot;_sipTls&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;_sip._tls&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;SRV&quot;</span><span class="p">,</span>
    <span class="n">data</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">RecordDataArgs</span><span class="p">(</span>
        <span class="n">service</span><span class="o">=</span><span class="s2">&quot;_sip&quot;</span><span class="p">,</span>
        <span class="n">proto</span><span class="o">=</span><span class="s2">&quot;_tls&quot;</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;terraform-srv&quot;</span><span class="p">,</span>
        <span class="n">priority</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">weight</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">port</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
        <span class="n">target</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Records can be imported using a composite ID formed of zone ID and record ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/record:Record default ae36f999674d196762efcc5abb06b345/d41d8cd98f00b204e9800998ecf8427e

where<span class="se">\ </span>* <span class="sb">``</span>ae36f999674d196762efcc5abb06b345<span class="sb">``</span> - the zone ID * <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - record ID as returned by <span class="sb">`</span>API &lt;https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordDataArgs'</em><em>]</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of the record</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the record to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[RecordDataArgs, Mapping[str, Any], Awaitable[Union[RecordDataArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxiable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.record.Record<a class="headerlink" href="#pulumi_cloudflare.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was created</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordDataArgs'</em><em>]</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the record</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A key-value map of string metadata Cloudflare associates with the record</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was last modified</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of the record</p></li>
<li><p><strong>proxiable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the record to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.created_on">
<em class="property">property </em><code class="sig-name descname">created_on</code><a class="headerlink" href="#pulumi_cloudflare.Record.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.data">
<em class="property">property </em><code class="sig-name descname">data</code><a class="headerlink" href="#pulumi_cloudflare.Record.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_cloudflare.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.metadata">
<em class="property">property </em><code class="sig-name descname">metadata</code><a class="headerlink" href="#pulumi_cloudflare.Record.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of string metadata Cloudflare associates with the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.Record.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was last modified</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_cloudflare.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.proxiable">
<em class="property">property </em><code class="sig-name descname">proxiable</code><a class="headerlink" href="#pulumi_cloudflare.Record.proxiable" title="Permalink to this definition">¶</a></dt>
<dd><p>Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.proxied">
<em class="property">property </em><code class="sig-name descname">proxied</code><a class="headerlink" href="#pulumi_cloudflare.Record.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_cloudflare.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_cloudflare.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the record to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">SpectrumApplication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">argo_smart_routing</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationDnsArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationDnsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ip_connectivity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ips</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_firewall</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_directs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_dns</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationOriginDnsArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationOriginDnsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port_range</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationOriginPortRangeArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationOriginPortRangeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare’s DDoS, TLS, and IP Firewall to your other TCP-based services.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Define a spectrum application proxies ssh traffic</span>
<span class="n">ssh_proxy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">SpectrumApplication</span><span class="p">(</span><span class="s2">&quot;sshProxy&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;tcp/22&quot;</span><span class="p">,</span>
    <span class="n">traffic_type</span><span class="o">=</span><span class="s2">&quot;direct&quot;</span><span class="p">,</span>
    <span class="n">dns</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">SpectrumApplicationDnsArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;CNAME&quot;</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;ssh.example.com&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">origin_directs</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;tcp://109.151.40.129:22&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Spectrum resource can be imported using a zone ID and Application ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/spectrumApplication:SpectrumApplication example d41d8cd98f00b204e9800998ecf8427e/9a7806061c88ada191ed06f989cc3dac

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID, as returned from <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-list-zones&gt;<span class="sb">`</span>_ * <span class="sb">``</span>9a7806061c88ada191ed06f989cc3dac<span class="sb">``</span> - Application ID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>argo_smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – . Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationDnsArgs'</em><em>]</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>edge_ip_connectivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>edge_ips</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationOriginDnsArgs'</em><em>]</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port_range</span></code>, this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>origin_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationOriginPortRangeArgs'</em><em>]</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port</span></code>, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22-23</span></code>. Fields documented below.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">argo_smart_routing</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationDnsArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationDnsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ip_connectivity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ips</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_firewall</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_directs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_dns</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationOriginDnsArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationOriginDnsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port_range</span><span class="p">:</span> <span class="n">Union[SpectrumApplicationOriginPortRangeArgs, Mapping[str, Any], Awaitable[Union[SpectrumApplicationOriginPortRangeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.spectrum_application.SpectrumApplication<a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpectrumApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>argo_smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – . Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationDnsArgs'</em><em>]</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>edge_ip_connectivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>edge_ips</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>. A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p>
</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationOriginDnsArgs'</em><em>]</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port_range</span></code>, this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>origin_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpectrumApplicationOriginPortRangeArgs'</em><em>]</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port</span></code>, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22-23</span></code>. Fields documented below.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.argo_smart_routing">
<em class="property">property </em><code class="sig-name descname">argo_smart_routing</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.argo_smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>. Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.dns">
<em class="property">property </em><code class="sig-name descname">dns</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name and type of DNS record for the Spectrum application. Fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.edge_ip_connectivity">
<em class="property">property </em><code class="sig-name descname">edge_ip_connectivity</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.edge_ip_connectivity" title="Permalink to this definition">¶</a></dt>
<dd><p>. Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.edge_ips">
<em class="property">property </em><code class="sig-name descname">edge_ips</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.edge_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>. A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.ip_firewall">
<em class="property">property </em><code class="sig-name descname">ip_firewall</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.ip_firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_directs">
<em class="property">property </em><code class="sig-name descname">origin_directs</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_directs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_dns">
<em class="property">property </em><code class="sig-name descname">origin_dns</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A destination DNS addresses to the origin. Fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_port">
<em class="property">property </em><code class="sig-name descname">origin_port</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_port" title="Permalink to this definition">¶</a></dt>
<dd><p>If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port_range</span></code>, this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_port_range">
<em class="property">property </em><code class="sig-name descname">origin_port_range</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> and not <code class="docutils literal notranslate"><span class="pre">origin_port</span></code>, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22-23</span></code>. Fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.proxy_protocol">
<em class="property">property </em><code class="sig-name descname">proxy_protocol</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.tls">
<em class="property">property </em><code class="sig-name descname">tls</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.tls" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.traffic_type">
<em class="property">property </em><code class="sig-name descname">traffic_type</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.traffic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the application to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">honey_pot</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafGroup</span><span class="p">(</span><span class="s2">&quot;honeyPot&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;de677e5818985db1285d0e80225f06e5&quot;</span><span class="p">,</span>
    <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>WAF Rule Groups can be imported using a composite ID formed of zone ID and the WAF Rule Group ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/wafGroup:WafGroup honey_pot ae36f999674d196762efcc5abb06b345/de677e5818985db1285d0e80225f06e5
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.waf_group.WafGroup<a class="headerlink" href="#pulumi_cloudflare.WafGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_cloudflare.WafGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule Group ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_cloudflare.WafGroup.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the group, can be one of [“on”, “off”].</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.package_id">
<em class="property">property </em><code class="sig-name descname">package_id</code><a class="headerlink" href="#pulumi_cloudflare.WafGroup.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.WafGroup.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafOverride">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafOverride</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rewrite_action</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF override resource. This enables the ability to toggle
WAF rules and groups on or off based on URIs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">shop_ecxample</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafOverride</span><span class="p">(</span><span class="s2">&quot;shopEcxample&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">urls</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;example.com/no-waf-here&quot;</span><span class="p">,</span>
        <span class="s2">&quot;example.com/another/path/*&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;100015&quot;</span><span class="p">:</span> <span class="s2">&quot;disable&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">groups</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ea8687e59929c1fd05ba97574ad43f77&quot;</span><span class="p">:</span> <span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">rewrite_action</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;default&quot;</span><span class="p">:</span> <span class="s2">&quot;block&quot;</span><span class="p">,</span>
        <span class="s2">&quot;challenge&quot;</span><span class="p">:</span> <span class="s2">&quot;block&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>WAF Overrides can be imported using a composite ID formed of zone ID and override ID.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/wafOverride:WafOverride my_example_waf_override 3abe5b950053dbddf1516d89f9ef1e8a/9d4e66d7649c178663bf62e06dbacb23
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of what the WAF override does.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Similar to <code class="docutils literal notranslate"><span class="pre">rules</span></code>; which WAF groups you want to alter.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this package is currently paused.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Relative priority of this configuration when multiple configurations match a single URL.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>rewrite_action</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – When a WAF rule matches, substitute its configured action for a different action specified by this definition.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of WAF rule ID to rule action you intend to apply.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of URLs to apply the WAF override to.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the WAF override condition should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">override_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rewrite_action</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.waf_override.WafOverride<a class="headerlink" href="#pulumi_cloudflare.WafOverride.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafOverride resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of what the WAF override does.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Similar to <code class="docutils literal notranslate"><span class="pre">rules</span></code>; which WAF groups you want to alter.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this package is currently paused.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Relative priority of this configuration when multiple configurations match a single URL.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>rewrite_action</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – When a WAF rule matches, substitute its configured action for a different action specified by this definition.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of WAF rule ID to rule action you intend to apply.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of URLs to apply the WAF override to.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the WAF override condition should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of what the WAF override does.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.groups">
<em class="property">property </em><code class="sig-name descname">groups</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Similar to <code class="docutils literal notranslate"><span class="pre">rules</span></code>; which WAF groups you want to alter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this package is currently paused.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Relative priority of this configuration when multiple configurations match a single URL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.rewrite_action">
<em class="property">property </em><code class="sig-name descname">rewrite_action</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.rewrite_action" title="Permalink to this definition">¶</a></dt>
<dd><p>When a WAF rule matches, substitute its configured action for a different action specified by this definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of WAF rule ID to rule action you intend to apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.urls">
<em class="property">property </em><code class="sig-name descname">urls</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of URLs to apply the WAF override to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.WafOverride.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the WAF override condition should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafOverride.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafOverride.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafPackage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitivity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule package resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall packages.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">owasp</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafPackage</span><span class="p">(</span><span class="s2">&quot;owasp&quot;</span><span class="p">,</span>
    <span class="n">action_mode</span><span class="o">=</span><span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
    <span class="n">package_id</span><span class="o">=</span><span class="s2">&quot;a25a9a7e9c00afc1fb2e0245519d725b&quot;</span><span class="p">,</span>
    <span class="n">sensitivity</span><span class="o">=</span><span class="s2">&quot;medium&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Packages can be imported using a composite ID formed of zone ID and the WAF Package ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/wafPackage:WafPackage owasp ae36f999674d196762efcc5abb06b345/a25a9a7e9c00afc1fb2e0245519d725b
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitivity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.waf_package.WafPackage<a class="headerlink" href="#pulumi_cloudflare.WafPackage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafPackage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.action_mode">
<em class="property">property </em><code class="sig-name descname">action_mode</code><a class="headerlink" href="#pulumi_cloudflare.WafPackage.action_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.package_id">
<em class="property">property </em><code class="sig-name descname">package_id</code><a class="headerlink" href="#pulumi_cloudflare.WafPackage.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Package ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.sensitivity">
<em class="property">property </em><code class="sig-name descname">sensitivity</code><a class="headerlink" href="#pulumi_cloudflare.WafPackage.sensitivity" title="Permalink to this definition">¶</a></dt>
<dd><p>The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.WafPackage.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">_100000</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafRule</span><span class="p">(</span><span class="s2">&quot;100000&quot;</span><span class="p">,</span>
    <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
    <span class="n">rule_id</span><span class="o">=</span><span class="s2">&quot;100000&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Rules can be imported using a composite ID formed of zone ID and the WAF Rule ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudflare:index/wafRule:WafRule <span class="m">100000</span> ae36f999674d196762efcc5abb06b345/100000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”] or [“on”, “off”] depending on the WAF Rule type.</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.waf_rule.WafRule<a class="headerlink" href="#pulumi_cloudflare.WafRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Group that contains the rule.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”] or [“on”, “off”] depending on the WAF Rule type.</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_cloudflare.WafRule.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Group that contains the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_cloudflare.WafRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”] or [“on”, “off”] depending on the WAF Rule type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.package_id">
<em class="property">property </em><code class="sig-name descname">package_id</code><a class="headerlink" href="#pulumi_cloudflare.WafRule.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.rule_id">
<em class="property">property </em><code class="sig-name descname">rule_id</code><a class="headerlink" href="#pulumi_cloudflare.WafRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.WafRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerRoute</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker route resource. A route will also require a <code class="docutils literal notranslate"><span class="pre">WorkerScript</span></code>. <em>NOTE:</em>  This resource uses the Cloudflare account APIs. This requires setting the <code class="docutils literal notranslate"><span class="pre">CLOUDFLARE_ACCOUNT_ID</span></code> environment variable or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> provider argument.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">my_script</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkerScript</span><span class="p">(</span><span class="s2">&quot;myScript&quot;</span><span class="p">)</span>
<span class="c1"># see &quot;cloudflare_worker_script&quot; documentation ...</span>
<span class="c1"># Runs the specified worker script for all URLs that match `example.com/*`</span>
<span class="n">my_route</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkerRoute</span><span class="p">(</span><span class="s2">&quot;myRoute&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;example.com/*&quot;</span><span class="p">,</span>
    <span class="n">script_name</span><span class="o">=</span><span class="n">my_script</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Records can be imported using a composite ID formed of zone ID and route ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/workerRoute:WorkerRoute default d41d8cd98f00b204e9800998ecf8427e/9a7806061c88ada191ed06f989cc3dac

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID * <span class="sb">``</span>9a7806061c88ada191ed06f989cc3dac<span class="sb">``</span> - route ID as returned by <span class="sb">`</span>API &lt;https://api.cloudflare.com/#worker-filters-list-filters&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p></li>
<li><p><strong>script_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.worker_route.WorkerRoute<a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
</p></li>
<li><p><strong>script_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.pattern">
<em class="property">property </em><code class="sig-name descname">pattern</code><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.script_name">
<em class="property">property </em><code class="sig-name descname">script_name</code><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.script_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the route to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerScript</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kv_namespace_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plain_text_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_text_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webassembly_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker script resource. In order for a script to be active, you’ll also need to setup a <code class="docutils literal notranslate"><span class="pre">WorkerRoute</span></code>. <em>NOTE:</em>  This resource uses the Cloudflare account APIs. This requires setting the <code class="docutils literal notranslate"><span class="pre">CLOUDFLARE_ACCOUNT_ID</span></code> environment variable or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> provider argument.</p>
<p>To import a script, use a script name, e.g. <code class="docutils literal notranslate"><span class="pre">script_name</span></code></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/workerScript:WorkerScript default script_name

where* <span class="sb">``</span>script_name<span class="sb">``</span> - the script name
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The global variable for the binding in your Worker code.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kv_namespace_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptKvNamespaceBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plain_text_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptPlainTextBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_text_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptSecretTextBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webassembly_bindings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any], Awaitable[Union[WorkerScriptWebassemblyBindingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.worker_script.WorkerScript<a class="headerlink" href="#pulumi_cloudflare.WorkerScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The global variable for the binding in your Worker code.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.content">
<em class="property">property </em><code class="sig-name descname">content</code><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The script content.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The global variable for the binding in your Worker code.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKv</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Pair.  <em>NOTE:</em>  This resource uses the Cloudflare account APIs.  This requires setting the <code class="docutils literal notranslate"><span class="pre">CLOUDFLARE_ACCOUNT_ID</span></code> environment variable or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> provider argument.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_ns</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKvNamespace</span><span class="p">(</span><span class="s2">&quot;exampleNs&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s2">&quot;test-namespace&quot;</span><span class="p">)</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKv</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">namespace_id</span><span class="o">=</span><span class="n">example_ns</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;test-key&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;test value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/workersKv:WorkersKv example beaeb6716c9443eaa4deef11763ccca6_test-key

where- <span class="sb">``</span>beaeb6716c9443eaa4deef11763ccca6<span class="sb">``</span> is the ID of the namespace and <span class="sb">``</span>test-key<span class="sb">``</span> is the key
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.workers_kv.WorkersKv<a class="headerlink" href="#pulumi_cloudflare.WorkersKv.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKv resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.namespace_id">
<em class="property">property </em><code class="sig-name descname">namespace_id</code><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Workers KV namespace in which you want to create the KV pair</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The string value to be stored in the key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKvNamespace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Namespace</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKvNamespace</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s2">&quot;test-namespace&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Workers KV Namespace settings can be imported using it’s ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/workersKvNamespace:WorkersKvNamespace example beaeb6716c9443eaa4deef11763ccca6

where- <span class="sb">``</span>beaeb6716c9443eaa4deef11763ccca6<span class="sb">``</span> is the ID of the namespace
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.workers_kv_namespace.WorkersKvNamespace<a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKvNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace you wish to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jump_start</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone resource. Zone is the basic resource for working with Cloudflare and is roughly equivalent to a domain name that the user purchases.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Zone resource can be imported using a zone ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/zone:Zone example d41d8cd98f00b204e9800998ecf8427e

where* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID, as returned from <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-list-zones&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jump_start</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="p">:</span> <span class="n">Union[ZoneMetaArgs, Mapping[str, Any], Awaitable[Union[ZoneMetaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_servers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vanity_name_servers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.zone.Zone<a class="headerlink" href="#pulumi_cloudflare.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>vanity_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of Vanity Nameservers (if set).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `meta.wildcard_proxiable` - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.
* `meta.phishing_detected` - Indicates if URLs on the zone have been identified as hosting phishing content.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>verification_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.jump_start">
<em class="property">property </em><code class="sig-name descname">jump_start</code><a class="headerlink" href="#pulumi_cloudflare.Zone.jump_start" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.name_servers">
<em class="property">property </em><code class="sig-name descname">name_servers</code><a class="headerlink" href="#pulumi_cloudflare.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_cloudflare.Zone.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_cloudflare.Zone.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudflare.Zone.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudflare.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.vanity_name_servers">
<em class="property">property </em><code class="sig-name descname">vanity_name_servers</code><a class="headerlink" href="#pulumi_cloudflare.Zone.vanity_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Vanity Nameservers (if set).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta.wildcard_proxiable</span></code> - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta.phishing_detected</span></code> - Indicates if URLs on the zone have been identified as hosting phishing content.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.verification_key">
<em class="property">property </em><code class="sig-name descname">verification_key</code><a class="headerlink" href="#pulumi_cloudflare.Zone.verification_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.zone">
<em class="property">property </em><code class="sig-name descname">zone</code><a class="headerlink" href="#pulumi_cloudflare.Zone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone name which will be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneDnssec">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneDnssec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone DNSSEC resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_zone</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;exampleZone&quot;</span><span class="p">,</span> <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
<span class="n">example_zone_dnssec</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneDnssec</span><span class="p">(</span><span class="s2">&quot;exampleZoneDnssec&quot;</span><span class="p">,</span> <span class="n">zone_id</span><span class="o">=</span><span class="n">example_zone</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Zone DNSSEC resource can be imported using a zone ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/zoneDnssec:ZoneDnssec example d41d8cd98f00b204e9800998ecf8427e

where* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID, as returned from <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-list-zones&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone DNSSEC updated time.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone id for the zone.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ds</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_tag</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.zone_dnssec.ZoneDnssec<a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneDnssec resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone DNSSEC algorithm.</p></li>
<li><p><strong>digest</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone DNSSEC digest.</p></li>
<li><p><strong>digest_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Digest algorithm use for Zone DNSSEC.</p></li>
<li><p><strong>digest_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Digest Type for Zone DNSSEC.</p></li>
<li><p><strong>ds</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DS for the Zone DNSSEC.</p></li>
<li><p><strong>flags</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Zone DNSSEC flags.</p></li>
<li><p><strong>key_tag</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Key Tag for the Zone DNSSEC.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key type used for Zone DNSSEC.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone DNSSEC updated time.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Public Key for the Zone DNSSEC.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Zone DNSSEC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone id for the zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC algorithm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.digest">
<em class="property">property </em><code class="sig-name descname">digest</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.digest" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC digest.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.digest_algorithm">
<em class="property">property </em><code class="sig-name descname">digest_algorithm</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.digest_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Digest algorithm use for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.digest_type">
<em class="property">property </em><code class="sig-name descname">digest_type</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.digest_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Digest Type for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.ds">
<em class="property">property </em><code class="sig-name descname">ds</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.ds" title="Permalink to this definition">¶</a></dt>
<dd><p>DS for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.flags">
<em class="property">property </em><code class="sig-name descname">flags</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.flags" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC flags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.key_tag">
<em class="property">property </em><code class="sig-name descname">key_tag</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.key_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Key Tag for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.key_type">
<em class="property">property </em><code class="sig-name descname">key_type</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Key type used for Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.modified_on">
<em class="property">property </em><code class="sig-name descname">modified_on</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone DNSSEC updated time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Key for the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Zone DNSSEC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone id for the zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneDnssec.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneDnssec.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneDnssec.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneLockdown</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any], Awaitable[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any], Awaitable[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows you to define one or more URLs (with wildcard matching on the domain or path) that will only permit access if the request originates from an IP address that matches a safelist of one or more IP addresses and/or IP ranges.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Restrict access to these endpoints to requests from a known IP address.</span>
<span class="n">endpoint_lockdown</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneLockdown</span><span class="p">(</span><span class="s2">&quot;endpointLockdown&quot;</span><span class="p">,</span>
    <span class="n">configurations</span><span class="o">=</span><span class="p">[</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneLockdownConfigurationArgs</span><span class="p">(</span>
        <span class="n">target</span><span class="o">=</span><span class="s2">&quot;ip&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;198.51.100.4&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Restrict access to these endpoints to requests from a known IP address&quot;</span><span class="p">,</span>
    <span class="n">paused</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;api.mysite.com/some/endpoint*&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Records can be imported using a composite ID formed of zone name and record ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import cloudflare:index/zoneLockdown:ZoneLockdown cloudflare_zone_lockdown d41d8cd98f00b204e9800998ecf8427e/37cb64fe4a90adb5ca3afc04f2c82a2f

where<span class="se">\ </span>* <span class="sb">``</span>d41d8cd98f00b204e9800998ecf8427e<span class="sb">``</span> - zone ID * <span class="sb">``</span>37cb64fe4a90adb5ca3afc04f2c82a2f<span class="sb">``</span> - zone lockdown ID as returned by <span class="sb">`</span>API &lt;https://api.cloudflare.com/#zone-lockdown-list-lockdown-rules&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneLockdownConfigurationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any], Awaitable[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any], Awaitable[Union[ZoneLockdownConfigurationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.zone_lockdown.ZoneLockdown<a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneLockdown resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneLockdownConfigurationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.configurations">
<em class="property">property </em><code class="sig-name descname">configurations</code><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone lockdown is currently paused. Default: false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.urls">
<em class="property">property </em><code class="sig-name descname">urls</code><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the access rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneSettingsOverride</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[ZoneSettingsOverrideSettingsArgs, Mapping[str, Any], Awaitable[Union[ZoneSettingsOverrideSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which customizes Cloudflare zone settings. Note that after destroying this resource Zone Settings will be reset to their initial values.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneSettingsOverride</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneSettingsOverrideSettingsArgs</span><span class="p">(</span>
        <span class="n">brotli</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">challenge_ttl</span><span class="o">=</span><span class="mi">2700</span><span class="p">,</span>
        <span class="n">security_level</span><span class="o">=</span><span class="s2">&quot;high&quot;</span><span class="p">,</span>
        <span class="n">opportunistic_encryption</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">automatic_https_rewrites</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">mirage</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">waf</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">minify</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneSettingsOverrideSettingsMinifyArgs</span><span class="p">(</span>
            <span class="n">css</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
            <span class="n">js</span><span class="o">=</span><span class="s2">&quot;off&quot;</span><span class="p">,</span>
            <span class="n">html</span><span class="o">=</span><span class="s2">&quot;off&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">security_header</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneSettingsOverrideSettingsSecurityHeaderArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneSettingsOverrideSettingsArgs'</em><em>]</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_settings</span><span class="p">:</span> <span class="n">Union[ZoneSettingsOverrideInitialSettingsArgs, Mapping[str, Any], Awaitable[Union[ZoneSettingsOverrideInitialSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_settings_read_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">readonly_settings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[ZoneSettingsOverrideSettingsArgs, Mapping[str, Any], Awaitable[Union[ZoneSettingsOverrideSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.zone_settings_override.ZoneSettingsOverride<a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneSettingsOverride resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>initial_settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneSettingsOverrideInitialSettingsArgs'</em><em>]</em><em>]</em>) – Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p></li>
<li><p><strong>readonly_settings</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `zone_status`. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.
* `zone_type`. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneSettingsOverrideSettingsArgs'</em><em>]</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.initial_settings">
<em class="property">property </em><code class="sig-name descname">initial_settings</code><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.initial_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.readonly_settings">
<em class="property">property </em><code class="sig-name descname">readonly_settings</code><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.readonly_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">zone_status</span></code>. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_type</span></code>. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.zone_id">
<em class="property">property </em><code class="sig-name descname">zone_id</code><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which apply settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.get_api_token_permission_groups">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_api_token_permission_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_api_token_permission_groups.AwaitableGetApiTokenPermissionGroupsResult<a class="headerlink" href="#pulumi_cloudflare.get_api_token_permission_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://developers.cloudflare.com/api/tokens/create/permissions">API Token Permission Groups</a>. Commonly used as references within <cite>``ApiToken`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/api_token.html">https://www.terraform.io/docs/providers/cloudflare/r/api_token.html</a>&gt;`_ resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_api_token_permission_groups</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;dnsReadPermissionId&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;DNS Read&quot;</span><span class="p">])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_ip_ranges.AwaitableGetIpRangesResult<a class="headerlink" href="#pulumi_cloudflare.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the <a class="reference external" href="https://www.cloudflare.com/ips/">IP ranges</a> of Cloudflare edge nodes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">cloudflare</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_ip_ranges</span><span class="p">()</span>
<span class="n">allow_cloudflare_ingress</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">Firewall</span><span class="p">(</span><span class="s2">&quot;allowCloudflareIngress&quot;</span><span class="p">,</span>
    <span class="n">network</span><span class="o">=</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">source_ranges</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ipv4_cidr_blocks</span><span class="p">,</span>
    <span class="n">allows</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_groups">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[GetWafGroupsFilterArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_waf_groups.AwaitableGetWafGroupsResult<a class="headerlink" href="#pulumi_cloudflare.get_waf_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-groups-properties">WAF Rule Groups</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.InputType</em><em>[</em><em>'GetWafGroupsFilterArgs'</em><em>]</em>) – One or more values used to look up WAF Rule Groups. If more than one value is given all
values must match in order to be included, see below for full list.</p></li>
<li><p><strong>package_id</strong> (<em>str</em>) – The ID of the WAF Rule Package in which to search for the WAF Rule Groups.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The ID of the DNS zone in which to search for the WAF Rule Groups.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_packages">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_packages</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[GetWafPackagesFilterArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_waf_packages.AwaitableGetWafPackagesResult<a class="headerlink" href="#pulumi_cloudflare.get_waf_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-packages-properties">WAF Rule Packages</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.InputType</em><em>[</em><em>'GetWafPackagesFilterArgs'</em><em>]</em>) – One or more values used to look up WAF Rule Packages. If more than one value is given all
values must match in order to be included, see below for full list.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The ID of the DNS zone in which to search for the WAF Rule Packages.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_rules">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[GetWafRulesFilterArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_waf_rules.AwaitableGetWafRulesResult<a class="headerlink" href="#pulumi_cloudflare.get_waf_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-groups-properties">WAF Rules</a>.</p>
<p>The example below matches all WAF Rules that are in the group of ID <code class="docutils literal notranslate"><span class="pre">de677e5818985db1285d0e80225f06e5</span></code>, contain <code class="docutils literal notranslate"><span class="pre">example</span></code> in their description, and are currently <code class="docutils literal notranslate"><span class="pre">on</span></code>. The matched WAF Rules are then returned as output.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_waf_rules</span><span class="p">(</span><span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">,</span>
    <span class="n">package_id</span><span class="o">=</span><span class="s2">&quot;a25a9a7e9c00afc1fb2e0245519d725b&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">GetWafRulesFilterArgs</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">&quot;.*example.*&quot;</span><span class="p">,</span>
        <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;de677e5818985db1285d0e80225f06e5&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;wafRules&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">rules</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.InputType</em><em>[</em><em>'GetWafRulesFilterArgs'</em><em>]</em>) – One or more values used to look up WAF Rules. If more than one value is given all
values must match in order to be included, see below for full list.</p></li>
<li><p><strong>package_id</strong> (<em>str</em>) – The ID of the WAF Rule Package in which to search for the WAF Rules.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The ID of the DNS zone in which to search for the WAF Rules.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_zone_dnssec">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_zone_dnssec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">zone_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_zone_dnssec.AwaitableGetZoneDnssecResult<a class="headerlink" href="#pulumi_cloudflare.get_zone_dnssec" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [Zone][1] DNSSEC settings.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_zone_dnssec</span><span class="p">(</span><span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;&lt;zone_id&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone_id</strong> (<em>str</em>) – The zone id for the zone.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_zones">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[GetZonesFilterArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudflare.get_zones.AwaitableGetZonesResult<a class="headerlink" href="#pulumi_cloudflare.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#zone-properties">Zone</a> records.</p>
<p>Given you have the following zones in Cloudflare.</p>
<ul class="simple">
<li><p>example.com</p></li>
<li><p>example.net</p></li>
<li><p>not-example.com</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">GetZonesFilterArgs</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
<span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">GetZonesFilterArgs</span><span class="p">(</span>
    <span class="n">lookup_type</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
<span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">GetZonesFilterArgs</span><span class="p">(</span>
    <span class="n">lookup_type</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
    <span class="n">match</span><span class="o">=</span><span class="s2">&quot;^not-&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
<span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>filter</strong> (<em>pulumi.InputType</em><em>[</em><em>'GetZonesFilterArgs'</em><em>]</em>) – One or more values used to look up zone records. If more than one value is given all
values must match in order to be included, see below for full list.</p>
</dd>
</dl>
</dd></dl>

</div>
