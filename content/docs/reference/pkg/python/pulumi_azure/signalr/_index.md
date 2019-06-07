---
---

<div class="section" id="module-pulumi_azure.signalr">
<span id="signalr"></span><h1>signalr<a class="headerlink" href="#module-pulumi_azure.signalr" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.signalr.Service">
<em class="property">class </em><code class="descclassname">pulumi_azure.signalr.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.signalr.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure SignalR service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SignalR service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The publicly accessible IP of the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SignalR service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.public_port">
<code class="descname">public_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.public_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The publicly accessible port of the SignalR service which is designed for browser/client use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the SignalR service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.server_port">
<code class="descname">server_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.server_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The publicly accessible port of the SignalR service which is designed for customer server side use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.signalr.Service.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.signalr.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.signalr.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.signalr.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.signalr.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.signalr.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
