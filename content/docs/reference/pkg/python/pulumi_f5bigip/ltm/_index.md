---
title: Module ltm
title_tag: Module ltm | Package pulumi_f5bigip | Python SDK
linktitle: ltm
notitle: true
---

<div class="section" id="ltm">
<h1>ltm<a class="headerlink" href="#ltm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-f5bigip/issues">pulumi/pulumi-f5bigip repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip/issues">terraform-providers/terraform-provider-f5bigip repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_f5bigip.ltm"></span><dl class="class">
<dt id="pulumi_f5bigip.ltm.DataGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">DataGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.DataGroup</span></code> Manages internal (in-line) datagroup configuration</p>
<p>Resource should be named with their “full path”. The full path is the combination of the partition + name of the resource, for example /Common/my-datagroup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a set of <code class="docutils literal notranslate"><span class="pre">name</span></code> and <code class="docutils literal notranslate"><span class="pre">data</span></code> attributes, name must be of type specified by the <code class="docutils literal notranslate"><span class="pre">type</span></code> attributed (<code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> and <code class="docutils literal notranslate"><span class="pre">integer</span></code>), data is optional and can take any value, multiple <code class="docutils literal notranslate"><span class="pre">record</span></code> sets can be specified as needed.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – datagroup type (applies to the <code class="docutils literal notranslate"><span class="pre">name</span></code> field of the record), supports: <code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> or <code class="docutils literal notranslate"><span class="pre">integer</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>records</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">data</span></code> attribute, specifying a value here will create a record in the form of <code class="docutils literal notranslate"><span class="pre">name</span> <span class="pre">:=</span> <span class="pre">data</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.DataGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>, sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.DataGroup.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.records" title="Permalink to this definition">¶</a></dt>
<dd><p>a set of <code class="docutils literal notranslate"><span class="pre">name</span></code> and <code class="docutils literal notranslate"><span class="pre">data</span></code> attributes, name must be of type specified by the <code class="docutils literal notranslate"><span class="pre">type</span></code> attributed (<code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> and <code class="docutils literal notranslate"><span class="pre">integer</span></code>), data is optional and can take any value, multiple <code class="docutils literal notranslate"><span class="pre">record</span></code> sets can be specified as needed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">data</span></code> attribute, specifying a value here will create a record in the form of <code class="docutils literal notranslate"><span class="pre">name</span> <span class="pre">:=</span> <span class="pre">data</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.DataGroup.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>datagroup type (applies to the <code class="docutils literal notranslate"><span class="pre">name</span></code> field of the record), supports: <code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> or <code class="docutils literal notranslate"><span class="pre">integer</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.DataGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a set of <code class="docutils literal notranslate"><span class="pre">name</span></code> and <code class="docutils literal notranslate"><span class="pre">data</span></code> attributes, name must be of type specified by the <code class="docutils literal notranslate"><span class="pre">type</span></code> attributed (<code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> and <code class="docutils literal notranslate"><span class="pre">integer</span></code>), data is optional and can take any value, multiple <code class="docutils literal notranslate"><span class="pre">record</span></code> sets can be specified as needed.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – datagroup type (applies to the <code class="docutils literal notranslate"><span class="pre">name</span></code> field of the record), supports: <code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code> or <code class="docutils literal notranslate"><span class="pre">integer</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>records</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">data</span></code> attribute, specifying a value here will create a record in the form of <code class="docutils literal notranslate"><span class="pre">name</span> <span class="pre">:=</span> <span class="pre">data</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - , sets the value of the record’s <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute, must be of type defined in <code class="docutils literal notranslate"><span class="pre">type</span></code> attribute</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.DataGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.DataGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.DataGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.IRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">IRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">irule=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.IRule</span></code> Creates iRule on BIG-IP F5 device</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>irule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Body of the iRule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the iRule</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.IRule.irule">
<code class="sig-name descname">irule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule.irule" title="Permalink to this definition">¶</a></dt>
<dd><p>Body of the iRule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.IRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the iRule</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.IRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">irule=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>irule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Body of the iRule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the iRule</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.IRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.IRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.IRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Monitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">adaptive=None</em>, <em class="sig-param">adaptive_limit=None</em>, <em class="sig-param">compatibility=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filename=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">ip_dscp=None</em>, <em class="sig-param">manual_resume=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">receive=None</em>, <em class="sig-param">receive_disable=None</em>, <em class="sig-param">reverse=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">time_until_up=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">transparent=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.Monitor</span></code> Configures a custom monitor for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adaptive</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ftp adaptive</p></li>
<li><p><strong>adaptive_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value</p></li>
<li><p><strong>compatibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL. Accepts ‘enabled’ or ‘disabled’ values, the default value is ‘enabled’.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the database in which the user is created</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Existing monitor to inherit from. Must be one of /Common/http, /Common/https, /Common/icmp or /Common/gateway-icmp.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an alias address for monitoring</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the full path and file name of the file that the system attempts to download. The health check is successful if the system can download the file.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Check interval in seconds</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data transfer process (DTP) mode. The default value is passive. The options are passive (Specifies that the monitor sends a data transfer request to the FTP server. When the FTP server receives the request, the FTP server then initiates and establishes the data connection.) and active (Specifies that the monitor initiates and establishes the data connection with the FTP server.).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the monitor</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Existing LTM monitor to inherit from</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the password if the monitored target requires authentication</p></li>
<li><p><strong>receive</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expected response string</p></li>
<li><p><strong>receive_disable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expected response string.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Request string to send</p></li>
<li><p><strong>time_until_up</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time in seconds</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout in seconds</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user name if the monitored target requires authentication</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.adaptive">
<code class="sig-name descname">adaptive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.adaptive" title="Permalink to this definition">¶</a></dt>
<dd><p>ftp adaptive</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.adaptive_limit">
<code class="sig-name descname">adaptive_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.adaptive_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.compatibility">
<code class="sig-name descname">compatibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.compatibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL. Accepts ‘enabled’ or ‘disabled’ values, the default value is ‘enabled’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.database" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the database in which the user is created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Existing monitor to inherit from. Must be one of /Common/http, /Common/https, /Common/icmp or /Common/gateway-icmp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify an alias address for monitoring</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.filename">
<code class="sig-name descname">filename</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.filename" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the full path and file name of the file that the system attempts to download. The health check is successful if the system can download the file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.interval">
<code class="sig-name descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Check interval in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the data transfer process (DTP) mode. The default value is passive. The options are passive (Specifies that the monitor sends a data transfer request to the FTP server. When the FTP server receives the request, the FTP server then initiates and establishes the data connection.) and active (Specifies that the monitor initiates and establishes the data connection with the FTP server.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the monitor</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>Existing LTM monitor to inherit from</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the password if the monitored target requires authentication</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.receive">
<code class="sig-name descname">receive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.receive" title="Permalink to this definition">¶</a></dt>
<dd><p>Expected response string</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.receive_disable">
<code class="sig-name descname">receive_disable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.receive_disable" title="Permalink to this definition">¶</a></dt>
<dd><p>Expected response string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.send">
<code class="sig-name descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Request string to send</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.time_until_up">
<code class="sig-name descname">time_until_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.time_until_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Time in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Monitor.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the user name if the monitored target requires authentication</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">adaptive=None</em>, <em class="sig-param">adaptive_limit=None</em>, <em class="sig-param">compatibility=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filename=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">ip_dscp=None</em>, <em class="sig-param">manual_resume=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">receive=None</em>, <em class="sig-param">receive_disable=None</em>, <em class="sig-param">reverse=None</em>, <em class="sig-param">send=None</em>, <em class="sig-param">time_until_up=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">transparent=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adaptive</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ftp adaptive</p></li>
<li><p><strong>adaptive_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value</p></li>
<li><p><strong>compatibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL. Accepts ‘enabled’ or ‘disabled’ values, the default value is ‘enabled’.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the database in which the user is created</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Existing monitor to inherit from. Must be one of /Common/http, /Common/https, /Common/icmp or /Common/gateway-icmp.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify an alias address for monitoring</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the full path and file name of the file that the system attempts to download. The health check is successful if the system can download the file.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Check interval in seconds</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data transfer process (DTP) mode. The default value is passive. The options are passive (Specifies that the monitor sends a data transfer request to the FTP server. When the FTP server receives the request, the FTP server then initiates and establishes the data connection.) and active (Specifies that the monitor initiates and establishes the data connection with the FTP server.).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the monitor</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Existing LTM monitor to inherit from</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the password if the monitored target requires authentication</p></li>
<li><p><strong>receive</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expected response string</p></li>
<li><p><strong>receive_disable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expected response string.</p></li>
<li><p><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Request string to send</p></li>
<li><p><strong>time_until_up</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time in seconds</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout in seconds</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user name if the monitored target requires authentication</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Monitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Monitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Monitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Node">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">Node</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamic_ratio=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">monitor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rate_limit=None</em>, <em class="sig-param">ratio=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Node" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.Node</span></code> Manages a node configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP or hostname of the node</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections allowed for the node or node address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined description give ltm_node</p></li>
<li><p><strong>dynamic_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the fixed ratio value used for a node during ratio load balancing.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – specifies the name of the monitor or monitor rule that you want to associate with the node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the node</p></li>
<li><p><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum number of connections per second allowed for a node or node address. The default value is ‘disabled’.</p></li>
<li><p><strong>ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Sets the ratio number for the node.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default is “user-up” you can set to “user-down” if you want to disable</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fqdn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">addressFamily</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the node’s address family. The default is ‘unspecified’, or IP-agnostic. This needs to be specified inside the fqdn (fully qualified domain name).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autopopulate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">downinterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the amount of time before sending the next DNS query. Default is 3600. This needs to be specified inside the fqdn (fully qualified domain name).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the node</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP or hostname of the node</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.connection_limit">
<code class="sig-name descname">connection_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of connections allowed for the node or node address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.description" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined description give ltm_node</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.dynamic_ratio">
<code class="sig-name descname">dynamic_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.dynamic_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the fixed ratio value used for a node during ratio load balancing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.monitor">
<code class="sig-name descname">monitor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>specifies the name of the monitor or monitor rule that you want to associate with the node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the node</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.rate_limit">
<code class="sig-name descname">rate_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.rate_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of connections per second allowed for a node or node address. The default value is ‘disabled’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.ratio">
<code class="sig-name descname">ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the ratio number for the node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Node.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Default is “user-up” you can set to “user-down” if you want to disable</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Node.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamic_ratio=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">monitor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rate_limit=None</em>, <em class="sig-param">ratio=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Node resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP or hostname of the node</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections allowed for the node or node address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined description give ltm_node</p></li>
<li><p><strong>dynamic_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the fixed ratio value used for a node during ratio load balancing.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – specifies the name of the monitor or monitor rule that you want to associate with the node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the node</p></li>
<li><p><strong>rate_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum number of connections per second allowed for a node or node address. The default value is ‘disabled’.</p></li>
<li><p><strong>ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Sets the ratio number for the node.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default is “user-up” you can set to “user-down” if you want to disable</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fqdn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">addressFamily</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the node’s address family. The default is ‘unspecified’, or IP-agnostic. This needs to be specified inside the fqdn (fully qualified domain name).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autopopulate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">downinterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the amount of time before sending the next DNS query. Default is 3600. This needs to be specified inside the fqdn (fully qualified domain name).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the node</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Node.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Node.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Node.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">PersistenceProfileCookie</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_send=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">cookie_encryption=None</em>, <em class="sig-param">cookie_encryption_passphrase=None</em>, <em class="sig-param">cookie_name=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">hash_length=None</em>, <em class="sig-param">hash_offset=None</em>, <em class="sig-param">httponly=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a cookie persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Name of the virtual address</p>
<p><code class="docutils literal notranslate"><span class="pre">defaults_from</span></code> - (Required) Parent cookie persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_pools</span></code> (Optional) (enabled or disabled) match across pools with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_services</span></code> (Optional) (enabled or disabled) match across services with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_virtuals</span></code> (Optional) (enabled or disabled) match across virtual servers with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">mirror</span></code> (Optional) (enabled or disabled) mirror persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (Optional) (enabled or disabled) Timeout for persistence of the session in seconds</p>
<p><code class="docutils literal notranslate"><span class="pre">override_conn_limit</span></code> (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.</p>
<p><code class="docutils literal notranslate"><span class="pre">always_send</span></code> (Optional) (enabled or disabled) always send cookies</p>
<p><code class="docutils literal notranslate"><span class="pre">cookie_encryption</span></code> (Optional) (required, preferred, or disabled) To required, preferred, or disabled policy for cookie encryption</p>
<p><code class="docutils literal notranslate"><span class="pre">cookie_encryption_passphrase</span></code> (Optional) (required, preferred, or disabled) Passphrase for encrypted cookies. The field is encrypted on the server and will always return differently then set.
If this is configured specify <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> under the <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> block to ignore returned encrypted value.</p>
<p><code class="docutils literal notranslate"><span class="pre">cookie_name</span></code> (Optional) Name of the cookie to track persistence</p>
<p><code class="docutils literal notranslate"><span class="pre">expiration</span></code> (Optional) Expiration TTL for cookie specified in DAY:HOUR:MIN:SECONDS (Examples: 1:0:0:0 one day, 1:0:0 one hour, 30:0 thirty minutes)</p>
<p><code class="docutils literal notranslate"><span class="pre">hash_length</span></code> (Optional) (Integer) Length of hash to apply to cookie</p>
<p><code class="docutils literal notranslate"><span class="pre">hash_offset</span></code> (Optional) (Integer) Number of characters to skip in the cookie for the hash</p>
<p><code class="docutils literal notranslate"><span class="pre">httponly</span></code> (Optional) (enabled or disabled) Sending only over http</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always*send</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable always sending cookies</p>
</p></li>
<li><p><strong>cookie_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To required, preferred, or disabled policy for cookie encryption</p></li>
<li><p><strong>cookie_encryption_passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Passphrase for encrypted cookies</p></li>
<li><p><strong>cookie_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cookie to track persistence</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration TTL for cookie specified in D:H:M:S or in seconds</p></li>
<li><p><strong>hash_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length of hash to apply to cookie</p></li>
<li><p><strong>hash*offset</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Number of characters to skip in the cookie for the hash</p>
</p></li>
<li><p><strong>httponly</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable * disable sending only over http</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across virtual servers with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.always_send">
<code class="sig-name descname">always_send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.always_send" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable always sending cookies</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_encryption">
<code class="sig-name descname">cookie_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>To required, preferred, or disabled policy for cookie encryption</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_encryption_passphrase">
<code class="sig-name descname">cookie_encryption_passphrase</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_encryption_passphrase" title="Permalink to this definition">¶</a></dt>
<dd><p>Passphrase for encrypted cookies</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_name">
<code class="sig-name descname">cookie_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.cookie_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cookie to track persistence</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Inherit defaults from parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.expiration">
<code class="sig-name descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Expiration TTL for cookie specified in D:H:M:S or in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.hash_length">
<code class="sig-name descname">hash_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.hash_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of hash to apply to cookie</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.hash_offset">
<code class="sig-name descname">hash_offset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.hash_offset" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of characters to skip in the cookie for the hash</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.httponly">
<code class="sig-name descname">httponly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.httponly" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable sending only over http</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_pools">
<code class="sig-name descname">match_across_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across pools with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_services">
<code class="sig-name descname">match_across_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_services" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_virtuals">
<code class="sig-name descname">match_across_virtuals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.match_across_virtuals" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across virtual servers with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.mirror">
<code class="sig-name descname">mirror</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.mirror" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the persistence profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.override_conn_limit">
<code class="sig-name descname">override_conn_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.override_conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout for persistence of the session</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_send=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">cookie_encryption=None</em>, <em class="sig-param">cookie_encryption_passphrase=None</em>, <em class="sig-param">cookie_name=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">hash_length=None</em>, <em class="sig-param">hash_offset=None</em>, <em class="sig-param">httponly=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PersistenceProfileCookie resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always*send</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable always sending cookies</p>
</p></li>
<li><p><strong>cookie_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To required, preferred, or disabled policy for cookie encryption</p></li>
<li><p><strong>cookie_encryption_passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Passphrase for encrypted cookies</p></li>
<li><p><strong>cookie_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cookie to track persistence</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration TTL for cookie specified in D:H:M:S or in seconds</p></li>
<li><p><strong>hash_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length of hash to apply to cookie</p></li>
<li><p><strong>hash*offset</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Number of characters to skip in the cookie for the hash</p>
</p></li>
<li><p><strong>httponly</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable * disable sending only over http</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across virtual servers with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileCookie.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileCookie.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">PersistenceProfileDstAddr</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">hash_algorithm=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a cookie persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Name of the virtual address</p>
<p><code class="docutils literal notranslate"><span class="pre">defaults_from</span></code> - (Optional) Specifies the existing profile from which the system imports settings for the new profile.</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_pools</span></code> (Optional) (enabled or disabled) match across pools with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_services</span></code> (Optional) (enabled or disabled) match across services with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_virtuals</span></code> (Optional) (enabled or disabled) match across virtual servers with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">mirror</span></code> (Optional) (enabled or disabled) mirror persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (Optional) (enabled or disabled) Timeout for persistence of the session in seconds</p>
<p><code class="docutils literal notranslate"><span class="pre">override_conn_limit</span></code> (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>hash_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the hash algorithm</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Inherit defaults from parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.hash_algorithm">
<code class="sig-name descname">hash_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.hash_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the hash algorithm</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.mask">
<code class="sig-name descname">mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.mask" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_pools">
<code class="sig-name descname">match_across_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across pools with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_services">
<code class="sig-name descname">match_across_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_services" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_virtuals">
<code class="sig-name descname">match_across_virtuals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.match_across_virtuals" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.mirror">
<code class="sig-name descname">mirror</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.mirror" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the persistence profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.override_conn_limit">
<code class="sig-name descname">override_conn_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.override_conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout for persistence of the session</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">hash_algorithm=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PersistenceProfileDstAddr resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>hash_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the hash algorithm</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileDstAddr.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileDstAddr.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">PersistenceProfileSrcAddr</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">hash_algorithm=None</em>, <em class="sig-param">map_proxies=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a source address persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Name of the virtual address</p>
<p><code class="docutils literal notranslate"><span class="pre">defaults_from</span></code> - (Required) Parent cookie persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_pools</span></code> (Optional) (enabled or disabled) match across pools with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_services</span></code> (Optional) (enabled or disabled) match across services with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_virtuals</span></code> (Optional) (enabled or disabled) match across virtual servers with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">mirror</span></code> (Optional) (enabled or disabled) mirror persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (Optional) (enabled or disabled) Timeout for persistence of the session in seconds</p>
<p><code class="docutils literal notranslate"><span class="pre">override_conn_limit</span></code> (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.</p>
<p><code class="docutils literal notranslate"><span class="pre">hash_algorithm</span></code> (Optional) Specify the hash algorithm</p>
<p><code class="docutils literal notranslate"><span class="pre">mask</span></code> (Optional) Identify a range of source IP addresses to manage together as a single source address affinity persistent connection when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p>
<p><code class="docutils literal notranslate"><span class="pre">map_proxies</span></code> (Optional) (enabled or disabled) Directs all to the same single pool member</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>hash_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the hash algorithm</p></li>
<li><p><strong>map*proxies</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable directs all to the same single pool member</p>
</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Inherit defaults from parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.hash_algorithm">
<code class="sig-name descname">hash_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.hash_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the hash algorithm</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.map_proxies">
<code class="sig-name descname">map_proxies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.map_proxies" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable directs all to the same single pool member</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.mask">
<code class="sig-name descname">mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.mask" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_pools">
<code class="sig-name descname">match_across_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across pools with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_services">
<code class="sig-name descname">match_across_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_services" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_virtuals">
<code class="sig-name descname">match_across_virtuals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.match_across_virtuals" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.mirror">
<code class="sig-name descname">mirror</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.mirror" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the persistence profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.override_conn_limit">
<code class="sig-name descname">override_conn_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.override_conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout for persistence of the session</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">hash_algorithm=None</em>, <em class="sig-param">map_proxies=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PersistenceProfileSrcAddr resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>hash_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the hash algorithm</p></li>
<li><p><strong>map*proxies</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable directs all to the same single pool member</p>
</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSrcAddr.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">PersistenceProfileSsl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures an SSL persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Name of the virtual address</p>
<p><code class="docutils literal notranslate"><span class="pre">defaults_from</span></code> - (Required) Parent cookie persistence profile</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_pools</span></code> (Optional) (enabled or disabled) match across pools with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_services</span></code> (Optional) (enabled or disabled) match across services with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">match_across_virtuals</span></code> (Optional) (enabled or disabled) match across virtual servers with given persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">mirror</span></code> (Optional) (enabled or disabled) mirror persistence record</p>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (Optional) (enabled or disabled) Timeout for persistence of the session in seconds</p>
<p><code class="docutils literal notranslate"><span class="pre">override_conn_limit</span></code> (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Inherit defaults from parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_pools">
<code class="sig-name descname">match_across_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across pools with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_services">
<code class="sig-name descname">match_across_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_services" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_virtuals">
<code class="sig-name descname">match_across_virtuals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.match_across_virtuals" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable match across services with given persistence record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.mirror">
<code class="sig-name descname">mirror</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.mirror" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the persistence profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.override_conn_limit">
<code class="sig-name descname">override_conn_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.override_conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout for persistence of the session</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">match_across_pools=None</em>, <em class="sig-param">match_across_services=None</em>, <em class="sig-param">match_across_virtuals=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_conn_limit=None</em>, <em class="sig-param">timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PersistenceProfileSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit defaults from parent profile</p></li>
<li><p><strong>match_across*pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across pools with given persistence record</p>
</p></li>
<li><p><strong>match_across*services</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>match_across*virtuals</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable match across services with given persistence record</p>
</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – To enable _ disable</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the persistence profile</p></li>
<li><p><strong>override_conn*limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>To enable * disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.</p>
</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout for persistence of the session</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PersistenceProfileSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PersistenceProfileSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">controls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">published_copy=None</em>, <em class="sig-param">requires=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">strategy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.Policy</span></code> Configures Virtual Server</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>controls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the controls</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Policy</p></li>
<li><p><strong>published_copy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you want to publish the policy else it will be deployed in Drafts mode.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the protocol</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules can be applied using the policy</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the match strategy</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">application</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">asm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">avr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">carp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">classify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clonePool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieInsert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiePassive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieRewrite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">decompress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirySecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facility</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - This action will affect forwarding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReply</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ifile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internalVirtual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">l7dos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ltmPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">member</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netmask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nexthop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">persist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This action will direct the stream to this pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateclass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remove</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">select</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snatpool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpNagle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wam</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherBits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUsage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceMake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">equals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greater</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greaterOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUserAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last15secs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last1min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last5mins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">less</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lessOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">local</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">major</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">missing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">not</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">org</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathSegment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">present</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslExtension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unnamedQueryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAgentToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Policy</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.controls">
<code class="sig-name descname">controls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.controls" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the controls</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Policy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.published_copy">
<code class="sig-name descname">published_copy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.published_copy" title="Permalink to this definition">¶</a></dt>
<dd><p>If you want to publish the policy else it will be deployed in Drafts mode.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.requires">
<code class="sig-name descname">requires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the protocol</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rules can be applied using the policy</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">application</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">asm</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">avr</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cache</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">carp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">classify</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clonePool</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieHash</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieInsert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiePassive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieRewrite</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">decompress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defer</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirySecs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facility</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - This action will affect forwarding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReply</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ifile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internalVirtual</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">l7dos</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ltmPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">member</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netmask</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nexthop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pem</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">persist</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pin</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pool</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This action will direct the stream to this pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateclass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remove</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replace</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reset</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">select</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snatpool</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpNagle</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uie</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wam</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserType</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipher</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherBits</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contains</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUsage</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceMake</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">equals</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoip</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greater</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greaterOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUserAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last15secs</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last1min</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last5mins</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">less</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lessOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">local</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">major</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matches</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minor</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">missing</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mss</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">not</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">org</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathSegment</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">present</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remote</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rtt</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_name</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslExtension</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unnamedQueryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAgentToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the Policy</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Policy.strategy">
<code class="sig-name descname">strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the match strategy</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">controls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">published_copy=None</em>, <em class="sig-param">requires=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">strategy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>controls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the controls</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Policy</p></li>
<li><p><strong>published_copy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you want to publish the policy else it will be deployed in Drafts mode.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the protocol</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules can be applied using the policy</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the match strategy</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">application</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">asm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">avr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">carp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">classify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clonePool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieInsert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiePassive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieRewrite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">decompress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expirySecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facility</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forward</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - This action will affect forwarding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReply</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ifile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internalVirtual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">l7dos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">length</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ltmPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">member</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netmask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nexthop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">persist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This action will direct the stream to this pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateclass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remove</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseAdapt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">select</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snatpool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSessionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpNagle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wam</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherBits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUsage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceMake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">equals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greater</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greaterOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpBasicAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpReferer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpSetCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUserAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last15secs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last1min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last5mins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">less</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lessOrEqual</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">local</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">major</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">missing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">not</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">org</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathSegment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">present</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslExtension</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHandshake</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslServerHello</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If Rule is used then you need to provide the tm_name it can be any value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unnamedQueryParameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAgentToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Policy</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Pool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">Pool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_nat=None</em>, <em class="sig-param">allow_snat=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">load_balancing_mode=None</em>, <em class="sig-param">monitors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">reselect_tries=None</em>, <em class="sig-param">service_down_action=None</em>, <em class="sig-param">slow_ramp_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.Pool</span></code> Manages a pool configuration.</p>
<p>Resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_nat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow NAT</p></li>
<li><p><strong>allow_snat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow SNAT</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Userdefined value to describe the pool</p></li>
<li><p><strong>load_balancing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values: round-robin, …</p></li>
<li><p><strong>monitors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of monitor names to associate with the pool</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>reselect_tries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of times the system tries to select a new pool member after a failure.</p></li>
<li><p><strong>service_down_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values: none, reset, reselect, drop</p></li>
<li><p><strong>slow_ramp_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Slow ramp time for pool members</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.allow_nat">
<code class="sig-name descname">allow_nat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.allow_nat" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow NAT</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.allow_snat">
<code class="sig-name descname">allow_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.allow_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow SNAT</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Userdefined value to describe the pool</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.load_balancing_mode">
<code class="sig-name descname">load_balancing_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.load_balancing_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Possible values: round-robin, …</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.monitors">
<code class="sig-name descname">monitors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.monitors" title="Permalink to this definition">¶</a></dt>
<dd><p>List of monitor names to associate with the pool</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the pool</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.reselect_tries">
<code class="sig-name descname">reselect_tries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.reselect_tries" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of times the system tries to select a new pool member after a failure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.service_down_action">
<code class="sig-name descname">service_down_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.service_down_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Possible values: none, reset, reselect, drop</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Pool.slow_ramp_time">
<code class="sig-name descname">slow_ramp_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.slow_ramp_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Slow ramp time for pool members</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Pool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_nat=None</em>, <em class="sig-param">allow_snat=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">load_balancing_mode=None</em>, <em class="sig-param">monitors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">reselect_tries=None</em>, <em class="sig-param">service_down_action=None</em>, <em class="sig-param">slow_ramp_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_nat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow NAT</p></li>
<li><p><strong>allow_snat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allow SNAT</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Userdefined value to describe the pool</p></li>
<li><p><strong>load_balancing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values: round-robin, …</p></li>
<li><p><strong>monitors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of monitor names to associate with the pool</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>reselect_tries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of times the system tries to select a new pool member after a failure.</p></li>
<li><p><strong>service_down_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values: none, reset, reselect, drop</p></li>
<li><p><strong>slow_ramp_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Slow ramp time for pool members</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Pool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Pool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PoolAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">PoolAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">node=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.PoolAttachment</span></code> Manages nodes membership in pools</p>
<p>Resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<p>Note: node must be the full path to the node followed by the port. For example /Common/my-node:80</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Node to add to the pool in /Partition/NodeName:Port format (e.g. /Common/Node01:80)</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool in /Partition/Name format</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PoolAttachment.node">
<code class="sig-name descname">node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment.node" title="Permalink to this definition">¶</a></dt>
<dd><p>Node to add to the pool in /Partition/NodeName:Port format (e.g. /Common/Node01:80)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.PoolAttachment.pool">
<code class="sig-name descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the pool in /Partition/Name format</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PoolAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">node=None</em>, <em class="sig-param">pool=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PoolAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Node to add to the pool in /Partition/NodeName:Port format (e.g. /Common/Node01:80)</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool in /Partition/Name format</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.PoolAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.PoolAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.PoolAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileClientSsl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_timeout=None</em>, <em class="sig-param">allow_non_ssl=None</em>, <em class="sig-param">authenticate=None</em>, <em class="sig-param">authenticate_depth=None</em>, <em class="sig-param">ca_file=None</em>, <em class="sig-param">cache_size=None</em>, <em class="sig-param">cache_timeout=None</em>, <em class="sig-param">cert=None</em>, <em class="sig-param">cert_extension_includes=None</em>, <em class="sig-param">cert_key_chains=None</em>, <em class="sig-param">cert_life_span=None</em>, <em class="sig-param">cert_lookup_by_ipaddr_port=None</em>, <em class="sig-param">chain=None</em>, <em class="sig-param">ciphers=None</em>, <em class="sig-param">client_cert_ca=None</em>, <em class="sig-param">crl_file=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">forward_proxy_bypass_default_action=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">generic_alert=None</em>, <em class="sig-param">handshake_timeout=None</em>, <em class="sig-param">inherit_cert_keychain=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">mod_ssl_methods=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">passphrase=None</em>, <em class="sig-param">peer_cert_mode=None</em>, <em class="sig-param">proxy_ca_cert=None</em>, <em class="sig-param">proxy_ca_key=None</em>, <em class="sig-param">proxy_ca_passphrase=None</em>, <em class="sig-param">proxy_ssl=None</em>, <em class="sig-param">proxy_ssl_passthrough=None</em>, <em class="sig-param">renegotiate_period=None</em>, <em class="sig-param">renegotiate_size=None</em>, <em class="sig-param">renegotiation=None</em>, <em class="sig-param">retain_certificate=None</em>, <em class="sig-param">secure_renegotiation=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">session_mirroring=None</em>, <em class="sig-param">session_ticket=None</em>, <em class="sig-param">sni_default=None</em>, <em class="sig-param">sni_require=None</em>, <em class="sig-param">ssl_forward_proxy=None</em>, <em class="sig-param">ssl_forward_proxy_bypass=None</em>, <em class="sig-param">ssl_sign_hash=None</em>, <em class="sig-param">strict_resume=None</em>, <em class="sig-param">tm_options=None</em>, <em class="sig-param">unclean_shutdown=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileClientSsl</span></code> Manages client SSL profiles on a BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert time out</p></li>
<li><p><strong>allow_non_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>authenticate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the frequency of client authentication for an SSL session.When <code class="docutils literal notranslate"><span class="pre">once</span></code>,specifies that the system authenticates the client once for an SSL session.
When <code class="docutils literal notranslate"><span class="pre">always</span></code>, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.</p></li>
<li><p><strong>authenticate_depth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of certificates to be traversed in a client certificate chain</p></li>
<li><p><strong>ca_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client certificate file path. Default None.</p></li>
<li><p><strong>cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache size (sessions).</p></li>
<li><p><strong>cache_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache time out</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a cert name for use.</p></li>
<li><p><strong>cert_extension_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cert extension includes for ssl forward proxy</p></li>
<li><p><strong>cert_life_span</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Life span of the certificate in days for ssl forward proxy</p></li>
<li><p><strong>cert_lookup_by_ipaddr_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cert lookup by ip address and port enabled / disabled</p></li>
<li><p><strong>chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional</p></li>
<li><p><strong>ciphers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p></li>
<li><p><strong>client_cert_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – client certificate name</p></li>
<li><p><strong>crl_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate revocation file name</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the <code class="docutils literal notranslate"><span class="pre">clientssl</span></code> parent on the <code class="docutils literal notranslate"><span class="pre">Common</span></code> partition.</p></li>
<li><p><strong>forward_proxy_bypass_default_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Forward proxy bypass default action. (enabled / disabled)</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – full path of the profile</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – generation</p></li>
<li><p><strong>generic_alert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Generic alerts enabled / disabled.</p></li>
<li><p><strong>handshake_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Handshake time out (seconds)</p></li>
<li><p><strong>inherit_cert_keychain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit cert key chain</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a key name</p></li>
<li><p><strong>mod_ssl_methods</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device partition to manage resources on.</p></li>
<li><p><strong>passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Certificate Constrained Delegation CA passphrase</p></li>
<li><p><strong>peer_cert_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p></li>
<li><p><strong>proxy_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Cert</p></li>
<li><p><strong>proxy_ca_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Key</p></li>
<li><p><strong>proxy_ca_passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Passphrase</p></li>
<li><p><strong>proxy_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL enabled / disabled. Default is disabled.</p></li>
<li><p><strong>proxy_ssl_passthrough</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL passthrough enabled / disabled. Default is disabled.</p></li>
<li><p><strong>renegotiate_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Period (seconds)</p></li>
<li><p><strong>renegotiate_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Size</p></li>
<li><p><strong>renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>retain_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p></li>
<li><p><strong>secure_renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p></li>
<li><p><strong>session_mirroring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Mirroring (enabled / disabled)</p></li>
<li><p><strong>session_ticket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Ticket (enabled / disabled)</p></li>
<li><p><strong>sni_default</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p></li>
<li><p><strong>sni_require</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>ssl_forward_proxy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy (enabled / disabled)</p></li>
<li><p><strong>ssl_forward_proxy_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy Bypass (enabled / disabled)</p></li>
<li><p><strong>ssl_sign_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL sign hash (any, sha1, sha256, sha384)</p></li>
<li><p><strong>strict_resume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p></li>
<li><p><strong>unclean_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (enabled / disabled)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cert_key_chains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a cert name for use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains a key name</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passphrase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.alert_timeout">
<code class="sig-name descname">alert_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.alert_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert time out</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.allow_non_ssl">
<code class="sig-name descname">allow_non_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.allow_non_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.authenticate">
<code class="sig-name descname">authenticate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.authenticate" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the frequency of client authentication for an SSL session.When <code class="docutils literal notranslate"><span class="pre">once</span></code>,specifies that the system authenticates the client once for an SSL session.
When <code class="docutils literal notranslate"><span class="pre">always</span></code>, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.authenticate_depth">
<code class="sig-name descname">authenticate_depth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.authenticate_depth" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of certificates to be traversed in a client certificate chain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.ca_file">
<code class="sig-name descname">ca_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.ca_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Client certificate file path. Default None.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cache_size">
<code class="sig-name descname">cache_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cache_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Cache size (sessions).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cache_timeout">
<code class="sig-name descname">cache_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cache_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Cache time out</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cert">
<code class="sig-name descname">cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a cert name for use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cert_extension_includes">
<code class="sig-name descname">cert_extension_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cert_extension_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Cert extension includes for ssl forward proxy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cert_life_span">
<code class="sig-name descname">cert_life_span</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cert_life_span" title="Permalink to this definition">¶</a></dt>
<dd><p>Life span of the certificate in days for ssl forward proxy</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.cert_lookup_by_ipaddr_port">
<code class="sig-name descname">cert_lookup_by_ipaddr_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.cert_lookup_by_ipaddr_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Cert lookup by ip address and port enabled / disabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.chain">
<code class="sig-name descname">chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.ciphers">
<code class="sig-name descname">ciphers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.ciphers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.client_cert_ca">
<code class="sig-name descname">client_cert_ca</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.client_cert_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>client certificate name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.crl_file">
<code class="sig-name descname">crl_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.crl_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate revocation file name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the <code class="docutils literal notranslate"><span class="pre">clientssl</span></code> parent on the <code class="docutils literal notranslate"><span class="pre">Common</span></code> partition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.forward_proxy_bypass_default_action">
<code class="sig-name descname">forward_proxy_bypass_default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.forward_proxy_bypass_default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Forward proxy bypass default action. (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.full_path">
<code class="sig-name descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>full path of the profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.generation">
<code class="sig-name descname">generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.generation" title="Permalink to this definition">¶</a></dt>
<dd><p>generation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.generic_alert">
<code class="sig-name descname">generic_alert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.generic_alert" title="Permalink to this definition">¶</a></dt>
<dd><p>Generic alerts enabled / disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.handshake_timeout">
<code class="sig-name descname">handshake_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.handshake_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Handshake time out (seconds)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.inherit_cert_keychain">
<code class="sig-name descname">inherit_cert_keychain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.inherit_cert_keychain" title="Permalink to this definition">¶</a></dt>
<dd><p>Inherit cert key chain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a key name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.mod_ssl_methods">
<code class="sig-name descname">mod_ssl_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.mod_ssl_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>ModSSL Methods enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>ModSSL Methods enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Device partition to manage resources on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.passphrase">
<code class="sig-name descname">passphrase</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.passphrase" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Certificate Constrained Delegation CA passphrase</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.peer_cert_mode">
<code class="sig-name descname">peer_cert_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.peer_cert_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_cert">
<code class="sig-name descname">proxy_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy CA Cert</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_key">
<code class="sig-name descname">proxy_ca_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy CA Key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_passphrase">
<code class="sig-name descname">proxy_ca_passphrase</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ca_passphrase" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy CA Passphrase</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ssl">
<code class="sig-name descname">proxy_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy SSL enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ssl_passthrough">
<code class="sig-name descname">proxy_ssl_passthrough</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.proxy_ssl_passthrough" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy SSL passthrough enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.renegotiate_period">
<code class="sig-name descname">renegotiate_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.renegotiate_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Renogotiate Period (seconds)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.renegotiate_size">
<code class="sig-name descname">renegotiate_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.renegotiate_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Renogotiate Size</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.renegotiation">
<code class="sig-name descname">renegotiation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.renegotiation" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.retain_certificate">
<code class="sig-name descname">retain_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.retain_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.secure_renegotiation">
<code class="sig-name descname">secure_renegotiation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.secure_renegotiation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.session_mirroring">
<code class="sig-name descname">session_mirroring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.session_mirroring" title="Permalink to this definition">¶</a></dt>
<dd><p>Session Mirroring (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.session_ticket">
<code class="sig-name descname">session_ticket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.session_ticket" title="Permalink to this definition">¶</a></dt>
<dd><p>Session Ticket (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.sni_default">
<code class="sig-name descname">sni_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.sni_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.sni_require">
<code class="sig-name descname">sni_require</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.sni_require" title="Permalink to this definition">¶</a></dt>
<dd><p>Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.ssl_forward_proxy">
<code class="sig-name descname">ssl_forward_proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.ssl_forward_proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL forward Proxy (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.ssl_forward_proxy_bypass">
<code class="sig-name descname">ssl_forward_proxy_bypass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.ssl_forward_proxy_bypass" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL forward Proxy Bypass (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.ssl_sign_hash">
<code class="sig-name descname">ssl_sign_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.ssl_sign_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL sign hash (any, sha1, sha256, sha384)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.strict_resume">
<code class="sig-name descname">strict_resume</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.strict_resume" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.unclean_shutdown">
<code class="sig-name descname">unclean_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.unclean_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Unclean Shutdown (enabled / disabled)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_timeout=None</em>, <em class="sig-param">allow_non_ssl=None</em>, <em class="sig-param">authenticate=None</em>, <em class="sig-param">authenticate_depth=None</em>, <em class="sig-param">ca_file=None</em>, <em class="sig-param">cache_size=None</em>, <em class="sig-param">cache_timeout=None</em>, <em class="sig-param">cert=None</em>, <em class="sig-param">cert_extension_includes=None</em>, <em class="sig-param">cert_key_chains=None</em>, <em class="sig-param">cert_life_span=None</em>, <em class="sig-param">cert_lookup_by_ipaddr_port=None</em>, <em class="sig-param">chain=None</em>, <em class="sig-param">ciphers=None</em>, <em class="sig-param">client_cert_ca=None</em>, <em class="sig-param">crl_file=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">forward_proxy_bypass_default_action=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">generic_alert=None</em>, <em class="sig-param">handshake_timeout=None</em>, <em class="sig-param">inherit_cert_keychain=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">mod_ssl_methods=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">passphrase=None</em>, <em class="sig-param">peer_cert_mode=None</em>, <em class="sig-param">proxy_ca_cert=None</em>, <em class="sig-param">proxy_ca_key=None</em>, <em class="sig-param">proxy_ca_passphrase=None</em>, <em class="sig-param">proxy_ssl=None</em>, <em class="sig-param">proxy_ssl_passthrough=None</em>, <em class="sig-param">renegotiate_period=None</em>, <em class="sig-param">renegotiate_size=None</em>, <em class="sig-param">renegotiation=None</em>, <em class="sig-param">retain_certificate=None</em>, <em class="sig-param">secure_renegotiation=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">session_mirroring=None</em>, <em class="sig-param">session_ticket=None</em>, <em class="sig-param">sni_default=None</em>, <em class="sig-param">sni_require=None</em>, <em class="sig-param">ssl_forward_proxy=None</em>, <em class="sig-param">ssl_forward_proxy_bypass=None</em>, <em class="sig-param">ssl_sign_hash=None</em>, <em class="sig-param">strict_resume=None</em>, <em class="sig-param">tm_options=None</em>, <em class="sig-param">unclean_shutdown=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileClientSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert time out</p></li>
<li><p><strong>allow_non_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>authenticate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the frequency of client authentication for an SSL session.When <code class="docutils literal notranslate"><span class="pre">once</span></code>,specifies that the system authenticates the client once for an SSL session.
When <code class="docutils literal notranslate"><span class="pre">always</span></code>, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.</p></li>
<li><p><strong>authenticate_depth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of certificates to be traversed in a client certificate chain</p></li>
<li><p><strong>ca_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client certificate file path. Default None.</p></li>
<li><p><strong>cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache size (sessions).</p></li>
<li><p><strong>cache_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache time out</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a cert name for use.</p></li>
<li><p><strong>cert_extension_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cert extension includes for ssl forward proxy</p></li>
<li><p><strong>cert_life_span</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Life span of the certificate in days for ssl forward proxy</p></li>
<li><p><strong>cert_lookup_by_ipaddr_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cert lookup by ip address and port enabled / disabled</p></li>
<li><p><strong>chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional</p></li>
<li><p><strong>ciphers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p></li>
<li><p><strong>client_cert_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – client certificate name</p></li>
<li><p><strong>crl_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Certificate revocation file name</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the <code class="docutils literal notranslate"><span class="pre">clientssl</span></code> parent on the <code class="docutils literal notranslate"><span class="pre">Common</span></code> partition.</p></li>
<li><p><strong>forward_proxy_bypass_default_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Forward proxy bypass default action. (enabled / disabled)</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – full path of the profile</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – generation</p></li>
<li><p><strong>generic_alert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Generic alerts enabled / disabled.</p></li>
<li><p><strong>handshake_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Handshake time out (seconds)</p></li>
<li><p><strong>inherit_cert_keychain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inherit cert key chain</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a key name</p></li>
<li><p><strong>mod_ssl_methods</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device partition to manage resources on.</p></li>
<li><p><strong>passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Certificate Constrained Delegation CA passphrase</p></li>
<li><p><strong>peer_cert_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p></li>
<li><p><strong>proxy_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Cert</p></li>
<li><p><strong>proxy_ca_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Key</p></li>
<li><p><strong>proxy_ca_passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy CA Passphrase</p></li>
<li><p><strong>proxy_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL enabled / disabled. Default is disabled.</p></li>
<li><p><strong>proxy_ssl_passthrough</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL passthrough enabled / disabled. Default is disabled.</p></li>
<li><p><strong>renegotiate_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Period (seconds)</p></li>
<li><p><strong>renegotiate_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Size</p></li>
<li><p><strong>renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>retain_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p></li>
<li><p><strong>secure_renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p></li>
<li><p><strong>session_mirroring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Mirroring (enabled / disabled)</p></li>
<li><p><strong>session_ticket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Ticket (enabled / disabled)</p></li>
<li><p><strong>sni_default</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p></li>
<li><p><strong>sni_require</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>ssl_forward_proxy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy (enabled / disabled)</p></li>
<li><p><strong>ssl_forward_proxy_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy Bypass (enabled / disabled)</p></li>
<li><p><strong>ssl_sign_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL sign hash (any, sha1, sha256, sha384)</p></li>
<li><p><strong>strict_resume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p></li>
<li><p><strong>unclean_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (enabled / disabled)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cert_key_chains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a cert name for use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">chain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains a key name</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">passphrase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileClientSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileClientSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileFastHttp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connpool_maxreuse=None</em>, <em class="sig-param">connpool_maxsize=None</em>, <em class="sig-param">connpool_minsize=None</em>, <em class="sig-param">connpool_replenish=None</em>, <em class="sig-param">connpool_step=None</em>, <em class="sig-param">connpoolidle_timeoutoverride=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">forcehttp10response=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">maxheader_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileFastHttp</span></code> Configures a custom profile_fasthttp for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connpool_maxreuse</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of times that the system can re-use a current connection. The default value is 0 (zero).</p></li>
<li><p><strong>connpool_maxsize</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.</p></li>
<li><p><strong>connpool_minsize</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the minimum number of connections to a load balancing pool. A setting of 0 specifies that there is no minimum. The default value is 10.</p></li>
<li><p><strong>connpool_replenish</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default value is enabled. When this option is enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool. When disabled, the system replenishes the connection that was closed by the server, only when there are fewer connections to the pool than the number of connections set in the connpool-min-size connections option. Also see the connpool-min-size option..</p></li>
<li><p><strong>connpool_step</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the increment in which the system makes additional connections available, when all available connections are in use. The default value is 4.</p></li>
<li><p><strong>connpoolidle_timeoutoverride</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.The value of this option overrides the idle-timeout value that you specify. The default value is 0 (zero) seconds, which disables the override setting.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>forcehttp10response</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to rewrite the HTTP version in the status line of the server to HTTP 1.0 to discourage the client from pipelining or chunking data. The default value is disabled.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p></li>
<li><p><strong>maxheader_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision. The default setting is 32768.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_fasthttp</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpool_maxreuse">
<code class="sig-name descname">connpool_maxreuse</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpool_maxreuse" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of times that the system can re-use a current connection. The default value is 0 (zero).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpool_maxsize">
<code class="sig-name descname">connpool_maxsize</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpool_maxsize" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpool_minsize">
<code class="sig-name descname">connpool_minsize</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpool_minsize" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the minimum number of connections to a load balancing pool. A setting of 0 specifies that there is no minimum. The default value is 10.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpool_replenish">
<code class="sig-name descname">connpool_replenish</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpool_replenish" title="Permalink to this definition">¶</a></dt>
<dd><p>The default value is enabled. When this option is enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool. When disabled, the system replenishes the connection that was closed by the server, only when there are fewer connections to the pool than the number of connections set in the connpool-min-size connections option. Also see the connpool-min-size option..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpool_step">
<code class="sig-name descname">connpool_step</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpool_step" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the increment in which the system makes additional connections available, when all available connections are in use. The default value is 4.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.connpoolidle_timeoutoverride">
<code class="sig-name descname">connpoolidle_timeoutoverride</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.connpoolidle_timeoutoverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.The value of this option overrides the idle-timeout value that you specify. The default value is 0 (zero) seconds, which disables the override setting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.forcehttp10response">
<code class="sig-name descname">forcehttp10response</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.forcehttp10response" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to rewrite the HTTP version in the status line of the server to HTTP 1.0 to discourage the client from pipelining or chunking data. The default value is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.idle_timeout">
<code class="sig-name descname">idle_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.maxheader_size">
<code class="sig-name descname">maxheader_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.maxheader_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision. The default setting is 32768.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_fasthttp</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connpool_maxreuse=None</em>, <em class="sig-param">connpool_maxsize=None</em>, <em class="sig-param">connpool_minsize=None</em>, <em class="sig-param">connpool_replenish=None</em>, <em class="sig-param">connpool_step=None</em>, <em class="sig-param">connpoolidle_timeoutoverride=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">forcehttp10response=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">maxheader_size=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileFastHttp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connpool_maxreuse</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of times that the system can re-use a current connection. The default value is 0 (zero).</p></li>
<li><p><strong>connpool_maxsize</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.</p></li>
<li><p><strong>connpool_minsize</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the minimum number of connections to a load balancing pool. A setting of 0 specifies that there is no minimum. The default value is 10.</p></li>
<li><p><strong>connpool_replenish</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default value is enabled. When this option is enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool. When disabled, the system replenishes the connection that was closed by the server, only when there are fewer connections to the pool than the number of connections set in the connpool-min-size connections option. Also see the connpool-min-size option..</p></li>
<li><p><strong>connpool_step</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the increment in which the system makes additional connections available, when all available connections are in use. The default value is 4.</p></li>
<li><p><strong>connpoolidle_timeoutoverride</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.The value of this option overrides the idle-timeout value that you specify. The default value is 0 (zero) seconds, which disables the override setting.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>forcehttp10response</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to rewrite the HTTP version in the status line of the server to HTTP 1.0 to discourage the client from pipelining or chunking data. The default value is disabled.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p></li>
<li><p><strong>maxheader_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision. The default setting is 32768.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_fasthttp</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileFastHttp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastHttp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileFastL4">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileFastL4</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">explicitflow_migration=None</em>, <em class="sig-param">hardware_syncookie=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">iptos_toclient=None</em>, <em class="sig-param">iptos_toserver=None</em>, <em class="sig-param">keepalive_interval=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileFastL4</span></code> Configures a custom profile_fastl4 for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies late binding client timeout in seconds. This setting specifies the number of seconds allowed for a client to transmit enough data to select a server when late binding is enabled. If it expires timeout-recovery mode will dictate what action to take.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>explicitflow_migration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables late binding explicit flow migration that allows iRules to control when flows move from software to hardware. Explicit flow migration is disabled by default hence BIG-IP automatically migrates flows from software to hardware.</p></li>
<li><p><strong>hardware_syncookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables hardware SYN cookie support when PVA10 is present on the system. Note that when you set the hardware syncookie option to enabled, you may also want to set the following bigdb database variables using the “/sys modify db” command, based on your requirements: pva.SynCookies.Full.ConnectionThreshold (default: 500000), pva.SynCookies.Assist.ConnectionThreshold (default: 500000) pva.SynCookies.ClientWindow (default: 0). The default value is disabled.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p></li>
<li><p><strong>iptos_toclient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP ToS number for the client side. This option specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to clients. The default value is 65535 (pass-through), which indicates, do not modify.</p></li>
<li><p><strong>iptos_toserver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP ToS number for the server side. This setting specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to servers. The default value is 65535 (pass-through), which indicates, do not modify.</p></li>
<li><p><strong>keepalive_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the keep alive probe interval, in seconds. The default value is disabled (0 seconds).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_fastl4</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.client_timeout">
<code class="sig-name descname">client_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.client_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies late binding client timeout in seconds. This setting specifies the number of seconds allowed for a client to transmit enough data to select a server when late binding is enabled. If it expires timeout-recovery mode will dictate what action to take.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.explicitflow_migration">
<code class="sig-name descname">explicitflow_migration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.explicitflow_migration" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables late binding explicit flow migration that allows iRules to control when flows move from software to hardware. Explicit flow migration is disabled by default hence BIG-IP automatically migrates flows from software to hardware.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.hardware_syncookie">
<code class="sig-name descname">hardware_syncookie</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.hardware_syncookie" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables hardware SYN cookie support when PVA10 is present on the system. Note that when you set the hardware syncookie option to enabled, you may also want to set the following bigdb database variables using the “/sys modify db” command, based on your requirements: pva.SynCookies.Full.ConnectionThreshold (default: 500000), pva.SynCookies.Assist.ConnectionThreshold (default: 500000) pva.SynCookies.ClientWindow (default: 0). The default value is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.idle_timeout">
<code class="sig-name descname">idle_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.iptos_toclient">
<code class="sig-name descname">iptos_toclient</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.iptos_toclient" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an IP ToS number for the client side. This option specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to clients. The default value is 65535 (pass-through), which indicates, do not modify.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.iptos_toserver">
<code class="sig-name descname">iptos_toserver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.iptos_toserver" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an IP ToS number for the server side. This setting specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to servers. The default value is 65535 (pass-through), which indicates, do not modify.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.keepalive_interval">
<code class="sig-name descname">keepalive_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.keepalive_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the keep alive probe interval, in seconds. The default value is disabled (0 seconds).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_fastl4</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays the administrative partition within which this profile resides</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">explicitflow_migration=None</em>, <em class="sig-param">hardware_syncookie=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">iptos_toclient=None</em>, <em class="sig-param">iptos_toserver=None</em>, <em class="sig-param">keepalive_interval=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileFastL4 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies late binding client timeout in seconds. This setting specifies the number of seconds allowed for a client to transmit enough data to select a server when late binding is enabled. If it expires timeout-recovery mode will dictate what action to take.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>explicitflow_migration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables late binding explicit flow migration that allows iRules to control when flows move from software to hardware. Explicit flow migration is disabled by default hence BIG-IP automatically migrates flows from software to hardware.</p></li>
<li><p><strong>hardware_syncookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables hardware SYN cookie support when PVA10 is present on the system. Note that when you set the hardware syncookie option to enabled, you may also want to set the following bigdb database variables using the “/sys modify db” command, based on your requirements: pva.SynCookies.Full.ConnectionThreshold (default: 500000), pva.SynCookies.Assist.ConnectionThreshold (default: 500000) pva.SynCookies.ClientWindow (default: 0). The default value is disabled.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.</p></li>
<li><p><strong>iptos_toclient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP ToS number for the client side. This option specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to clients. The default value is 65535 (pass-through), which indicates, do not modify.</p></li>
<li><p><strong>iptos_toserver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP ToS number for the server side. This setting specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to servers. The default value is 65535 (pass-through), which indicates, do not modify.</p></li>
<li><p><strong>keepalive_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the keep alive probe interval, in seconds. The default value is disabled (0 seconds).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_fastl4</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileFastL4.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileFastL4.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileHttp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accept_xff=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">basic_auth_realm=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypt_cookie_secret=None</em>, <em class="sig-param">encrypt_cookies=None</em>, <em class="sig-param">fallback_host=None</em>, <em class="sig-param">fallback_status_codes=None</em>, <em class="sig-param">head_erase=None</em>, <em class="sig-param">head_insert=None</em>, <em class="sig-param">insert_xforwarded_for=None</em>, <em class="sig-param">lws_separator=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oneconnect_transformations=None</em>, <em class="sig-param">proxy_type=None</em>, <em class="sig-param">redirect_rewrite=None</em>, <em class="sig-param">request_chunking=None</em>, <em class="sig-param">response_chunking=None</em>, <em class="sig-param">response_headers_permitteds=None</em>, <em class="sig-param">server_agent_name=None</em>, <em class="sig-param">tm_partition=None</em>, <em class="sig-param">via_host_name=None</em>, <em class="sig-param">via_request=None</em>, <em class="sig-param">via_response=None</em>, <em class="sig-param">xff_alternative_names=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileHttp</span></code> Configures a custom profile_http for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accept_xff</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request’s
XFF (X-forwarded-for) headers, if they exist.</p></li>
<li><p><strong>app_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application service to which the object belongs.</p></li>
<li><p><strong>basic_auth_realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User defibned description</p></li>
<li><p><strong>encrypt_cookie_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a passphrase for the cookie encryption</p></li>
<li><p><strong>encrypt_cookies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Encrypts specified cookies that the BIG-IP system sends to a client system</p></li>
<li><p><strong>fallback_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number</p></li>
<li><p><strong>fallback_status_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more three-digit status codes that can be returned by an HTTP server.</p></li>
<li><p><strong>head_erase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the header string that you want to erase from an HTTP request. You can also specify none</p></li>
<li><p><strong>head_insert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted header string that you want to insert into an HTTP request</p></li>
<li><p><strong>insert_xforwarded_for</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When using connection pooling, which allows clients to make use of other client requests’ server-side connections, you can insert the X-Forwarded-For header and specify a client IP address</p></li>
<li><p><strong>lws_separator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_http</p></li>
<li><p><strong>oneconnect_transformations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile</p></li>
<li><p><strong>proxy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of HTTP proxy.</p></li>
<li><p><strong>redirect_rewrite</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies which of the application HTTP redirects the system rewrites to HTTPS.</p></li>
<li><p><strong>request_chunking</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle chunked and unchunked requests.</p></li>
<li><p><strong>response_chunking</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle chunked and unchunked responses.</p></li>
<li><p><strong>response_headers_permitteds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies headers that the BIG-IP system allows in an HTTP response.</p></li>
<li><p><strong>server_agent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses</p></li>
<li><p><strong>tm_partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides.</p></li>
<li><p><strong>via_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the hostname to include into Via header</p></li>
<li><p><strong>via_request</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to append, remove, or preserve a Via header in an HTTP request</p></li>
<li><p><strong>via_response</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to append, remove, or preserve a Via header in an HTTP request</p></li>
<li><p><strong>xff_alternative_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies alternative XFF headers instead of the default X-forwarded-for header</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.accept_xff">
<code class="sig-name descname">accept_xff</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.accept_xff" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request’s
XFF (X-forwarded-for) headers, if they exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.app_service">
<code class="sig-name descname">app_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.app_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The application service to which the object belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.basic_auth_realm">
<code class="sig-name descname">basic_auth_realm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.basic_auth_realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>User defibned description</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.encrypt_cookie_secret">
<code class="sig-name descname">encrypt_cookie_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.encrypt_cookie_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a passphrase for the cookie encryption</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.encrypt_cookies">
<code class="sig-name descname">encrypt_cookies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.encrypt_cookies" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypts specified cookies that the BIG-IP system sends to a client system</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.fallback_host">
<code class="sig-name descname">fallback_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.fallback_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.fallback_status_codes">
<code class="sig-name descname">fallback_status_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.fallback_status_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies one or more three-digit status codes that can be returned by an HTTP server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.head_erase">
<code class="sig-name descname">head_erase</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.head_erase" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the header string that you want to erase from an HTTP request. You can also specify none</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.head_insert">
<code class="sig-name descname">head_insert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.head_insert" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a quoted header string that you want to insert into an HTTP request</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.insert_xforwarded_for">
<code class="sig-name descname">insert_xforwarded_for</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.insert_xforwarded_for" title="Permalink to this definition">¶</a></dt>
<dd><p>When using connection pooling, which allows clients to make use of other client requests’ server-side connections, you can insert the X-Forwarded-For header and specify a client IP address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.lws_separator">
<code class="sig-name descname">lws_separator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.lws_separator" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_http</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.oneconnect_transformations">
<code class="sig-name descname">oneconnect_transformations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.oneconnect_transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.proxy_type">
<code class="sig-name descname">proxy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.proxy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of HTTP proxy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.redirect_rewrite">
<code class="sig-name descname">redirect_rewrite</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.redirect_rewrite" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies which of the application HTTP redirects the system rewrites to HTTPS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.request_chunking">
<code class="sig-name descname">request_chunking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.request_chunking" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle chunked and unchunked requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.response_chunking">
<code class="sig-name descname">response_chunking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.response_chunking" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle chunked and unchunked responses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.response_headers_permitteds">
<code class="sig-name descname">response_headers_permitteds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.response_headers_permitteds" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies headers that the BIG-IP system allows in an HTTP response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.server_agent_name">
<code class="sig-name descname">server_agent_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.server_agent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.tm_partition">
<code class="sig-name descname">tm_partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.tm_partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays the administrative partition within which this profile resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.via_host_name">
<code class="sig-name descname">via_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.via_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the hostname to include into Via header</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.via_request">
<code class="sig-name descname">via_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.via_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to append, remove, or preserve a Via header in an HTTP request</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.via_response">
<code class="sig-name descname">via_response</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.via_response" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to append, remove, or preserve a Via header in an HTTP request</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.xff_alternative_names">
<code class="sig-name descname">xff_alternative_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.xff_alternative_names" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies alternative XFF headers instead of the default X-forwarded-for header</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accept_xff=None</em>, <em class="sig-param">app_service=None</em>, <em class="sig-param">basic_auth_realm=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypt_cookie_secret=None</em>, <em class="sig-param">encrypt_cookies=None</em>, <em class="sig-param">fallback_host=None</em>, <em class="sig-param">fallback_status_codes=None</em>, <em class="sig-param">head_erase=None</em>, <em class="sig-param">head_insert=None</em>, <em class="sig-param">insert_xforwarded_for=None</em>, <em class="sig-param">lws_separator=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oneconnect_transformations=None</em>, <em class="sig-param">proxy_type=None</em>, <em class="sig-param">redirect_rewrite=None</em>, <em class="sig-param">request_chunking=None</em>, <em class="sig-param">response_chunking=None</em>, <em class="sig-param">response_headers_permitteds=None</em>, <em class="sig-param">server_agent_name=None</em>, <em class="sig-param">tm_partition=None</em>, <em class="sig-param">via_host_name=None</em>, <em class="sig-param">via_request=None</em>, <em class="sig-param">via_response=None</em>, <em class="sig-param">xff_alternative_names=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileHttp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accept_xff</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request’s
XFF (X-forwarded-for) headers, if they exist.</p></li>
<li><p><strong>app_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application service to which the object belongs.</p></li>
<li><p><strong>basic_auth_realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User defibned description</p></li>
<li><p><strong>encrypt_cookie_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a passphrase for the cookie encryption</p></li>
<li><p><strong>encrypt_cookies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Encrypts specified cookies that the BIG-IP system sends to a client system</p></li>
<li><p><strong>fallback_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number</p></li>
<li><p><strong>fallback_status_codes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more three-digit status codes that can be returned by an HTTP server.</p></li>
<li><p><strong>head_erase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the header string that you want to erase from an HTTP request. You can also specify none</p></li>
<li><p><strong>head_insert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted header string that you want to insert into an HTTP request</p></li>
<li><p><strong>insert_xforwarded_for</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When using connection pooling, which allows clients to make use of other client requests’ server-side connections, you can insert the X-Forwarded-For header and specify a client IP address</p></li>
<li><p><strong>lws_separator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_http</p></li>
<li><p><strong>oneconnect_transformations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile</p></li>
<li><p><strong>proxy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of HTTP proxy.</p></li>
<li><p><strong>redirect_rewrite</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies which of the application HTTP redirects the system rewrites to HTTPS.</p></li>
<li><p><strong>request_chunking</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle chunked and unchunked requests.</p></li>
<li><p><strong>response_chunking</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle chunked and unchunked responses.</p></li>
<li><p><strong>response_headers_permitteds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies headers that the BIG-IP system allows in an HTTP response.</p></li>
<li><p><strong>server_agent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses</p></li>
<li><p><strong>tm_partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides.</p></li>
<li><p><strong>via_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the hostname to include into Via header</p></li>
<li><p><strong>via_request</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to append, remove, or preserve a Via header in an HTTP request</p></li>
<li><p><strong>via_response</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to append, remove, or preserve a Via header in an HTTP request</p></li>
<li><p><strong>xff_alternative_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies alternative XFF headers instead of the default X-forwarded-for header</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttp2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileHttp2</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_modes=None</em>, <em class="sig-param">concurrent_streams_per_connection=None</em>, <em class="sig-param">connection_idle_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">header_table_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileHttp2</span></code> Configures a custom profile_http2 for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_modes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies what will cause an incoming connection to be handled as a HTTP/2 connection. The default values npn and alpn specify that the TLS next-protocol-negotiation and application-layer-protocol-negotiation extensions will be used.</p></li>
<li><p><strong>concurrent_streams_per_connection</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.</p></li>
<li><p><strong>connection_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection is eligible for deletion..</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>header_table_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the parent Http2 profile</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_http2</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.activation_modes">
<code class="sig-name descname">activation_modes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.activation_modes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what will cause an incoming connection to be handled as a HTTP/2 connection. The default values npn and alpn specify that the TLS next-protocol-negotiation and application-layer-protocol-negotiation extensions will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.concurrent_streams_per_connection">
<code class="sig-name descname">concurrent_streams_per_connection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.concurrent_streams_per_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.connection_idle_timeout">
<code class="sig-name descname">connection_idle_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.connection_idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection is idle before the connection is eligible for deletion..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.header_table_size">
<code class="sig-name descname">header_table_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.header_table_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the parent Http2 profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_http2</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">activation_modes=None</em>, <em class="sig-param">concurrent_streams_per_connection=None</em>, <em class="sig-param">connection_idle_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">header_table_size=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileHttp2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_modes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies what will cause an incoming connection to be handled as a HTTP/2 connection. The default values npn and alpn specify that the TLS next-protocol-negotiation and application-layer-protocol-negotiation extensions will be used.</p></li>
<li><p><strong>concurrent_streams_per_connection</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.</p></li>
<li><p><strong>connection_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection is eligible for deletion..</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>header_table_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the parent Http2 profile</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_http2</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttp2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttp2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileHttpCompress</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type_excludes=None</em>, <em class="sig-param">content_type_includes=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">uri_excludes=None</em>, <em class="sig-param">uri_includes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileHttpCompress</span></code>  Virtual server HTTP compression profile configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Excludes a specified list of content types from compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p></li>
<li><p><strong>content_type_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a list of content types for compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_httpcompress</p></li>
<li><p><strong>uri_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Disables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you do not want to compress.</p></li>
<li><p><strong>uri_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you want to compress.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.content_type_excludes">
<code class="sig-name descname">content_type_excludes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.content_type_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>Excludes a specified list of content types from compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.content_type_includes">
<code class="sig-name descname">content_type_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.content_type_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a list of content types for compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_httpcompress</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.uri_excludes">
<code class="sig-name descname">uri_excludes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.uri_excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>Disables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you do not want to compress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.uri_includes">
<code class="sig-name descname">uri_includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.uri_includes" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you want to compress.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type_excludes=None</em>, <em class="sig-param">content_type_includes=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">uri_excludes=None</em>, <em class="sig-param">uri_includes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileHttpCompress resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Excludes a specified list of content types from compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p></li>
<li><p><strong>content_type_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a list of content types for compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_httpcompress</p></li>
<li><p><strong>uri_excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Disables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you do not want to compress.</p></li>
<li><p><strong>uri_includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you want to compress.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileHttpCompress.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileHttpCompress.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileOneConnect</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">idle_timeout_override=None</em>, <em class="sig-param">max_age=None</em>, <em class="sig-param">max_reuse=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">share_pools=None</em>, <em class="sig-param">source_mask=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileOneConnect</span></code> Configures a custom profile_oneconnect for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>idle_timeout_override</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion. Possible values are disabled, indefinite, or a numeric value that you specify. The default value is disabled.</p></li>
<li><p><strong>max_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum age in number of seconds allowed for a connection in the connection reuse pool. For any connection with an age higher than this value, the system removes that connection from the reuse pool. The default value is 86400.</p></li>
<li><p><strong>max_reuse</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of times that a server-side connection can be reused. The default value is 1000.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections that the system holds in the connection reuse pool. If the pool is already full, then the server-side connection closes after the response is completed. The default value is 10000.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_oneconnect</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
<li><p><strong>share_pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify if you want to share the pool, default value is “disabled”</p></li>
<li><p><strong>source_mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a source IP mask. The default value is 0.0.0.0. The system applies the value of this option to the source address to determine its eligibility for reuse. A mask of 0.0.0.0 causes the system to share reused connections across all clients. A host mask (all 1’s in binary), causes the system to share only those reused connections originating from the same client IP address.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.idle_timeout_override">
<code class="sig-name descname">idle_timeout_override</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.idle_timeout_override" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion. Possible values are disabled, indefinite, or a numeric value that you specify. The default value is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.max_age">
<code class="sig-name descname">max_age</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.max_age" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum age in number of seconds allowed for a connection in the connection reuse pool. For any connection with an age higher than this value, the system removes that connection from the reuse pool. The default value is 86400.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.max_reuse">
<code class="sig-name descname">max_reuse</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.max_reuse" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of times that a server-side connection can be reused. The default value is 1000.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of connections that the system holds in the connection reuse pool. If the pool is already full, then the server-side connection closes after the response is completed. The default value is 10000.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_oneconnect</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays the administrative partition within which this profile resides</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.share_pools">
<code class="sig-name descname">share_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.share_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify if you want to share the pool, default value is “disabled”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.source_mask">
<code class="sig-name descname">source_mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.source_mask" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a source IP mask. The default value is 0.0.0.0. The system applies the value of this option to the source address to determine its eligibility for reuse. A mask of 0.0.0.0 causes the system to share reused connections across all clients. A host mask (all 1’s in binary), causes the system to share only those reused connections originating from the same client IP address.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">idle_timeout_override=None</em>, <em class="sig-param">max_age=None</em>, <em class="sig-param">max_reuse=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">share_pools=None</em>, <em class="sig-param">source_mask=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileOneConnect resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>idle_timeout_override</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion. Possible values are disabled, indefinite, or a numeric value that you specify. The default value is disabled.</p></li>
<li><p><strong>max_age</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum age in number of seconds allowed for a connection in the connection reuse pool. For any connection with an age higher than this value, the system removes that connection from the reuse pool. The default value is 86400.</p></li>
<li><p><strong>max_reuse</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of times that a server-side connection can be reused. The default value is 1000.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of connections that the system holds in the connection reuse pool. If the pool is already full, then the server-side connection closes after the response is completed. The default value is 10000.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_oneconnect</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
<li><p><strong>share_pools</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify if you want to share the pool, default value is “disabled”</p></li>
<li><p><strong>source_mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a source IP mask. The default value is 0.0.0.0. The system applies the value of this option to the source address to determine its eligibility for reuse. A mask of 0.0.0.0 causes the system to share reused connections across all clients. A host mask (all 1’s in binary), causes the system to share only those reused connections originating from the same client IP address.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileOneConnect.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileOneConnect.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileServerSsl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_timeout=None</em>, <em class="sig-param">authenticate=None</em>, <em class="sig-param">authenticate_depth=None</em>, <em class="sig-param">ca_file=None</em>, <em class="sig-param">cache_size=None</em>, <em class="sig-param">cache_timeout=None</em>, <em class="sig-param">cert=None</em>, <em class="sig-param">chain=None</em>, <em class="sig-param">ciphers=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">expire_cert_response_control=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">generic_alert=None</em>, <em class="sig-param">handshake_timeout=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">mod_ssl_methods=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">passphrase=None</em>, <em class="sig-param">peer_cert_mode=None</em>, <em class="sig-param">proxy_ssl=None</em>, <em class="sig-param">renegotiate_period=None</em>, <em class="sig-param">renegotiate_size=None</em>, <em class="sig-param">renegotiation=None</em>, <em class="sig-param">retain_certificate=None</em>, <em class="sig-param">secure_renegotiation=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">session_mirroring=None</em>, <em class="sig-param">session_ticket=None</em>, <em class="sig-param">sni_default=None</em>, <em class="sig-param">sni_require=None</em>, <em class="sig-param">ssl_forward_proxy=None</em>, <em class="sig-param">ssl_forward_proxy_bypass=None</em>, <em class="sig-param">ssl_sign_hash=None</em>, <em class="sig-param">strict_resume=None</em>, <em class="sig-param">tm_options=None</em>, <em class="sig-param">unclean_shutdown=None</em>, <em class="sig-param">untrusted_cert_response_control=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileServerSsl</span></code> Manages server SSL profiles on a BIG-IP</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert time out</p></li>
<li><p><strong>authenticate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Server authentication once / always (default is once).</p></li>
<li><p><strong>authenticate_depth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Client certificate chain traversal depth. Default 9.</p></li>
<li><p><strong>ca_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client certificate file path. Default None.</p></li>
<li><p><strong>cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache size (sessions).</p></li>
<li><p><strong>cache_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache time out</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate that the system uses for server-side SSL processing.</p></li>
<li><p><strong>chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the certificates-key chain to associate with the SSL profile</p></li>
<li><p><strong>ciphers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is <code class="docutils literal notranslate"><span class="pre">/Common/serverssl</span></code>.</p></li>
<li><p><strong>expire_cert_response_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Response if the cert is expired (drop / ignore).</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – full path of the profile</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – generation</p></li>
<li><p><strong>generic_alert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Generic alerts enabled / disabled.</p></li>
<li><p><strong>handshake_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Handshake time out (seconds)</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the file name of the SSL key.</p></li>
<li><p><strong>mod_ssl_methods</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device partition to manage resources on.</p></li>
<li><p><strong>passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Certificate Constrained Delegation CA passphrase</p></li>
<li><p><strong>peer_cert_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p></li>
<li><p><strong>proxy_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL enabled / disabled. Default is disabled.</p></li>
<li><p><strong>renegotiate_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Period (seconds)</p></li>
<li><p><strong>renegotiate_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Size</p></li>
<li><p><strong>renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>retain_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p></li>
<li><p><strong>secure_renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p></li>
<li><p><strong>session_mirroring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Mirroring (enabled / disabled)</p></li>
<li><p><strong>session_ticket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Ticket (enabled / disabled)</p></li>
<li><p><strong>sni_default</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p></li>
<li><p><strong>sni_require</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>ssl_forward_proxy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy (enabled / disabled)</p></li>
<li><p><strong>ssl_forward_proxy_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy Bypass (enabled / disabled)</p></li>
<li><p><strong>ssl_sign_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL sign hash (any, sha1, sha256, sha384)</p></li>
<li><p><strong>strict_resume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p></li>
<li><p><strong>unclean_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (enabled / disabled)</p></li>
<li><p><strong>untrusted_cert_response_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (drop / ignore)</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.alert_timeout">
<code class="sig-name descname">alert_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.alert_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert time out</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.authenticate">
<code class="sig-name descname">authenticate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.authenticate" title="Permalink to this definition">¶</a></dt>
<dd><p>Server authentication once / always (default is once).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.authenticate_depth">
<code class="sig-name descname">authenticate_depth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.authenticate_depth" title="Permalink to this definition">¶</a></dt>
<dd><p>Client certificate chain traversal depth. Default 9.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.ca_file">
<code class="sig-name descname">ca_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.ca_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Client certificate file path. Default None.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.cache_size">
<code class="sig-name descname">cache_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.cache_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Cache size (sessions).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.cache_timeout">
<code class="sig-name descname">cache_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.cache_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Cache time out</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.cert">
<code class="sig-name descname">cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the certificate that the system uses for server-side SSL processing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.chain">
<code class="sig-name descname">chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.chain" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the certificates-key chain to associate with the SSL profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.ciphers">
<code class="sig-name descname">ciphers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.ciphers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is <code class="docutils literal notranslate"><span class="pre">/Common/serverssl</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.expire_cert_response_control">
<code class="sig-name descname">expire_cert_response_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.expire_cert_response_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Response if the cert is expired (drop / ignore).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.full_path">
<code class="sig-name descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>full path of the profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.generation">
<code class="sig-name descname">generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.generation" title="Permalink to this definition">¶</a></dt>
<dd><p>generation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.generic_alert">
<code class="sig-name descname">generic_alert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.generic_alert" title="Permalink to this definition">¶</a></dt>
<dd><p>Generic alerts enabled / disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.handshake_timeout">
<code class="sig-name descname">handshake_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.handshake_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Handshake time out (seconds)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the file name of the SSL key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.mod_ssl_methods">
<code class="sig-name descname">mod_ssl_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.mod_ssl_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>ModSSL Methods enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>ModSSL Methods enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Device partition to manage resources on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.passphrase">
<code class="sig-name descname">passphrase</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.passphrase" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Certificate Constrained Delegation CA passphrase</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.peer_cert_mode">
<code class="sig-name descname">peer_cert_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.peer_cert_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.proxy_ssl">
<code class="sig-name descname">proxy_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.proxy_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy SSL enabled / disabled. Default is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.renegotiate_period">
<code class="sig-name descname">renegotiate_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.renegotiate_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Renogotiate Period (seconds)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.renegotiate_size">
<code class="sig-name descname">renegotiate_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.renegotiate_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Renogotiate Size</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.renegotiation">
<code class="sig-name descname">renegotiation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.renegotiation" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.retain_certificate">
<code class="sig-name descname">retain_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.retain_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.secure_renegotiation">
<code class="sig-name descname">secure_renegotiation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.secure_renegotiation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.session_mirroring">
<code class="sig-name descname">session_mirroring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.session_mirroring" title="Permalink to this definition">¶</a></dt>
<dd><p>Session Mirroring (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.session_ticket">
<code class="sig-name descname">session_ticket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.session_ticket" title="Permalink to this definition">¶</a></dt>
<dd><p>Session Ticket (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.sni_default">
<code class="sig-name descname">sni_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.sni_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.sni_require">
<code class="sig-name descname">sni_require</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.sni_require" title="Permalink to this definition">¶</a></dt>
<dd><p>Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.ssl_forward_proxy">
<code class="sig-name descname">ssl_forward_proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.ssl_forward_proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL forward Proxy (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.ssl_forward_proxy_bypass">
<code class="sig-name descname">ssl_forward_proxy_bypass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.ssl_forward_proxy_bypass" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL forward Proxy Bypass (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.ssl_sign_hash">
<code class="sig-name descname">ssl_sign_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.ssl_sign_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL sign hash (any, sha1, sha256, sha384)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.strict_resume">
<code class="sig-name descname">strict_resume</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.strict_resume" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.unclean_shutdown">
<code class="sig-name descname">unclean_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.unclean_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Unclean Shutdown (enabled / disabled)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.untrusted_cert_response_control">
<code class="sig-name descname">untrusted_cert_response_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.untrusted_cert_response_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Unclean Shutdown (drop / ignore)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_timeout=None</em>, <em class="sig-param">authenticate=None</em>, <em class="sig-param">authenticate_depth=None</em>, <em class="sig-param">ca_file=None</em>, <em class="sig-param">cache_size=None</em>, <em class="sig-param">cache_timeout=None</em>, <em class="sig-param">cert=None</em>, <em class="sig-param">chain=None</em>, <em class="sig-param">ciphers=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">expire_cert_response_control=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">generic_alert=None</em>, <em class="sig-param">handshake_timeout=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">mod_ssl_methods=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">passphrase=None</em>, <em class="sig-param">peer_cert_mode=None</em>, <em class="sig-param">proxy_ssl=None</em>, <em class="sig-param">renegotiate_period=None</em>, <em class="sig-param">renegotiate_size=None</em>, <em class="sig-param">renegotiation=None</em>, <em class="sig-param">retain_certificate=None</em>, <em class="sig-param">secure_renegotiation=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">session_mirroring=None</em>, <em class="sig-param">session_ticket=None</em>, <em class="sig-param">sni_default=None</em>, <em class="sig-param">sni_require=None</em>, <em class="sig-param">ssl_forward_proxy=None</em>, <em class="sig-param">ssl_forward_proxy_bypass=None</em>, <em class="sig-param">ssl_sign_hash=None</em>, <em class="sig-param">strict_resume=None</em>, <em class="sig-param">tm_options=None</em>, <em class="sig-param">unclean_shutdown=None</em>, <em class="sig-param">untrusted_cert_response_control=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileServerSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert time out</p></li>
<li><p><strong>authenticate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Server authentication once / always (default is once).</p></li>
<li><p><strong>authenticate_depth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Client certificate chain traversal depth. Default 9.</p></li>
<li><p><strong>ca_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client certificate file path. Default None.</p></li>
<li><p><strong>cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache size (sessions).</p></li>
<li><p><strong>cache_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cache time out</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the certificate that the system uses for server-side SSL processing.</p></li>
<li><p><strong>chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the certificates-key chain to associate with the SSL profile</p></li>
<li><p><strong>ciphers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is <code class="docutils literal notranslate"><span class="pre">/Common/serverssl</span></code>.</p></li>
<li><p><strong>expire_cert_response_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Response if the cert is expired (drop / ignore).</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – full path of the profile</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – generation</p></li>
<li><p><strong>generic_alert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Generic alerts enabled / disabled.</p></li>
<li><p><strong>handshake_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Handshake time out (seconds)</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the file name of the SSL key.</p></li>
<li><p><strong>mod_ssl_methods</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ModSSL Methods enabled / disabled. Default is disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the profile. (type <code class="docutils literal notranslate"><span class="pre">string</span></code>)</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device partition to manage resources on.</p></li>
<li><p><strong>passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Certificate Constrained Delegation CA passphrase</p></li>
<li><p><strong>peer_cert_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.</p></li>
<li><p><strong>proxy_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy SSL enabled / disabled. Default is disabled.</p></li>
<li><p><strong>renegotiate_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Period (seconds)</p></li>
<li><p><strong>renegotiate_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renogotiate Size</p></li>
<li><p><strong>renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>retain_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, client certificate is retained in SSL session.</p></li>
<li><p><strong>secure_renegotiation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When <code class="docutils literal notranslate"><span class="pre">request</span></code> is set the system request secure renegotation of SSL connections.
<code class="docutils literal notranslate"><span class="pre">require</span></code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The <code class="docutils literal notranslate"><span class="pre">require-strict</span></code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk <code class="docutils literal notranslate"><span class="pre">*</span></code> character.</p></li>
<li><p><strong>session_mirroring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Mirroring (enabled / disabled)</p></li>
<li><p><strong>session_ticket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Session Ticket (enabled / disabled)</p></li>
<li><p><strong>sni_default</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.</p></li>
<li><p><strong>sni_require</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requires that the network peers also provide SNI support, this setting only takes effect when <code class="docutils literal notranslate"><span class="pre">sni_default</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.When creating a new profile, the setting is provided by the parent profile</p></li>
<li><p><strong>ssl_forward_proxy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy (enabled / disabled)</p></li>
<li><p><strong>ssl_forward_proxy_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL forward Proxy Bypass (enabled / disabled)</p></li>
<li><p><strong>ssl_sign_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL sign hash (any, sha1, sha256, sha384)</p></li>
<li><p><strong>strict_resume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.</p></li>
<li><p><strong>unclean_shutdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (enabled / disabled)</p></li>
<li><p><strong>untrusted_cert_response_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unclean Shutdown (drop / ignore)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileServerSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileServerSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileTcp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">ProfileTcp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">close_wait_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">deferred_accept=None</em>, <em class="sig-param">fast_open=None</em>, <em class="sig-param">finwait2timeout=None</em>, <em class="sig-param">finwait_timeout=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">keepalive_interval=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.ProfileTcp</span></code> Configures a custom profile_tcp for use by health checks.</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>close_wait_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection remains in a LAST-ACK state before quitting. A value of 0 represents a term of forever (or until the maxrtx of the FIN state). The default value is 5 seconds.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>deferred_accept</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies, when enabled, that the system defers allocation of the connection chain context until the client response is received. This option is useful for dealing with 3-way handshake DOS attacks. The default value is disabled.</p></li>
<li><p><strong>fast_open</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When enabled, permits TCP Fast Open, allowing properly equipped TCP clients to send data with the SYN packet.</p></li>
<li><p><strong>finwait2timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is in the FIN-WAIT-2 state before quitting. The default value is 300 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state).</p></li>
<li><p><strong>finwait_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is in the FIN-WAIT-1 or closing state before quitting. The default value is 5 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state). You can also specify immediate or indefinite.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection is eligible for deletion. The default value is 300 seconds.</p></li>
<li><p><strong>keepalive_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the keep alive probe interval, in seconds. The default value is 1800 seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_tcp</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.close_wait_timeout">
<code class="sig-name descname">close_wait_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.close_wait_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection remains in a LAST-ACK state before quitting. A value of 0 represents a term of forever (or until the maxrtx of the FIN state). The default value is 5 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.defaults_from">
<code class="sig-name descname">defaults_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.defaults_from" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.deferred_accept">
<code class="sig-name descname">deferred_accept</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.deferred_accept" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies, when enabled, that the system defers allocation of the connection chain context until the client response is received. This option is useful for dealing with 3-way handshake DOS attacks. The default value is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.fast_open">
<code class="sig-name descname">fast_open</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.fast_open" title="Permalink to this definition">¶</a></dt>
<dd><p>When enabled, permits TCP Fast Open, allowing properly equipped TCP clients to send data with the SYN packet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.finwait2timeout">
<code class="sig-name descname">finwait2timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.finwait2timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection is in the FIN-WAIT-2 state before quitting. The default value is 300 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.finwait_timeout">
<code class="sig-name descname">finwait_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.finwait_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection is in the FIN-WAIT-1 or closing state before quitting. The default value is 5 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state). You can also specify immediate or indefinite.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.idle_timeout">
<code class="sig-name descname">idle_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of seconds that a connection is idle before the connection is eligible for deletion. The default value is 300 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.keepalive_interval">
<code class="sig-name descname">keepalive_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.keepalive_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the keep alive probe interval, in seconds. The default value is 1800 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the profile_tcp</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays the administrative partition within which this profile resides</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">close_wait_timeout=None</em>, <em class="sig-param">defaults_from=None</em>, <em class="sig-param">deferred_accept=None</em>, <em class="sig-param">fast_open=None</em>, <em class="sig-param">finwait2timeout=None</em>, <em class="sig-param">finwait_timeout=None</em>, <em class="sig-param">idle_timeout=None</em>, <em class="sig-param">keepalive_interval=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProfileTcp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>close_wait_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection remains in a LAST-ACK state before quitting. A value of 0 represents a term of forever (or until the maxrtx of the FIN state). The default value is 5 seconds.</p></li>
<li><p><strong>defaults_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.</p></li>
<li><p><strong>deferred_accept</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies, when enabled, that the system defers allocation of the connection chain context until the client response is received. This option is useful for dealing with 3-way handshake DOS attacks. The default value is disabled.</p></li>
<li><p><strong>fast_open</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When enabled, permits TCP Fast Open, allowing properly equipped TCP clients to send data with the SYN packet.</p></li>
<li><p><strong>finwait2timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is in the FIN-WAIT-2 state before quitting. The default value is 300 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state).</p></li>
<li><p><strong>finwait_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is in the FIN-WAIT-1 or closing state before quitting. The default value is 5 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state). You can also specify immediate or indefinite.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of seconds that a connection is idle before the connection is eligible for deletion. The default value is 300 seconds.</p></li>
<li><p><strong>keepalive_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the keep alive probe interval, in seconds. The default value is 1800 seconds.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the profile_tcp</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.ProfileTcp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.ProfileTcp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.ProfileTcp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Snat">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">Snat</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autolasthop=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">origins=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">snatpool=None</em>, <em class="sig-param">sourceport=None</em>, <em class="sig-param">translation=None</em>, <em class="sig-param">vlans=None</em>, <em class="sig-param">vlansdisabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.Snat</span></code> Manages a snat configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autolasthop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – -(Optional) Specifies whether to automatically map last hop for pools or not. The default is to use next level’s default.</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fullpath</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables mirroring of SNAT connections.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snat</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – IP or hostname of the snat</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
<li><p><strong>snatpool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of a SNAT pool. You can only use this option when automap and translation are not used.</p></li>
<li><p><strong>sourceport</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the system preserves the source port of the connection. The default is preserve. Use of the preserve-strict setting should be restricted to UDP only under very special circumstances such as nPath or transparent (that is, no translation of any other L3/L4 field), where there is a 1:1 relationship between virtual IP addresses and node addresses, or when clustered multi-processing (CMP) is disabled. The change setting is useful for obfuscating internal network addresses.</p></li>
<li><p><strong>translation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of a translated IP address. Note that translated addresses are outside the traffic management system. You can only use this option when automap and snatpool are not used.</p></li>
<li><p><strong>vlans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the name of the VLAN to which you want to assign the SNAT. The default is vlans-enabled.</p></li>
<li><p><strong>vlansdisabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the SNAT on all VLANs.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the snat</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.autolasthop">
<code class="sig-name descname">autolasthop</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.autolasthop" title="Permalink to this definition">¶</a></dt>
<dd><p>-(Optional) Specifies whether to automatically map last hop for pools or not. The default is to use next level’s default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.full_path">
<code class="sig-name descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Fullpath</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.mirror">
<code class="sig-name descname">mirror</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.mirror" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables mirroring of SNAT connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the snat</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.origins">
<code class="sig-name descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>IP or hostname of the snat</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the snat</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays the administrative partition within which this profile resides</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.snatpool">
<code class="sig-name descname">snatpool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.snatpool" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of a SNAT pool. You can only use this option when automap and translation are not used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.sourceport">
<code class="sig-name descname">sourceport</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.sourceport" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the system preserves the source port of the connection. The default is preserve. Use of the preserve-strict setting should be restricted to UDP only under very special circumstances such as nPath or transparent (that is, no translation of any other L3/L4 field), where there is a 1:1 relationship between virtual IP addresses and node addresses, or when clustered multi-processing (CMP) is disabled. The change setting is useful for obfuscating internal network addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.translation">
<code class="sig-name descname">translation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.translation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of a translated IP address. Note that translated addresses are outside the traffic management system. You can only use this option when automap and snatpool are not used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.vlans">
<code class="sig-name descname">vlans</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.vlans" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the VLAN to which you want to assign the SNAT. The default is vlans-enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.Snat.vlansdisabled">
<code class="sig-name descname">vlansdisabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.vlansdisabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Disables the SNAT on all VLANs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Snat.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autolasthop=None</em>, <em class="sig-param">full_path=None</em>, <em class="sig-param">mirror=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">origins=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">snatpool=None</em>, <em class="sig-param">sourceport=None</em>, <em class="sig-param">translation=None</em>, <em class="sig-param">vlans=None</em>, <em class="sig-param">vlansdisabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snat resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autolasthop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – -(Optional) Specifies whether to automatically map last hop for pools or not. The default is to use next level’s default.</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fullpath</p></li>
<li><p><strong>mirror</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables mirroring of SNAT connections.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snat</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – IP or hostname of the snat</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Displays the administrative partition within which this profile resides</p></li>
<li><p><strong>snatpool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of a SNAT pool. You can only use this option when automap and translation are not used.</p></li>
<li><p><strong>sourceport</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the system preserves the source port of the connection. The default is preserve. Use of the preserve-strict setting should be restricted to UDP only under very special circumstances such as nPath or transparent (that is, no translation of any other L3/L4 field), where there is a 1:1 relationship between virtual IP addresses and node addresses, or when clustered multi-processing (CMP) is disabled. The change setting is useful for obfuscating internal network addresses.</p></li>
<li><p><strong>translation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of a translated IP address. Note that translated addresses are outside the traffic management system. You can only use this option when automap and snatpool are not used.</p></li>
<li><p><strong>vlans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the name of the VLAN to which you want to assign the SNAT. The default is vlans-enabled.</p></li>
<li><p><strong>vlansdisabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the SNAT on all VLANs.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">app_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the snat</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.Snat.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.Snat.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.Snat.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.SnatPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">SnatPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.SnatPool</span></code> Collections of SNAT translation addresses</p>
<p>Resource should be named with their “full path”. The full path is the combination of the partition + name of the resource, for example /Common/my-snatpool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a translation address to add to or delete from a SNAT pool (at least one address is required)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snatpool</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.SnatPool.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool.members" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a translation address to add to or delete from a SNAT pool (at least one address is required)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.SnatPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the snatpool</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.SnatPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SnatPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a translation address to add to or delete from a SNAT pool (at least one address is required)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snatpool</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.SnatPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.SnatPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.SnatPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.VirtualAddress">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">VirtualAddress</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advertize_route=None</em>, <em class="sig-param">arp=None</em>, <em class="sig-param">auto_delete=None</em>, <em class="sig-param">conn_limit=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">icmp_echo=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">traffic_group=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.VirtualAddress</span></code> Configures Virtual Server</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertize_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enabled dynamic routing of the address</p></li>
<li><p><strong>arp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable ARP for the virtual address</p></li>
<li><p><strong>auto_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatically delete the virtual address with the virtual server</p></li>
<li><p><strong>conn_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max number of connections for virtual address</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the virtual address</p></li>
<li><p><strong>icmp_echo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/Disable ICMP response to the virtual address</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual address</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the partition and traffic group</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.advertize_route">
<code class="sig-name descname">advertize_route</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.advertize_route" title="Permalink to this definition">¶</a></dt>
<dd><p>Enabled dynamic routing of the address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.arp">
<code class="sig-name descname">arp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.arp" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable ARP for the virtual address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.auto_delete">
<code class="sig-name descname">auto_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.auto_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatically delete the virtual address with the virtual server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.conn_limit">
<code class="sig-name descname">conn_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Max number of connections for virtual address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the virtual address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.icmp_echo">
<code class="sig-name descname">icmp_echo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.icmp_echo" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable/Disable ICMP response to the virtual address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the virtual address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.traffic_group">
<code class="sig-name descname">traffic_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.traffic_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the partition and traffic group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advertize_route=None</em>, <em class="sig-param">arp=None</em>, <em class="sig-param">auto_delete=None</em>, <em class="sig-param">conn_limit=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">icmp_echo=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">traffic_group=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualAddress resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertize_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enabled dynamic routing of the address</p></li>
<li><p><strong>arp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable ARP for the virtual address</p></li>
<li><p><strong>auto_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatically delete the virtual address with the virtual server</p></li>
<li><p><strong>conn_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Max number of connections for virtual address</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the virtual address</p></li>
<li><p><strong>icmp_echo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/Disable ICMP response to the virtual address</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual address</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the partition and traffic group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.VirtualAddress.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.VirtualAddress.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualAddress.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.VirtualServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.ltm.</code><code class="sig-name descname">VirtualServer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_profiles=None</em>, <em class="sig-param">default_persistence_profile=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">fallback_persistence_profile=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">irules=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">persistence_profiles=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">profiles=None</em>, <em class="sig-param">server_profiles=None</em>, <em class="sig-param">snatpool=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">source_address_translation=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">translate_address=None</em>, <em class="sig-param">translate_port=None</em>, <em class="sig-param">vlans=None</em>, <em class="sig-param">vlans_enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ltm.VirtualServer</span></code> Configures Virtual Server</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of client context profiles associated on the virtual server. Not mutually exclusive with profiles and server_profiles</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of Virtual server</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination IP</p></li>
<li><p><strong>fallback_persistence_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a fallback persistence profile for the Virtual Server to use when the default persistence profile is not available.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the IP protocol to use with the the virtual server (all, tcp, or udp are valid)</p></li>
<li><p><strong>irules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The iRules list you want run on this virtual server. iRules help automate the intercepting, processing, and routing of application traffic.</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mask can either be in CIDR notation or decimal, i.e.: 24 or 255.255.255.0. A CIDR mask of 0 is the same as 0.0.0.0</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual server</p></li>
<li><p><strong>persistence_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of persistence profiles associated with the Virtual Server.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default pool name</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Listen port for the virtual server</p></li>
<li><p><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of profiles associated both client and server contexts on the virtual server. This includes protocol, ssl, http, etc.</p></li>
<li><p><strong>server_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of server context profiles associated on the virtual server. Not mutually exclusive with profiles and client_profiles</p></li>
<li><p><strong>snatpool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of an existing SNAT pool that you want the virtual server to use to implement selective and intelligent SNATs. DEPRECATED - see Virtual Server Property Groups source-address-translation</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP address or network from which the virtual server will accept traffic.</p></li>
<li><p><strong>source_address_translation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be either omitted for none or the values automap or snat</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the virtual server and its resources are available for load balancing. The default is Enabled</p></li>
<li><p><strong>translate_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables address translation for the virtual server. Turn address translation off for a virtual server if you want to use the virtual server to load balance connections to any address. This option is useful when the system is load balancing devices that have the same IP address.</p></li>
<li><p><strong>translate_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables port translation. Turn port translation off for a virtual server if you want to use the virtual server to load balance connections to any service</p></li>
<li><p><strong>vlans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The virtual server is enabled/disabled on this set of VLANs. See vlans-disabled and vlans-enabled.</p></li>
<li><p><strong>vlans_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the virtual server on the VLANs specified by the VLANs option.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.client_profiles">
<code class="sig-name descname">client_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.client_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of client context profiles associated on the virtual server. Not mutually exclusive with profiles and server_profiles</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of Virtual server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination IP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.fallback_persistence_profile">
<code class="sig-name descname">fallback_persistence_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.fallback_persistence_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a fallback persistence profile for the Virtual Server to use when the default persistence profile is not available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the IP protocol to use with the the virtual server (all, tcp, or udp are valid)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.irules">
<code class="sig-name descname">irules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.irules" title="Permalink to this definition">¶</a></dt>
<dd><p>The iRules list you want run on this virtual server. iRules help automate the intercepting, processing, and routing of application traffic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.mask">
<code class="sig-name descname">mask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.mask" title="Permalink to this definition">¶</a></dt>
<dd><p>Mask can either be in CIDR notation or decimal, i.e.: 24 or 255.255.255.0. A CIDR mask of 0 is the same as 0.0.0.0</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the virtual server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.persistence_profiles">
<code class="sig-name descname">persistence_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.persistence_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of persistence profiles associated with the Virtual Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.pool">
<code class="sig-name descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Default pool name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Listen port for the virtual server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.profiles">
<code class="sig-name descname">profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of profiles associated both client and server contexts on the virtual server. This includes protocol, ssl, http, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.server_profiles">
<code class="sig-name descname">server_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.server_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of server context profiles associated on the virtual server. Not mutually exclusive with profiles and client_profiles</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.snatpool">
<code class="sig-name descname">snatpool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.snatpool" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of an existing SNAT pool that you want the virtual server to use to implement selective and intelligent SNATs. DEPRECATED - see Virtual Server Property Groups source-address-translation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an IP address or network from which the virtual server will accept traffic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.source_address_translation">
<code class="sig-name descname">source_address_translation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.source_address_translation" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be either omitted for none or the values automap or snat</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the virtual server and its resources are available for load balancing. The default is Enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.translate_address">
<code class="sig-name descname">translate_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.translate_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables address translation for the virtual server. Turn address translation off for a virtual server if you want to use the virtual server to load balance connections to any address. This option is useful when the system is load balancing devices that have the same IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.translate_port">
<code class="sig-name descname">translate_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.translate_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables port translation. Turn port translation off for a virtual server if you want to use the virtual server to load balance connections to any service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.vlans">
<code class="sig-name descname">vlans</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.vlans" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual server is enabled/disabled on this set of VLANs. See vlans-disabled and vlans-enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.ltm.VirtualServer.vlans_enabled">
<code class="sig-name descname">vlans_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.vlans_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the virtual server on the VLANs specified by the VLANs option.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.VirtualServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_profiles=None</em>, <em class="sig-param">default_persistence_profile=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">fallback_persistence_profile=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">irules=None</em>, <em class="sig-param">mask=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">persistence_profiles=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">profiles=None</em>, <em class="sig-param">server_profiles=None</em>, <em class="sig-param">snatpool=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">source_address_translation=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">translate_address=None</em>, <em class="sig-param">translate_port=None</em>, <em class="sig-param">vlans=None</em>, <em class="sig-param">vlans_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of client context profiles associated on the virtual server. Not mutually exclusive with profiles and server_profiles</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of Virtual server</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination IP</p></li>
<li><p><strong>fallback_persistence_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a fallback persistence profile for the Virtual Server to use when the default persistence profile is not available.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the IP protocol to use with the the virtual server (all, tcp, or udp are valid)</p></li>
<li><p><strong>irules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The iRules list you want run on this virtual server. iRules help automate the intercepting, processing, and routing of application traffic.</p></li>
<li><p><strong>mask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mask can either be in CIDR notation or decimal, i.e.: 24 or 255.255.255.0. A CIDR mask of 0 is the same as 0.0.0.0</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual server</p></li>
<li><p><strong>persistence_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of persistence profiles associated with the Virtual Server.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default pool name</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Listen port for the virtual server</p></li>
<li><p><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of profiles associated both client and server contexts on the virtual server. This includes protocol, ssl, http, etc.</p></li>
<li><p><strong>server_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of server context profiles associated on the virtual server. Not mutually exclusive with profiles and client_profiles</p></li>
<li><p><strong>snatpool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of an existing SNAT pool that you want the virtual server to use to implement selective and intelligent SNATs. DEPRECATED - see Virtual Server Property Groups source-address-translation</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies an IP address or network from which the virtual server will accept traffic.</p></li>
<li><p><strong>source_address_translation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be either omitted for none or the values automap or snat</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the virtual server and its resources are available for load balancing. The default is Enabled</p></li>
<li><p><strong>translate_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables address translation for the virtual server. Turn address translation off for a virtual server if you want to use the virtual server to load balance connections to any address. This option is useful when the system is load balancing devices that have the same IP address.</p></li>
<li><p><strong>translate_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables or disables port translation. Turn port translation off for a virtual server if you want to use the virtual server to load balance connections to any service</p></li>
<li><p><strong>vlans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The virtual server is enabled/disabled on this set of VLANs. See vlans-disabled and vlans-enabled.</p></li>
<li><p><strong>vlans_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the virtual server on the VLANs specified by the VLANs option.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.ltm.VirtualServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.ltm.VirtualServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.ltm.VirtualServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
