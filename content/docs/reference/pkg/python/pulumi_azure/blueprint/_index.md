---
title: Module blueprint
title_tag: Module blueprint | Package pulumi_azure | Python SDK
linktitle: blueprint
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="blueprint">
<h1>blueprint<a class="headerlink" href="#blueprint" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.blueprint"></span><dl class="py class">
<dt id="pulumi_azure.blueprint.Assignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">Assignment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_exclude_principals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_values</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.Assignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Assignment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: The Azure location of the Assignment.
:param pulumi.Input[list] lock_exclude_principals: a list of up to 5 Principal IDs that are permitted to bypass the locks applied by the Blueprint.
:param pulumi.Input[str] lock_mode: The locking mode of the Blueprint Assignment.  One of <code class="docutils literal notranslate"><span class="pre">None</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">AllResourcesReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">AlResourcesDoNotDelete</span></code>.
:param pulumi.Input[str] name: The name of the Blueprint Assignment
:param pulumi.Input[str] parameter_values: a JSON string to supply Blueprint Assignment parameter values.
:param pulumi.Input[str] resource_groups: a JSON string to supply the Blueprint Resource Group information.
:param pulumi.Input[str] target_subscription_id: The Subscription ID the Blueprint Published Version is to be applied to.
:param pulumi.Input[str] version_id: The ID of the Published Version of the blueprint to be assigned.</p>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Identity type for the Managed Service Identity. Currently only <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> is supported.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.blueprint_name">
<code class="sig-name descname">blueprint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.blueprint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the blueprint assigned</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description on the Blueprint</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the blueprint</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location of the Assignment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.lock_exclude_principals">
<code class="sig-name descname">lock_exclude_principals</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.lock_exclude_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>a list of up to 5 Principal IDs that are permitted to bypass the locks applied by the Blueprint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.lock_mode">
<code class="sig-name descname">lock_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.lock_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The locking mode of the Blueprint Assignment.  One of <code class="docutils literal notranslate"><span class="pre">None</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">AllResourcesReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">AlResourcesDoNotDelete</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Blueprint Assignment</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.parameter_values">
<code class="sig-name descname">parameter_values</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.parameter_values" title="Permalink to this definition">¶</a></dt>
<dd><p>a JSON string to supply Blueprint Assignment parameter values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.resource_groups">
<code class="sig-name descname">resource_groups</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.resource_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>a JSON string to supply the Blueprint Resource Group information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.target_subscription_id">
<code class="sig-name descname">target_subscription_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.target_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Subscription ID the Blueprint Published Version is to be applied to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identity type for the Managed Service Identity. Currently only <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> is supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.Assignment.version_id">
<code class="sig-name descname">version_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Published Version of the blueprint to be assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.blueprint.Assignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blueprint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_exclude_principals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_values</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Assignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blueprint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the blueprint assigned</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description on the Blueprint</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the blueprint</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location of the Assignment.</p></li>
<li><p><strong>lock_exclude_principals</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a list of up to 5 Principal IDs that are permitted to bypass the locks applied by the Blueprint.</p></li>
<li><p><strong>lock_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The locking mode of the Blueprint Assignment.  One of <code class="docutils literal notranslate"><span class="pre">None</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">AllResourcesReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">AlResourcesDoNotDelete</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Blueprint Assignment</p></li>
<li><p><strong>parameter_values</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – a JSON string to supply Blueprint Assignment parameter values.</p></li>
<li><p><strong>resource_groups</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – a JSON string to supply the Blueprint Resource Group information.</p></li>
<li><p><strong>target_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Subscription ID the Blueprint Published Version is to be applied to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identity type for the Managed Service Identity. Currently only <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> is supported.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Published Version of the blueprint to be assigned.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Identity type for the Managed Service Identity. Currently only <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> is supported.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.blueprint.Assignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.blueprint.Assignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.Assignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.blueprint.AwaitableGetDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">AwaitableGetDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.AwaitableGetDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.blueprint.AwaitableGetPublishedVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">AwaitableGetPublishedVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">blueprint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.AwaitableGetPublishedVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.blueprint.GetDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">GetDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefinition.</p>
<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Blueprint Definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the Blueprint Definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.last_modified">
<code class="sig-name descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp of when this last modification was saved to the Blueprint Definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.target_scope">
<code class="sig-name descname">target_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.target_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The target scope.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.time_created">
<code class="sig-name descname">time_created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.time_created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp of when this Blueprint Definition was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetDefinitionResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetDefinitionResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions published for this Blueprint Definition.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">GetPublishedVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">blueprint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublishedVersion.</p>
<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Blueprint Published Version</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the Blueprint Published Version</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult.target_scope">
<code class="sig-name descname">target_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult.target_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The target scope</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.blueprint.GetPublishedVersionResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.blueprint.GetPublishedVersionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Blueprint</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.blueprint.get_definition">
<code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">get_definition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.get_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Azure Blueprint Definition</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure Blueprints are in Preview and potentially subject to breaking change without notice.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">management</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">current</span><span class="o">.</span><span class="n">tenant_id</span><span class="p">)</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">blueprint</span><span class="o">.</span><span class="n">get_definition</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;exampleManagementGroupBP&quot;</span><span class="p">,</span>
    <span class="n">scope_id</span><span class="o">=</span><span class="n">root</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Blueprint</p></li>
<li><p><strong>scope_id</strong> (<em>str</em>) – The Resource ID of the scope at which the blueprint definition is stored. This will be with either a Subscription ID or Management Group ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.blueprint.get_published_version">
<code class="sig-prename descclassname">pulumi_azure.blueprint.</code><code class="sig-name descname">get_published_version</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">blueprint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.blueprint.get_published_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Azure Blueprint Published Version</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure Blueprints are in Preview and potentially subject to breaking change without notice.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_subscription</span><span class="p">()</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">blueprint</span><span class="o">.</span><span class="n">get_published_version</span><span class="p">(</span><span class="n">scope_id</span><span class="o">=</span><span class="n">current</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">blueprint_name</span><span class="o">=</span><span class="s2">&quot;exampleBluePrint&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;dev_v2.3&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>blueprint_name</strong> (<em>str</em>) – The name of the Blueprint Definition</p></li>
<li><p><strong>scope_id</strong> (<em>str</em>) – The Resource ID of the scope where the Blueprint Definition is stored. This will be with either a Subscription ID or Management Group ID.</p></li>
<li><p><strong>version</strong> (<em>str</em>) – The Version name of the Published Version of the Blueprint Definition</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
