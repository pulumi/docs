---
---

<div class="section" id="module-pulumi_azure.msi">
<span id="msi"></span><h1>msi<a class="headerlink" href="#module-pulumi_azure.msi" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.msi.UserAssignedIdentity">
<em class="property">class </em><code class="descclassname">pulumi_azure.msi.</code><code class="descname">UserAssignedIdentity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a user assigned identity.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the user assigned identity is
created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user assigned identity. Changing this forces a
new identity to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the user assigned identity.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.client_id">
<code class="descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID associated with the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the user assigned identity is
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user assigned identity. Changing this forces a
new identity to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.principal_id">
<code class="descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Service Principal ID associated with the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.msi.UserAssignedIdentity.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.msi.UserAssignedIdentity.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.msi.UserAssignedIdentity.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
