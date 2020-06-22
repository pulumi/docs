---
title: Module entitlement
title_tag: Module entitlement | Package pulumi_azuredevops | Python SDK
linktitle: entitlement
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="entitlement">
<h1>entitlement<a class="headerlink" href="#entitlement" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.entitlement"></span><dl class="py class">
<dt id="pulumi_azuredevops.entitlement.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.entitlement.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">licensing_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.entitlement.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a user entitlement within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">entitlement</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span> <span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;foo@contoso.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user%20entitlements/add?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - User Entitlements - Add</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Member Entitlement Management</strong>: Read &amp; Write</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p></li>
<li><p><strong>licensing_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source provider for the origin identifier.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p></li>
<li><p><strong>principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.account_license_type">
<code class="sig-name descname">account_license_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.account_license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.descriptor">
<code class="sig-name descname">descriptor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.licensing_source">
<code class="sig-name descname">licensing_source</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.licensing_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.origin">
<code class="sig-name descname">origin</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.origin_id">
<code class="sig-name descname">origin_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.entitlement.User.principal_name">
<code class="sig-name descname">principal_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.entitlement.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">licensing_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p></li>
<li><p><strong>descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.</p></li>
<li><p><strong>licensing_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source provider for the origin identifier.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p></li>
<li><p><strong>principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.entitlement.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.entitlement.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.entitlement.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
