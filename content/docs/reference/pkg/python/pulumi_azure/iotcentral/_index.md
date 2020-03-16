---
title: Module iotcentral
title_tag: Module iotcentral | Package pulumi_azure | Python SDK
linktitle: iotcentral
notitle: true
---

<div class="section" id="iotcentral">
<h1>iotcentral<a class="headerlink" href="#iotcentral" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.iotcentral"></span><dl class="class">
<dt id="pulumi_azure.iotcentral.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iotcentral.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sub_domain=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iotcentral.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotCentral Application</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iotcentral_application.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iotcentral_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">display_name</span></code> name. Custom display name for the IoT Central application. Default is resource name.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> name. Possible values is <code class="docutils literal notranslate"><span class="pre">ST1</span></code>, <code class="docutils literal notranslate"><span class="pre">ST2</span></code>, Default value is <code class="docutils literal notranslate"><span class="pre">ST1</span></code></p></li>
<li><p><strong>sub_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sub_domain</span></code> name. Subdomain for the IoT Central URL. Each application must have a unique subdomain.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">template</span></code> name. IoT Central application template name. Default is a custom application.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">display_name</span></code> name. Custom display name for the IoT Central application. Default is resource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> name. Possible values is <code class="docutils literal notranslate"><span class="pre">ST1</span></code>, <code class="docutils literal notranslate"><span class="pre">ST2</span></code>, Default value is <code class="docutils literal notranslate"><span class="pre">ST1</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.sub_domain">
<code class="sig-name descname">sub_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.sub_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sub_domain</span></code> name. Subdomain for the IoT Central URL. Each application must have a unique subdomain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iotcentral.Application.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iotcentral.Application.template" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">template</span></code> name. IoT Central application template name. Default is a custom application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iotcentral.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sub_domain=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iotcentral.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">display_name</span></code> name. Custom display name for the IoT Central application. Default is resource name.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> name. Possible values is <code class="docutils literal notranslate"><span class="pre">ST1</span></code>, <code class="docutils literal notranslate"><span class="pre">ST2</span></code>, Default value is <code class="docutils literal notranslate"><span class="pre">ST1</span></code></p></li>
<li><p><strong>sub_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sub_domain</span></code> name. Subdomain for the IoT Central URL. Each application must have a unique subdomain.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">template</span></code> name. IoT Central application template name. Default is a custom application.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iotcentral.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iotcentral.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iotcentral.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iotcentral.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
