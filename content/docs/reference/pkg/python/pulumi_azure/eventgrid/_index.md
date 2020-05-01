---
title: Module eventgrid
title_tag: Module eventgrid | Package pulumi_azure | Python SDK
linktitle: eventgrid
notitle: true
---

<div class="section" id="eventgrid">
<h1>eventgrid<a class="headerlink" href="#eventgrid" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.eventgrid"></span><dl class="py class">
<dt id="pulumi_azure.eventgrid.AwaitableGetTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">AwaitableGetTopicResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.AwaitableGetTopicResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.eventgrid.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_mapping_default_values</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_mapping_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Domain</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>input_mapping_default_values</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p></li>
<li><p><strong>input_mapping_fields</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p></li>
<li><p><strong>input_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>input_mapping_default_values</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>input_mapping_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.input_mapping_default_values">
<code class="sig-name descname">input_mapping_default_values</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.input_mapping_default_values" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.input_mapping_fields">
<code class="sig-name descname">input_mapping_fields</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.input_mapping_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.input_schema">
<code class="sig-name descname">input_schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.input_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Domain.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_mapping_default_values</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_mapping_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint associated with the EventGrid Domain.</p></li>
<li><p><strong>input_mapping_default_values</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p></li>
<li><p><strong>input_mapping_fields</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p></li>
<li><p><strong>input_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Shared Access Key associated with the EventGrid Domain.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Shared Access Key associated with the EventGrid Domain.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>input_mapping_default_values</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>input_mapping_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventgrid.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventgrid.EventSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">EventSubscription</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_delivery_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hybrid_connection_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">included_event_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_blob_dead_letter_destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_queue_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Event Subscription</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>event_delivery_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p></li>
<li><p><strong>eventhub_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>hybrid_connection_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>included_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applicable event types that need to be part of the event subscription.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of labels to assign to the event subscription.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retry_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_blob_dead_letter_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p></li>
<li><p><strong>storage_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the topic to associate with the event subscription.</p></li>
<li><p><strong>webhook_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>eventhub_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>hybrid_connection_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>retry_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
<p>The <strong>storage_blob_dead_letter_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
<p>The <strong>storage_queue_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage queue is located.</p></li>
</ul>
<p>The <strong>subject_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
<p>The <strong>webhook_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.event_delivery_schema">
<code class="sig-name descname">event_delivery_schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.event_delivery_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.eventhub_endpoint">
<code class="sig-name descname">eventhub_endpoint</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.eventhub_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.hybrid_connection_endpoint">
<code class="sig-name descname">hybrid_connection_endpoint</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.hybrid_connection_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.included_event_types">
<code class="sig-name descname">included_event_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.included_event_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applicable event types that need to be part of the event subscription.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of labels to assign to the event subscription.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.retry_policy">
<code class="sig-name descname">retry_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.retry_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.storage_blob_dead_letter_destination">
<code class="sig-name descname">storage_blob_dead_letter_destination</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.storage_blob_dead_letter_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.storage_queue_endpoint">
<code class="sig-name descname">storage_queue_endpoint</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.storage_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the id of the storage account id where the storage queue is located.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.subject_filter">
<code class="sig-name descname">subject_filter</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.subject_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.topic_name">
<code class="sig-name descname">topic_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the topic to associate with the event subscription.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.EventSubscription.webhook_endpoint">
<code class="sig-name descname">webhook_endpoint</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.webhook_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.EventSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_delivery_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hybrid_connection_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">included_event_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_blob_dead_letter_destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_queue_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_endpoint</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>event_delivery_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p></li>
<li><p><strong>eventhub_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>hybrid_connection_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>included_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applicable event types that need to be part of the event subscription.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of labels to assign to the event subscription.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retry_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_blob_dead_letter_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p></li>
<li><p><strong>storage_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the topic to associate with the event subscription.</p></li>
<li><p><strong>webhook_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>eventhub_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventhub_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the eventhub where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>hybrid_connection_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hybridConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the hybrid connection where the Event Subscription will receive events.</p></li>
</ul>
<p>The <strong>retry_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventTimeToLive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (in minutes) for events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDeliveryAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the maximum number of delivery retry attempts for events.</p></li>
</ul>
<p>The <strong>storage_blob_dead_letter_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage blob is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageBlobContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Storage blob container that is the destination of the deadletter events</p></li>
</ul>
<p>The <strong>storage_queue_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">queue_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage queue where the Event Subscriptio will receive events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the id of the storage account id where the storage queue is located.</p></li>
</ul>
<p>The <strong>subject_filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if <code class="docutils literal notranslate"><span class="pre">subject_begins_with</span></code> and <code class="docutils literal notranslate"><span class="pre">subject_ends_with</span></code> case sensitive. This value defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectBeginsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subjectEndsWith</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string to filter events for an event subscription based on a resource path suffix.</p></li>
</ul>
<p>The <strong>webhook_endpoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the url of the webhook where the Event Subscription will receive events.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.EventSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventgrid.EventSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventgrid.GetTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">GetTopicResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.GetTopicResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopic.</p>
<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.GetTopicResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.GetTopicResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.GetTopicResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.GetTopicResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.GetTopicResult.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.GetTopicResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.GetTopicResult.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.GetTopicResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.eventgrid.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Topic</p>
<blockquote>
<div><p><strong>Note:</strong> at this time EventGrid Topic’s are only available in a limited number of regions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.eventgrid.Topic.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint associated with the EventGrid Topic.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Shared Access Key associated with the EventGrid Topic.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Shared Access Key associated with the EventGrid Topic.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.eventgrid.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventgrid.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_azure.eventgrid.get_topic">
<code class="sig-prename descclassname">pulumi_azure.eventgrid.</code><code class="sig-name descname">get_topic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventgrid.get_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing EventGrid Topic</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the EventGrid Topic resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the EventGrid Topic exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
