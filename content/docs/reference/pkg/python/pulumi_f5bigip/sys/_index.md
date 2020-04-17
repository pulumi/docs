---
title: Module sys
title_tag: Module sys | Package pulumi_f5bigip | Python SDK
linktitle: sys
notitle: true
---

<div class="section" id="sys">
<h1>sys<a class="headerlink" href="#sys" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-f5bigip/issues">pulumi/pulumi-f5bigip repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip/issues">terraform-providers/terraform-provider-f5bigip repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_f5bigip.sys"></span><dl class="class">
<dt id="pulumi_f5bigip.sys.BigIpLicense">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">BigIpLicense</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">command=None</em>, <em class="sig-param">registration_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BigIpLicense resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] command: Tmsh command to execute tmsh commands like install
:param pulumi.Input[str] registration_key: A unique Key F5 provides for Licensing BIG-IP</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.BigIpLicense.command">
<code class="sig-name descname">command</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.command" title="Permalink to this definition">¶</a></dt>
<dd><p>Tmsh command to execute tmsh commands like install</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.BigIpLicense.registration_key">
<code class="sig-name descname">registration_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.registration_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique Key F5 provides for Licensing BIG-IP</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.BigIpLicense.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">command=None</em>, <em class="sig-param">registration_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BigIpLicense resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tmsh command to execute tmsh commands like install</p></li>
<li><p><strong>registration_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique Key F5 provides for Licensing BIG-IP</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.BigIpLicense.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.BigIpLicense.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Dns">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">Dns</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">number_of_dots=None</em>, <em class="sig-param">searches=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.Dns</span></code> Configures DNS server on F5 BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Dns Servers</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name or IP address of the DNS server</p></li>
<li><p><strong>number_of_dots</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Configures the number of dots needed in a name before an initial absolute query will be made.</p></li>
<li><p><strong>searches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify what domains you want to search</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Dns Servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or IP address of the DNS server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.number_of_dots">
<code class="sig-name descname">number_of_dots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.number_of_dots" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the number of dots needed in a name before an initial absolute query will be made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.searches">
<code class="sig-name descname">searches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.searches" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify what domains you want to search</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Dns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">number_of_dots=None</em>, <em class="sig-param">searches=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dns resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Dns Servers</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name or IP address of the DNS server</p></li>
<li><p><strong>number_of_dots</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Configures the number of dots needed in a name before an initial absolute query will be made.</p></li>
<li><p><strong>searches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specify what domains you want to search</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Dns.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Dns.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.IApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">IApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">devicegroup=None</em>, <em class="sig-param">execute_action=None</em>, <em class="sig-param">inherited_devicegroup=None</em>, <em class="sig-param">inherited_traffic_group=None</em>, <em class="sig-param">jsonfile=None</em>, <em class="sig-param">lists=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">strict_updates=None</em>, <em class="sig-param">tables=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">template_modified=None</em>, <em class="sig-param">template_prerequisite_errors=None</em>, <em class="sig-param">traffic_group=None</em>, <em class="sig-param">variables=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.IApp</span></code> resource helps you to deploy Application Services template that can be used to automate and orchestrate Layer 4-7 applications service deployments using F5 Network.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Iapp which needs to be Iappensed</p></li>
<li><p><strong>devicegroup</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>execute_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>inherited_devicegroup</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>inherited_traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>jsonfile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Refer to the Json file which will be deployed on F5 BIG-IP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the iApp.</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Iapp which needs to be Iappensed</p></li>
<li><p><strong>strict_updates</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template_modified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template_prerequisite_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">persists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">columnNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptedColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the iApp.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the iApp.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Address of the Iapp which needs to be Iappensed</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.devicegroup">
<code class="sig-name descname">devicegroup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.devicegroup" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.execute_action">
<code class="sig-name descname">execute_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.execute_action" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.inherited_devicegroup">
<code class="sig-name descname">inherited_devicegroup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.inherited_devicegroup" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.inherited_traffic_group">
<code class="sig-name descname">inherited_traffic_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.inherited_traffic_group" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.jsonfile">
<code class="sig-name descname">jsonfile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.jsonfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Refer to the Json file which will be deployed on F5 BIG-IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the iApp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Address of the Iapp which needs to be Iappensed</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.strict_updates">
<code class="sig-name descname">strict_updates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.strict_updates" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.template" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.template_modified">
<code class="sig-name descname">template_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.template_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.template_prerequisite_errors">
<code class="sig-name descname">template_prerequisite_errors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.template_prerequisite_errors" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.traffic_group">
<code class="sig-name descname">traffic_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.traffic_group" title="Permalink to this definition">¶</a></dt>
<dd><p>BIG-IP password</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.IApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">devicegroup=None</em>, <em class="sig-param">execute_action=None</em>, <em class="sig-param">inherited_devicegroup=None</em>, <em class="sig-param">inherited_traffic_group=None</em>, <em class="sig-param">jsonfile=None</em>, <em class="sig-param">lists=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">strict_updates=None</em>, <em class="sig-param">tables=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">template_modified=None</em>, <em class="sig-param">template_prerequisite_errors=None</em>, <em class="sig-param">traffic_group=None</em>, <em class="sig-param">variables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IApp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Iapp which needs to be Iappensed</p></li>
<li><p><strong>devicegroup</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>execute_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>inherited_devicegroup</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>inherited_traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>jsonfile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Refer to the Json file which will be deployed on F5 BIG-IP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the iApp.</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Iapp which needs to be Iappensed</p></li>
<li><p><strong>strict_updates</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template_modified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>template_prerequisite_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIG-IP password</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">persists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">columnNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptedColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the iApp.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the iApp.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.IApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.IApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Ntp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">Ntp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">servers=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.Ntp</span></code> provides details about a specific bigip</p>
<p>This resource is helpful when configuring NTP server on the BIG-IP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the ntp Servers</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Adds NTP servers to or deletes NTP servers from the BIG-IP system.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone that you want to use for the system time.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Ntp.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the ntp Servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Ntp.servers">
<code class="sig-name descname">servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds NTP servers to or deletes NTP servers from the BIG-IP system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Ntp.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the time zone that you want to use for the system time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Ntp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">servers=None</em>, <em class="sig-param">timezone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ntp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the ntp Servers</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Adds NTP servers to or deletes NTP servers from the BIG-IP system.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone that you want to use for the system time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Ntp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Ntp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Provision">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">Provision</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cpu_ratio=None</em>, <em class="sig-param">disk_ratio=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">level=None</em>, <em class="sig-param">memory_ratio=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.Provision</span></code> provides details bout how to enable “ilx”, “asm” “apm” resource on BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cpu_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – cpu Ratio</p></li>
<li><p><strong>disk_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – disk Ratio</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – path</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – what level nominal or dedicated</p></li>
<li><p><strong>memory_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – memory Ratio</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the module to be provisioned</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.cpu_ratio">
<code class="sig-name descname">cpu_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.cpu_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>cpu Ratio</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.disk_ratio">
<code class="sig-name descname">disk_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.disk_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>disk Ratio</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.full_path">
<code class="sig-name descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>path</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.level">
<code class="sig-name descname">level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.level" title="Permalink to this definition">¶</a></dt>
<dd><p>what level nominal or dedicated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.memory_ratio">
<code class="sig-name descname">memory_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.memory_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>memory Ratio</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Provision.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the module to be provisioned</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Provision.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cpu_ratio=None</em>, <em class="sig-param">disk_ratio=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">level=None</em>, <em class="sig-param">memory_ratio=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provision resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cpu_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – cpu Ratio</p></li>
<li><p><strong>disk_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – disk Ratio</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – path</p></li>
<li><p><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – what level nominal or dedicated</p></li>
<li><p><strong>memory_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – memory Ratio</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the module to be provisioned</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Provision.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Provision.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Snmp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">Snmp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowedaddresses=None</em>, <em class="sig-param">sys_contact=None</em>, <em class="sig-param">sys_location=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.Snmp</span></code> provides details bout how to enable “ilx”, “asm” “apm” resource on BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowedaddresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.</p></li>
<li><p><strong>sys_contact</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the contact information for the system administrator.</p></li>
<li><p><strong>sys_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the system’s physical location.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.allowedaddresses">
<code class="sig-name descname">allowedaddresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.allowedaddresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.sys_contact">
<code class="sig-name descname">sys_contact</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.sys_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the contact information for the system administrator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.sys_location">
<code class="sig-name descname">sys_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.sys_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the system’s physical location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Snmp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowedaddresses=None</em>, <em class="sig-param">sys_contact=None</em>, <em class="sig-param">sys_location=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snmp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowedaddresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.</p></li>
<li><p><strong>sys_contact</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the contact information for the system administrator.</p></li>
<li><p><strong>sys_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the system’s physical location.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Snmp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.Snmp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.SnmpTraps">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.sys.</code><code class="sig-name descname">SnmpTraps</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_passwordencrypted=None</em>, <em class="sig-param">auth_protocol=None</em>, <em class="sig-param">community=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine_id=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">privacy_password=None</em>, <em class="sig-param">privacy_password_encrypted=None</em>, <em class="sig-param">privacy_protocol=None</em>, <em class="sig-param">security_level=None</em>, <em class="sig-param">security_name=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sys.SnmpTraps</span></code> provides details bout how to enable snmp_traps resource on BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_passwordencrypted</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Encrypted password</p></li>
<li><p><strong>auth_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol used to authenticate the user.</p></li>
<li><p><strong>community</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the community string used for this trap.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port that the trap will be sent to.</p></li>
<li><p><strong>engine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the authoritative security engine for SNMPv3.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host the trap will be sent to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snmp trap.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User defined description.</p></li>
<li><p><strong>privacy_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the clear text password used to encrypt traffic. This field will not be displayed.</p></li>
<li><p><strong>privacy_password_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the encrypted password used to encrypt traffic.</p></li>
<li><p><strong>privacy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol used to encrypt traffic.</p></li>
<li><p><strong>security_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not traffic is encrypted and whether or not authentication is required.</p></li>
<li><p><strong>security_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Security name used in conjunction with SNMPv3.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNMP version used for sending the trap.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.auth_passwordencrypted">
<code class="sig-name descname">auth_passwordencrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.auth_passwordencrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypted password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.auth_protocol">
<code class="sig-name descname">auth_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.auth_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the protocol used to authenticate the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.community">
<code class="sig-name descname">community</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.community" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the community string used for this trap.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The port that the trap will be sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.engine_id">
<code class="sig-name descname">engine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.engine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the authoritative security engine for SNMPv3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The host the trap will be sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the snmp trap.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.port" title="Permalink to this definition">¶</a></dt>
<dd><p>User defined description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.privacy_password">
<code class="sig-name descname">privacy_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.privacy_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the clear text password used to encrypt traffic. This field will not be displayed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.privacy_password_encrypted">
<code class="sig-name descname">privacy_password_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.privacy_password_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the encrypted password used to encrypt traffic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.privacy_protocol">
<code class="sig-name descname">privacy_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.privacy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the protocol used to encrypt traffic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.security_level">
<code class="sig-name descname">security_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.security_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not traffic is encrypted and whether or not authentication is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.security_name">
<code class="sig-name descname">security_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.security_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Security name used in conjunction with SNMPv3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.version" title="Permalink to this definition">¶</a></dt>
<dd><p>SNMP version used for sending the trap.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.SnmpTraps.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_passwordencrypted=None</em>, <em class="sig-param">auth_protocol=None</em>, <em class="sig-param">community=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine_id=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">privacy_password=None</em>, <em class="sig-param">privacy_password_encrypted=None</em>, <em class="sig-param">privacy_protocol=None</em>, <em class="sig-param">security_level=None</em>, <em class="sig-param">security_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SnmpTraps resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_passwordencrypted</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Encrypted password</p></li>
<li><p><strong>auth_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol used to authenticate the user.</p></li>
<li><p><strong>community</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the community string used for this trap.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port that the trap will be sent to.</p></li>
<li><p><strong>engine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the authoritative security engine for SNMPv3.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host the trap will be sent to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snmp trap.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User defined description.</p></li>
<li><p><strong>privacy_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the clear text password used to encrypt traffic. This field will not be displayed.</p></li>
<li><p><strong>privacy_password_encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the encrypted password used to encrypt traffic.</p></li>
<li><p><strong>privacy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol used to encrypt traffic.</p></li>
<li><p><strong>security_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether or not traffic is encrypted and whether or not authentication is required.</p></li>
<li><p><strong>security_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Security name used in conjunction with SNMPv3.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNMP version used for sending the trap.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.SnmpTraps.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.sys.SnmpTraps.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
