---
---

<div class="section" id="module-pulumi_gcp.servicenetworking">
<span id="servicenetworking"></span><h1>servicenetworking<a class="headerlink" href="#module-pulumi_gcp.servicenetworking" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.servicenetworking.Connection">
<em class="property">class </em><code class="descclassname">pulumi_gcp.servicenetworking.</code><code class="descname">Connection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>network=None</em>, <em>reserved_peering_ranges=None</em>, <em>service=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a private VPC connection with a GCP service provider. For more information see
<a class="reference external" href="https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of VPC network connected with service producers using VPC peering.</li>
<li><strong>reserved_peering_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.</li>
<li><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
‘servicenetworking.googleapis.com’.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_networking_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_networking_connection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of VPC network connected with service producers using VPC peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.reserved_peering_ranges">
<code class="descname">reserved_peering_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.reserved_peering_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.service">
<code class="descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
‘servicenetworking.googleapis.com’.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.servicenetworking.Connection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.servicenetworking.Connection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
