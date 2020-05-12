---
title: Module healthcare
title_tag: Module healthcare | Package pulumi_azure | Python SDK
linktitle: healthcare
notitle: true
---

<div class="section" id="healthcare">
<h1>healthcare<a class="headerlink" href="#healthcare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.healthcare"></span><dl class="py class">
<dt id="pulumi_azure.healthcare.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.healthcare.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_policy_object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cosmosdb_throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.healthcare.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.healthcare.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_policy_object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cosmosdb_throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.authentication_configurations">
<code class="sig-name descname">authentication_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.authentication_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">authentication_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.cors_configurations">
<code class="sig-name descname">cors_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.cors_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">cors_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Service is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.GetServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.healthcare.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.healthcare.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy_object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cosmosdb_throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Healthcare Service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">healthcare</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">access_policy_object_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;</span><span class="p">],</span>
    <span class="n">authentication_configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;audience&quot;</span><span class="p">:</span> <span class="s2">&quot;https://azurehealthcareapis.com/&quot;</span><span class="p">,</span>
        <span class="s2">&quot;authority&quot;</span><span class="p">:</span> <span class="s2">&quot;https://login.microsoftonline.com/$$%7Bdata.azurerm_client_config.current.tenant_id%7D&quot;</span><span class="p">,</span>
        <span class="s2">&quot;smartProxyEnabled&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">cors_configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;allowCredentials&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="s2">&quot;allowedHeaders&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;x-tempo-*&quot;</span><span class="p">,</span>
            <span class="s2">&quot;x-tempo2-*&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;allowedMethods&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;GET&quot;</span><span class="p">,</span>
            <span class="s2">&quot;PUT&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;allowedOrigins&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;http://www.example.com&quot;</span><span class="p">,</span>
            <span class="s2">&quot;http://www.example2.com&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;maxAgeInSeconds&quot;</span><span class="p">:</span> <span class="s2">&quot;500&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">cosmosdb_throughput</span><span class="o">=</span><span class="s2">&quot;2000&quot;</span><span class="p">,</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;fhir-R4&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;westus2&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;sample-resource-group&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;environment&quot;</span><span class="p">:</span> <span class="s2">&quot;testenv&quot;</span><span class="p">,</span>
        <span class="s2">&quot;purpose&quot;</span><span class="p">:</span> <span class="s2">&quot;AcceptanceTests&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">authentication_configuration</span></code> block as defined below.</p></li>
<li><p><strong>cors_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">cors_configuration</span></code> block as defined below.</p></li>
<li><p><strong>cosmosdb_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The provisioned throughput for the backing database. Range of <code class="docutils literal notranslate"><span class="pre">400</span></code>-<code class="docutils literal notranslate"><span class="pre">1000</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">400</span></code>.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the service. Values at time of publication are: <code class="docutils literal notranslate"><span class="pre">fhir</span></code>, <code class="docutils literal notranslate"><span class="pre">fhir-Stu3</span></code> and <code class="docutils literal notranslate"><span class="pre">fhir-R4</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">fhir</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the Service should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service instance. Used for service endpoint, must be unique within the audience.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Service.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The intended audience to receive authentication tokens for the service. The default value is <a class="reference external" href="https://azurehealthcareapis.com">https://azurehealthcareapis.com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
Authority must be registered to Azure AD and in the following format: <a class="reference external" href="https:/">https:/</a>/{Azure-AD-endpoint}/{tenant-id}.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smartProxyEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the ‘SMART on FHIR’ option for mobile and web implementations.</p></li>
</ul>
<p>The <strong>cors_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If credentials are allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of headers to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The methods to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of origins to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The max age to be allowed via CORS.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.authentication_configuration">
<code class="sig-name descname">authentication_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.authentication_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">authentication_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The intended audience to receive authentication tokens for the service. The default value is <a class="reference external" href="https://azurehealthcareapis.com">https://azurehealthcareapis.com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
Authority must be registered to Azure AD and in the following format: <a class="reference external" href="https:/">https:/</a>/{Azure-AD-endpoint}/{tenant-id}.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smartProxyEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables the ‘SMART on FHIR’ option for mobile and web implementations.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.cors_configuration">
<code class="sig-name descname">cors_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.cors_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">cors_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If credentials are allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of headers to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The methods to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of origins to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The max age to be allowed via CORS.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.cosmosdb_throughput">
<code class="sig-name descname">cosmosdb_throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.cosmosdb_throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The provisioned throughput for the backing database. Range of <code class="docutils literal notranslate"><span class="pre">400</span></code>-<code class="docutils literal notranslate"><span class="pre">1000</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">400</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the service. Values at time of publication are: <code class="docutils literal notranslate"><span class="pre">fhir</span></code>, <code class="docutils literal notranslate"><span class="pre">fhir-Stu3</span></code> and <code class="docutils literal notranslate"><span class="pre">fhir-R4</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">fhir</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure Region where the Service should be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service instance. Used for service endpoint, must be unique within the audience.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the Service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.healthcare.Service.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.healthcare.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.healthcare.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy_object_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cosmosdb_throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">authentication_configuration</span></code> block as defined below.</p></li>
<li><p><strong>cors_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">cors_configuration</span></code> block as defined below.</p></li>
<li><p><strong>cosmosdb_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The provisioned throughput for the backing database. Range of <code class="docutils literal notranslate"><span class="pre">400</span></code>-<code class="docutils literal notranslate"><span class="pre">1000</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">400</span></code>.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the service. Values at time of publication are: <code class="docutils literal notranslate"><span class="pre">fhir</span></code>, <code class="docutils literal notranslate"><span class="pre">fhir-Stu3</span></code> and <code class="docutils literal notranslate"><span class="pre">fhir-R4</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">fhir</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the Service should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service instance. Used for service endpoint, must be unique within the audience.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Service.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The intended audience to receive authentication tokens for the service. The default value is <a class="reference external" href="https://azurehealthcareapis.com">https://azurehealthcareapis.com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
Authority must be registered to Azure AD and in the following format: <a class="reference external" href="https:/">https:/</a>/{Azure-AD-endpoint}/{tenant-id}.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smartProxyEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the ‘SMART on FHIR’ option for mobile and web implementations.</p></li>
</ul>
<p>The <strong>cors_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If credentials are allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of headers to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The methods to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of origins to be allowed via CORS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The max age to be allowed via CORS.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.healthcare.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.healthcare.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.healthcare.get_service">
<code class="sig-prename descclassname">pulumi_azure.healthcare.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.healthcare.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Healthcare Service</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">healthcare</span><span class="o">.</span><span class="n">get_service</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-healthcare_service&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resources&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;westus2&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;healthcareServiceId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – The Azure Region where the Service is located.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Healthcare Service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Healthcare Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
