---
title: Module service_endpoint
title_tag: Module service_endpoint | Package pulumi_azuredevops | Python SDK
linktitle: service_endpoint
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="service-endpoint">
<h1>service_endpoint<a class="headerlink" href="#service-endpoint" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.service_endpoint"></span><dl class="py class">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.service_endpoint.</code><code class="sig-name descname">AzureRM</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.</p>
<p>Before to create a service end point in Azure DevOps, you need to create a Service Principal in your Azure subscription.</p>
<p>For detailed steps to create a service principal with Azure cli see the <a class="reference external" href="https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest">documentation</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">endpointazure</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">AzureRM</span><span class="p">(</span><span class="s2">&quot;endpointazure&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;TestServiceRM&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;serviceprincipalid&quot;</span><span class="p">:</span> <span class="s2">&quot;xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx&quot;</span><span class="p">,</span>
        <span class="s2">&quot;serviceprincipalkey&quot;</span><span class="p">:</span> <span class="s2">&quot;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="s2">&quot;xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="s2">&quot;xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="s2">&quot;Sample Subscription&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">endpointazure</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">AzureRM</span><span class="p">(</span><span class="s2">&quot;endpointazure&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;TestServiceRM&quot;</span><span class="p">,</span>
    <span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="s2">&quot;xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="s2">&quot;xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="s2">&quot;Microsoft Azure DEMO&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service End points</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurerm_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id if the service principal.</p></li>
<li><p><strong>azurerm_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Id of the Azure targets.</p></li>
<li><p><strong>azurerm_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Name of the targets.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group used for scope of automatic service endpoint.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal application Id</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkeyHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.azurerm_spn_tenantid">
<code class="sig-name descname">azurerm_spn_tenantid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.azurerm_spn_tenantid" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id if the service principal.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.azurerm_subscription_id">
<code class="sig-name descname">azurerm_subscription_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.azurerm_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription Id of the Azure targets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.azurerm_subscription_name">
<code class="sig-name descname">azurerm_subscription_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.azurerm_subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription Name of the targets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.credentials">
<code class="sig-name descname">credentials</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service principal application Id</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service principal secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkeyHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.resource_group">
<code class="sig-name descname">resource_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group used for scope of automatic service endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.service_endpoint_name">
<code class="sig-name descname">service_endpoint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AzureRM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurerm_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id if the service principal.</p></li>
<li><p><strong>azurerm_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Id of the Azure targets.</p></li>
<li><p><strong>azurerm_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Name of the targets.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group used for scope of automatic service endpoint.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal application Id</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceprincipalkeyHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.AzureRM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.AzureRM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.BitBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.service_endpoint.</code><code class="sig-name descname">BitBucket</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Bitbucket service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">serviceendpoint</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">BitBucket</span><span class="p">(</span><span class="s2">&quot;serviceendpoint&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;test-bitbucket&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account password.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account username.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Bitbucket account password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.password_hash">
<code class="sig-name descname">password_hash</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.password_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘password’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.service_endpoint_name">
<code class="sig-name descname">service_endpoint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Bitbucket account username.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_hash</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BitBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account password.</p></li>
<li><p><strong>password_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘password’</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account username.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.BitBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.BitBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.service_endpoint.</code><code class="sig-name descname">DockerRegistry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_registry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Docker Registry service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="c1"># dockerhub registry service connection</span>
<span class="n">dockerhubregistry</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">DockerRegistry</span><span class="p">(</span><span class="s2">&quot;dockerhubregistry&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample Docker Hub&quot;</span><span class="p">,</span>
    <span class="n">docker_username</span><span class="o">=</span><span class="s2">&quot;sample&quot;</span><span class="p">,</span>
    <span class="n">docker_email</span><span class="o">=</span><span class="s2">&quot;email@example.com&quot;</span><span class="p">,</span>
    <span class="n">docker_password</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">registry_type</span><span class="o">=</span><span class="s2">&quot;DockerHub&quot;</span><span class="p">)</span>
<span class="c1"># other docker registry service connection</span>
<span class="n">otherregistry</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">DockerRegistry</span><span class="p">(</span><span class="s2">&quot;otherregistry&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample Docker Registry&quot;</span><span class="p">,</span>
    <span class="n">docker_registry</span><span class="o">=</span><span class="s2">&quot;https://sample.azurecr.io/v1&quot;</span><span class="p">,</span>
    <span class="n">docker_username</span><span class="o">=</span><span class="s2">&quot;sample&quot;</span><span class="p">,</span>
    <span class="n">docker_password</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">registry_type</span><span class="o">=</span><span class="s2">&quot;Others&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service Endpoints</a></p></li>
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&amp;tabs=yaml#sep-docreg">Docker Registry Service Connection</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>docker_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email for Docker account user.</p></li>
<li><p><strong>docker_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the account user identified above.</p></li>
<li><p><strong>docker_registry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p></li>
<li><p><strong>docker_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the Docker account user.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>registry_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be “DockerHub” or “Others” (Default “DockerHub”)</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.docker_email">
<code class="sig-name descname">docker_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.docker_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email for Docker account user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.docker_password">
<code class="sig-name descname">docker_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.docker_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the account user identified above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.docker_password_hash">
<code class="sig-name descname">docker_password_hash</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.docker_password_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘docker_password’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.docker_registry">
<code class="sig-name descname">docker_registry</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.docker_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.docker_username">
<code class="sig-name descname">docker_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.docker_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the Docker account user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.registry_type">
<code class="sig-name descname">registry_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.registry_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be “DockerHub” or “Others” (Default “DockerHub”)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.service_endpoint_name">
<code class="sig-name descname">service_endpoint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password_hash</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_registry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DockerRegistry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>docker_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email for Docker account user.</p></li>
<li><p><strong>docker_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the account user identified above.</p></li>
<li><p><strong>docker_password_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘docker_password’</p></li>
<li><p><strong>docker_registry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p></li>
<li><p><strong>docker_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the Docker account user.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>registry_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be “DockerHub” or “Others” (Default “DockerHub”)</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.DockerRegistry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.DockerRegistry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.GitHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.service_endpoint.</code><code class="sig-name descname">GitHub</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_oauth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_personal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a GitHub service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">serviceendpoint_gh1</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">GitHub</span><span class="p">(</span><span class="s2">&quot;serviceendpointGh1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample GithHub Personal Access Token&quot;</span><span class="p">,</span>
    <span class="n">auth_personal</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;personalAccessToken&quot;</span><span class="p">:</span> <span class="s2">&quot;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_oauth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p></li>
<li><p><strong>auth_personal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_oauth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oauthConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>auth_personal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Personal Access Token for Github.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessTokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.auth_oauth">
<code class="sig-name descname">auth_oauth</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.auth_oauth" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oauthConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.auth_personal">
<code class="sig-name descname">auth_personal</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.auth_personal" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Personal Access Token for Github.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessTokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.service_endpoint_name">
<code class="sig-name descname">service_endpoint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_oauth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_personal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GitHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_oauth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p></li>
<li><p><strong>auth_personal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_oauth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oauthConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>auth_personal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Personal Access Token for Github.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">personalAccessTokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.GitHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.GitHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.GitHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.service_endpoint.</code><code class="sig-name descname">Kubernetes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apiserver_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfigs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_accounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Kubernetes service endpoint within Azure DevOps.</p>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Endpoints</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apiserver_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint description.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p></li>
<li><p><strong>azure_subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”AzureSubscription”.</p></li>
<li><p><strong>kubeconfigs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”Kubeconfig”.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_subscriptions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureEnvironment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kubernetes namespace. Default value is “default”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourcegroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource group id, to which the Kubernetes cluster is deployed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the tenant used by the subscription.</p></li>
</ul>
<p>The <strong>kubeconfigs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptUntrustedCerts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this option to allow clients to accept a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfigHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caCertHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.apiserver_url">
<code class="sig-name descname">apiserver_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.apiserver_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.authorization_type">
<code class="sig-name descname">authorization_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.azure_subscriptions">
<code class="sig-name descname">azure_subscriptions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.azure_subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”AzureSubscription”.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureEnvironment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kubernetes namespace. Default value is “default”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourcegroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource group id, to which the Kubernetes cluster is deployed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The id of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The id of the tenant used by the subscription.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.kubeconfigs">
<code class="sig-name descname">kubeconfigs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.kubeconfigs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”Kubeconfig”.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptUntrustedCerts</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set this option to allow clients to accept a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterContext</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfigHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.service_accounts">
<code class="sig-name descname">service_accounts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.service_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The certificate from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caCertHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The token from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.service_endpoint_name">
<code class="sig-name descname">service_endpoint_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apiserver_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfigs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_accounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Kubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apiserver_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint description.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p></li>
<li><p><strong>azure_subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”AzureSubscription”.</p></li>
<li><p><strong>kubeconfigs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”Kubeconfig”.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_subscriptions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureEnvironment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kubernetes namespace. Default value is “default”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourcegroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource group id, to which the Kubernetes cluster is deployed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscriptionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the tenant used by the subscription.</p></li>
</ul>
<p>The <strong>kubeconfigs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptUntrustedCerts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this option to allow clients to accept a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeConfigHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caCertHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token from a Kubernetes secret object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.service_endpoint.Kubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.service_endpoint.Kubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
