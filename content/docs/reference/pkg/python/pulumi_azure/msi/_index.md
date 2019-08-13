---
title: Module msi
---

<div class="section" id="msi">
<h1>msi<a class="headerlink" href="#msi" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.msi"></span><dl class="class">
<dt id="pulumi_azure.msi.UserAssignedIdentity">
<em class="property">class </em><code class="descclassname">pulumi_azure.msi.</code><code class="descname">UserAssignedIdentity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/user_assigned_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/user_assigned_identity.html.markdown</a>.</div></blockquote>
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

<dl class="staticmethod">
<dt id="pulumi_azure.msi.UserAssignedIdentity.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>client_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>principal_id=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.msi.UserAssignedIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserAssignedIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] client_id: Client ID associated with the user assigned identity.
:param pulumi.Input[str] location: The location/region where the user assigned identity is</p>
<blockquote>
<div>created.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user assigned identity. Changing this forces a
new identity to be created.</li>
<li><strong>principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service Principal ID associated with the user assigned identity.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the user assigned identity.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/user_assigned_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/user_assigned_identity.html.markdown</a>.</div></blockquote>
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
