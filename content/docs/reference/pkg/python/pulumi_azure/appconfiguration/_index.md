---
title: Module appconfiguration
title_tag: Module appconfiguration | Package pulumi_azure | Python SDK
linktitle: appconfiguration
notitle: true
---

<div class="section" id="appconfiguration">
<h1>appconfiguration<a class="headerlink" href="#appconfiguration" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.appconfiguration"></span><dl class="class">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.appconfiguration.</code><code class="sig-name descname">ConfigurationStore</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure App Configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the the App Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">free</span></code> and <code class="docutils literal notranslate"><span class="pre">standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the App Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the App Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.primary_read_keys">
<code class="sig-name descname">primary_read_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.primary_read_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the primary read access key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret of the access key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.primary_write_keys">
<code class="sig-name descname">primary_write_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.primary_write_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the primary write access key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret of the access key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.secondary_read_keys">
<code class="sig-name descname">secondary_read_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.secondary_read_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the secondary read access key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret of the access key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.secondary_write_keys">
<code class="sig-name descname">secondary_write_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.secondary_write_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the secondary write access key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret of the access key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU name of the the App Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">free</span></code> and <code class="docutils literal notranslate"><span class="pre">standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_read_keys=None</em>, <em class="sig-param">primary_write_keys=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_read_keys=None</em>, <em class="sig-param">secondary_write_keys=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfigurationStore resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the App Configuration.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the App Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_read_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the primary read access key.</p></li>
<li><p><strong>primary_write_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the primary write access key.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_read_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the secondary read access key.</p></li>
<li><p><strong>secondary_write_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">access_key</span></code> block as defined below containing the secondary write access key.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the the App Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">free</span></code> and <code class="docutils literal notranslate"><span class="pre">standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>primary_read_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret of the access key.</p></li>
</ul>
<p>The <strong>primary_write_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret of the access key.</p></li>
</ul>
<p>The <strong>secondary_read_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret of the access key.</p></li>
</ul>
<p>The <strong>secondary_write_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string including the endpoint, id and secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret of the access key.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/app_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appconfiguration.ConfigurationStore.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appconfiguration.ConfigurationStore.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
