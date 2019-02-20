<div class="section" id="module-pulumi_f5bigip.sys">
<span id="sys"></span><h1>sys<a class="headerlink" href="#module-pulumi_f5bigip.sys" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_f5bigip.sys.BigIpLicense">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">BigIpLicense</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>command=None</em>, <em>registration_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BigIpLicense resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] command
:param pulumi.Input[str] registration_key</p>
<dl class="method">
<dt id="pulumi_f5bigip.sys.BigIpLicense.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.BigIpLicense.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.BigIpLicense.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.Dns">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">Dns</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name_servers=None</em>, <em>number_of_dots=None</em>, <em>searches=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_ltm_dns</span></code> Configures DNS server on F5 BIG-IP</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[list] name_servers: Name or IP address of the DNS server
:param pulumi.Input[int] number_of_dots: Configures the number of dots needed in a name before an initial absolute query will be made.
:param pulumi.Input[list] searches: Specify what domains you want to search</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.name_servers">
<code class="descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or IP address of the DNS server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.number_of_dots">
<code class="descname">number_of_dots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.number_of_dots" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the number of dots needed in a name before an initial absolute query will be made.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Dns.searches">
<code class="descname">searches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.searches" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify what domains you want to search</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Dns.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Dns.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Dns.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.IApp">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">IApp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>devicegroup=None</em>, <em>execute_action=None</em>, <em>inherited_devicegroup=None</em>, <em>inherited_traffic_group=None</em>, <em>jsonfile=None</em>, <em>lists=None</em>, <em>metadatas=None</em>, <em>name=None</em>, <em>partition=None</em>, <em>strict_updates=None</em>, <em>tables=None</em>, <em>template=None</em>, <em>template_modified=None</em>, <em>template_prerequisite_errors=None</em>, <em>traffic_group=None</em>, <em>variables=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_sys_iapp</span></code> resource helps you to deploy Application Services template that can be used to automate and orchestrate Layer 4-7 applications service deployments using F5 Network. More information on iApp 2.0 is at <a class="reference external" href="https://devcentral.f5.com/wiki/iApp.AppSvcsiApp_userguide_userguide.ashx">https://devcentral.f5.com/wiki/iApp.AppSvcsiApp_userguide_userguide.ashx</a> This resource requires a iApp template already imported on BIG-IP, the template can be found at <a class="reference external" href="https://github.com/F5Networks/f5-application-services-integration-iApp/releases/download/v2.0.003/appsvcs_integration_v2.0.003.tmpl">https://github.com/F5Networks/f5-application-services-integration-iApp/releases/download/v2.0.003/appsvcs_integration_v2.0.003.tmpl</a></p>
<dl class="docutils">
<dt>{</dt>
<dd><dl class="first last docutils">
<dt>“name”:”policywaf”,</dt>
<dd><p class="first">“partition”: “Common”,
“inheritedDevicegroup”: “true”,
“inheritedTrafficGroup”: “true”,
“strictUpdates”: “enabled”,
“template”: “/Common/appsvcs_integration_v2.0.003”,
“execute-action”: “definition”,</p>
<blockquote class="last">
<div><dl class="docutils">
<dt>“tables”: [{</dt>
<dd><p class="first">“name”: “feature__easyL4FirewallBlacklist”,
“columnNames”: [</p>
<blockquote>
<div>“CIDRRange”</div></blockquote>
<p class="last">],
“rows”: [</p>
</dd>
</dl>
</div></blockquote>
</dd>
</dl>
</dd>
</dl>
<p>}</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">description</span></code> - User defined description.</li>
<li><code class="docutils literal notranslate"><span class="pre">deviceGroup</span></code> - The name of the device group that the application service is assigned to.</li>
<li><code class="docutils literal notranslate"><span class="pre">executeAction</span></code> - Run the specified template action associated with the application.</li>
<li><code class="docutils literal notranslate"><span class="pre">inheritedDevicegroup</span></code>- Read-only. Shows whether the application folder will automatically remain with the same device-group as its parent folder. Use ‘device-group default’ or ‘device-group non-default’ to set this.</li>
<li><code class="docutils literal notranslate"><span class="pre">inheritedTrafficGroup</span></code> - Read-only. Shows whether the application folder will automatically remain with the same traffic-group as its parent folder. Use ‘traffic-group default’ or ‘traffic-group non-default’ to set this.</li>
<li><code class="docutils literal notranslate"><span class="pre">partition</span></code> - Displays the administrative partition within which the application resides.</li>
<li><code class="docutils literal notranslate"><span class="pre">strictUpdates</span></code> - Specifies whether configuration objects contained in the application may be directly modified, outside the context of the system’s application management interfaces.</li>
<li><code class="docutils literal notranslate"><span class="pre">template</span></code> - The template defines the configuration for the application. This may be changed after the application has been created to move the application to a new template.</li>
<li><code class="docutils literal notranslate"><span class="pre">templateModified</span></code> - Indicates that the application template used to deploy the application has been modified. The application should be updated to make use of the latest changes.</li>
<li><code class="docutils literal notranslate"><span class="pre">templatePrerequisiteErrors</span></code> - Indicates any missing prerequisites associated with the template that defines this application.</li>
<li><code class="docutils literal notranslate"><span class="pre">trafficGroup</span></code> - The name of the traffic group that the application service is assigned to.</li>
<li><code class="docutils literal notranslate"><span class="pre">lists</span></code> - string values</li>
<li><code class="docutils literal notranslate"><span class="pre">metadata</span></code> - User defined generic data for the application service. It is a name and value pair.</li>
<li><code class="docutils literal notranslate"><span class="pre">tables</span></code> - Values provided like pool name, nodes etc.</li>
<li><code class="docutils literal notranslate"><span class="pre">variables</span></code> - Name, values, encrypted or not</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] devicegroup
:param pulumi.Input[str] execute_action
:param pulumi.Input[str] inherited_devicegroup
:param pulumi.Input[str] inherited_traffic_group
:param pulumi.Input[str] jsonfile: Refer to the Json file which will be deployed on F5 BIG-IP.
:param pulumi.Input[list] lists
:param pulumi.Input[list] metadatas
:param pulumi.Input[str] name: Name of the iApp.
:param pulumi.Input[str] partition
:param pulumi.Input[str] strict_updates
:param pulumi.Input[list] tables
:param pulumi.Input[str] template
:param pulumi.Input[str] template_modified
:param pulumi.Input[str] template_prerequisite_errors
:param pulumi.Input[str] traffic_group
:param pulumi.Input[list] variables</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.jsonfile">
<code class="descname">jsonfile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.jsonfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Refer to the Json file which will be deployed on F5 BIG-IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.IApp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the iApp.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.IApp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.IApp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.IApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.Ntp">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">Ntp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>servers=None</em>, <em>timezone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_sys_ntp</span></code> provides details about a specific bigip</p>
<p>This resource is helpful when configuring NTP server on the BIG-IP.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[list] servers: Adds NTP servers to or deletes NTP servers from the BIG-IP system.
:param pulumi.Input[str] timezone: Specifies the time zone that you want to use for the system time.</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Ntp.servers">
<code class="descname">servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds NTP servers to or deletes NTP servers from the BIG-IP system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Ntp.timezone">
<code class="descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the time zone that you want to use for the system time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Ntp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Ntp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Ntp.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.Provision">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">Provision</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cpu_ratio=None</em>, <em>disk_ratio=None</em>, <em>full_path=None</em>, <em>level=None</em>, <em>memory_ratio=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_sys_provision</span></code> provides details bout how to enable “ilx”, “asm” “apm” resource on BIG-IP</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] cpu_ratio
:param pulumi.Input[int] disk_ratio
:param pulumi.Input[str] full_path
:param pulumi.Input[str] level
:param pulumi.Input[int] memory_ratio
:param pulumi.Input[str] name</p>
<dl class="method">
<dt id="pulumi_f5bigip.sys.Provision.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Provision.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Provision.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.Snmp">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">Snmp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowedaddresses=None</em>, <em>sys_contact=None</em>, <em>sys_location=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_sys_snmp</span></code> provides details bout how to enable “ilx”, “asm” “apm” resource on BIG-IP</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowedaddresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.</li>
<li><strong>sys_contact</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the contact information for the system administrator.</li>
<li><strong>sys_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the system’s physical location.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.allowedaddresses">
<code class="descname">allowedaddresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.allowedaddresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.sys_contact">
<code class="descname">sys_contact</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.sys_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the contact information for the system administrator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.Snmp.sys_location">
<code class="descname">sys_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.sys_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the system’s physical location.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Snmp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.Snmp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.Snmp.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_f5bigip.sys.SnmpTraps">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.sys.</code><code class="descname">SnmpTraps</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auth_passwordencrypted=None</em>, <em>auth_protocol=None</em>, <em>community=None</em>, <em>description=None</em>, <em>engine_id=None</em>, <em>host=None</em>, <em>name=None</em>, <em>port=None</em>, <em>privacy_password=None</em>, <em>privacy_password_encrypted=None</em>, <em>privacy_protocol=None</em>, <em>security_level=None</em>, <em>security_name=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_sys_snmp_traps</span></code> provides details bout how to enable snmp_traps resource on BIG-IP</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] auth_passwordencrypted
:param pulumi.Input[str] auth_protocol
:param pulumi.Input[str] community: Specifies the community string used for this trap.
:param pulumi.Input[str] description: The port that the trap will be sent to.
:param pulumi.Input[str] engine_id
:param pulumi.Input[str] host: The host the trap will be sent to.
:param pulumi.Input[str] name: Name of the snmp trap.
:param pulumi.Input[int] port: User defined description.
:param pulumi.Input[str] privacy_password
:param pulumi.Input[str] privacy_password_encrypted
:param pulumi.Input[str] privacy_protocol
:param pulumi.Input[str] security_level
:param pulumi.Input[str] security_name
:param pulumi.Input[str] version</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.community">
<code class="descname">community</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.community" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the community string used for this trap.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The port that the trap will be sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The host the trap will be sent to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the snmp trap.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.sys.SnmpTraps.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.port" title="Permalink to this definition">¶</a></dt>
<dd><p>User defined description.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.SnmpTraps.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.sys.SnmpTraps.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.sys.SnmpTraps.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
