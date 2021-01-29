---
title: Package pulumi_splunk
title_tag: Package pulumi_splunk | Python SDK
linktitle: pulumi_splunk
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "splunk" >}}

<div class="section" id="pulumi-splunk">
<h1>Pulumi Splunk<a class="headerlink" href="#pulumi-splunk" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-splunk">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-splunk/issues">pulumi/pulumi-splunk repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-splunk/issues">terraform-providers/terraform-provider-splunk repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_splunk"></span><dl class="py class">
<dt id="pulumi_splunk.AdminSamlGroups">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">AdminSamlGroups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups" title="Permalink to this definition"></a></dt>
<dd><p>Manage external groups in an IdP response to internal Splunk roles.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">saml_group</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">AdminSamlGroups</span><span class="p">(</span><span class="s2">&quot;saml-group&quot;</span><span class="p">,</span> <span class="n">roles</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="s2">&quot;power&quot;</span><span class="p">,</span>
<span class="p">])</span>
</pre></div>
</div>
<p>SAML groups can be imported using the id, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import splunk:index/adminSamlGroups:AdminSamlGroups saml-group mygroup
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the external group.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of internal roles assigned to the group.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.AdminSamlGroups.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.AdminSamlGroups" title="pulumi_splunk.AdminSamlGroups">AdminSamlGroups</a><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing AdminSamlGroups resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the external group.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of internal roles assigned to the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AdminSamlGroups.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the external group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AdminSamlGroups.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups.roles" title="Permalink to this definition"></a></dt>
<dd><p>List of internal roles assigned to the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AdminSamlGroups.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AdminSamlGroups.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AdminSamlGroups.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AppsLocal">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">AppsLocal</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AppsLocalAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AppsLocalAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">author</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configured</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">explicit_appname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AppsLocal" title="Permalink to this definition"></a></dt>
<dd><p>Create, install and manage apps on your Splunk instance</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">amazon_connect_app</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">AppsLocal</span><span class="p">(</span><span class="s2">&quot;amazonConnectApp&quot;</span><span class="p">,</span>
    <span class="n">explicit_appname</span><span class="o">=</span><span class="s2">&quot;amazon_connect_app_for_splunk&quot;</span><span class="p">,</span>
    <span class="n">filename</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AppsLocalAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Splunkbase session token for operations like install and update that require login. Use auth or session when installing or updating an app through Splunkbase.</p></li>
<li><p><strong>author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For apps posted to Splunkbase, use your Splunk account username. For internal apps, include your name and contact information.</p></li>
<li><p><strong>configured</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Custom setup complete indication:
<span class="raw-html-m2r"><br></span>true = Custom app setup complete.
<span class="raw-html-m2r"><br></span>false = Custom app setup not complete.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short app description also displayed below the app title in Splunk Web Launcher.</p></li>
<li><p><strong>explicit_appname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom app name. Overrides name when installing an app from a file where filename is set to true. See also filename.</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to use the name value as the app source location.
<span class="raw-html-m2r"><br></span>true indicates that name is a path to a file to install.
<span class="raw-html-m2r"><br></span>false indicates that name is the literal app name and that the app is created from Splunkbase using a template.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App name displayed in Splunk Web, from five to eighty characters excluding the prefix “Splunk for”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal app name or path for the file to install, depending on the value of filename.
<span class="raw-html-m2r"><br></span>filename = false indicates that name is the literal app name and that the app is created from Splunkbase using a template.
<span class="raw-html-m2r"><br></span>filename = true indicates that name is the URL or path to the local .tar, .tgz or .spl file. If name is the Splunkbase URL, set auth or session to authenticate the request.
The app folder name cannot include spaces or special characters.</p></li>
<li><p><strong>session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login session token for installing or updating an app on Splunkbase. Alternatively, use auth.</p></li>
<li><p><strong>update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – File-based update indication:
<span class="raw-html-m2r"><br></span>true specifies that filename should be used to update an existing app. If not specified, update defaults to
<span class="raw-html-m2r"><br></span>false, which indicates that filename should not be used to update an existing app.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App version.</p></li>
<li><p><strong>visible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the app is visible and navigable from Splunk Web.
<span class="raw-html-m2r"><br></span>true = App is visible and navigable.
<span class="raw-html-m2r"><br></span>false = App is not visible or navigable.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AppsLocalAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AppsLocalAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">author</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configured</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">explicit_appname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.AppsLocal" title="pulumi_splunk.AppsLocal">AppsLocal</a><a class="headerlink" href="#pulumi_splunk.AppsLocal.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing AppsLocal resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AppsLocalAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Splunkbase session token for operations like install and update that require login. Use auth or session when installing or updating an app through Splunkbase.</p></li>
<li><p><strong>author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For apps posted to Splunkbase, use your Splunk account username. For internal apps, include your name and contact information.</p></li>
<li><p><strong>configured</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Custom setup complete indication:
<span class="raw-html-m2r"><br></span>true = Custom app setup complete.
<span class="raw-html-m2r"><br></span>false = Custom app setup not complete.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short app description also displayed below the app title in Splunk Web Launcher.</p></li>
<li><p><strong>explicit_appname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom app name. Overrides name when installing an app from a file where filename is set to true. See also filename.</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to use the name value as the app source location.
<span class="raw-html-m2r"><br></span>true indicates that name is a path to a file to install.
<span class="raw-html-m2r"><br></span>false indicates that name is the literal app name and that the app is created from Splunkbase using a template.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App name displayed in Splunk Web, from five to eighty characters excluding the prefix “Splunk for”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal app name or path for the file to install, depending on the value of filename.
<span class="raw-html-m2r"><br></span>filename = false indicates that name is the literal app name and that the app is created from Splunkbase using a template.
<span class="raw-html-m2r"><br></span>filename = true indicates that name is the URL or path to the local .tar, .tgz or .spl file. If name is the Splunkbase URL, set auth or session to authenticate the request.
The app folder name cannot include spaces or special characters.</p></li>
<li><p><strong>session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login session token for installing or updating an app on Splunkbase. Alternatively, use auth.</p></li>
<li><p><strong>update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – File-based update indication:
<span class="raw-html-m2r"><br></span>true specifies that filename should be used to update an existing app. If not specified, update defaults to
<span class="raw-html-m2r"><br></span>false, which indicates that filename should not be used to update an existing app.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App version.</p></li>
<li><p><strong>visible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the app is visible and navigable from Splunk Web.
<span class="raw-html-m2r"><br></span>true = App is visible and navigable.
<span class="raw-html-m2r"><br></span>false = App is not visible or navigable.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.auth">
<em class="property">property </em><code class="sig-name descname">auth</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.auth" title="Permalink to this definition"></a></dt>
<dd><p>Splunkbase session token for operations like install and update that require login. Use auth or session when installing or updating an app through Splunkbase.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.author">
<em class="property">property </em><code class="sig-name descname">author</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.author" title="Permalink to this definition"></a></dt>
<dd><p>For apps posted to Splunkbase, use your Splunk account username. For internal apps, include your name and contact information.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.configured">
<em class="property">property </em><code class="sig-name descname">configured</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.configured" title="Permalink to this definition"></a></dt>
<dd><p>Custom setup complete indication:
<span class="raw-html-m2r"><br></span>true = Custom app setup complete.
<span class="raw-html-m2r"><br></span>false = Custom app setup not complete.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.description" title="Permalink to this definition"></a></dt>
<dd><p>Short app description also displayed below the app title in Splunk Web Launcher.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.explicit_appname">
<em class="property">property </em><code class="sig-name descname">explicit_appname</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.explicit_appname" title="Permalink to this definition"></a></dt>
<dd><p>Custom app name. Overrides name when installing an app from a file where filename is set to true. See also filename.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.filename">
<em class="property">property </em><code class="sig-name descname">filename</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.filename" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to use the name value as the app source location.
<span class="raw-html-m2r"><br></span>true indicates that name is a path to a file to install.
<span class="raw-html-m2r"><br></span>false indicates that name is the literal app name and that the app is created from Splunkbase using a template.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.label" title="Permalink to this definition"></a></dt>
<dd><p>App name displayed in Splunk Web, from five to eighty characters excluding the prefix “Splunk for”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.name" title="Permalink to this definition"></a></dt>
<dd><p>Literal app name or path for the file to install, depending on the value of filename.
<span class="raw-html-m2r"><br></span>filename = false indicates that name is the literal app name and that the app is created from Splunkbase using a template.
<span class="raw-html-m2r"><br></span>filename = true indicates that name is the URL or path to the local .tar, .tgz or .spl file. If name is the Splunkbase URL, set auth or session to authenticate the request.
The app folder name cannot include spaces or special characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.session">
<em class="property">property </em><code class="sig-name descname">session</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.session" title="Permalink to this definition"></a></dt>
<dd><p>Login session token for installing or updating an app on Splunkbase. Alternatively, use auth.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.update">
<em class="property">property </em><code class="sig-name descname">update</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.update" title="Permalink to this definition"></a></dt>
<dd><p>File-based update indication:
<span class="raw-html-m2r"><br></span>true specifies that filename should be used to update an existing app. If not specified, update defaults to
<span class="raw-html-m2r"><br></span>false, which indicates that filename should not be used to update an existing app.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.version" title="Permalink to this definition"></a></dt>
<dd><p>App version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.visible">
<em class="property">property </em><code class="sig-name descname">visible</code><a class="headerlink" href="#pulumi_splunk.AppsLocal.visible" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the app is visible and navigable from Splunk Web.
<span class="raw-html-m2r"><br></span>true = App is visible and navigable.
<span class="raw-html-m2r"><br></span>false = App is not visible or navigable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AppsLocal.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AppsLocal.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AppsLocal.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AppsLocal.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AuthenticationUsers">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">AuthenticationUsers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_change_pass</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart_background_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tz</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers" title="Permalink to this definition"></a></dt>
<dd><p>Create and update user information or delete the user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">user01</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">AuthenticationUsers</span><span class="p">(</span><span class="s2">&quot;user01&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;user01@example.com&quot;</span><span class="p">,</span>
    <span class="n">force_change_pass</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password01&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;terraform-user01-role&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User default app. Overrides the default app inherited from the user roles.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User email address.</p></li>
<li><p><strong>force_change_pass</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Force user to change password indication</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique user login name.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User login password.</p></li>
<li><p><strong>realname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full user name.</p></li>
<li><p><strong>restart_background_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Restart background search job that has not completed when Splunk restarts indication.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Role to assign to this user. At least one existing role is required.</p></li>
<li><p><strong>tz</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User timezone.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_change_pass</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart_background_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tz</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.AuthenticationUsers" title="pulumi_splunk.AuthenticationUsers">AuthenticationUsers</a><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing AuthenticationUsers resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User default app. Overrides the default app inherited from the user roles.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User email address.</p></li>
<li><p><strong>force_change_pass</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Force user to change password indication</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique user login name.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User login password.</p></li>
<li><p><strong>realname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full user name.</p></li>
<li><p><strong>restart_background_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Restart background search job that has not completed when Splunk restarts indication.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Role to assign to this user. At least one existing role is required.</p></li>
<li><p><strong>tz</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User timezone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.default_app">
<em class="property">property </em><code class="sig-name descname">default_app</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.default_app" title="Permalink to this definition"></a></dt>
<dd><p>User default app. Overrides the default app inherited from the user roles.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.email" title="Permalink to this definition"></a></dt>
<dd><p>User email address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.force_change_pass">
<em class="property">property </em><code class="sig-name descname">force_change_pass</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.force_change_pass" title="Permalink to this definition"></a></dt>
<dd><p>Force user to change password indication</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.name" title="Permalink to this definition"></a></dt>
<dd><p>Unique user login name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.password" title="Permalink to this definition"></a></dt>
<dd><p>User login password.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.realname">
<em class="property">property </em><code class="sig-name descname">realname</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.realname" title="Permalink to this definition"></a></dt>
<dd><p>Full user name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.restart_background_jobs">
<em class="property">property </em><code class="sig-name descname">restart_background_jobs</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.restart_background_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Restart background search job that has not completed when Splunk restarts indication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.roles" title="Permalink to this definition"></a></dt>
<dd><p>Role to assign to this user. At least one existing role is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.tz">
<em class="property">property </em><code class="sig-name descname">tz</code><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.tz" title="Permalink to this definition"></a></dt>
<dd><p>User timezone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthenticationUsers.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AuthenticationUsers.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthenticationUsers.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AuthorizationRoles">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">AuthorizationRoles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cumulative_realtime_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cumulative_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">imported_roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realtime_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_disk_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_indexes_alloweds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_indexes_defaults</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_time_win</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles" title="Permalink to this definition"></a></dt>
<dd><p>Create and update role information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">role01</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">AuthorizationRoles</span><span class="p">(</span><span class="s2">&quot;role01&quot;</span><span class="p">,</span>
    <span class="n">capabilities</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;accelerate_datamodel&quot;</span><span class="p">,</span>
        <span class="s2">&quot;change_authentication&quot;</span><span class="p">,</span>
        <span class="s2">&quot;restart_splunkd&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">default_app</span><span class="o">=</span><span class="s2">&quot;search&quot;</span><span class="p">,</span>
    <span class="n">imported_roles</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;power&quot;</span><span class="p">,</span>
        <span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">search_indexes_alloweds</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;_audit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;_internal&quot;</span><span class="p">,</span>
        <span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">search_indexes_defaults</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;_audit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;_internal&quot;</span><span class="p">,</span>
        <span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of capabilities assigned to role.</p></li>
<li><p><strong>cumulative_realtime_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of concurrently running real-time searches that all members of this role can have.</p></li>
<li><p><strong>cumulative_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of concurrently running searches for all role members. Warning message logged when limit is reached.</p></li>
<li><p><strong>default_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the folder name of the default app to use for this role. A user-specific default app overrides this.</p></li>
<li><p><strong>imported_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of imported roles for this role. <span class="raw-html-m2r"><br></span>Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is value with the broadest permissions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user role to create.</p></li>
<li><p><strong>realtime_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify the maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit.</p></li>
<li><p><strong>search_disk_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the maximum disk space in MB that can be used by a user’s search jobs. For example, a value of 100 limits this role to 100 MB total.</p></li>
<li><p><strong>search_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify. In the case that a user has multiple roles with different search filters, they are combined with an OR.</p></li>
<li><p><strong>search_indexes_alloweds</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of indexes that this role has permissions to search. These may be wildcarded, but the index name must begin with an underscore to match internal indexes.</p></li>
<li><p><strong>search_indexes*defaults</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>List of indexes to search when no index is specified. These indexes can be wildcarded, with the exception that ‘*’ does not match internal indexes. To match internal indexes, start with ‘<em>‘. All internal indexes are represented by ‘_</em>’. A user with this role can search other indexes using “index= “</p>
</p></li>
<li><p><strong>search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of concurrent searches a user with this role is allowed to run. For users with multiple roles, the maximum quota value among all of the roles applies.</p></li>
<li><p><strong>search_time_win</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum time span of a search, in seconds. By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to ‘0’, as the ‘admin’ role does.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cumulative_realtime_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cumulative_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">imported_roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realtime_search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_disk_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_indexes_alloweds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_indexes_defaults</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_jobs_quota</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_time_win</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.AuthorizationRoles" title="pulumi_splunk.AuthorizationRoles">AuthorizationRoles</a><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing AuthorizationRoles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of capabilities assigned to role.</p></li>
<li><p><strong>cumulative_realtime_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of concurrently running real-time searches that all members of this role can have.</p></li>
<li><p><strong>cumulative_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of concurrently running searches for all role members. Warning message logged when limit is reached.</p></li>
<li><p><strong>default_app</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the folder name of the default app to use for this role. A user-specific default app overrides this.</p></li>
<li><p><strong>imported_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of imported roles for this role. <span class="raw-html-m2r"><br></span>Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is value with the broadest permissions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user role to create.</p></li>
<li><p><strong>realtime_search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify the maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit.</p></li>
<li><p><strong>search_disk_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the maximum disk space in MB that can be used by a user’s search jobs. For example, a value of 100 limits this role to 100 MB total.</p></li>
<li><p><strong>search_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify. In the case that a user has multiple roles with different search filters, they are combined with an OR.</p></li>
<li><p><strong>search_indexes_alloweds</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of indexes that this role has permissions to search. These may be wildcarded, but the index name must begin with an underscore to match internal indexes.</p></li>
<li><p><strong>search_indexes*defaults</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>List of indexes to search when no index is specified. These indexes can be wildcarded, with the exception that ‘*’ does not match internal indexes. To match internal indexes, start with ‘<em>‘. All internal indexes are represented by ‘_</em>’. A user with this role can search other indexes using “index= “</p>
</p></li>
<li><p><strong>search_jobs_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of concurrent searches a user with this role is allowed to run. For users with multiple roles, the maximum quota value among all of the roles applies.</p></li>
<li><p><strong>search_time_win</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum time span of a search, in seconds. By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to ‘0’, as the ‘admin’ role does.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.capabilities">
<em class="property">property </em><code class="sig-name descname">capabilities</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.capabilities" title="Permalink to this definition"></a></dt>
<dd><p>List of capabilities assigned to role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.cumulative_realtime_search_jobs_quota">
<em class="property">property </em><code class="sig-name descname">cumulative_realtime_search_jobs_quota</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.cumulative_realtime_search_jobs_quota" title="Permalink to this definition"></a></dt>
<dd><p>Maximum number of concurrently running real-time searches that all members of this role can have.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.cumulative_search_jobs_quota">
<em class="property">property </em><code class="sig-name descname">cumulative_search_jobs_quota</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.cumulative_search_jobs_quota" title="Permalink to this definition"></a></dt>
<dd><p>Maximum number of concurrently running searches for all role members. Warning message logged when limit is reached.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.default_app">
<em class="property">property </em><code class="sig-name descname">default_app</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.default_app" title="Permalink to this definition"></a></dt>
<dd><p>Specify the folder name of the default app to use for this role. A user-specific default app overrides this.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.imported_roles">
<em class="property">property </em><code class="sig-name descname">imported_roles</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.imported_roles" title="Permalink to this definition"></a></dt>
<dd><p>List of imported roles for this role. <span class="raw-html-m2r"><br></span>Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is value with the broadest permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the user role to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.realtime_search_jobs_quota">
<em class="property">property </em><code class="sig-name descname">realtime_search_jobs_quota</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.realtime_search_jobs_quota" title="Permalink to this definition"></a></dt>
<dd><p>Specify the maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_disk_quota">
<em class="property">property </em><code class="sig-name descname">search_disk_quota</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_disk_quota" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the maximum disk space in MB that can be used by a user’s search jobs. For example, a value of 100 limits this role to 100 MB total.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_filter">
<em class="property">property </em><code class="sig-name descname">search_filter</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_filter" title="Permalink to this definition"></a></dt>
<dd><p>Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify. In the case that a user has multiple roles with different search filters, they are combined with an OR.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_indexes_alloweds">
<em class="property">property </em><code class="sig-name descname">search_indexes_alloweds</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_indexes_alloweds" title="Permalink to this definition"></a></dt>
<dd><p>List of indexes that this role has permissions to search. These may be wildcarded, but the index name must begin with an underscore to match internal indexes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_indexes_defaults">
<em class="property">property </em><code class="sig-name descname">search_indexes_defaults</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_indexes_defaults" title="Permalink to this definition"></a></dt>
<dd><p>List of indexes to search when no index is specified. These indexes can be wildcarded, with the exception that ‘<em>‘ does not match internal indexes. To match internal indexes, start with ‘*’. All internal indexes are represented by ‘</em><a href="#id5"><span class="problematic" id="id6">*</span></a>‘. A user with this role can search other indexes using “index= “</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_jobs_quota">
<em class="property">property </em><code class="sig-name descname">search_jobs_quota</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_jobs_quota" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of concurrent searches a user with this role is allowed to run. For users with multiple roles, the maximum quota value among all of the roles applies.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.search_time_win">
<em class="property">property </em><code class="sig-name descname">search_time_win</code><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.search_time_win" title="Permalink to this definition"></a></dt>
<dd><p>Maximum time span of a search, in seconds. By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to ‘0’, as the ‘admin’ role does.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.AuthorizationRoles.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.AuthorizationRoles.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.AuthorizationRoles.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.ConfigsConf">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">ConfigsConf</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ConfigsConfAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ConfigsConfAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.ConfigsConf" title="Permalink to this definition"></a></dt>
<dd><p>Create and manage configuration file stanzas.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">new_conf_stanza</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">ConfigsConf</span><span class="p">(</span><span class="s2">&quot;new-conf-stanza&quot;</span><span class="p">,</span> <span class="n">variables</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;disabled&quot;</span><span class="p">:</span> <span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="s2">&quot;custom_key&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
<span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ConfigsConfAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A ‘/’ separated string consisting of {conf_file_name}/{stanza_name} ex. props/custom_stanza</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of key value pairs for a stanza.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.ConfigsConf.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ConfigsConfAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ConfigsConfAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.ConfigsConf" title="pulumi_splunk.ConfigsConf">ConfigsConf</a><a class="headerlink" href="#pulumi_splunk.ConfigsConf.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ConfigsConf resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ConfigsConfAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A ‘/’ separated string consisting of {conf_file_name}/{stanza_name} ex. props/custom_stanza</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of key value pairs for a stanza.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.ConfigsConf.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.ConfigsConf.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.ConfigsConf.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.ConfigsConf.name" title="Permalink to this definition"></a></dt>
<dd><p>A ‘/’ separated string consisting of {conf_file_name}/{stanza_name} ex. props/custom_stanza</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.ConfigsConf.variables">
<em class="property">property </em><code class="sig-name descname">variables</code><a class="headerlink" href="#pulumi_splunk.ConfigsConf.variables" title="Permalink to this definition"></a></dt>
<dd><p>A map of key value pairs for a stanza.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.ConfigsConf.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.ConfigsConf.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.ConfigsConf.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.ConfigsConf.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.DataUiViews">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">DataUiViews</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>DataUiViewsAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DataUiViewsAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eai_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.DataUiViews" title="Permalink to this definition"></a></dt>
<dd><p>Create and manage splunk dashboards/views.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">dashboard</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">DataUiViews</span><span class="p">(</span><span class="s2">&quot;dashboard&quot;</span><span class="p">,</span>
    <span class="n">acl</span><span class="o">=</span><span class="n">splunk</span><span class="o">.</span><span class="n">DataUiViewsAclArgs</span><span class="p">(</span>
        <span class="n">app</span><span class="o">=</span><span class="s2">&quot;search&quot;</span><span class="p">,</span>
        <span class="n">owner</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">eai_data</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  &lt;dashboard&gt;</span>
<span class="s2">    &lt;label&gt; </span>
<span class="s2">      Terraform Test Dashboard</span>
<span class="s2">    &lt;/label&gt;</span>
<span class="s2">  &lt;/dashboard&gt;</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eai_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dashboard XML definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dashboard name.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `eai:data` - (Required) Dashboard XML definition.
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_splunk.DataUiViews.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>DataUiViewsAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DataUiViewsAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eai_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.DataUiViews" title="pulumi_splunk.DataUiViews">DataUiViews</a><a class="headerlink" href="#pulumi_splunk.DataUiViews.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DataUiViews resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eai_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dashboard XML definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dashboard name.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `eai:data` - (Required) Dashboard XML definition.
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.DataUiViews.eai_data">
<em class="property">property </em><code class="sig-name descname">eai_data</code><a class="headerlink" href="#pulumi_splunk.DataUiViews.eai_data" title="Permalink to this definition"></a></dt>
<dd><p>Dashboard XML definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.DataUiViews.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.DataUiViews.name" title="Permalink to this definition"></a></dt>
<dd><p>Dashboard name.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eai:data</span></code> - (Required) Dashboard XML definition.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.DataUiViews.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.DataUiViews.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.DataUiViews.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.DataUiViews.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.GlobalHttpEventCollector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">GlobalHttpEventCollector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dedicated_io_threads</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_sockets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_threads</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_deployment_server</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector" title="Permalink to this definition"></a></dt>
<dd><p>Update Global HTTP Event Collector input configuration.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">http</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">GlobalHttpEventCollector</span><span class="p">(</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">enable_ssl</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">8088</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dedicated_io_threads</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of threads used by HTTP Input server.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Input disabled indicator.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable SSL protocol for HTTP data input. <code class="docutils literal notranslate"><span class="pre">true</span></code> = SSL enabled, <code class="docutils literal notranslate"><span class="pre">false</span></code> = SSL disabled.</p></li>
<li><p><strong>max_sockets</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of simultaneous HTTP connections accepted. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p></li>
<li><p><strong>max_threads</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of threads that can be used by active HTTP transactions. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – HTTP data input IP port.</p></li>
<li><p><strong>use_deployment_server</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Indicates whether the event collector input writes its configuration to a deployment server repository. When this setting is set to 1 (enabled), the input writes its configuration to the directory specified as repositoryLocation in serverclass.conf.
Copy the full contents of the splunk_httpinput app directory to this directory for the configuration to work. When enabled, only the tokens defined in the splunk_httpinput app in this repository are viewable and editable on the API and the Data Inputs page in Splunk Web. When disabled, the input writes its configuration to $SPLUNK_HOME/etc/apps by default. Defaults to 0 (disabled).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dedicated_io_threads</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_sockets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_threads</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_deployment_server</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.GlobalHttpEventCollector" title="pulumi_splunk.GlobalHttpEventCollector">GlobalHttpEventCollector</a><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing GlobalHttpEventCollector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dedicated_io_threads</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of threads used by HTTP Input server.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Input disabled indicator.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable SSL protocol for HTTP data input. <code class="docutils literal notranslate"><span class="pre">true</span></code> = SSL enabled, <code class="docutils literal notranslate"><span class="pre">false</span></code> = SSL disabled.</p></li>
<li><p><strong>max_sockets</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of simultaneous HTTP connections accepted. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p></li>
<li><p><strong>max_threads</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of threads that can be used by active HTTP transactions. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – HTTP data input IP port.</p></li>
<li><p><strong>use_deployment_server</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Indicates whether the event collector input writes its configuration to a deployment server repository. When this setting is set to 1 (enabled), the input writes its configuration to the directory specified as repositoryLocation in serverclass.conf.
Copy the full contents of the splunk_httpinput app directory to this directory for the configuration to work. When enabled, only the tokens defined in the splunk_httpinput app in this repository are viewable and editable on the API and the Data Inputs page in Splunk Web. When disabled, the input writes its configuration to $SPLUNK_HOME/etc/apps by default. Defaults to 0 (disabled).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.dedicated_io_threads">
<em class="property">property </em><code class="sig-name descname">dedicated_io_threads</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.dedicated_io_threads" title="Permalink to this definition"></a></dt>
<dd><p>Number of threads used by HTTP Input server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Input disabled indicator.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.enable_ssl">
<em class="property">property </em><code class="sig-name descname">enable_ssl</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.enable_ssl" title="Permalink to this definition"></a></dt>
<dd><p>Enable SSL protocol for HTTP data input. <code class="docutils literal notranslate"><span class="pre">true</span></code> = SSL enabled, <code class="docutils literal notranslate"><span class="pre">false</span></code> = SSL disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.max_sockets">
<em class="property">property </em><code class="sig-name descname">max_sockets</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.max_sockets" title="Permalink to this definition"></a></dt>
<dd><p>Maximum number of simultaneous HTTP connections accepted. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.max_threads">
<em class="property">property </em><code class="sig-name descname">max_threads</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.max_threads" title="Permalink to this definition"></a></dt>
<dd><p>Maximum number of threads that can be used by active HTTP transactions. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.port" title="Permalink to this definition"></a></dt>
<dd><p>HTTP data input IP port.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.use_deployment_server">
<em class="property">property </em><code class="sig-name descname">use_deployment_server</code><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.use_deployment_server" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the event collector input writes its configuration to a deployment server repository. When this setting is set to 1 (enabled), the input writes its configuration to the directory specified as repositoryLocation in serverclass.conf.
Copy the full contents of the splunk_httpinput app directory to this directory for the configuration to work. When enabled, only the tokens defined in the splunk_httpinput app in this repository are viewable and editable on the API and the Data Inputs page in Splunk Web. When disabled, the input writes its configuration to $SPLUNK_HOME/etc/apps by default. Defaults to 0 (disabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.GlobalHttpEventCollector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.GlobalHttpEventCollector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.GlobalHttpEventCollector.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.Indexes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">Indexes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>IndexesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IndexesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_sign_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_rebuild_memory_hint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_to_frozen_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_to_frozen_script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress_rawdata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datatype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_online_bucket_repair</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frozen_time_period_in_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bloom_backfill_bucket_age</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrent_optimizes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_data_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_idle_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_span_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_mem_mb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_meta_entries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_time_unreplicated_no_acks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_time_unreplicated_with_acks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_total_data_size_mb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_warm_db_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_raw_file_sync_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_stream_group_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partial_service_meta_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_tracker_service_interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quarantine_future_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quarantine_past_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">raw_chunk_size_bytes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rep_factor</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rotate_period_in_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_meta_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_meta</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thawed_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttle_check_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tstats_home_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warm_to_cold_script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Indexes" title="Permalink to this definition"></a></dt>
<dd><p>Create and manage data indexes.</p>
<p>By default, all users can list all indexes. However, if the indexes_list_all capability is enabled in authorize.conf, access to all indexes is limited to only those roles with this capability.
To enable indexes_list_all capability restrictions on the data/indexes endpoint, create a [capability::indexes_list_all] stanza in authorize.conf. Specify indexes_list_all=enabled for any role permitted to list all indexes from this endpoint.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">user01_index</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">Indexes</span><span class="p">(</span><span class="s2">&quot;user01-index&quot;</span><span class="p">,</span>
    <span class="n">max_hot_buckets</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span>
    <span class="n">max_total_data_size_mb</span><span class="o">=</span><span class="mi">1000000</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'IndexesAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>block_sign_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. <span class="raw-html-m2r"><br></span>A recommended value is 100.</p></li>
<li><p><strong>bucket_rebuild_memory_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make.
<span class="raw-html-m2r"><be></span>Caution: This is an advanced parameter. Inappropriate use of this parameter causes splunkd to not start if rebuild is required. Do not set this parameter unless instructed by Splunk Support.
Default value, auto, varies by the amount of physical RAM on the host<span class="raw-html-m2r"><br></span>
less than 2GB RAM = 67108864 (64MB) tsidx
2GB to 8GB RAM = 134217728 (128MB) tsidx
more than 8GB RAM = 268435456 (256MB) tsidx<span class="raw-html-m2r"><br></span>
Values other than “auto” must be 16MB-1GB. Highest legal value (of the numerical part) is 4294967295 You can specify the value using a size suffix: “16777216” or “16MB” are equivalent.</p></li>
<li><p><strong>cold_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the colddbs for the index. The path must be readable and writable. Cold databases are opened as needed when searching.</p></li>
<li><p><strong>cold_to_frozen_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination path for the frozen archive. Use as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory.
<span class="raw-html-m2r"><br></span>
Bucket freezing policy is as follows:<span class="raw-html-m2r"><br></span>
New style buckets (4.2 and on): removes all files but the rawdata<span class="raw-html-m2r"><br></span>
To thaw, run splunk rebuild <span class="raw-html-m2r"><bucket dir></span> on the bucket, then move to the thawed directory<span class="raw-html-m2r"><br></span>
Old style buckets (Pre-4.2): gzip all the .data and .tsidx files<span class="raw-html-m2r"><br></span>
To thaw, gunzip the zipped files and move the bucket into the thawed directory<span class="raw-html-m2r"><br></span>
If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence</p></li>
<li><p><strong>cold_to_frozen_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the archiving script.
<span class="raw-html-m2r"><br></span>If your script requires a program to run it (for example, python), specify the program followed by the path. The script must be in $SPLUNK_HOME/bin or one of its subdirectories.
<span class="raw-html-m2r"><br></span>Splunk software ships with an example archiving script in $SPLUNK_HOME/bin called coldToFrozenExample.py. DO NOT use this example script directly. It uses a default path, and if modified in place any changes are overwritten on upgrade.
<span class="raw-html-m2r"><br></span>It is best to copy the example script to a new file in bin and modify it for your system. Most importantly, change the default archive path to an existing directory that fits your needs.</p></li>
<li><p><strong>compress_rawdata</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is ignored. The splunkd process always compresses raw data.</p></li>
<li><p><strong>datatype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (event | metric). Specifies the type of index.</p></li>
<li><p><strong>enable_online_bucket_repair</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables asynchronous “online fsck” bucket repair, which runs concurrently with Splunk software.
When enabled, you do not have to wait until buckets are repaired to start the Splunk platform. However, you might observe a slight performance degratation.</p></li>
<li><p><strong>frozen_time_period_in_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of seconds after which indexed data rolls to frozen.
Defaults to 188697600 (6 years).Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.</p></li>
<li><p><strong>home_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the hot and warm buckets for the index.
Required. Splunk software does not start if an index lacks a valid homePath.
<span class="raw-html-m2r"><br></span>Caution: The path must be readable and writable.</p></li>
<li><p><strong>max_bloom_backfill_bucket_age</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are: Integer[m|s|h|d].
<span class="raw-html-m2r"><br></span>If a warm or cold bucket is older than the specified age, do not create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters.</p></li>
<li><p><strong>max_concurrent_optimizes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of concurrent optimize processes that can run against a hot bucket.
This number should be increased if instructed by Splunk Support. Typically the default value should suffice.</p></li>
<li><p><strong>max_data_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying “auto” or “auto_high_volume” causes Splunk software to autotune this parameter (recommended).
Use “auto_high_volume” for high volume indexes (such as the main index); otherwise, use “auto”. A “high volume index” would typically be considered one that gets over 10GB of data per day.</p></li>
<li><p><strong>max_hot_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum hot buckets that can exist per index. Defaults to 3.
<span class="raw-html-m2r"><br></span>When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll.</p></li>
<li><p><strong>max_hot_idle_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum life, in seconds, of a hot bucket. Defaults to 0. If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. A value of 0 turns off the idle check (equivalent to INFINITE idle time).</p></li>
<li><p><strong>max_hot_span_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days).</p></li>
<li><p><strong>max_mem_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of memory, expressed in MB, to allocate for buffering a single tsidx file into memory before flushing to disk. Defaults to 5. The default is recommended for all environments.</p></li>
<li><p><strong>max_meta_entries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0.</p></li>
<li><p><strong>max_time_unreplicated_no_acks</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored.
If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies.
Highest legal value is 2147483647. To disable this parameter, set to 0.</p></li>
<li><p><strong>max_time_unreplicated_with_acks</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering).
Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza.
To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647.</p></li>
<li><p><strong>max_total_data_size_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.</p></li>
<li><p><strong>max_warm_db_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times is moved to cold.</p></li>
<li><p><strong>min_raw_file_sync_secs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer (or “disable”) for this parameter.
This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices.
During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files.
If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying “disable” disables syncing entirely: uncompressed slices are removed as soon as compression is complete.</p></li>
<li><p><strong>min_stream_group_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Minimum size of the queue that stores events in memory before committing them to a tsidx file.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index to create.</p></li>
<li><p><strong>partial_service_meta_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Related to serviceMetaPeriod. If set, it enables metadata sync every <span class="raw-html-m2r"><integer></span> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync’ed at serviceMetaPeriod.
partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens.
If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect.
By default it is turned off (zero).</p></li>
<li><p><strong>process_tracker_service_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. Defaults to 15.
If set to 0, the indexer checks child process status every second.
Highest legal value is 4294967295.</p></li>
<li><p><strong>quarantine_future_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Events with timestamp of quarantineFutureSecs newer than “now” are dropped into quarantine bucket. Defaults to 2592000 (30 days).
This is a mechanism to prevent main hot buckets from being polluted with fringe events.</p></li>
<li><p><strong>quarantine_past_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Events with timestamp of quarantinePastSecs older than “now” are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events.</p></li>
<li><p><strong>raw_chunk_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value.</p></li>
<li><p><strong>rep_factor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index replication control. This parameter applies to only clustering slaves.
auto = Use the master index replication configuration value.
0 = Turn off replication for this index.</p></li>
<li><p><strong>rotate_period_in_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.</p></li>
<li><p><strong>service_meta_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds).
You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path.</p></li>
<li><p><strong>sync_meta</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures.</p></li>
<li><p><strong>thawed_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the thawed (resurrected) databases for the index.
Cannot be defined in terms of a volume definition.
Required. Splunk software does not start if an index lacks a valid thawedPath.</p></li>
<li><p><strong>throttle_check_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds).</p></li>
<li><p><strong>tstats_home_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location to store datamodel acceleration TSIDX data for this index. Restart splunkd after changing this parameter.
If specified, it must be defined in terms of a volume definition.</p></li>
<li><p><strong>warm_to_cold_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a script to run when moving data from warm to cold.
This attribute is supported for backwards compatibility with Splunk software versions older than 4.0. Contact Splunk support if you need help configuring this setting.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.Indexes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>IndexesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IndexesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_sign_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_rebuild_memory_hint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_to_frozen_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_to_frozen_script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress_rawdata</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datatype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_online_bucket_repair</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frozen_time_period_in_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bloom_backfill_bucket_age</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrent_optimizes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_data_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_idle_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_hot_span_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_mem_mb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_meta_entries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_time_unreplicated_no_acks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_time_unreplicated_with_acks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_total_data_size_mb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_warm_db_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_raw_file_sync_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_stream_group_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partial_service_meta_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_tracker_service_interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quarantine_future_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quarantine_past_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">raw_chunk_size_bytes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rep_factor</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rotate_period_in_secs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_meta_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_meta</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thawed_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttle_check_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tstats_home_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warm_to_cold_script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.Indexes" title="pulumi_splunk.Indexes">Indexes</a><a class="headerlink" href="#pulumi_splunk.Indexes.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Indexes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'IndexesAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>block_sign_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. <span class="raw-html-m2r"><br></span>A recommended value is 100.</p></li>
<li><p><strong>bucket_rebuild_memory_hint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make.
<span class="raw-html-m2r"><be></span>Caution: This is an advanced parameter. Inappropriate use of this parameter causes splunkd to not start if rebuild is required. Do not set this parameter unless instructed by Splunk Support.
Default value, auto, varies by the amount of physical RAM on the host<span class="raw-html-m2r"><br></span>
less than 2GB RAM = 67108864 (64MB) tsidx
2GB to 8GB RAM = 134217728 (128MB) tsidx
more than 8GB RAM = 268435456 (256MB) tsidx<span class="raw-html-m2r"><br></span>
Values other than “auto” must be 16MB-1GB. Highest legal value (of the numerical part) is 4294967295 You can specify the value using a size suffix: “16777216” or “16MB” are equivalent.</p></li>
<li><p><strong>cold_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the colddbs for the index. The path must be readable and writable. Cold databases are opened as needed when searching.</p></li>
<li><p><strong>cold_to_frozen_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination path for the frozen archive. Use as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory.
<span class="raw-html-m2r"><br></span>
Bucket freezing policy is as follows:<span class="raw-html-m2r"><br></span>
New style buckets (4.2 and on): removes all files but the rawdata<span class="raw-html-m2r"><br></span>
To thaw, run splunk rebuild <span class="raw-html-m2r"><bucket dir></span> on the bucket, then move to the thawed directory<span class="raw-html-m2r"><br></span>
Old style buckets (Pre-4.2): gzip all the .data and .tsidx files<span class="raw-html-m2r"><br></span>
To thaw, gunzip the zipped files and move the bucket into the thawed directory<span class="raw-html-m2r"><br></span>
If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence</p></li>
<li><p><strong>cold_to_frozen_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the archiving script.
<span class="raw-html-m2r"><br></span>If your script requires a program to run it (for example, python), specify the program followed by the path. The script must be in $SPLUNK_HOME/bin or one of its subdirectories.
<span class="raw-html-m2r"><br></span>Splunk software ships with an example archiving script in $SPLUNK_HOME/bin called coldToFrozenExample.py. DO NOT use this example script directly. It uses a default path, and if modified in place any changes are overwritten on upgrade.
<span class="raw-html-m2r"><br></span>It is best to copy the example script to a new file in bin and modify it for your system. Most importantly, change the default archive path to an existing directory that fits your needs.</p></li>
<li><p><strong>compress_rawdata</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is ignored. The splunkd process always compresses raw data.</p></li>
<li><p><strong>datatype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (event | metric). Specifies the type of index.</p></li>
<li><p><strong>enable_online_bucket_repair</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables asynchronous “online fsck” bucket repair, which runs concurrently with Splunk software.
When enabled, you do not have to wait until buckets are repaired to start the Splunk platform. However, you might observe a slight performance degratation.</p></li>
<li><p><strong>frozen_time_period_in_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of seconds after which indexed data rolls to frozen.
Defaults to 188697600 (6 years).Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.</p></li>
<li><p><strong>home_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the hot and warm buckets for the index.
Required. Splunk software does not start if an index lacks a valid homePath.
<span class="raw-html-m2r"><br></span>Caution: The path must be readable and writable.</p></li>
<li><p><strong>max_bloom_backfill_bucket_age</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are: Integer[m|s|h|d].
<span class="raw-html-m2r"><br></span>If a warm or cold bucket is older than the specified age, do not create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters.</p></li>
<li><p><strong>max_concurrent_optimizes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of concurrent optimize processes that can run against a hot bucket.
This number should be increased if instructed by Splunk Support. Typically the default value should suffice.</p></li>
<li><p><strong>max_data_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying “auto” or “auto_high_volume” causes Splunk software to autotune this parameter (recommended).
Use “auto_high_volume” for high volume indexes (such as the main index); otherwise, use “auto”. A “high volume index” would typically be considered one that gets over 10GB of data per day.</p></li>
<li><p><strong>max_hot_buckets</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum hot buckets that can exist per index. Defaults to 3.
<span class="raw-html-m2r"><br></span>When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll.</p></li>
<li><p><strong>max_hot_idle_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum life, in seconds, of a hot bucket. Defaults to 0. If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. A value of 0 turns off the idle check (equivalent to INFINITE idle time).</p></li>
<li><p><strong>max_hot_span_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days).</p></li>
<li><p><strong>max_mem_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of memory, expressed in MB, to allocate for buffering a single tsidx file into memory before flushing to disk. Defaults to 5. The default is recommended for all environments.</p></li>
<li><p><strong>max_meta_entries</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0.</p></li>
<li><p><strong>max_time_unreplicated_no_acks</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored.
If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies.
Highest legal value is 2147483647. To disable this parameter, set to 0.</p></li>
<li><p><strong>max_time_unreplicated_with_acks</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering).
Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza.
To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647.</p></li>
<li><p><strong>max_total_data_size_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.</p></li>
<li><p><strong>max_warm_db_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times is moved to cold.</p></li>
<li><p><strong>min_raw_file_sync_secs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer (or “disable”) for this parameter.
This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices.
During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files.
If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying “disable” disables syncing entirely: uncompressed slices are removed as soon as compression is complete.</p></li>
<li><p><strong>min_stream_group_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Minimum size of the queue that stores events in memory before committing them to a tsidx file.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index to create.</p></li>
<li><p><strong>partial_service_meta_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Related to serviceMetaPeriod. If set, it enables metadata sync every <span class="raw-html-m2r"><integer></span> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync’ed at serviceMetaPeriod.
partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens.
If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect.
By default it is turned off (zero).</p></li>
<li><p><strong>process_tracker_service_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. Defaults to 15.
If set to 0, the indexer checks child process status every second.
Highest legal value is 4294967295.</p></li>
<li><p><strong>quarantine_future_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Events with timestamp of quarantineFutureSecs newer than “now” are dropped into quarantine bucket. Defaults to 2592000 (30 days).
This is a mechanism to prevent main hot buckets from being polluted with fringe events.</p></li>
<li><p><strong>quarantine_past_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Events with timestamp of quarantinePastSecs older than “now” are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events.</p></li>
<li><p><strong>raw_chunk_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value.</p></li>
<li><p><strong>rep_factor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index replication control. This parameter applies to only clustering slaves.
auto = Use the master index replication configuration value.
0 = Turn off replication for this index.</p></li>
<li><p><strong>rotate_period_in_secs</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.</p></li>
<li><p><strong>service_meta_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds).
You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path.</p></li>
<li><p><strong>sync_meta</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures.</p></li>
<li><p><strong>thawed_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path that contains the thawed (resurrected) databases for the index.
Cannot be defined in terms of a volume definition.
Required. Splunk software does not start if an index lacks a valid thawedPath.</p></li>
<li><p><strong>throttle_check_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds).</p></li>
<li><p><strong>tstats_home_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location to store datamodel acceleration TSIDX data for this index. Restart splunkd after changing this parameter.
If specified, it must be defined in terms of a volume definition.</p></li>
<li><p><strong>warm_to_cold_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a script to run when moving data from warm to cold.
This attribute is supported for backwards compatibility with Splunk software versions older than 4.0. Contact Splunk support if you need help configuring this setting.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.Indexes.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.block_sign_size">
<em class="property">property </em><code class="sig-name descname">block_sign_size</code><a class="headerlink" href="#pulumi_splunk.Indexes.block_sign_size" title="Permalink to this definition"></a></dt>
<dd><p>Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. <span class="raw-html-m2r"><br></span>A recommended value is 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.bucket_rebuild_memory_hint">
<em class="property">property </em><code class="sig-name descname">bucket_rebuild_memory_hint</code><a class="headerlink" href="#pulumi_splunk.Indexes.bucket_rebuild_memory_hint" title="Permalink to this definition"></a></dt>
<dd><p>Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make.</p>
<p><span class="raw-html-m2r"><be></span>Caution: This is an advanced parameter. Inappropriate use of this parameter causes splunkd to not start if rebuild is required. Do not set this parameter unless instructed by Splunk Support.
Default value, auto, varies by the amount of physical RAM on the host<span class="raw-html-m2r"><br></span>
less than 2GB RAM = 67108864 (64MB) tsidx
2GB to 8GB RAM = 134217728 (128MB) tsidx
more than 8GB RAM = 268435456 (256MB) tsidx<span class="raw-html-m2r"><br></span>
Values other than “auto” must be 16MB-1GB. Highest legal value (of the numerical part) is 4294967295 You can specify the value using a size suffix: “16777216” or “16MB” are equivalent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.cold_path">
<em class="property">property </em><code class="sig-name descname">cold_path</code><a class="headerlink" href="#pulumi_splunk.Indexes.cold_path" title="Permalink to this definition"></a></dt>
<dd><p>An absolute path that contains the colddbs for the index. The path must be readable and writable. Cold databases are opened as needed when searching.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.cold_to_frozen_dir">
<em class="property">property </em><code class="sig-name descname">cold_to_frozen_dir</code><a class="headerlink" href="#pulumi_splunk.Indexes.cold_to_frozen_dir" title="Permalink to this definition"></a></dt>
<dd><p>Destination path for the frozen archive. Use as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory.
<span class="raw-html-m2r"><br></span>
Bucket freezing policy is as follows:<span class="raw-html-m2r"><br></span>
New style buckets (4.2 and on): removes all files but the rawdata<span class="raw-html-m2r"><br></span>
To thaw, run splunk rebuild <span class="raw-html-m2r"><bucket dir></span> on the bucket, then move to the thawed directory<span class="raw-html-m2r"><br></span>
Old style buckets (Pre-4.2): gzip all the .data and .tsidx files<span class="raw-html-m2r"><br></span>
To thaw, gunzip the zipped files and move the bucket into the thawed directory<span class="raw-html-m2r"><br></span>
If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.cold_to_frozen_script">
<em class="property">property </em><code class="sig-name descname">cold_to_frozen_script</code><a class="headerlink" href="#pulumi_splunk.Indexes.cold_to_frozen_script" title="Permalink to this definition"></a></dt>
<dd><p>Path to the archiving script.
<span class="raw-html-m2r"><br></span>If your script requires a program to run it (for example, python), specify the program followed by the path. The script must be in $SPLUNK_HOME/bin or one of its subdirectories.
<span class="raw-html-m2r"><br></span>Splunk software ships with an example archiving script in $SPLUNK_HOME/bin called coldToFrozenExample.py. DO NOT use this example script directly. It uses a default path, and if modified in place any changes are overwritten on upgrade.
<span class="raw-html-m2r"><br></span>It is best to copy the example script to a new file in bin and modify it for your system. Most importantly, change the default archive path to an existing directory that fits your needs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.compress_rawdata">
<em class="property">property </em><code class="sig-name descname">compress_rawdata</code><a class="headerlink" href="#pulumi_splunk.Indexes.compress_rawdata" title="Permalink to this definition"></a></dt>
<dd><p>This parameter is ignored. The splunkd process always compresses raw data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.datatype">
<em class="property">property </em><code class="sig-name descname">datatype</code><a class="headerlink" href="#pulumi_splunk.Indexes.datatype" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (event | metric). Specifies the type of index.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.enable_online_bucket_repair">
<em class="property">property </em><code class="sig-name descname">enable_online_bucket_repair</code><a class="headerlink" href="#pulumi_splunk.Indexes.enable_online_bucket_repair" title="Permalink to this definition"></a></dt>
<dd><p>Enables asynchronous “online fsck” bucket repair, which runs concurrently with Splunk software.
When enabled, you do not have to wait until buckets are repaired to start the Splunk platform. However, you might observe a slight performance degratation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.frozen_time_period_in_secs">
<em class="property">property </em><code class="sig-name descname">frozen_time_period_in_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.frozen_time_period_in_secs" title="Permalink to this definition"></a></dt>
<dd><p>Number of seconds after which indexed data rolls to frozen.
Defaults to 188697600 (6 years).Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.home_path">
<em class="property">property </em><code class="sig-name descname">home_path</code><a class="headerlink" href="#pulumi_splunk.Indexes.home_path" title="Permalink to this definition"></a></dt>
<dd><p>An absolute path that contains the hot and warm buckets for the index.
Required. Splunk software does not start if an index lacks a valid homePath.
<span class="raw-html-m2r"><br></span>Caution: The path must be readable and writable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_bloom_backfill_bucket_age">
<em class="property">property </em><code class="sig-name descname">max_bloom_backfill_bucket_age</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_bloom_backfill_bucket_age" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[m|s|h|d].
<span class="raw-html-m2r"><br></span>If a warm or cold bucket is older than the specified age, do not create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_concurrent_optimizes">
<em class="property">property </em><code class="sig-name descname">max_concurrent_optimizes</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_concurrent_optimizes" title="Permalink to this definition"></a></dt>
<dd><p>The number of concurrent optimize processes that can run against a hot bucket.
This number should be increased if instructed by Splunk Support. Typically the default value should suffice.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_data_size">
<em class="property">property </em><code class="sig-name descname">max_data_size</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_data_size" title="Permalink to this definition"></a></dt>
<dd><p>The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying “auto” or “auto_high_volume” causes Splunk software to autotune this parameter (recommended).
Use “auto_high_volume” for high volume indexes (such as the main index); otherwise, use “auto”. A “high volume index” would typically be considered one that gets over 10GB of data per day.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_hot_buckets">
<em class="property">property </em><code class="sig-name descname">max_hot_buckets</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_hot_buckets" title="Permalink to this definition"></a></dt>
<dd><p>Maximum hot buckets that can exist per index. Defaults to 3.
<span class="raw-html-m2r"><br></span>When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_hot_idle_secs">
<em class="property">property </em><code class="sig-name descname">max_hot_idle_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_hot_idle_secs" title="Permalink to this definition"></a></dt>
<dd><p>Maximum life, in seconds, of a hot bucket. Defaults to 0. If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. A value of 0 turns off the idle check (equivalent to INFINITE idle time).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_hot_span_secs">
<em class="property">property </em><code class="sig-name descname">max_hot_span_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_hot_span_secs" title="Permalink to this definition"></a></dt>
<dd><p>Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_mem_mb">
<em class="property">property </em><code class="sig-name descname">max_mem_mb</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_mem_mb" title="Permalink to this definition"></a></dt>
<dd><p>The amount of memory, expressed in MB, to allocate for buffering a single tsidx file into memory before flushing to disk. Defaults to 5. The default is recommended for all environments.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_meta_entries">
<em class="property">property </em><code class="sig-name descname">max_meta_entries</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_meta_entries" title="Permalink to this definition"></a></dt>
<dd><p>Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_time_unreplicated_no_acks">
<em class="property">property </em><code class="sig-name descname">max_time_unreplicated_no_acks</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_time_unreplicated_no_acks" title="Permalink to this definition"></a></dt>
<dd><p>Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored.
If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies.
Highest legal value is 2147483647. To disable this parameter, set to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_time_unreplicated_with_acks">
<em class="property">property </em><code class="sig-name descname">max_time_unreplicated_with_acks</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_time_unreplicated_with_acks" title="Permalink to this definition"></a></dt>
<dd><p>Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering).
Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza.
To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_total_data_size_mb">
<em class="property">property </em><code class="sig-name descname">max_total_data_size_mb</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_total_data_size_mb" title="Permalink to this definition"></a></dt>
<dd><p>The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.max_warm_db_count">
<em class="property">property </em><code class="sig-name descname">max_warm_db_count</code><a class="headerlink" href="#pulumi_splunk.Indexes.max_warm_db_count" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times is moved to cold.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.min_raw_file_sync_secs">
<em class="property">property </em><code class="sig-name descname">min_raw_file_sync_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.min_raw_file_sync_secs" title="Permalink to this definition"></a></dt>
<dd><p>Specify an integer (or “disable”) for this parameter.
This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices.
During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files.
If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying “disable” disables syncing entirely: uncompressed slices are removed as soon as compression is complete.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.min_stream_group_queue_size">
<em class="property">property </em><code class="sig-name descname">min_stream_group_queue_size</code><a class="headerlink" href="#pulumi_splunk.Indexes.min_stream_group_queue_size" title="Permalink to this definition"></a></dt>
<dd><p>Minimum size of the queue that stores events in memory before committing them to a tsidx file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.Indexes.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the index to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.partial_service_meta_period">
<em class="property">property </em><code class="sig-name descname">partial_service_meta_period</code><a class="headerlink" href="#pulumi_splunk.Indexes.partial_service_meta_period" title="Permalink to this definition"></a></dt>
<dd><p>Related to serviceMetaPeriod. If set, it enables metadata sync every <span class="raw-html-m2r"><integer></span> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync’ed at serviceMetaPeriod.
partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens.
If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect.
By default it is turned off (zero).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.process_tracker_service_interval">
<em class="property">property </em><code class="sig-name descname">process_tracker_service_interval</code><a class="headerlink" href="#pulumi_splunk.Indexes.process_tracker_service_interval" title="Permalink to this definition"></a></dt>
<dd><p>Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. Defaults to 15.
If set to 0, the indexer checks child process status every second.
Highest legal value is 4294967295.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.quarantine_future_secs">
<em class="property">property </em><code class="sig-name descname">quarantine_future_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.quarantine_future_secs" title="Permalink to this definition"></a></dt>
<dd><p>Events with timestamp of quarantineFutureSecs newer than “now” are dropped into quarantine bucket. Defaults to 2592000 (30 days).
This is a mechanism to prevent main hot buckets from being polluted with fringe events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.quarantine_past_secs">
<em class="property">property </em><code class="sig-name descname">quarantine_past_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.quarantine_past_secs" title="Permalink to this definition"></a></dt>
<dd><p>Events with timestamp of quarantinePastSecs older than “now” are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.raw_chunk_size_bytes">
<em class="property">property </em><code class="sig-name descname">raw_chunk_size_bytes</code><a class="headerlink" href="#pulumi_splunk.Indexes.raw_chunk_size_bytes" title="Permalink to this definition"></a></dt>
<dd><p>Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.rep_factor">
<em class="property">property </em><code class="sig-name descname">rep_factor</code><a class="headerlink" href="#pulumi_splunk.Indexes.rep_factor" title="Permalink to this definition"></a></dt>
<dd><p>Index replication control. This parameter applies to only clustering slaves.
auto = Use the master index replication configuration value.
0 = Turn off replication for this index.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.rotate_period_in_secs">
<em class="property">property </em><code class="sig-name descname">rotate_period_in_secs</code><a class="headerlink" href="#pulumi_splunk.Indexes.rotate_period_in_secs" title="Permalink to this definition"></a></dt>
<dd><p>How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.service_meta_period">
<em class="property">property </em><code class="sig-name descname">service_meta_period</code><a class="headerlink" href="#pulumi_splunk.Indexes.service_meta_period" title="Permalink to this definition"></a></dt>
<dd><p>Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds).
You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.sync_meta">
<em class="property">property </em><code class="sig-name descname">sync_meta</code><a class="headerlink" href="#pulumi_splunk.Indexes.sync_meta" title="Permalink to this definition"></a></dt>
<dd><p>When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.thawed_path">
<em class="property">property </em><code class="sig-name descname">thawed_path</code><a class="headerlink" href="#pulumi_splunk.Indexes.thawed_path" title="Permalink to this definition"></a></dt>
<dd><p>An absolute path that contains the thawed (resurrected) databases for the index.
Cannot be defined in terms of a volume definition.
Required. Splunk software does not start if an index lacks a valid thawedPath.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.throttle_check_period">
<em class="property">property </em><code class="sig-name descname">throttle_check_period</code><a class="headerlink" href="#pulumi_splunk.Indexes.throttle_check_period" title="Permalink to this definition"></a></dt>
<dd><p>Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.tstats_home_path">
<em class="property">property </em><code class="sig-name descname">tstats_home_path</code><a class="headerlink" href="#pulumi_splunk.Indexes.tstats_home_path" title="Permalink to this definition"></a></dt>
<dd><p>Location to store datamodel acceleration TSIDX data for this index. Restart splunkd after changing this parameter.
If specified, it must be defined in terms of a volume definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.warm_to_cold_script">
<em class="property">property </em><code class="sig-name descname">warm_to_cold_script</code><a class="headerlink" href="#pulumi_splunk.Indexes.warm_to_cold_script" title="Permalink to this definition"></a></dt>
<dd><p>Path to a script to run when moving data from warm to cold.
This attribute is supported for backwards compatibility with Splunk software versions older than 4.0. Contact Splunk support if you need help configuring this setting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.Indexes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Indexes.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.Indexes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Indexes.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsHttpEventCollector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsHttpEventCollector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsHttpEventCollectorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsHttpEventCollectorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ack</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector" title="Permalink to this definition"></a></dt>
<dd><p>Create or update HTTP Event Collector input configuration tokens.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsHttpEventCollectorAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Input disabled indicator</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default host value for events with this token</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index to store generated events</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of indexes allowed for events with this token</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token name (inputs.conf key)</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default source for events with this token</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default source type for events with this token</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token value for sending data to collector/event endpoint</p></li>
<li><p><strong>use_ack</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Indexer acknowledgement for this token</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsHttpEventCollectorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsHttpEventCollectorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ack</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsHttpEventCollector" title="pulumi_splunk.InputsHttpEventCollector">InputsHttpEventCollector</a><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsHttpEventCollector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsHttpEventCollectorAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Input disabled indicator</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default host value for events with this token</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index to store generated events</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of indexes allowed for events with this token</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token name (inputs.conf key)</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default source for events with this token</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default source type for events with this token</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token value for sending data to collector/event endpoint</p></li>
<li><p><strong>use_ack</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Indexer acknowledgement for this token</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Input disabled indicator</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.host" title="Permalink to this definition"></a></dt>
<dd><p>Default host value for events with this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.index">
<em class="property">property </em><code class="sig-name descname">index</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.index" title="Permalink to this definition"></a></dt>
<dd><p>Index to store generated events</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.indexes">
<em class="property">property </em><code class="sig-name descname">indexes</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.indexes" title="Permalink to this definition"></a></dt>
<dd><p>Set of indexes allowed for events with this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.name" title="Permalink to this definition"></a></dt>
<dd><p>Token name (inputs.conf key)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.source" title="Permalink to this definition"></a></dt>
<dd><p>Default source for events with this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>Default source type for events with this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.token" title="Permalink to this definition"></a></dt>
<dd><p>Token value for sending data to collector/event endpoint</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.use_ack">
<em class="property">property </em><code class="sig-name descname">use_ack</code><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.use_ack" title="Permalink to this definition"></a></dt>
<dd><p>Indexer acknowledgement for this token</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsHttpEventCollector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsHttpEventCollector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsHttpEventCollector.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsMonitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsMonitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsMonitorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsMonitorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklist</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">crc_salt</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_tail</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_regex</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_segment</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_older_than</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recursive</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rename_source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_before_close</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelist</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsMonitor" title="Permalink to this definition"></a></dt>
<dd><p>Create or update a new file or directory monitor input.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">monitor</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsMonitor</span><span class="p">(</span><span class="s2">&quot;monitor&quot;</span><span class="p">,</span>
    <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">sourcetype</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsMonitorAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>blacklist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. The file path that matches this regular expression is not indexed.</p></li>
<li><p><strong>crc_salt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string that modifies the file tracking identity for files in this input. The magic value <span class="raw-html-m2r"><SOURCE></span> invokes special behavior.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input monitoring is disabled.</p></li>
<li><p><strong>follow_tail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, files that are seen for the first time is read from the end.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the host field for events from this data input.</p></li>
<li><p><strong>host_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group.</p></li>
<li><p><strong>host_segment</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Use the specified slash-separate segment of the filepath as the host field value.</p></li>
<li><p><strong>ignore_older_than</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which index events from this input should be stored in. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file or directory path to monitor on the system.</p></li>
<li><p><strong>recursive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Setting this to false prevents monitoring of any subdirectories encountered within this data input.</p></li>
<li><p><strong>rename_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the sourcetype field for incoming events.</p></li>
<li><p><strong>time_before_close</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data.</p></li>
<li><p><strong>whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. Only file paths that match this regular expression are indexed.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsMonitorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsMonitorAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklist</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">crc_salt</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_tail</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_regex</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_segment</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_older_than</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recursive</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rename_source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_before_close</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelist</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsMonitor" title="pulumi_splunk.InputsMonitor">InputsMonitor</a><a class="headerlink" href="#pulumi_splunk.InputsMonitor.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsMonitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsMonitorAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>blacklist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. The file path that matches this regular expression is not indexed.</p></li>
<li><p><strong>crc_salt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string that modifies the file tracking identity for files in this input. The magic value <span class="raw-html-m2r"><SOURCE></span> invokes special behavior.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input monitoring is disabled.</p></li>
<li><p><strong>follow_tail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, files that are seen for the first time is read from the end.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the host field for events from this data input.</p></li>
<li><p><strong>host_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group.</p></li>
<li><p><strong>host_segment</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Use the specified slash-separate segment of the filepath as the host field value.</p></li>
<li><p><strong>ignore_older_than</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which index events from this input should be stored in. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file or directory path to monitor on the system.</p></li>
<li><p><strong>recursive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Setting this to false prevents monitoring of any subdirectories encountered within this data input.</p></li>
<li><p><strong>rename_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the sourcetype field for incoming events.</p></li>
<li><p><strong>time_before_close</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data.</p></li>
<li><p><strong>whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a regular expression for a file path. Only file paths that match this regular expression are indexed.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.blacklist">
<em class="property">property </em><code class="sig-name descname">blacklist</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.blacklist" title="Permalink to this definition"></a></dt>
<dd><p>Specify a regular expression for a file path. The file path that matches this regular expression is not indexed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.crc_salt">
<em class="property">property </em><code class="sig-name descname">crc_salt</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.crc_salt" title="Permalink to this definition"></a></dt>
<dd><p>A string that modifies the file tracking identity for files in this input. The magic value <span class="raw-html-m2r"><SOURCE></span> invokes special behavior.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if input monitoring is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.follow_tail">
<em class="property">property </em><code class="sig-name descname">follow_tail</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.follow_tail" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, files that are seen for the first time is read from the end.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.host" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the host field for events from this data input.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.host_regex">
<em class="property">property </em><code class="sig-name descname">host_regex</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.host_regex" title="Permalink to this definition"></a></dt>
<dd><p>Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.host_segment">
<em class="property">property </em><code class="sig-name descname">host_segment</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.host_segment" title="Permalink to this definition"></a></dt>
<dd><p>Use the specified slash-separate segment of the filepath as the host field value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.ignore_older_than">
<em class="property">property </em><code class="sig-name descname">ignore_older_than</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.ignore_older_than" title="Permalink to this definition"></a></dt>
<dd><p>Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.index">
<em class="property">property </em><code class="sig-name descname">index</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.index" title="Permalink to this definition"></a></dt>
<dd><p>Which index events from this input should be stored in. Defaults to default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.name" title="Permalink to this definition"></a></dt>
<dd><p>The file or directory path to monitor on the system.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.recursive">
<em class="property">property </em><code class="sig-name descname">recursive</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.recursive" title="Permalink to this definition"></a></dt>
<dd><p>Setting this to false prevents monitoring of any subdirectories encountered within this data input.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.rename_source">
<em class="property">property </em><code class="sig-name descname">rename_source</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.rename_source" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the sourcetype field for incoming events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.time_before_close">
<em class="property">property </em><code class="sig-name descname">time_before_close</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.time_before_close" title="Permalink to this definition"></a></dt>
<dd><p>When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.whitelist">
<em class="property">property </em><code class="sig-name descname">whitelist</code><a class="headerlink" href="#pulumi_splunk.InputsMonitor.whitelist" title="Permalink to this definition"></a></dt>
<dd><p>Specify a regular expression for a file path. Only file paths that match this regular expression are indexed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsMonitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsMonitor.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsMonitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsMonitor.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsScript</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsScriptAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsScriptAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passauth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rename_source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsScript" title="Permalink to this definition"></a></dt>
<dd><p>Create or update scripted inputs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsScriptAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the input script is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host for events from this input. Defaults to whatever host sent the event.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the index for events from this input. Defaults to the main index.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify an integer or cron schedule. This parameter specifies how often to execute the specified script, in seconds or a valid cron schedule. If you specify a cron schedule, the script is not executed on start-up.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the name of the scripted input.</p></li>
<li><p><strong>passauth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User to run the script as. If you provide a username, Splunk software generates an auth token for that user and passes it to the script.</p></li>
<li><p><strong>rename_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a new name for the source field for the script.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the sourcetype key/field for events from this input. If unset, Splunk software picks a source type based on various aspects of the data. As a convenience, the chosen string is prepended with ‘sourcetype::’. There is no hard-coded default.
Sets the sourcetype key initial value. The key is used during parsing/indexing, in particular to set the source type field during indexing. It is also the source type field used at search time.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsScriptAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsScriptAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passauth</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rename_source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsScript" title="pulumi_splunk.InputsScript">InputsScript</a><a class="headerlink" href="#pulumi_splunk.InputsScript.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsScriptAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the input script is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host for events from this input. Defaults to whatever host sent the event.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the index for events from this input. Defaults to the main index.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify an integer or cron schedule. This parameter specifies how often to execute the specified script, in seconds or a valid cron schedule. If you specify a cron schedule, the script is not executed on start-up.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the name of the scripted input.</p></li>
<li><p><strong>passauth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User to run the script as. If you provide a username, Splunk software generates an auth token for that user and passes it to the script.</p></li>
<li><p><strong>rename_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a new name for the source field for the script.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the sourcetype key/field for events from this input. If unset, Splunk software picks a source type based on various aspects of the data. As a convenience, the chosen string is prepended with ‘sourcetype::’. There is no hard-coded default.
Sets the sourcetype key initial value. The key is used during parsing/indexing, in particular to set the source type field during indexing. It is also the source type field used at search time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsScript.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsScript.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether the input script is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsScript.host" title="Permalink to this definition"></a></dt>
<dd><p>Sets the host for events from this input. Defaults to whatever host sent the event.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.index">
<em class="property">property </em><code class="sig-name descname">index</code><a class="headerlink" href="#pulumi_splunk.InputsScript.index" title="Permalink to this definition"></a></dt>
<dd><p>Sets the index for events from this input. Defaults to the main index.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.interval">
<em class="property">property </em><code class="sig-name descname">interval</code><a class="headerlink" href="#pulumi_splunk.InputsScript.interval" title="Permalink to this definition"></a></dt>
<dd><p>Specify an integer or cron schedule. This parameter specifies how often to execute the specified script, in seconds or a valid cron schedule. If you specify a cron schedule, the script is not executed on start-up.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsScript.name" title="Permalink to this definition"></a></dt>
<dd><p>Specify the name of the scripted input.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.passauth">
<em class="property">property </em><code class="sig-name descname">passauth</code><a class="headerlink" href="#pulumi_splunk.InputsScript.passauth" title="Permalink to this definition"></a></dt>
<dd><p>User to run the script as. If you provide a username, Splunk software generates an auth token for that user and passes it to the script.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.rename_source">
<em class="property">property </em><code class="sig-name descname">rename_source</code><a class="headerlink" href="#pulumi_splunk.InputsScript.rename_source" title="Permalink to this definition"></a></dt>
<dd><p>Specify a new name for the source field for the script.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_splunk.InputsScript.source" title="Permalink to this definition"></a></dt>
<dd><p>Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_splunk.InputsScript.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>Sets the sourcetype key/field for events from this input. If unset, Splunk software picks a source type based on various aspects of the data. As a convenience, the chosen string is prepended with ‘sourcetype::’. There is no hard-coded default.
Sets the sourcetype key initial value. The key is used during parsing/indexing, in particular to set the source type field during indexing. It is also the source type field used at search time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsScript.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsScript.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpCooked">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsTcpCooked</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpCookedAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpCookedAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked" title="Permalink to this definition"></a></dt>
<dd><p>Create or update cooked TCP input information and create new containers for managing cooked data.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_cooked</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsTcpCooked</span><span class="p">(</span><span class="s2">&quot;tcpCooked&quot;</span><span class="p">,</span>
    <span class="n">connection_host</span><span class="o">=</span><span class="s2">&quot;dns&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">restrict_to_host</span><span class="o">=</span><span class="s2">&quot;splunk&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpCookedAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which the indexer gets data.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port number of this input.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restrict incoming connections on this port to the host specified here.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpCookedAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpCookedAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsTcpCooked" title="pulumi_splunk.InputsTcpCooked">InputsTcpCooked</a><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsTcpCooked resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpCookedAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which the indexer gets data.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port number of this input.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restrict incoming connections on this port to the host specified here.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.connection_host">
<em class="property">property </em><code class="sig-name descname">connection_host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.connection_host" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if input is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.host" title="Permalink to this definition"></a></dt>
<dd><p>Host from which the indexer gets data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.name" title="Permalink to this definition"></a></dt>
<dd><p>The port number of this input.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.restrict_to_host">
<em class="property">property </em><code class="sig-name descname">restrict_to_host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.restrict_to_host" title="Permalink to this definition"></a></dt>
<dd><p>Restrict incoming connections on this port to the host specified here.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpCooked.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpCooked.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpCooked.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpRaw">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsTcpRaw</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpRawAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpRawAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">raw_tcp_done_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw" title="Permalink to this definition"></a></dt>
<dd><p>Create or update raw TCP input information for managing raw tcp inputs from forwarders.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_raw</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsTcpRaw</span><span class="p">(</span><span class="s2">&quot;tcpRaw&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">index</span><span class="o">=</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">queue</span><span class="o">=</span><span class="s2">&quot;indexQueue&quot;</span><span class="p">,</span>
    <span class="n">source</span><span class="o">=</span><span class="s2">&quot;new&quot;</span><span class="p">,</span>
    <span class="n">sourcetype</span><span class="o">=</span><span class="s2">&quot;new&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpRawAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which the indexer gets data.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index to store generated events. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input port which receives raw data.</p></li>
<li><p><strong>queue</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (parsingQueue | indexQueue)
Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at “Monitor files and directories with inputs.conf”
Set queue to indexQueue to send your data directly into the index.</p></li>
<li><p><strong>raw_tcp_done_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows for restricting this input to only accept data from the host specified here.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the source type for events from this input.
“sourcetype=” is automatically prepended to <span class="raw-html-m2r"><string></span>.
Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpRawAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpRawAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">raw_tcp_done_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsTcpRaw" title="pulumi_splunk.InputsTcpRaw">InputsTcpRaw</a><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsTcpRaw resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpRawAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which the indexer gets data.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Index to store generated events. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input port which receives raw data.</p></li>
<li><p><strong>queue</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (parsingQueue | indexQueue)
Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at “Monitor files and directories with inputs.conf”
Set queue to indexQueue to send your data directly into the index.</p></li>
<li><p><strong>raw_tcp_done_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows for restricting this input to only accept data from the host specified here.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the source type for events from this input.
“sourcetype=” is automatically prepended to <span class="raw-html-m2r"><string></span>.
Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.connection_host">
<em class="property">property </em><code class="sig-name descname">connection_host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.connection_host" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if input is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.host" title="Permalink to this definition"></a></dt>
<dd><p>Host from which the indexer gets data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.index">
<em class="property">property </em><code class="sig-name descname">index</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.index" title="Permalink to this definition"></a></dt>
<dd><p>Index to store generated events. Defaults to default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.name" title="Permalink to this definition"></a></dt>
<dd><p>The input port which receives raw data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.queue">
<em class="property">property </em><code class="sig-name descname">queue</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.queue" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (parsingQueue | indexQueue)
Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at “Monitor files and directories with inputs.conf”
Set queue to indexQueue to send your data directly into the index.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.raw_tcp_done_timeout">
<em class="property">property </em><code class="sig-name descname">raw_tcp_done_timeout</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.raw_tcp_done_timeout" title="Permalink to this definition"></a></dt>
<dd><p>Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.restrict_to_host">
<em class="property">property </em><code class="sig-name descname">restrict_to_host</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.restrict_to_host" title="Permalink to this definition"></a></dt>
<dd><p>Allows for restricting this input to only accept data from the host specified here.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.source" title="Permalink to this definition"></a></dt>
<dd><p>Sets the source key/field for events from this input. Defaults to the input file path.
Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>Set the source type for events from this input.
“sourcetype=” is automatically prepended to <span class="raw-html-m2r"><string></span>.
Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpRaw.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpRaw.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpRaw.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsTcpSplunkTcpToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpSplunkTcpTokenAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpSplunkTcpTokenAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken" title="Permalink to this definition"></a></dt>
<dd><p>Manage receiver access using tokens.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_splunk_tcp_token</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsTcpSplunkTcpToken</span><span class="p">(</span><span class="s2">&quot;tcpSplunkTcpToken&quot;</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="s2">&quot;D66C45B3-7C28-48A1-A13A-027914146501&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpSplunkTcpTokenAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Name for the token to create.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional. Token value to use. If unspecified, a token is generated automatically.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsTcpSplunkTcpTokenAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsTcpSplunkTcpTokenAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsTcpSplunkTcpToken" title="pulumi_splunk.InputsTcpSplunkTcpToken">InputsTcpSplunkTcpToken</a><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsTcpSplunkTcpToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsTcpSplunkTcpTokenAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Name for the token to create.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional. Token value to use. If unspecified, a token is generated automatically.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.name" title="Permalink to this definition"></a></dt>
<dd><p>Required. Name for the token to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.token" title="Permalink to this definition"></a></dt>
<dd><p>Optional. Token value to use. If unspecified, a token is generated automatically.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpSplunkTcpToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSplunkTcpToken.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsTcpSsl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_client_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_ca</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl" title="Permalink to this definition"></a></dt>
<dd><p>Access or update the SSL configuration for the host.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsTcpSsl</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">require_client_cert</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Server certificate password, if any.</p></li>
<li><p><strong>require_client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a client must authenticate.</p></li>
<li><p><strong>root_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate authority list (root file)</p></li>
<li><p><strong>server_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full path to the server certificate.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_client_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_ca</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsTcpSsl" title="pulumi_splunk.InputsTcpSsl">InputsTcpSsl</a><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsTcpSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Server certificate password, if any.</p></li>
<li><p><strong>require_client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether a client must authenticate.</p></li>
<li><p><strong>root_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate authority list (root file)</p></li>
<li><p><strong>server_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full path to the server certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if input is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.password" title="Permalink to this definition"></a></dt>
<dd><p>Server certificate password, if any.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.require_client_cert">
<em class="property">property </em><code class="sig-name descname">require_client_cert</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.require_client_cert" title="Permalink to this definition"></a></dt>
<dd><p>Determines whether a client must authenticate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.root_ca">
<em class="property">property </em><code class="sig-name descname">root_ca</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.root_ca" title="Permalink to this definition"></a></dt>
<dd><p>Certificate authority list (root file)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.server_cert">
<em class="property">property </em><code class="sig-name descname">server_cert</code><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.server_cert" title="Permalink to this definition"></a></dt>
<dd><p>Full path to the server certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsTcpSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsTcpSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsTcpSsl.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsUdp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">InputsUdp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsUdpAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsUdpAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_appending_timestamp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_priority_stripping</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsUdp" title="Permalink to this definition"></a></dt>
<dd><p>Create and manage UDP data inputs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">udp</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">InputsUdp</span><span class="p">(</span><span class="s2">&quot;udp&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">index</span><span class="o">=</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">source</span><span class="o">=</span><span class="s2">&quot;new&quot;</span><span class="p">,</span>
    <span class="n">sourcetype</span><span class="o">=</span><span class="s2">&quot;new&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsUdpAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the host field for incoming events. This is used during parsing/indexing, in particular to set the host field. It is also the host field used at search time.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which index events from this input should be stored in. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UDP port that this input should listen on.</p></li>
<li><p><strong>no_appending_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, prevents Splunk software from prepending a timestamp and hostname to incoming events.</p></li>
<li><p><strong>no_priority_stripping</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, Splunk software does not remove the priority field from incoming syslog events.</p></li>
<li><p><strong>queue</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which queue events from this input should be sent to. Generally this does not need to be changed.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restrict incoming connections on this port to the host specified here.
If this is not set, the value specified in [udp://<span class="raw-html-m2r"><remote server></span>:<span class="raw-html-m2r"><port></span>] in inputs.conf is used.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the source field for incoming events. The same source should not be used for multiple data inputs.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the sourcetype field for incoming events.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InputsUdpAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InputsUdpAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_appending_timestamp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_priority_stripping</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrict_to_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.InputsUdp" title="pulumi_splunk.InputsUdp">InputsUdp</a><a class="headerlink" href="#pulumi_splunk.InputsUdp.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing InputsUdp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InputsUdpAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>connection_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if input is disabled.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the host field for incoming events. This is used during parsing/indexing, in particular to set the host field. It is also the host field used at search time.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which index events from this input should be stored in. Defaults to default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UDP port that this input should listen on.</p></li>
<li><p><strong>no_appending_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, prevents Splunk software from prepending a timestamp and hostname to incoming events.</p></li>
<li><p><strong>no_priority_stripping</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, Splunk software does not remove the priority field from incoming syslog events.</p></li>
<li><p><strong>queue</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which queue events from this input should be sent to. Generally this does not need to be changed.</p></li>
<li><p><strong>restrict_to_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restrict incoming connections on this port to the host specified here.
If this is not set, the value specified in [udp://<span class="raw-html-m2r"><remote server></span>:<span class="raw-html-m2r"><port></span>] in inputs.conf is used.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the source field for incoming events. The same source should not be used for multiple data inputs.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to populate in the sourcetype field for incoming events.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.connection_host">
<em class="property">property </em><code class="sig-name descname">connection_host</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.connection_host" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (ip | dns | none)
Set the host for the remote server that is sending data.
ip sets the host to the IP address of the remote server sending data.
dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
Default value is dns.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if input is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.host" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the host field for incoming events. This is used during parsing/indexing, in particular to set the host field. It is also the host field used at search time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.index">
<em class="property">property </em><code class="sig-name descname">index</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.index" title="Permalink to this definition"></a></dt>
<dd><p>Which index events from this input should be stored in. Defaults to default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.name" title="Permalink to this definition"></a></dt>
<dd><p>The UDP port that this input should listen on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.no_appending_timestamp">
<em class="property">property </em><code class="sig-name descname">no_appending_timestamp</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.no_appending_timestamp" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, prevents Splunk software from prepending a timestamp and hostname to incoming events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.no_priority_stripping">
<em class="property">property </em><code class="sig-name descname">no_priority_stripping</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.no_priority_stripping" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, Splunk software does not remove the priority field from incoming syslog events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.queue">
<em class="property">property </em><code class="sig-name descname">queue</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.queue" title="Permalink to this definition"></a></dt>
<dd><p>Which queue events from this input should be sent to. Generally this does not need to be changed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.restrict_to_host">
<em class="property">property </em><code class="sig-name descname">restrict_to_host</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.restrict_to_host" title="Permalink to this definition"></a></dt>
<dd><p>Restrict incoming connections on this port to the host specified here.
If this is not set, the value specified in [udp://<span class="raw-html-m2r"><remote server></span>:<span class="raw-html-m2r"><port></span>] in inputs.conf is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.source" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the source field for incoming events. The same source should not be used for multiple data inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_splunk.InputsUdp.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>The value to populate in the sourcetype field for incoming events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.InputsUdp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsUdp.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.InputsUdp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.InputsUdp.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpDefault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">OutputsTcpDefault</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpDefaultAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpDefaultAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_events_on_queue_full</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index_and_forward</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_cooked_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault" title="Permalink to this definition"></a></dt>
<dd><p>Manage to global tcpout properties.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_default</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">OutputsTcpDefault</span><span class="p">(</span><span class="s2">&quot;tcpDefault&quot;</span><span class="p">,</span>
    <span class="n">default_group</span><span class="o">=</span><span class="s2">&quot;test-indexers&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">drop_events_on_queue_full</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">index_and_forward</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">max_queue_size</span><span class="o">=</span><span class="s2">&quot;100KB&quot;</span><span class="p">,</span>
    <span class="n">send_cooked_data</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpDefaultAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>default_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comma-separated list of one or more target group names, specified later in [tcpout:<span class="raw-html-m2r"><target_group></span>] stanzas of outputs.conf.spec file.
The forwarder sends all data to the specified groups. If you do not want to forward data automatically, do not set this attribute. Can be overridden by an inputs.conf _TCP_ROUTING setting, which in turn can be overridden by a props.conf/transforms.conf modifier.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables default tcpout settings</p></li>
<li><p><strong>drop_events_on_queue_full</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p></li>
<li><p><strong>heartbeat_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p></li>
<li><p><strong>index_and_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to index all data locally, in addition to forwarding it. Defaults to false.
This is known as an “index-and-forward” configuration. This attribute is only available for heavy forwarders. It is available only at the top level [tcpout] stanza in outputs.conf. It cannot be overridden in a target group.</p></li>
<li><p><strong>max_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration to be edited. The only valid value is “tcpout”.</p></li>
<li><p><strong>send_cooked_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpDefaultAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpDefaultAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_events_on_queue_full</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index_and_forward</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_cooked_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.OutputsTcpDefault" title="pulumi_splunk.OutputsTcpDefault">OutputsTcpDefault</a><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing OutputsTcpDefault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpDefaultAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>default_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comma-separated list of one or more target group names, specified later in [tcpout:<span class="raw-html-m2r"><target_group></span>] stanzas of outputs.conf.spec file.
The forwarder sends all data to the specified groups. If you do not want to forward data automatically, do not set this attribute. Can be overridden by an inputs.conf _TCP_ROUTING setting, which in turn can be overridden by a props.conf/transforms.conf modifier.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables default tcpout settings</p></li>
<li><p><strong>drop_events_on_queue_full</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p></li>
<li><p><strong>heartbeat_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p></li>
<li><p><strong>index_and_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to index all data locally, in addition to forwarding it. Defaults to false.
This is known as an “index-and-forward” configuration. This attribute is only available for heavy forwarders. It is available only at the top level [tcpout] stanza in outputs.conf. It cannot be overridden in a target group.</p></li>
<li><p><strong>max_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration to be edited. The only valid value is “tcpout”.</p></li>
<li><p><strong>send_cooked_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.default_group">
<em class="property">property </em><code class="sig-name descname">default_group</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.default_group" title="Permalink to this definition"></a></dt>
<dd><p>Comma-separated list of one or more target group names, specified later in [tcpout:<span class="raw-html-m2r"><target_group></span>] stanzas of outputs.conf.spec file.
The forwarder sends all data to the specified groups. If you do not want to forward data automatically, do not set this attribute. Can be overridden by an inputs.conf _TCP_ROUTING setting, which in turn can be overridden by a props.conf/transforms.conf modifier.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Disables default tcpout settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.drop_events_on_queue_full">
<em class="property">property </em><code class="sig-name descname">drop_events_on_queue_full</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.drop_events_on_queue_full" title="Permalink to this definition"></a></dt>
<dd><p>If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.heartbeat_frequency">
<em class="property">property </em><code class="sig-name descname">heartbeat_frequency</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.heartbeat_frequency" title="Permalink to this definition"></a></dt>
<dd><p>How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.index_and_forward">
<em class="property">property </em><code class="sig-name descname">index_and_forward</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.index_and_forward" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether to index all data locally, in addition to forwarding it. Defaults to false.
This is known as an “index-and-forward” configuration. This attribute is only available for heavy forwarders. It is available only at the top level [tcpout] stanza in outputs.conf. It cannot be overridden in a target group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.max_queue_size">
<em class="property">property </em><code class="sig-name descname">max_queue_size</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.max_queue_size" title="Permalink to this definition"></a></dt>
<dd><p>Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.name" title="Permalink to this definition"></a></dt>
<dd><p>Configuration to be edited. The only valid value is “tcpout”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.send_cooked_data">
<em class="property">property </em><code class="sig-name descname">send_cooked_data</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.send_cooked_data" title="Permalink to this definition"></a></dt>
<dd><p>If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpDefault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpDefault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpDefault.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">OutputsTcpGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpGroupAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpGroupAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compressed</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_events_on_queue_full</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_cooked_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup" title="Permalink to this definition"></a></dt>
<dd><p>Access to the configuration of a group of one or more data forwarding destinations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_group</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">OutputsTcpGroup</span><span class="p">(</span><span class="s2">&quot;tcpGroup&quot;</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">drop_events_on_queue_full</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">max_queue_size</span><span class="o">=</span><span class="s2">&quot;100KB&quot;</span><span class="p">,</span>
    <span class="n">send_cooked_data</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">servers</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;1.1.1.1:1234&quot;</span><span class="p">,</span>
        <span class="s2">&quot;2.2.2.2:1234&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpGroupAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>compressed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, forwarder sends compressed data. If set to true, the receiver port must also have compression turned on.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables the group.</p></li>
<li><p><strong>drop_events_on_queue_full</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p></li>
<li><p><strong>heartbeat_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p></li>
<li><p><strong>max_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (tcpout | syslog). Specifies the type of output processor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group of receivers.</p></li>
<li><p><strong>send_cooked_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Comma-separated list of servers to include in the group.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token value generated by the indexer after configuration.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpGroupAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpGroupAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compressed</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_events_on_queue_full</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queue_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_cooked_data</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.OutputsTcpGroup" title="pulumi_splunk.OutputsTcpGroup">OutputsTcpGroup</a><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing OutputsTcpGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpGroupAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>compressed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, forwarder sends compressed data. If set to true, the receiver port must also have compression turned on.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables the group.</p></li>
<li><p><strong>drop_events_on_queue_full</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p></li>
<li><p><strong>heartbeat_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p></li>
<li><p><strong>max_queue_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (tcpout | syslog). Specifies the type of output processor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group of receivers.</p></li>
<li><p><strong>send_cooked_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Comma-separated list of servers to include in the group.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token value generated by the indexer after configuration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.compressed">
<em class="property">property </em><code class="sig-name descname">compressed</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.compressed" title="Permalink to this definition"></a></dt>
<dd><p>If true, forwarder sends compressed data. If set to true, the receiver port must also have compression turned on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.disabled" title="Permalink to this definition"></a></dt>
<dd><p>If true, disables the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.drop_events_on_queue_full">
<em class="property">property </em><code class="sig-name descname">drop_events_on_queue_full</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.drop_events_on_queue_full" title="Permalink to this definition"></a></dt>
<dd><p>If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).
<span class="raw-html-m2r"><br></span>CAUTION: Do not set this value to a positive integer if you are monitoring files.
Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group queue is blocked, no more data reaches any other target group.
Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.heartbeat_frequency">
<em class="property">property </em><code class="sig-name descname">heartbeat_frequency</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.heartbeat_frequency" title="Permalink to this definition"></a></dt>
<dd><p>How often (in seconds) to send a heartbeat packet to the receiving server.
Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.max_queue_size">
<em class="property">property </em><code class="sig-name descname">max_queue_size</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.max_queue_size" title="Permalink to this definition"></a></dt>
<dd><p>Specify an integer or integer[KB|MB|GB].
<span class="raw-html-m2r"><br></span>Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).
Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue in-memory (RAM) buffer.
For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder is likely to be much smaller than on a non-parsing forwarder, if you use this version of the setting.
If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.
If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.method" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (tcpout | syslog). Specifies the type of output processor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the group of receivers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.send_cooked_data">
<em class="property">property </em><code class="sig-name descname">send_cooked_data</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.send_cooked_data" title="Permalink to this definition"></a></dt>
<dd><p>If true, events are cooked (processed by Splunk software). If false, events are raw and untouched prior to sending. Defaults to true.
Set to false if you are sending to a third-party system.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.servers">
<em class="property">property </em><code class="sig-name descname">servers</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.servers" title="Permalink to this definition"></a></dt>
<dd><p>Comma-separated list of servers to include in the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.token" title="Permalink to this definition"></a></dt>
<dd><p>Token value generated by the indexer after configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpGroup.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">OutputsTcpServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpServerAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpServerAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_alt_name_to_check</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cipher</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_common_name_to_check</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_root_ca_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_verify_server_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer" title="Permalink to this definition"></a></dt>
<dd><p>Access data forwarding configurations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_server</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">OutputsTcpServer</span><span class="p">(</span><span class="s2">&quot;tcpServer&quot;</span><span class="p">,</span> <span class="n">ssl_alt_name_to_check</span><span class="o">=</span><span class="s2">&quot;old-host&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpServerAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables the group.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (clone | balance | autobalance)
The data distribution method used when two or more servers exist in the same forwarder group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <span class="raw-html-m2r"><host></span>:<span class="raw-html-m2r"><port></span> of the Splunk receiver. <span class="raw-html-m2r"><host></span> can be either an ip address or server name. <span class="raw-html-m2r"><port></span> is the that port that the Splunk receiver is listening on.</p></li>
<li><p><strong>ssl_alt_name_to_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alternate name to match in the remote server’s SSL certificate.</p></li>
<li><p><strong>ssl_cert_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the client certificate. If specified, connection uses SSL.</p></li>
<li><p><strong>ssl_cipher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL Cipher in the form ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM</p></li>
<li><p><strong>ssl_common_name_to_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Check the common name of the server’s certificate against this name.
If there is no match, assume that Splunk Enterprise is not authenticated against this server. You must specify this setting if sslVerifyServerCert is true.</p></li>
<li><p><strong>ssl_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the CAcert.
The default Splunk Enterprise CAcert uses the password “password.”</p></li>
<li><p><strong>ssl_root_ca_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the root certificate authority file.</p></li>
<li><p><strong>ssl_verify_server_cert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, make sure that the server you are connecting to is a valid one (authenticated). Both the common name and the alternate name of the server are then checked for a match.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpServerAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpServerAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_alt_name_to_check</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cipher</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_common_name_to_check</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_root_ca_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_verify_server_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.OutputsTcpServer" title="pulumi_splunk.OutputsTcpServer">OutputsTcpServer</a><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing OutputsTcpServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpServerAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables the group.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: (clone | balance | autobalance)
The data distribution method used when two or more servers exist in the same forwarder group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <span class="raw-html-m2r"><host></span>:<span class="raw-html-m2r"><port></span> of the Splunk receiver. <span class="raw-html-m2r"><host></span> can be either an ip address or server name. <span class="raw-html-m2r"><port></span> is the that port that the Splunk receiver is listening on.</p></li>
<li><p><strong>ssl_alt_name_to_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alternate name to match in the remote server’s SSL certificate.</p></li>
<li><p><strong>ssl_cert_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the client certificate. If specified, connection uses SSL.</p></li>
<li><p><strong>ssl_cipher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL Cipher in the form ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM</p></li>
<li><p><strong>ssl_common_name_to_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Check the common name of the server’s certificate against this name.
If there is no match, assume that Splunk Enterprise is not authenticated against this server. You must specify this setting if sslVerifyServerCert is true.</p></li>
<li><p><strong>ssl_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the CAcert.
The default Splunk Enterprise CAcert uses the password “password.”</p></li>
<li><p><strong>ssl_root_ca_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the root certificate authority file.</p></li>
<li><p><strong>ssl_verify_server_cert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, make sure that the server you are connecting to is a valid one (authenticated). Both the common name and the alternate name of the server are then checked for a match.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.disabled" title="Permalink to this definition"></a></dt>
<dd><p>If true, disables the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.method" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (clone | balance | autobalance)
The data distribution method used when two or more servers exist in the same forwarder group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.name" title="Permalink to this definition"></a></dt>
<dd><p><span class="raw-html-m2r"><host></span>:<span class="raw-html-m2r"><port></span> of the Splunk receiver. <span class="raw-html-m2r"><host></span> can be either an ip address or server name. <span class="raw-html-m2r"><port></span> is the that port that the Splunk receiver is listening on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_alt_name_to_check">
<em class="property">property </em><code class="sig-name descname">ssl_alt_name_to_check</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_alt_name_to_check" title="Permalink to this definition"></a></dt>
<dd><p>The alternate name to match in the remote server’s SSL certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_cert_path">
<em class="property">property </em><code class="sig-name descname">ssl_cert_path</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_cert_path" title="Permalink to this definition"></a></dt>
<dd><p>Path to the client certificate. If specified, connection uses SSL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_cipher">
<em class="property">property </em><code class="sig-name descname">ssl_cipher</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_cipher" title="Permalink to this definition"></a></dt>
<dd><p>SSL Cipher in the form ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_common_name_to_check">
<em class="property">property </em><code class="sig-name descname">ssl_common_name_to_check</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_common_name_to_check" title="Permalink to this definition"></a></dt>
<dd><p>Check the common name of the server’s certificate against this name.
If there is no match, assume that Splunk Enterprise is not authenticated against this server. You must specify this setting if sslVerifyServerCert is true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_password">
<em class="property">property </em><code class="sig-name descname">ssl_password</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_password" title="Permalink to this definition"></a></dt>
<dd><p>The password associated with the CAcert.
The default Splunk Enterprise CAcert uses the password “password.”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_root_ca_path">
<em class="property">property </em><code class="sig-name descname">ssl_root_ca_path</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_root_ca_path" title="Permalink to this definition"></a></dt>
<dd><p>The path to the root certificate authority file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.ssl_verify_server_cert">
<em class="property">property </em><code class="sig-name descname">ssl_verify_server_cert</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.ssl_verify_server_cert" title="Permalink to this definition"></a></dt>
<dd><p>If true, make sure that the server you are connecting to is a valid one (authenticated). Both the common name and the alternate name of the server are then checked for a match.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpServer.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpSyslog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">OutputsTcpSyslog</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpSyslogAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpSyslogAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslog_sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timestamp_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog" title="Permalink to this definition"></a></dt>
<dd><p>Access the configuration of a forwarded server configured to provide data in standard syslog format.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_splunk</span> <span class="k">as</span> <span class="nn">splunk</span>

<span class="n">tcp_syslog</span> <span class="o">=</span> <span class="n">splunk</span><span class="o">.</span><span class="n">OutputsTcpSyslog</span><span class="p">(</span><span class="s2">&quot;tcpSyslog&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">server</span><span class="o">=</span><span class="s2">&quot;new-host-1:1234&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpSyslogAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables global syslog settings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the syslog output group. This is name used when creating syslog configuration in outputs.conf.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Sets syslog priority value. The priority value should specified as an integer. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – host:port of the server where syslog data should be sent</p></li>
<li><p><strong>syslog_sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a rule for handling data in addition to that provided by the “syslog” sourcetype. By default, there is no value for syslogSourceType.
<span class="raw-html-m2r"><br></span>This string is used as a substring match against the sourcetype key. For example, if the string is set to ‘syslog’, then all source types containing the string “syslog” receives this special treatment.
To match a source type explicitly, use the pattern “sourcetype::sourcetype_name.” For example
syslogSourcetype = sourcetype::apache_common
Data that is “syslog” or matches this setting is assumed to already be in syslog format.
Data that does not match the rules has a header, potentially a timestamp, and a hostname added to the front of the event. This is how Splunk software causes arbitrary log data to match syslog expectations.</p></li>
<li><p><strong>timestamp_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Format of timestamp to add at start of the events to be forwarded.
The format is a strftime-style timestamp formatting string. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protocol to use to send syslog data. Valid values: (tcp | udp ).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>OutputsTcpSyslogAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OutputsTcpSyslogAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslog_sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timestamp_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.OutputsTcpSyslog" title="pulumi_splunk.OutputsTcpSyslog">OutputsTcpSyslog</a><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing OutputsTcpSyslog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OutputsTcpSyslogAclArgs'</em><em>]</em><em>]</em>) – The app/user context that is the namespace for the resource</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, disables global syslog settings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the syslog output group. This is name used when creating syslog configuration in outputs.conf.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Sets syslog priority value. The priority value should specified as an integer. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – host:port of the server where syslog data should be sent</p></li>
<li><p><strong>syslog_sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a rule for handling data in addition to that provided by the “syslog” sourcetype. By default, there is no value for syslogSourceType.
<span class="raw-html-m2r"><br></span>This string is used as a substring match against the sourcetype key. For example, if the string is set to ‘syslog’, then all source types containing the string “syslog” receives this special treatment.
To match a source type explicitly, use the pattern “sourcetype::sourcetype_name.” For example
syslogSourcetype = sourcetype::apache_common
Data that is “syslog” or matches this setting is assumed to already be in syslog format.
Data that does not match the rules has a header, potentially a timestamp, and a hostname added to the front of the event. This is how Splunk software causes arbitrary log data to match syslog expectations.</p></li>
<li><p><strong>timestamp_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Format of timestamp to add at start of the events to be forwarded.
The format is a strftime-style timestamp formatting string. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protocol to use to send syslog data. Valid values: (tcp | udp ).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.disabled" title="Permalink to this definition"></a></dt>
<dd><p>If true, disables global syslog settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the syslog output group. This is name used when creating syslog configuration in outputs.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.priority" title="Permalink to this definition"></a></dt>
<dd><p>Sets syslog priority value. The priority value should specified as an integer. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.server">
<em class="property">property </em><code class="sig-name descname">server</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.server" title="Permalink to this definition"></a></dt>
<dd><p>host:port of the server where syslog data should be sent</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.syslog_sourcetype">
<em class="property">property </em><code class="sig-name descname">syslog_sourcetype</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.syslog_sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>Specifies a rule for handling data in addition to that provided by the “syslog” sourcetype. By default, there is no value for syslogSourceType.
<span class="raw-html-m2r"><br></span>This string is used as a substring match against the sourcetype key. For example, if the string is set to ‘syslog’, then all source types containing the string “syslog” receives this special treatment.
To match a source type explicitly, use the pattern “sourcetype::sourcetype_name.” For example
syslogSourcetype = sourcetype::apache_common
Data that is “syslog” or matches this setting is assumed to already be in syslog format.
Data that does not match the rules has a header, potentially a timestamp, and a hostname added to the front of the event. This is how Splunk software causes arbitrary log data to match syslog expectations.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.timestamp_format">
<em class="property">property </em><code class="sig-name descname">timestamp_format</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.timestamp_format" title="Permalink to this definition"></a></dt>
<dd><p>Format of timestamp to add at start of the events to be forwarded.
The format is a strftime-style timestamp formatting string. See $SPLUNK_HOME/etc/system/README/outputs.conf.spec for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.type" title="Permalink to this definition"></a></dt>
<dd><p>Protocol to use to send syslog data. Valid values: (tcp | udp ).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.OutputsTcpSyslog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.OutputsTcpSyslog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.OutputsTcpSyslog.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure_skip_verify</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the splunk package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authentication tokens, also known as JSON Web Tokens (JWT), are a method for authenticating Splunk platform users into
the Splunk platform</p></li>
<li><p><strong>insecure_skip_verify</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – insecure skip verification flag</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Splunk instance password</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Timeout when making calls to Splunk server. Defaults to 60 seconds</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Splunk instance URL</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Splunk instance admin username</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.SavedSearches">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_splunk.</code><code class="sig-name descname">SavedSearches</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>SavedSearchesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SavedSearchesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_auth_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_auth_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_bcc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_cc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_from</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_results_link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_trigger_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_view_link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_inline</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_mailserver</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_message_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_message_report</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_pdfview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_preprocess_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_cid_font_list</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_include_splunk_logo</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_paper_orientation</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_paper_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_server_enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_server_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_csv</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_pdf</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_subject</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_to</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_use_ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_use_tls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_width_sort_columns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_dest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_filename</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_attachment</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_channel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_webhook_url_override</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_inline</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_comparator</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_condition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_digest_mode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_expires</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_severity</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_threshold</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_track</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_skew</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_cron_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_earliest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_latest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_time_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_disabled_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_summary_ratio</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_summary_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_suspend_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_timespan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_earliest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_index_earliest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_index_latest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime_minspan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime_offset</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_latest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_lookups</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_max_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_reduce_freq</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_rt_backfill</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_rt_maximum_span</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_spawn_process</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_time_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_view</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_scheduled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_visible</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realtime_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_ui_dispatch_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_ui_dispatch_view</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart_on_searchpeer_add</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_on_startup</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_pool</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.SavedSearches" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>## # Resource: SavedSearches

Create and manage saved searches.

## Example Usage

```python
import pulumi
import pulumi_splunk as splunk

saved_search = splunk.SavedSearches(&quot;savedSearch&quot;,
    acl=splunk.SavedSearchesAclArgs(
        app=&quot;launcher&quot;,
        owner=&quot;admin&quot;,
        sharing=&quot;app&quot;,
    ),
    action_email_format=&quot;table&quot;,
    action_email_max_results=10,
    action_email_max_time=&quot;5m&quot;,
    action_email_send_results=False,
    action_email_subject=&quot;Splunk Alert: $name$&quot;,
    action_email_to=&quot;splunk@splunk.com&quot;,
    action_email_track_alert=True,
    actions=&quot;email&quot;,
    cron_schedule=&quot;*/5 * * * *&quot;,
    dispatch_earliest_time=&quot;rt-15m&quot;,
    dispatch_latest_time=&quot;rt-0m&quot;,
    search=&quot;index=main&quot;)
```

:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[pulumi.InputType[&#39;SavedSearchesAclArgs&#39;]] acl: The app/user context that is the namespace for the resource
:param pulumi.Input[str] action_email_auth_password: The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next platform restart.Defaults to empty string.
:param pulumi.Input[str] action_email_auth_username: The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty stringNOTE: Your SMTP server might reject unauthenticated emails.
:param pulumi.Input[str] action_email_bcc: BCC email address to use if action.email is enabled.
:param pulumi.Input[str] action_email_cc: CC email address to use if action.email is enabled.
:param pulumi.Input[str] action_email_command: The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.
:param pulumi.Input[str] action_email_format: Valid values: (table | plain | html | raw | csv)Specify the format of text in the email. This value also applies to any attachments.
:param pulumi.Input[str] action_email_from: Email address from which the email action originates.Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf.
:param pulumi.Input[str] action_email_hostname: Sets the hostname used in the web link (url) sent in email actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)
:param pulumi.Input[int] action_email_include_results_link: Specify whether to include a link to the results. Defaults to 0.
:param pulumi.Input[int] action_email_include_search: Specify whether to include the search that caused an email to be sent. Defaults to 0.
:param pulumi.Input[int] action_email_include_trigger: Specify whether to show the trigger condition that caused the alert to fire. Defaults to 0.
:param pulumi.Input[int] action_email_include_trigger_time: Specify whether to show the time that the alert was fired. Defaults to 0.
:param pulumi.Input[int] action_email_include_view_link: Specify whether to show the title and a link to enable the user to edit the saved search. Defaults to 0.
:param pulumi.Input[bool] action_email_inline: Indicates whether the search results are contained in the body of the email.Results can be either inline or attached to an email.
:param pulumi.Input[str] action_email_mailserver: Set the address of the MTA server to be used to send the emails.Defaults to &lt;LOCALHOST&gt; or whatever is set in alert_actions.conf.
:param pulumi.Input[int] action_email_max_results: Sets the global maximum number of search results to send when email.action is enabled. Defaults to 100.
:param pulumi.Input[str] action_email_max_time: Valid values are Integer[m|s|h|d].Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.
:param pulumi.Input[str] action_email_message_alert: Customize the message sent in the emailed alert. Defaults to: The alert condition for &#39;$name$&#39; was triggered.
:param pulumi.Input[str] action_email_message_report: Customize the message sent in the emailed report. Defaults to: The scheduled report &#39;$name$&#39; has run
:param pulumi.Input[str] action_email_pdfview: The name of the view to deliver if sendpdf is enabled
:param pulumi.Input[str] action_email_preprocess_results: Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).Usually the preprocessing consists of filtering out unwanted internal fields.
:param pulumi.Input[str] action_email_report_cid_font_list: Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering.If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used.To skip loading any CID fonts, specify the empty string.Defaults to &#39;gb cns jp kor&#39;
:param pulumi.Input[bool] action_email_report_include_splunk_logo: Indicates whether to include the Splunk logo with the report.
:param pulumi.Input[str] action_email_report_paper_orientation: Valid values: (portrait | landscape)Specifies the paper orientation: portrait or landscape. Defaults to portrait.
:param pulumi.Input[str] action_email_report_paper_size: Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5)Specifies the paper size for PDFs. Defaults to letter.
:param pulumi.Input[bool] action_email_report_server_enabled: No Supported
:param pulumi.Input[str] action_email_report_server_url: Not supported.For a default locally installed report server, the URL is http://localhost:8091/
:param pulumi.Input[int] action_email_send_csv: Specify whether to send results as a CSV file. Defaults to 0.
:param pulumi.Input[bool] action_email_send_pdf: Indicates whether to create and send the results as a PDF. Defaults to false.
:param pulumi.Input[bool] action_email_send_results: Indicates whether to attach the search results in the email.Results can be either attached or inline. See action.email.inline.
:param pulumi.Input[str] action_email_subject: Specifies an alternate email subject.Defaults to SplunkAlert-&lt;savedsearchname&gt;.
:param pulumi.Input[str] action_email_to: A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.
:param pulumi.Input[bool] action_email_track_alert: Indicates whether the execution of this action signifies a trackable alert.
:param pulumi.Input[str] action_email_ttl: Valid values are Integer[p].Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows &lt;Integer&gt;, int is the number of scheduled periods. Defaults to 86400 (24 hours).If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.
:param pulumi.Input[bool] action_email_use_ssl: Indicates whether to use SSL when communicating with the SMTP server. Defaults to false.
:param pulumi.Input[bool] action_email_use_tls: Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).Defaults to false.
:param pulumi.Input[bool] action_email_width_sort_columns: Indicates whether columns should be sorted from least wide to most wide, left to right.Only valid if format=text.
:param pulumi.Input[str] action_populate_lookup_command: The search command (or pipeline) which is responsible for executing the action.
:param pulumi.Input[str] action_populate_lookup_dest: Lookup name of path of the lookup to populate
:param pulumi.Input[str] action_populate_lookup_hostname: Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com)
</pre></div>
</div>
<dl class="simple">
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_populate_lookup_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_populate_lookup_max_time</dt>
<dd class="field-even"><p>Valid values are: Integer[m|s|h|d]Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_populate_lookup_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_populate_lookup_ttl</dt>
<dd class="field-even"><p>Valid values are Integer[p]Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_rss_command</dt>
<dd class="field-odd"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_rss_hostname</dt>
<dd class="field-even"><p>Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)</p>
</dd>
</dl>
</dd>
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_rss_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_rss_max_time</dt>
<dd class="field-even"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_rss_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_rss_ttl</dt>
<dd class="field-even"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_script_command</dt>
<dd class="field-odd"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_script_filename</dt>
<dd class="field-even"><p>File name of the script to call. Required if script action is enabled</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_script_hostname</dt>
<dd class="field-odd"><p>Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)</p>
</dd>
</dl>
</dd>
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_script_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_script_max_time</dt>
<dd class="field-even"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_script_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_script_ttl</dt>
<dd class="field-even"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_attachment</dt>
<dd class="field-odd"><p>Include a message attachment. Valid values are message, none, or alert_link</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_slack_param_channel</dt>
<dd class="field-even"><p>Slack channel to send the message to (Should start with # or &#64;)</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_fields</dt>
<dd class="field-odd"><p>Show one or more fields from the search results below your Slack message. Comma-separated list of field names. Allows wildcards. eg. index,source*</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_slack_param_message</dt>
<dd class="field-even"><p>Enter the chat message to send to the Slack channel. The message can include tokens that insert text based on the results of the search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_webhook_url_override</dt>
<dd class="field-odd"><p>You can override the Slack webhook URL here if you need to send the alert message to a different Slack team</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_summary_index_command</dt>
<dd class="field-even"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_summary_index_hostname</dt>
<dd class="field-odd"><p>Sets the hostname used in the web link (url) sent in summary-index alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] action_summary_index_inline</dt>
<dd class="field-even"><p>Determines whether to execute the summary indexing action as part of the scheduled search.NOTE: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always).Defaults to true</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] action_summary_index_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_summary_index_max_time</dt>
<dd class="field-even"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_summary_index_name</dt>
<dd class="field-odd"><p>Specifies the name of the summary index where the results of the scheduled search are saved.Defaults to summary.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] action_summary_index_track_alert</dt>
<dd class="field-even"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_summary_index_ttl</dt>
<dd class="field-odd"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-even">param pulumi.Input[str] actions</dt>
<dd class="field-even"><p>A comma-separated list of actions to enable. For example: rss,email</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_comparator</dt>
<dd class="field-odd"><p>One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by percUsed with alert_threshold to trigger alert actions.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_condition</dt>
<dd class="field-even"><p>Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] alert_digest_mode</dt>
<dd class="field-odd"><p>Specifies whether alert actions are applied to the entire result set or on each individual result.Defaults to 1 (true).</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_expires</dt>
<dd class="field-even"><p>Valid values: [number][time-unit]Sets the period of time to show the alert in the dashboard. Defaults to 24h.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] alert_severity</dt>
<dd class="field-odd"><p>Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level.Valid values are:1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL Defaults to 3.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] alert_suppress</dt>
<dd class="field-even"><p>Indicates whether alert suppression is enabled for this scheduled search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_suppress_fields</dt>
<dd class="field-odd"><p>Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_suppress_period</dt>
<dd class="field-even"><p>Valid values: [number][time-unit] Specifies the suppresion period. Only valid if alert.supress is enabled.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_threshold</dt>
<dd class="field-odd"><p>Valid values are: Integer[%]Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc or drops by perc.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_track</dt>
<dd class="field-even"><p>Valid values: (true | false | auto) Specifies whether to track the actions triggered by this scheduled search.auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. Default value true - force alert tracking.false - disable alert tracking for this search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_type</dt>
<dd class="field-odd"><p>What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] allow_skew</dt>
<dd class="field-even"><p>Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] auto_summarize</dt>
<dd class="field-odd"><p>Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_command</dt>
<dd class="field-even"><p>An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_cron_schedule</dt>
<dd class="field-odd"><p>Cron schedule that probes and generates the summaries for this saved search.The default value is <a href="#id7"><span class="problematic" id="id8">*</span></a>/10 * * * * and corresponds to <cite>every ten hours</cite>.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_dispatch_earliest_time</dt>
<dd class="field-even"><p>A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_dispatch_latest_time</dt>
<dd class="field-odd"><p>A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_dispatch_time_format</dt>
<dd class="field-even"><p>Defines the time format that Splunk software uses to specify the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_dispatch_ttl</dt>
<dd class="field-odd"><p>Valid values: Integer[p]. Defaults to 60.Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] auto_summarize_max_disabled_buckets</dt>
<dd class="field-even"><p>The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2.</p>
</dd>
<dt class="field-odd">param pulumi.Input[float] auto_summarize_max_summary_ratio</dt>
<dd class="field-odd"><p>The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1 Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] auto_summarize_max_summary_size</dt>
<dd class="field-even"><p>The minimum summary size, in bytes, before testing whether the summarization is helpful.The default value is 52428800 and is equivalent to 5MB.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] auto_summarize_max_time</dt>
<dd class="field-odd"><p>Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600.Note: This is an approximate time. The summary search stops at clean bucket boundaries.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_suspend_period</dt>
<dd class="field-even"><p>Time specfier indicating when to suspend summarization of this search if the summarization is deemed unhelpful.Defaults to 24h.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_timespan</dt>
<dd class="field-odd"><p>The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. Specify a comma delimited list of time specifiers.For example a timechart over the last month whose granuality is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] cron_schedule</dt>
<dd class="field-even"><p>Valid values: cron stringThe cron schedule to execute this search. For example: <a href="#id9"><span class="problematic" id="id10">*</span></a>/5 * * * * causes the search to execute every 5 minutes.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] description</dt>
<dd class="field-odd"><p>Human-readable description of this saved search. Defaults to empty string.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] disabled</dt>
<dd class="field-even"><p>Indicates if the saved search is enabled. Defaults to 0.Disabled saved searches are not visible in Splunk Web.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_buckets</dt>
<dd class="field-odd"><p>The maximum number of timeline buckets. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_earliest_time</dt>
<dd class="field-even"><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_index_earliest</dt>
<dd class="field-odd"><p>A time string that specifies the earliest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_index_latest</dt>
<dd class="field-even"><p>A time string that specifies the latest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] dispatch_indexed_realtime</dt>
<dd class="field-odd"><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_indexed_realtime_minspan</dt>
<dd class="field-even"><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_indexed_realtime_offset</dt>
<dd class="field-odd"><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_latest_time</dt>
<dd class="field-even"><p>A time string that specifies the latest time for this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] dispatch_lookups</dt>
<dd class="field-odd"><p>Enables or disables the lookups for this search. Defaults to 1.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_max_count</dt>
<dd class="field-even"><p>The maximum number of results before finalizing the search. Defaults to 500000.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_max_time</dt>
<dd class="field-odd"><p>Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_reduce_freq</dt>
<dd class="field-even"><p>Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] dispatch_rt_backfill</dt>
<dd class="field-odd"><p>Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_rt_maximum_span</dt>
<dd class="field-even"><p>Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] dispatch_spawn_process</dt>
<dd class="field-odd"><p>Specifies whether a new search process spawns when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_time_format</dt>
<dd class="field-even"><p>A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_ttl</dt>
<dd class="field-odd"><p>Valid values: Integer[p]. Defaults to 2p.Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] display_view</dt>
<dd class="field-even"><p>Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] is_scheduled</dt>
<dd class="field-odd"><p>Whether this search is to be run on a schedule</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] is_visible</dt>
<dd class="field-even"><p>Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] max_concurrent</dt>
<dd class="field-odd"><p>The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] name</dt>
<dd class="field-even"><p>A name for the search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] realtime_schedule</dt>
<dd class="field-odd"><p>Defaults to 1. Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] request_ui_dispatch_app</dt>
<dd class="field-even"><p>Specifies a field used by Splunk Web to denote the app this search should be dispatched in.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] request_ui_dispatch_view</dt>
<dd class="field-odd"><p>Specifies a field used by Splunk Web to denote the view this search should be displayed in.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] restart_on_searchpeer_add</dt>
<dd class="field-even"><p>Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] run_on_startup</dt>
<dd class="field-odd"><p>Indicates whether this search runs at startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set to 1 for scheduled searches that populate lookup tables.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] schedule_priority</dt>
<dd class="field-even"><p>Raises the scheduling priority of the named search. Defaults to Default</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] schedule_window</dt>
<dd class="field-odd"><p>Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period.Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] search</dt>
<dd class="field-even"><p>Required when creating a new search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] vsid</dt>
<dd class="field-odd"><p>Defines the viewstate id associated with the UI view listed in ‘displayview’.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] workload_pool</dt>
<dd class="field-even"><p>Specifies the new workload pool where the existing running search will be placed.`</p>
</dd>
</dl>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>SavedSearchesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SavedSearchesAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_auth_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_auth_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_bcc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_cc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_from</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_results_link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_trigger</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_trigger_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_include_view_link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_inline</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_mailserver</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_message_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_message_report</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_pdfview</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_preprocess_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_cid_font_list</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_include_splunk_logo</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_paper_orientation</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_paper_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_server_enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_report_server_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_csv</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_pdf</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_send_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_subject</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_to</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_use_ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_use_tls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_email_width_sort_columns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_dest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_populate_lookup_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_rss_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_filename</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_script_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_attachment</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_channel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_slack_param_webhook_url_override</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_inline</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_max_results</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_track_alert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_summary_index_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_comparator</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_condition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_digest_mode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_expires</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_severity</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_suppress_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_threshold</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_track</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_skew</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_command</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_cron_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_earliest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_latest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_time_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_dispatch_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_disabled_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_summary_ratio</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_summary_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_suspend_period</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_summarize_timespan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_buckets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_earliest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_index_earliest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_index_latest</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime_minspan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_indexed_realtime_offset</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_latest_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_lookups</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_max_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_max_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_reduce_freq</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_rt_backfill</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_rt_maximum_span</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_spawn_process</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_time_format</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dispatch_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_view</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_scheduled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_visible</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realtime_schedule</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_ui_dispatch_app</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_ui_dispatch_view</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart_on_searchpeer_add</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_on_startup</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vsid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_pool</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_splunk.SavedSearches" title="pulumi_splunk.SavedSearches">SavedSearches</a><a class="headerlink" href="#pulumi_splunk.SavedSearches.get" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Get an existing SavedSearches resource&#39;s state with the given name, id, and optional extra
properties used to qualify the lookup.

:param str resource_name: The unique name of the resulting resource.
:param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[pulumi.InputType[&#39;SavedSearchesAclArgs&#39;]] acl: The app/user context that is the namespace for the resource
:param pulumi.Input[bool] action_email: The state of the email action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
:param pulumi.Input[str] action_email_auth_password: The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next platform restart.Defaults to empty string.
:param pulumi.Input[str] action_email_auth_username: The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty stringNOTE: Your SMTP server might reject unauthenticated emails.
:param pulumi.Input[str] action_email_bcc: BCC email address to use if action.email is enabled.
:param pulumi.Input[str] action_email_cc: CC email address to use if action.email is enabled.
:param pulumi.Input[str] action_email_command: The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.
:param pulumi.Input[str] action_email_format: Valid values: (table | plain | html | raw | csv)Specify the format of text in the email. This value also applies to any attachments.
:param pulumi.Input[str] action_email_from: Email address from which the email action originates.Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf.
:param pulumi.Input[str] action_email_hostname: Sets the hostname used in the web link (url) sent in email actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)
:param pulumi.Input[int] action_email_include_results_link: Specify whether to include a link to the results. Defaults to 0.
:param pulumi.Input[int] action_email_include_search: Specify whether to include the search that caused an email to be sent. Defaults to 0.
:param pulumi.Input[int] action_email_include_trigger: Specify whether to show the trigger condition that caused the alert to fire. Defaults to 0.
:param pulumi.Input[int] action_email_include_trigger_time: Specify whether to show the time that the alert was fired. Defaults to 0.
:param pulumi.Input[int] action_email_include_view_link: Specify whether to show the title and a link to enable the user to edit the saved search. Defaults to 0.
:param pulumi.Input[bool] action_email_inline: Indicates whether the search results are contained in the body of the email.Results can be either inline or attached to an email.
:param pulumi.Input[str] action_email_mailserver: Set the address of the MTA server to be used to send the emails.Defaults to &lt;LOCALHOST&gt; or whatever is set in alert_actions.conf.
:param pulumi.Input[int] action_email_max_results: Sets the global maximum number of search results to send when email.action is enabled. Defaults to 100.
:param pulumi.Input[str] action_email_max_time: Valid values are Integer[m|s|h|d].Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.
:param pulumi.Input[str] action_email_message_alert: Customize the message sent in the emailed alert. Defaults to: The alert condition for &#39;$name$&#39; was triggered.
:param pulumi.Input[str] action_email_message_report: Customize the message sent in the emailed report. Defaults to: The scheduled report &#39;$name$&#39; has run
:param pulumi.Input[str] action_email_pdfview: The name of the view to deliver if sendpdf is enabled
:param pulumi.Input[str] action_email_preprocess_results: Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).Usually the preprocessing consists of filtering out unwanted internal fields.
:param pulumi.Input[str] action_email_report_cid_font_list: Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering.If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used.To skip loading any CID fonts, specify the empty string.Defaults to &#39;gb cns jp kor&#39;
:param pulumi.Input[bool] action_email_report_include_splunk_logo: Indicates whether to include the Splunk logo with the report.
:param pulumi.Input[str] action_email_report_paper_orientation: Valid values: (portrait | landscape)Specifies the paper orientation: portrait or landscape. Defaults to portrait.
:param pulumi.Input[str] action_email_report_paper_size: Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5)Specifies the paper size for PDFs. Defaults to letter.
:param pulumi.Input[bool] action_email_report_server_enabled: No Supported
:param pulumi.Input[str] action_email_report_server_url: Not supported.For a default locally installed report server, the URL is http://localhost:8091/
:param pulumi.Input[int] action_email_send_csv: Specify whether to send results as a CSV file. Defaults to 0.
:param pulumi.Input[bool] action_email_send_pdf: Indicates whether to create and send the results as a PDF. Defaults to false.
:param pulumi.Input[bool] action_email_send_results: Indicates whether to attach the search results in the email.Results can be either attached or inline. See action.email.inline.
:param pulumi.Input[str] action_email_subject: Specifies an alternate email subject.Defaults to SplunkAlert-&lt;savedsearchname&gt;.
:param pulumi.Input[str] action_email_to: A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.
:param pulumi.Input[bool] action_email_track_alert: Indicates whether the execution of this action signifies a trackable alert.
:param pulumi.Input[str] action_email_ttl: Valid values are Integer[p].Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows &lt;Integer&gt;, int is the number of scheduled periods. Defaults to 86400 (24 hours).If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.
:param pulumi.Input[bool] action_email_use_ssl: Indicates whether to use SSL when communicating with the SMTP server. Defaults to false.
:param pulumi.Input[bool] action_email_use_tls: Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).Defaults to false.
:param pulumi.Input[bool] action_email_width_sort_columns: Indicates whether columns should be sorted from least wide to most wide, left to right.Only valid if format=text.
:param pulumi.Input[bool] action_populate_lookup: The state of the populate lookup action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
:param pulumi.Input[str] action_populate_lookup_command: The search command (or pipeline) which is responsible for executing the action.
:param pulumi.Input[str] action_populate_lookup_dest: Lookup name of path of the lookup to populate
:param pulumi.Input[str] action_populate_lookup_hostname: Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com)
</pre></div>
</div>
<dl class="simple">
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_populate_lookup_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_populate_lookup_max_time</dt>
<dd class="field-even"><p>Valid values are: Integer[m|s|h|d]Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_populate_lookup_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_populate_lookup_ttl</dt>
<dd class="field-even"><p>Valid values are Integer[p]Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_rss</dt>
<dd class="field-odd"><p>The state of the rss action. Read-only attribute. Value ignored on POST.Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_rss_command</dt>
<dd class="field-even"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_rss_hostname</dt>
<dd class="field-odd"><p>Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)</p>
</dd>
</dl>
</dd>
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_rss_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_rss_max_time</dt>
<dd class="field-even"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_rss_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_rss_ttl</dt>
<dd class="field-even"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_script</dt>
<dd class="field-odd"><p>The state of the script action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_script_command</dt>
<dd class="field-even"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_script_filename</dt>
<dd class="field-odd"><p>File name of the script to call. Required if script action is enabled</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_script_hostname</dt>
<dd class="field-even"><p>Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)</p>
</dd>
</dl>
</dd>
<dt>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</dt><dd><dl class="field-list simple">
<dt class="field-odd">param pulumi.Input[int] action_script_max_results</dt>
<dd class="field-odd"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_script_max_time</dt>
<dd class="field-even"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_script_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_script_ttl</dt>
<dd class="field-even"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_attachment</dt>
<dd class="field-odd"><p>Include a message attachment. Valid values are message, none, or alert_link</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_slack_param_channel</dt>
<dd class="field-even"><p>Slack channel to send the message to (Should start with # or &#64;)</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_fields</dt>
<dd class="field-odd"><p>Show one or more fields from the search results below your Slack message. Comma-separated list of field names. Allows wildcards. eg. index,source*</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_slack_param_message</dt>
<dd class="field-even"><p>Enter the chat message to send to the Slack channel. The message can include tokens that insert text based on the results of the search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_slack_param_webhook_url_override</dt>
<dd class="field-odd"><p>You can override the Slack webhook URL here if you need to send the alert message to a different Slack team</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] action_summary_index</dt>
<dd class="field-even"><p>The state of the summary index action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] action_summary_index_command</dt>
<dd class="field-odd"><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_summary_index_hostname</dt>
<dd class="field-even"><p>Sets the hostname used in the web link (url) sent in summary-index alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_summary_index_inline</dt>
<dd class="field-odd"><p>Determines whether to execute the summary indexing action as part of the scheduled search.NOTE: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always).Defaults to true</p>
</dd>
<dt class="field-even">param pulumi.Input[int] action_summary_index_max_results</dt>
<dd class="field-even"><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] action_summary_index_max_time</dt>
<dd class="field-odd"><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_summary_index_name</dt>
<dd class="field-even"><p>Specifies the name of the summary index where the results of the scheduled search are saved.Defaults to summary.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] action_summary_index_track_alert</dt>
<dd class="field-odd"><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] action_summary_index_ttl</dt>
<dd class="field-even"><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] actions</dt>
<dd class="field-odd"><p>A comma-separated list of actions to enable. For example: rss,email</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_comparator</dt>
<dd class="field-even"><p>One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by percUsed with alert_threshold to trigger alert actions.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_condition</dt>
<dd class="field-odd"><p>Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] alert_digest_mode</dt>
<dd class="field-even"><p>Specifies whether alert actions are applied to the entire result set or on each individual result.Defaults to 1 (true).</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_expires</dt>
<dd class="field-odd"><p>Valid values: [number][time-unit]Sets the period of time to show the alert in the dashboard. Defaults to 24h.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] alert_severity</dt>
<dd class="field-even"><p>Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level.Valid values are:1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL Defaults to 3.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] alert_suppress</dt>
<dd class="field-odd"><p>Indicates whether alert suppression is enabled for this scheduled search.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_suppress_fields</dt>
<dd class="field-even"><p>Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_suppress_period</dt>
<dd class="field-odd"><p>Valid values: [number][time-unit] Specifies the suppresion period. Only valid if alert.supress is enabled.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_threshold</dt>
<dd class="field-even"><p>Valid values are: Integer[%]Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc or drops by perc.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] alert_track</dt>
<dd class="field-odd"><p>Valid values: (true | false | auto) Specifies whether to track the actions triggered by this scheduled search.auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. Default value true - force alert tracking.false - disable alert tracking for this search.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] alert_type</dt>
<dd class="field-even"><p>What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] allow_skew</dt>
<dd class="field-odd"><p>Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] auto_summarize</dt>
<dd class="field-even"><p>Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_command</dt>
<dd class="field-odd"><p>An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_cron_schedule</dt>
<dd class="field-even"><p>Cron schedule that probes and generates the summaries for this saved search.The default value is <a href="#id11"><span class="problematic" id="id12">*</span></a>/10 * * * * and corresponds to <cite>every ten hours</cite>.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_dispatch_earliest_time</dt>
<dd class="field-odd"><p>A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_dispatch_latest_time</dt>
<dd class="field-even"><p>A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_dispatch_time_format</dt>
<dd class="field-odd"><p>Defines the time format that Splunk software uses to specify the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_dispatch_ttl</dt>
<dd class="field-even"><p>Valid values: Integer[p]. Defaults to 60.Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] auto_summarize_max_disabled_buckets</dt>
<dd class="field-odd"><p>The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2.</p>
</dd>
<dt class="field-even">param pulumi.Input[float] auto_summarize_max_summary_ratio</dt>
<dd class="field-even"><p>The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1 Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] auto_summarize_max_summary_size</dt>
<dd class="field-odd"><p>The minimum summary size, in bytes, before testing whether the summarization is helpful.The default value is 52428800 and is equivalent to 5MB.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] auto_summarize_max_time</dt>
<dd class="field-even"><p>Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600.Note: This is an approximate time. The summary search stops at clean bucket boundaries.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] auto_summarize_suspend_period</dt>
<dd class="field-odd"><p>Time specfier indicating when to suspend summarization of this search if the summarization is deemed unhelpful.Defaults to 24h.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] auto_summarize_timespan</dt>
<dd class="field-even"><p>The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. Specify a comma delimited list of time specifiers.For example a timechart over the last month whose granuality is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] cron_schedule</dt>
<dd class="field-odd"><p>Valid values: cron stringThe cron schedule to execute this search. For example: <a href="#id13"><span class="problematic" id="id14">*</span></a>/5 * * * * causes the search to execute every 5 minutes.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] description</dt>
<dd class="field-even"><p>Human-readable description of this saved search. Defaults to empty string.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] disabled</dt>
<dd class="field-odd"><p>Indicates if the saved search is enabled. Defaults to 0.Disabled saved searches are not visible in Splunk Web.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_buckets</dt>
<dd class="field-even"><p>The maximum number of timeline buckets. Defaults to 0.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_earliest_time</dt>
<dd class="field-odd"><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_index_earliest</dt>
<dd class="field-even"><p>A time string that specifies the earliest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_index_latest</dt>
<dd class="field-odd"><p>A time string that specifies the latest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] dispatch_indexed_realtime</dt>
<dd class="field-even"><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_indexed_realtime_minspan</dt>
<dd class="field-odd"><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_indexed_realtime_offset</dt>
<dd class="field-even"><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_latest_time</dt>
<dd class="field-odd"><p>A time string that specifies the latest time for this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] dispatch_lookups</dt>
<dd class="field-even"><p>Enables or disables the lookups for this search. Defaults to 1.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_max_count</dt>
<dd class="field-odd"><p>The maximum number of results before finalizing the search. Defaults to 500000.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] dispatch_max_time</dt>
<dd class="field-even"><p>Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_reduce_freq</dt>
<dd class="field-odd"><p>Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] dispatch_rt_backfill</dt>
<dd class="field-even"><p>Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0.</p>
</dd>
<dt class="field-odd">param pulumi.Input[int] dispatch_rt_maximum_span</dt>
<dd class="field-odd"><p>Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] dispatch_spawn_process</dt>
<dd class="field-even"><p>Specifies whether a new search process spawns when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] dispatch_time_format</dt>
<dd class="field-odd"><p>A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd>
<dt class="field-even">param pulumi.Input[str] dispatch_ttl</dt>
<dd class="field-even"><p>Valid values: Integer[p]. Defaults to 2p.Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] display_view</dt>
<dd class="field-odd"><p>Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] is_scheduled</dt>
<dd class="field-even"><p>Whether this search is to be run on a schedule</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] is_visible</dt>
<dd class="field-odd"><p>Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1.</p>
</dd>
<dt class="field-even">param pulumi.Input[int] max_concurrent</dt>
<dd class="field-even"><p>The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] name</dt>
<dd class="field-odd"><p>A name for the search.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] realtime_schedule</dt>
<dd class="field-even"><p>Defaults to 1. Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] request_ui_dispatch_app</dt>
<dd class="field-odd"><p>Specifies a field used by Splunk Web to denote the app this search should be dispatched in.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] request_ui_dispatch_view</dt>
<dd class="field-even"><p>Specifies a field used by Splunk Web to denote the view this search should be displayed in.</p>
</dd>
<dt class="field-odd">param pulumi.Input[bool] restart_on_searchpeer_add</dt>
<dd class="field-odd"><p>Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1.</p>
</dd>
<dt class="field-even">param pulumi.Input[bool] run_on_startup</dt>
<dd class="field-even"><p>Indicates whether this search runs at startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set to 1 for scheduled searches that populate lookup tables.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] schedule_priority</dt>
<dd class="field-odd"><p>Raises the scheduling priority of the named search. Defaults to Default</p>
</dd>
<dt class="field-even">param pulumi.Input[str] schedule_window</dt>
<dd class="field-even"><p>Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period.Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] search</dt>
<dd class="field-odd"><p>Required when creating a new search.</p>
</dd>
<dt class="field-even">param pulumi.Input[str] vsid</dt>
<dd class="field-even"><p>Defines the viewstate id associated with the UI view listed in ‘displayview’.</p>
</dd>
<dt class="field-odd">param pulumi.Input[str] workload_pool</dt>
<dd class="field-odd"><p>Specifies the new workload pool where the existing running search will be placed.`</p>
</dd>
</dl>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.acl" title="Permalink to this definition"></a></dt>
<dd><p>The app/user context that is the namespace for the resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email">
<em class="property">property </em><code class="sig-name descname">action_email</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email" title="Permalink to this definition"></a></dt>
<dd><p>The state of the email action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_auth_password">
<em class="property">property </em><code class="sig-name descname">action_email_auth_password</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_auth_password" title="Permalink to this definition"></a></dt>
<dd><p>The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next platform restart.Defaults to empty string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_auth_username">
<em class="property">property </em><code class="sig-name descname">action_email_auth_username</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_auth_username" title="Permalink to this definition"></a></dt>
<dd><p>The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty stringNOTE: Your SMTP server might reject unauthenticated emails.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_bcc">
<em class="property">property </em><code class="sig-name descname">action_email_bcc</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_bcc" title="Permalink to this definition"></a></dt>
<dd><p>BCC email address to use if action.email is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_cc">
<em class="property">property </em><code class="sig-name descname">action_email_cc</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_cc" title="Permalink to this definition"></a></dt>
<dd><p>CC email address to use if action.email is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_command">
<em class="property">property </em><code class="sig-name descname">action_email_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_command" title="Permalink to this definition"></a></dt>
<dd><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_format">
<em class="property">property </em><code class="sig-name descname">action_email_format</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_format" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (table | plain | html | raw | csv)Specify the format of text in the email. This value also applies to any attachments.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_from">
<em class="property">property </em><code class="sig-name descname">action_email_from</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_from" title="Permalink to this definition"></a></dt>
<dd><p>Email address from which the email action originates.Defaults to <a class="reference external" href="mailto:splunk&#37;&#52;&#48;$LOCALHOST">splunk<span>&#64;</span>$LOCALHOST</a> or whatever value is set in alert_actions.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_hostname">
<em class="property">property </em><code class="sig-name descname">action_email_hostname</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_hostname" title="Permalink to this definition"></a></dt>
<dd><p>Sets the hostname used in the web link (url) sent in email actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_include_results_link">
<em class="property">property </em><code class="sig-name descname">action_email_include_results_link</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_include_results_link" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to include a link to the results. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_include_search">
<em class="property">property </em><code class="sig-name descname">action_email_include_search</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_include_search" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to include the search that caused an email to be sent. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_include_trigger">
<em class="property">property </em><code class="sig-name descname">action_email_include_trigger</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_include_trigger" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to show the trigger condition that caused the alert to fire. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_include_trigger_time">
<em class="property">property </em><code class="sig-name descname">action_email_include_trigger_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_include_trigger_time" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to show the time that the alert was fired. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_include_view_link">
<em class="property">property </em><code class="sig-name descname">action_email_include_view_link</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_include_view_link" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to show the title and a link to enable the user to edit the saved search. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_inline">
<em class="property">property </em><code class="sig-name descname">action_email_inline</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_inline" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the search results are contained in the body of the email.Results can be either inline or attached to an email.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_mailserver">
<em class="property">property </em><code class="sig-name descname">action_email_mailserver</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_mailserver" title="Permalink to this definition"></a></dt>
<dd><p>Set the address of the MTA server to be used to send the emails.Defaults to <span class="raw-html-m2r"><LOCALHOST></span> or whatever is set in alert_actions.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_max_results">
<em class="property">property </em><code class="sig-name descname">action_email_max_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_max_results" title="Permalink to this definition"></a></dt>
<dd><p>Sets the global maximum number of search results to send when email.action is enabled. Defaults to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_max_time">
<em class="property">property </em><code class="sig-name descname">action_email_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[m|s|h|d].Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_message_alert">
<em class="property">property </em><code class="sig-name descname">action_email_message_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_message_alert" title="Permalink to this definition"></a></dt>
<dd><p>Customize the message sent in the emailed alert. Defaults to: The alert condition for ‘$name$’ was triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_message_report">
<em class="property">property </em><code class="sig-name descname">action_email_message_report</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_message_report" title="Permalink to this definition"></a></dt>
<dd><p>Customize the message sent in the emailed report. Defaults to: The scheduled report ‘$name$’ has run</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_pdfview">
<em class="property">property </em><code class="sig-name descname">action_email_pdfview</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_pdfview" title="Permalink to this definition"></a></dt>
<dd><p>The name of the view to deliver if sendpdf is enabled</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_preprocess_results">
<em class="property">property </em><code class="sig-name descname">action_email_preprocess_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_preprocess_results" title="Permalink to this definition"></a></dt>
<dd><p>Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).Usually the preprocessing consists of filtering out unwanted internal fields.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_cid_font_list">
<em class="property">property </em><code class="sig-name descname">action_email_report_cid_font_list</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_cid_font_list" title="Permalink to this definition"></a></dt>
<dd><p>Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering.If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used.To skip loading any CID fonts, specify the empty string.Defaults to ‘gb cns jp kor’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_include_splunk_logo">
<em class="property">property </em><code class="sig-name descname">action_email_report_include_splunk_logo</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_include_splunk_logo" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to include the Splunk logo with the report.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_paper_orientation">
<em class="property">property </em><code class="sig-name descname">action_email_report_paper_orientation</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_paper_orientation" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (portrait | landscape)Specifies the paper orientation: portrait or landscape. Defaults to portrait.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_paper_size">
<em class="property">property </em><code class="sig-name descname">action_email_report_paper_size</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_paper_size" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5)Specifies the paper size for PDFs. Defaults to letter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_server_enabled">
<em class="property">property </em><code class="sig-name descname">action_email_report_server_enabled</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_server_enabled" title="Permalink to this definition"></a></dt>
<dd><p>No Supported</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_report_server_url">
<em class="property">property </em><code class="sig-name descname">action_email_report_server_url</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_report_server_url" title="Permalink to this definition"></a></dt>
<dd><p>Not supported.For a default locally installed report server, the URL is <a class="reference external" href="http://localhost:8091/">http://localhost:8091/</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_send_csv">
<em class="property">property </em><code class="sig-name descname">action_email_send_csv</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_send_csv" title="Permalink to this definition"></a></dt>
<dd><p>Specify whether to send results as a CSV file. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_send_pdf">
<em class="property">property </em><code class="sig-name descname">action_email_send_pdf</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_send_pdf" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to create and send the results as a PDF. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_send_results">
<em class="property">property </em><code class="sig-name descname">action_email_send_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_send_results" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to attach the search results in the email.Results can be either attached or inline. See action.email.inline.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_subject">
<em class="property">property </em><code class="sig-name descname">action_email_subject</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_subject" title="Permalink to this definition"></a></dt>
<dd><p>Specifies an alternate email subject.Defaults to SplunkAlert-<span class="raw-html-m2r"><savedsearchname></span>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_to">
<em class="property">property </em><code class="sig-name descname">action_email_to</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_to" title="Permalink to this definition"></a></dt>
<dd><p>A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_track_alert">
<em class="property">property </em><code class="sig-name descname">action_email_track_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_track_alert" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_ttl">
<em class="property">property </em><code class="sig-name descname">action_email_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[p].Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <span class="raw-html-m2r"><Integer></span>, int is the number of scheduled periods. Defaults to 86400 (24 hours).If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_use_ssl">
<em class="property">property </em><code class="sig-name descname">action_email_use_ssl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_use_ssl" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to use SSL when communicating with the SMTP server. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_use_tls">
<em class="property">property </em><code class="sig-name descname">action_email_use_tls</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_use_tls" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_email_width_sort_columns">
<em class="property">property </em><code class="sig-name descname">action_email_width_sort_columns</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_email_width_sort_columns" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether columns should be sorted from least wide to most wide, left to right.Only valid if format=text.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup" title="Permalink to this definition"></a></dt>
<dd><p>The state of the populate lookup action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_command">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_command" title="Permalink to this definition"></a></dt>
<dd><p>The search command (or pipeline) which is responsible for executing the action.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_dest">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_dest</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_dest" title="Permalink to this definition"></a></dt>
<dd><p>Lookup name of path of the lookup to populate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_hostname">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_hostname</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_hostname" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Sets</span> <span class="n">the</span> <span class="n">hostname</span> <span class="n">used</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">web</span> <span class="n">link</span> <span class="p">(</span><span class="n">url</span><span class="p">)</span> <span class="n">sent</span> <span class="ow">in</span> <span class="n">alert</span> <span class="n">actions</span><span class="o">.</span><span class="n">This</span> <span class="n">value</span> <span class="n">accepts</span> <span class="n">two</span> <span class="n">forms</span><span class="p">:</span> <span class="n">hostname</span> <span class="p">(</span><span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">splunkserver</span><span class="p">,</span> <span class="n">splunkserver</span><span class="o">.</span><span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="p">)</span>
</pre></div>
</div>
<p>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_max_results">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_max_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_max_results" title="Permalink to this definition"></a></dt>
<dd><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_max_time">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[m|s|h|d]Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_track_alert">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_track_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_track_alert" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_populate_lookup_ttl">
<em class="property">property </em><code class="sig-name descname">action_populate_lookup_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_populate_lookup_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[p]Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss">
<em class="property">property </em><code class="sig-name descname">action_rss</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss" title="Permalink to this definition"></a></dt>
<dd><p>The state of the rss action. Read-only attribute. Value ignored on POST.Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_command">
<em class="property">property </em><code class="sig-name descname">action_rss_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_command" title="Permalink to this definition"></a></dt>
<dd><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_hostname">
<em class="property">property </em><code class="sig-name descname">action_rss_hostname</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_hostname" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Sets</span> <span class="n">the</span> <span class="n">hostname</span> <span class="n">used</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">web</span> <span class="n">link</span> <span class="p">(</span><span class="n">url</span><span class="p">)</span> <span class="n">sent</span> <span class="ow">in</span> <span class="n">alert</span> <span class="n">actions</span><span class="o">.</span><span class="n">This</span> <span class="n">value</span> <span class="n">accepts</span> <span class="n">two</span> <span class="n">forms</span><span class="p">:</span><span class="n">hostname</span> <span class="p">(</span><span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">splunkserver</span><span class="p">,</span> <span class="n">splunkserver</span><span class="o">.</span><span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="p">)</span>
</pre></div>
</div>
<p>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_max_results">
<em class="property">property </em><code class="sig-name descname">action_rss_max_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_max_results" title="Permalink to this definition"></a></dt>
<dd><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_max_time">
<em class="property">property </em><code class="sig-name descname">action_rss_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_track_alert">
<em class="property">property </em><code class="sig-name descname">action_rss_track_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_track_alert" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_rss_ttl">
<em class="property">property </em><code class="sig-name descname">action_rss_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_rss_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script">
<em class="property">property </em><code class="sig-name descname">action_script</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script" title="Permalink to this definition"></a></dt>
<dd><p>The state of the script action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_command">
<em class="property">property </em><code class="sig-name descname">action_script_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_command" title="Permalink to this definition"></a></dt>
<dd><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_filename">
<em class="property">property </em><code class="sig-name descname">action_script_filename</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_filename" title="Permalink to this definition"></a></dt>
<dd><p>File name of the script to call. Required if script action is enabled</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_hostname">
<em class="property">property </em><code class="sig-name descname">action_script_hostname</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_hostname" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Sets</span> <span class="n">the</span> <span class="n">hostname</span> <span class="n">used</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">web</span> <span class="n">link</span> <span class="p">(</span><span class="n">url</span><span class="p">)</span> <span class="n">sent</span> <span class="ow">in</span> <span class="n">alert</span> <span class="n">actions</span><span class="o">.</span><span class="n">This</span> <span class="n">value</span> <span class="n">accepts</span> <span class="n">two</span> <span class="n">forms</span><span class="p">:</span><span class="n">hostname</span> <span class="p">(</span><span class="k">for</span> <span class="n">example</span><span class="p">,</span> <span class="n">splunkserver</span><span class="p">,</span> <span class="n">splunkserver</span><span class="o">.</span><span class="n">example</span><span class="o">.</span><span class="n">com</span><span class="p">)</span>
</pre></div>
</div>
<p>protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_max_results">
<em class="property">property </em><code class="sig-name descname">action_script_max_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_max_results" title="Permalink to this definition"></a></dt>
<dd><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_max_time">
<em class="property">property </em><code class="sig-name descname">action_script_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_track_alert">
<em class="property">property </em><code class="sig-name descname">action_script_track_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_track_alert" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_script_ttl">
<em class="property">property </em><code class="sig-name descname">action_script_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_script_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_slack_param_attachment">
<em class="property">property </em><code class="sig-name descname">action_slack_param_attachment</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_slack_param_attachment" title="Permalink to this definition"></a></dt>
<dd><p>Include a message attachment. Valid values are message, none, or alert_link</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_slack_param_channel">
<em class="property">property </em><code class="sig-name descname">action_slack_param_channel</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_slack_param_channel" title="Permalink to this definition"></a></dt>
<dd><p>Slack channel to send the message to (Should start with # or &#64;)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_slack_param_fields">
<em class="property">property </em><code class="sig-name descname">action_slack_param_fields</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_slack_param_fields" title="Permalink to this definition"></a></dt>
<dd><p>Show one or more fields from the search results below your Slack message. Comma-separated list of field names. Allows wildcards. eg. index,source*</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_slack_param_message">
<em class="property">property </em><code class="sig-name descname">action_slack_param_message</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_slack_param_message" title="Permalink to this definition"></a></dt>
<dd><p>Enter the chat message to send to the Slack channel. The message can include tokens that insert text based on the results of the search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_slack_param_webhook_url_override">
<em class="property">property </em><code class="sig-name descname">action_slack_param_webhook_url_override</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_slack_param_webhook_url_override" title="Permalink to this definition"></a></dt>
<dd><p>You can override the Slack webhook URL here if you need to send the alert message to a different Slack team</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index">
<em class="property">property </em><code class="sig-name descname">action_summary_index</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index" title="Permalink to this definition"></a></dt>
<dd><p>The state of the summary index action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_command">
<em class="property">property </em><code class="sig-name descname">action_summary_index_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_command" title="Permalink to this definition"></a></dt>
<dd><p>The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_hostname">
<em class="property">property </em><code class="sig-name descname">action_summary_index_hostname</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_hostname" title="Permalink to this definition"></a></dt>
<dd><p>Sets the hostname used in the web link (url) sent in summary-index alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_inline">
<em class="property">property </em><code class="sig-name descname">action_summary_index_inline</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_inline" title="Permalink to this definition"></a></dt>
<dd><p>Determines whether to execute the summary indexing action as part of the scheduled search.NOTE: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always).Defaults to true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_max_results">
<em class="property">property </em><code class="sig-name descname">action_summary_index_max_results</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_max_results" title="Permalink to this definition"></a></dt>
<dd><p>Sets the maximum number of search results sent using alerts. Defaults to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_max_time">
<em class="property">property </em><code class="sig-name descname">action_summary_index_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_name">
<em class="property">property </em><code class="sig-name descname">action_summary_index_name</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_name" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the name of the summary index where the results of the scheduled search are saved.Defaults to summary.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_track_alert">
<em class="property">property </em><code class="sig-name descname">action_summary_index_track_alert</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_track_alert" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the execution of this action signifies a trackable alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.action_summary_index_ttl">
<em class="property">property </em><code class="sig-name descname">action_summary_index_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.action_summary_index_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.actions">
<em class="property">property </em><code class="sig-name descname">actions</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.actions" title="Permalink to this definition"></a></dt>
<dd><p>A comma-separated list of actions to enable. For example: rss,email</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_comparator">
<em class="property">property </em><code class="sig-name descname">alert_comparator</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_comparator" title="Permalink to this definition"></a></dt>
<dd><p>One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by percUsed with alert_threshold to trigger alert actions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_condition">
<em class="property">property </em><code class="sig-name descname">alert_condition</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_condition" title="Permalink to this definition"></a></dt>
<dd><p>Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_digest_mode">
<em class="property">property </em><code class="sig-name descname">alert_digest_mode</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_digest_mode" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether alert actions are applied to the entire result set or on each individual result.Defaults to 1 (true).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_expires">
<em class="property">property </em><code class="sig-name descname">alert_expires</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_expires" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: [number][time-unit]Sets the period of time to show the alert in the dashboard. Defaults to 24h.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_severity">
<em class="property">property </em><code class="sig-name descname">alert_severity</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_severity" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level.Valid values are:1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL Defaults to 3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_suppress">
<em class="property">property </em><code class="sig-name descname">alert_suppress</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_suppress" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether alert suppression is enabled for this scheduled search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_suppress_fields">
<em class="property">property </em><code class="sig-name descname">alert_suppress_fields</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_suppress_fields" title="Permalink to this definition"></a></dt>
<dd><p>Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_suppress_period">
<em class="property">property </em><code class="sig-name descname">alert_suppress_period</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_suppress_period" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: [number][time-unit] Specifies the suppresion period. Only valid if alert.supress is enabled.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_threshold">
<em class="property">property </em><code class="sig-name descname">alert_threshold</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_threshold" title="Permalink to this definition"></a></dt>
<dd><p>Valid values are: Integer[%]Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc or drops by perc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_track">
<em class="property">property </em><code class="sig-name descname">alert_track</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_track" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: (true | false | auto) Specifies whether to track the actions triggered by this scheduled search.auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. Default value true - force alert tracking.false - disable alert tracking for this search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.alert_type">
<em class="property">property </em><code class="sig-name descname">alert_type</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.alert_type" title="Permalink to this definition"></a></dt>
<dd><p>What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.allow_skew">
<em class="property">property </em><code class="sig-name descname">allow_skew</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.allow_skew" title="Permalink to this definition"></a></dt>
<dd><p>Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize">
<em class="property">property </em><code class="sig-name descname">auto_summarize</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_command">
<em class="property">property </em><code class="sig-name descname">auto_summarize_command</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_command" title="Permalink to this definition"></a></dt>
<dd><p>An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_cron_schedule">
<em class="property">property </em><code class="sig-name descname">auto_summarize_cron_schedule</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_cron_schedule" title="Permalink to this definition"></a></dt>
<dd><p>Cron schedule that probes and generates the summaries for this saved search.The default value is <a href="#id15"><span class="problematic" id="id16">*</span></a>/10 * * * * and corresponds to <cite>every ten hours</cite>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_dispatch_earliest_time">
<em class="property">property </em><code class="sig-name descname">auto_summarize_dispatch_earliest_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_dispatch_earliest_time" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_dispatch_latest_time">
<em class="property">property </em><code class="sig-name descname">auto_summarize_dispatch_latest_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_dispatch_latest_time" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_dispatch_time_format">
<em class="property">property </em><code class="sig-name descname">auto_summarize_dispatch_time_format</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_dispatch_time_format" title="Permalink to this definition"></a></dt>
<dd><p>Defines the time format that Splunk software uses to specify the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_dispatch_ttl">
<em class="property">property </em><code class="sig-name descname">auto_summarize_dispatch_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_dispatch_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: Integer[p]. Defaults to 60.Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_max_disabled_buckets">
<em class="property">property </em><code class="sig-name descname">auto_summarize_max_disabled_buckets</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_max_disabled_buckets" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_max_summary_ratio">
<em class="property">property </em><code class="sig-name descname">auto_summarize_max_summary_ratio</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_max_summary_ratio" title="Permalink to this definition"></a></dt>
<dd><p>The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1 Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_max_summary_size">
<em class="property">property </em><code class="sig-name descname">auto_summarize_max_summary_size</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_max_summary_size" title="Permalink to this definition"></a></dt>
<dd><p>The minimum summary size, in bytes, before testing whether the summarization is helpful.The default value is 52428800 and is equivalent to 5MB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_max_time">
<em class="property">property </em><code class="sig-name descname">auto_summarize_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600.Note: This is an approximate time. The summary search stops at clean bucket boundaries.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_suspend_period">
<em class="property">property </em><code class="sig-name descname">auto_summarize_suspend_period</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_suspend_period" title="Permalink to this definition"></a></dt>
<dd><p>Time specfier indicating when to suspend summarization of this search if the summarization is deemed unhelpful.Defaults to 24h.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.auto_summarize_timespan">
<em class="property">property </em><code class="sig-name descname">auto_summarize_timespan</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.auto_summarize_timespan" title="Permalink to this definition"></a></dt>
<dd><p>The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. Specify a comma delimited list of time specifiers.For example a timechart over the last month whose granuality is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.cron_schedule">
<em class="property">property </em><code class="sig-name descname">cron_schedule</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.cron_schedule" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: cron stringThe cron schedule to execute this search. For example: <a href="#id17"><span class="problematic" id="id18">*</span></a>/5 * * * * causes the search to execute every 5 minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.description" title="Permalink to this definition"></a></dt>
<dd><p>Human-readable description of this saved search. Defaults to empty string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.disabled" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if the saved search is enabled. Defaults to 0.Disabled saved searches are not visible in Splunk Web.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_buckets">
<em class="property">property </em><code class="sig-name descname">dispatch_buckets</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_buckets" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of timeline buckets. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_earliest_time">
<em class="property">property </em><code class="sig-name descname">dispatch_earliest_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_earliest_time" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_index_earliest">
<em class="property">property </em><code class="sig-name descname">dispatch_index_earliest</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_index_earliest" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the earliest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_index_latest">
<em class="property">property </em><code class="sig-name descname">dispatch_index_latest</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_index_latest" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the latest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_indexed_realtime">
<em class="property">property </em><code class="sig-name descname">dispatch_indexed_realtime</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_indexed_realtime" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_indexed_realtime_minspan">
<em class="property">property </em><code class="sig-name descname">dispatch_indexed_realtime_minspan</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_indexed_realtime_minspan" title="Permalink to this definition"></a></dt>
<dd><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_indexed_realtime_offset">
<em class="property">property </em><code class="sig-name descname">dispatch_indexed_realtime_offset</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_indexed_realtime_offset" title="Permalink to this definition"></a></dt>
<dd><p>Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_latest_time">
<em class="property">property </em><code class="sig-name descname">dispatch_latest_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_latest_time" title="Permalink to this definition"></a></dt>
<dd><p>A time string that specifies the latest time for this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_lookups">
<em class="property">property </em><code class="sig-name descname">dispatch_lookups</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_lookups" title="Permalink to this definition"></a></dt>
<dd><p>Enables or disables the lookups for this search. Defaults to 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_max_count">
<em class="property">property </em><code class="sig-name descname">dispatch_max_count</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_max_count" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of results before finalizing the search. Defaults to 500000.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_max_time">
<em class="property">property </em><code class="sig-name descname">dispatch_max_time</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_max_time" title="Permalink to this definition"></a></dt>
<dd><p>Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_reduce_freq">
<em class="property">property </em><code class="sig-name descname">dispatch_reduce_freq</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_reduce_freq" title="Permalink to this definition"></a></dt>
<dd><p>Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_rt_backfill">
<em class="property">property </em><code class="sig-name descname">dispatch_rt_backfill</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_rt_backfill" title="Permalink to this definition"></a></dt>
<dd><p>Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_rt_maximum_span">
<em class="property">property </em><code class="sig-name descname">dispatch_rt_maximum_span</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_rt_maximum_span" title="Permalink to this definition"></a></dt>
<dd><p>Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_spawn_process">
<em class="property">property </em><code class="sig-name descname">dispatch_spawn_process</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_spawn_process" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether a new search process spawns when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_time_format">
<em class="property">property </em><code class="sig-name descname">dispatch_time_format</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_time_format" title="Permalink to this definition"></a></dt>
<dd><p>A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.dispatch_ttl">
<em class="property">property </em><code class="sig-name descname">dispatch_ttl</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.dispatch_ttl" title="Permalink to this definition"></a></dt>
<dd><p>Valid values: Integer[p]. Defaults to 2p.Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.display_view">
<em class="property">property </em><code class="sig-name descname">display_view</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.display_view" title="Permalink to this definition"></a></dt>
<dd><p>Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.is_scheduled">
<em class="property">property </em><code class="sig-name descname">is_scheduled</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.is_scheduled" title="Permalink to this definition"></a></dt>
<dd><p>Whether this search is to be run on a schedule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.is_visible">
<em class="property">property </em><code class="sig-name descname">is_visible</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.is_visible" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.max_concurrent">
<em class="property">property </em><code class="sig-name descname">max_concurrent</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.max_concurrent" title="Permalink to this definition"></a></dt>
<dd><p>The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.name" title="Permalink to this definition"></a></dt>
<dd><p>A name for the search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.realtime_schedule">
<em class="property">property </em><code class="sig-name descname">realtime_schedule</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.realtime_schedule" title="Permalink to this definition"></a></dt>
<dd><p>Defaults to 1. Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.request_ui_dispatch_app">
<em class="property">property </em><code class="sig-name descname">request_ui_dispatch_app</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.request_ui_dispatch_app" title="Permalink to this definition"></a></dt>
<dd><p>Specifies a field used by Splunk Web to denote the app this search should be dispatched in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.request_ui_dispatch_view">
<em class="property">property </em><code class="sig-name descname">request_ui_dispatch_view</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.request_ui_dispatch_view" title="Permalink to this definition"></a></dt>
<dd><p>Specifies a field used by Splunk Web to denote the view this search should be displayed in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.restart_on_searchpeer_add">
<em class="property">property </em><code class="sig-name descname">restart_on_searchpeer_add</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.restart_on_searchpeer_add" title="Permalink to this definition"></a></dt>
<dd><p>Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.run_on_startup">
<em class="property">property </em><code class="sig-name descname">run_on_startup</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.run_on_startup" title="Permalink to this definition"></a></dt>
<dd><p>Indicates whether this search runs at startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set to 1 for scheduled searches that populate lookup tables.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.schedule_priority">
<em class="property">property </em><code class="sig-name descname">schedule_priority</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.schedule_priority" title="Permalink to this definition"></a></dt>
<dd><p>Raises the scheduling priority of the named search. Defaults to Default</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.schedule_window">
<em class="property">property </em><code class="sig-name descname">schedule_window</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.schedule_window" title="Permalink to this definition"></a></dt>
<dd><p>Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period.Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.search">
<em class="property">property </em><code class="sig-name descname">search</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.search" title="Permalink to this definition"></a></dt>
<dd><p>Required when creating a new search.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.vsid">
<em class="property">property </em><code class="sig-name descname">vsid</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.vsid" title="Permalink to this definition"></a></dt>
<dd><p>Defines the viewstate id associated with the UI view listed in ‘displayview’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.workload_pool">
<em class="property">property </em><code class="sig-name descname">workload_pool</code><a class="headerlink" href="#pulumi_splunk.SavedSearches.workload_pool" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the new workload pool where the existing running search will be placed.`</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_splunk.SavedSearches.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.SavedSearches.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_splunk.SavedSearches.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_splunk.SavedSearches.translate_input_property" title="Permalink to this definition"></a></dt>
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
