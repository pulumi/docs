---
title: Module powerbi
title_tag: Module powerbi | Package pulumi_azure | Python SDK
linktitle: powerbi
notitle: true
---

<div class="section" id="powerbi">
<h1>powerbi<a class="headerlink" href="#powerbi" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.powerbi"></span><dl class="class">
<dt id="pulumi_azure.powerbi.Embedded">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.powerbi.</code><code class="sig-name descname">Embedded</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrators=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.powerbi.Embedded" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PowerBI Embedded.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of administrator user identities, which manages the Power BI Embedded and must be a member user or a service principal in your AAD tenant.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the PowerBI Embedded. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the PowerBI Embedded should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the PowerBI Embedded’s pricing level’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">A1</span></code>, <code class="docutils literal notranslate"><span class="pre">A2</span></code>, <code class="docutils literal notranslate"><span class="pre">A3</span></code>, <code class="docutils literal notranslate"><span class="pre">A4</span></code>, <code class="docutils literal notranslate"><span class="pre">A5</span></code>, <code class="docutils literal notranslate"><span class="pre">A6</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.administrators">
<code class="sig-name descname">administrators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.administrators" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of administrator user identities, which manages the Power BI Embedded and must be a member user or a service principal in your AAD tenant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the PowerBI Embedded. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the PowerBI Embedded should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the PowerBI Embedded’s pricing level’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">A1</span></code>, <code class="docutils literal notranslate"><span class="pre">A2</span></code>, <code class="docutils literal notranslate"><span class="pre">A3</span></code>, <code class="docutils literal notranslate"><span class="pre">A4</span></code>, <code class="docutils literal notranslate"><span class="pre">A5</span></code>, <code class="docutils literal notranslate"><span class="pre">A6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.powerbi.Embedded.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.powerbi.Embedded.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrators=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Embedded resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of administrator user identities, which manages the Power BI Embedded and must be a member user or a service principal in your AAD tenant.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the PowerBI Embedded. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the PowerBI Embedded should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the PowerBI Embedded’s pricing level’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">A1</span></code>, <code class="docutils literal notranslate"><span class="pre">A2</span></code>, <code class="docutils literal notranslate"><span class="pre">A3</span></code>, <code class="docutils literal notranslate"><span class="pre">A4</span></code>, <code class="docutils literal notranslate"><span class="pre">A5</span></code>, <code class="docutils literal notranslate"><span class="pre">A6</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.powerbi.Embedded.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.powerbi.Embedded.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.powerbi.Embedded.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
