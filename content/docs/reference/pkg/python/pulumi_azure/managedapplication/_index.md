---
title: Module managedapplication
title_tag: Module managedapplication | Package pulumi_azure | Python SDK
linktitle: managedapplication
notitle: true
---

<div class="section" id="managedapplication">
<h1>managedapplication<a class="headerlink" href="#managedapplication" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.managedapplication"></span><dl class="class">
<dt id="pulumi_azure.managedapplication.AwaitableGetDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managedapplication.</code><code class="sig-name descname">AwaitableGetDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.AwaitableGetDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.managedapplication.Definition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managedapplication.</code><code class="sig-name descname">Definition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorizations=None</em>, <em class="sig-param">create_ui_definition=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">lock_level=None</em>, <em class="sig-param">main_template=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">package_enabled=None</em>, <em class="sig-param">package_file_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.Definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Managed Application Definition.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_application_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_application_definition.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block defined below.</p></li>
<li><p><strong>create_ui_definition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the <code class="docutils literal notranslate"><span class="pre">createUiDefinition</span></code> json for the backing template with <code class="docutils literal notranslate"><span class="pre">Microsoft.Solutions/applications</span></code> resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition description.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition display name.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>lock_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application lock level. Valid values include <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>main_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the inline main template json which has resources to be provisioned.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Managed Application Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>package_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the package enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>package_file_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition package file Uri.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Managed Application Definition should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authorizations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a role definition identifier for the provider. This role will define all the permissions that the provider must have on the managed application’s container resource group. This role definition cannot have permission to delete the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a service principal identifier for the provider. This is the identity that the provider will use to call ARM to manage the managed application resources.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.authorizations">
<code class="sig-name descname">authorizations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.authorizations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a role definition identifier for the provider. This role will define all the permissions that the provider must have on the managed application’s container resource group. This role definition cannot have permission to delete the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a service principal identifier for the provider. This is the identity that the provider will use to call ARM to manage the managed application resources.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.create_ui_definition">
<code class="sig-name descname">create_ui_definition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.create_ui_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the <code class="docutils literal notranslate"><span class="pre">createUiDefinition</span></code> json for the backing template with <code class="docutils literal notranslate"><span class="pre">Microsoft.Solutions/applications</span></code> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the managed application definition description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the managed application definition display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.lock_level">
<code class="sig-name descname">lock_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.lock_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the managed application lock level. Valid values include <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.main_template">
<code class="sig-name descname">main_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.main_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the inline main template json which has resources to be provisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Managed Application Definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.package_enabled">
<code class="sig-name descname">package_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.package_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the package enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.package_file_uri">
<code class="sig-name descname">package_file_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.package_file_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the managed application definition package file Uri.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Managed Application Definition should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managedapplication.Definition.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managedapplication.Definition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorizations=None</em>, <em class="sig-param">create_ui_definition=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">lock_level=None</em>, <em class="sig-param">main_template=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">package_enabled=None</em>, <em class="sig-param">package_file_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Definition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorizations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block defined below.</p></li>
<li><p><strong>create_ui_definition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the <code class="docutils literal notranslate"><span class="pre">createUiDefinition</span></code> json for the backing template with <code class="docutils literal notranslate"><span class="pre">Microsoft.Solutions/applications</span></code> resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition description.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition display name.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>lock_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application lock level. Valid values include <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>main_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the inline main template json which has resources to be provisioned.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Managed Application Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>package_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the package enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>package_file_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the managed application definition package file Uri.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Managed Application Definition should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authorizations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a role definition identifier for the provider. This role will define all the permissions that the provider must have on the managed application’s container resource group. This role definition cannot have permission to delete the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a service principal identifier for the provider. This is the identity that the provider will use to call ARM to manage the managed application resources.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managedapplication.Definition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managedapplication.Definition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.Definition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managedapplication.GetDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managedapplication.</code><code class="sig-name descname">GetDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.GetDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefinition.</p>
<dl class="attribute">
<dt id="pulumi_azure.managedapplication.GetDefinitionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managedapplication.GetDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.managedapplication.get_definition">
<code class="sig-prename descclassname">pulumi_azure.managedapplication.</code><code class="sig-name descname">get_definition</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managedapplication.get_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing Managed Application Definition.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/managed_application_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/managed_application_definition.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Managed Application Definition.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where this Managed Application Definition exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
