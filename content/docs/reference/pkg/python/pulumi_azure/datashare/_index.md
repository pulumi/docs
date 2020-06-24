---
title: Module datashare
title_tag: Module datashare | Package pulumi_azure | Python SDK
linktitle: datashare
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="datashare">
<h1>datashare<a class="headerlink" href="#datashare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.datashare"></span><dl class="py class">
<dt id="pulumi_azure.datashare.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Data Share Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">identity</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;SystemAssigned&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share Account. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Data Share Account.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Data Share Account. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.Account.identity">
<code class="sig-name descname">identity</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Account.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the Data Share Account. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Account.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Account.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Data Share Account. Changing this forces a new Data Share Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Account.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to the Data Share Account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share Account. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Data Share Account should exist. Changing this forces a new Data Share Account to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Data Share Account.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Data Share Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Data Share Account. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.AwaitableGetDatasetBlobStorageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">AwaitableGetDatasetBlobStorageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_accounts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.AwaitableGetDatasetBlobStorageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.AwaitableGetShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">AwaitableGetShareResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.AwaitableGetShareResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.DatasetBlobStorage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">DatasetBlobStorage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Data Share Blob Storage Dataset.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>
<span class="kn">import</span> <span class="nn">pulumi_azuread</span> <span class="k">as</span> <span class="nn">azuread</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">identity</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;SystemAssigned&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">example_share</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">Share</span><span class="p">(</span><span class="s2">&quot;exampleShare&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;CopyBased&quot;</span><span class="p">)</span>
<span class="n">example_storage_account_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleStorage/accountAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;RAGRS&quot;</span><span class="p">)</span>
<span class="n">example_container</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;exampleContainer&quot;</span><span class="p">,</span>
    <span class="n">storage_account_name</span><span class="o">=</span><span class="n">example_storage</span> <span class="o">/</span> <span class="n">account_account</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">container_access_type</span><span class="o">=</span><span class="s2">&quot;container&quot;</span><span class="p">)</span>
<span class="n">example_service_principal</span> <span class="o">=</span> <span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="n">azuread</span><span class="o">.</span><span class="n">get_service_principal</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="n">name</span><span class="p">))</span>
<span class="n">example_assignment</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">authorization</span><span class="o">.</span><span class="n">Assignment</span><span class="p">(</span><span class="s2">&quot;exampleAssignment&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="n">example_storage</span> <span class="o">/</span> <span class="n">account_account</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">role_definition_name</span><span class="o">=</span><span class="s2">&quot;Storage Blob Data Reader&quot;</span><span class="p">,</span>
    <span class="n">principal_id</span><span class="o">=</span><span class="n">example_service_principal</span><span class="o">.</span><span class="n">object_id</span><span class="p">)</span>
<span class="n">example_dataset_blob_storage</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">DatasetBlobStorage</span><span class="p">(</span><span class="s2">&quot;exampleDatasetBlobStorage&quot;</span><span class="p">,</span>
    <span class="n">data_share_id</span><span class="o">=</span><span class="n">example_share</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">container_name</span><span class="o">=</span><span class="n">example_container</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">storage_account</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">example_storage</span> <span class="o">/</span> <span class="n">account_account</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
        <span class="s2">&quot;resource_group_name&quot;</span><span class="p">:</span> <span class="n">example_storage</span> <span class="o">/</span> <span class="n">account_account</span><span class="p">[</span><span class="s2">&quot;resourceGroupName&quot;</span><span class="p">],</span>
        <span class="s2">&quot;subscription_id&quot;</span><span class="p">:</span> <span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">file_path</span><span class="o">=</span><span class="s2">&quot;myfile.txt&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage account container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>data_share_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Share in which this Data Share Blob Storage Dataset should be created. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the file in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>folder_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the folder in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share Blob Storage Dataset. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>storage_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource group name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subscription id of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.container_name">
<code class="sig-name descname">container_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage account container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.data_share_id">
<code class="sig-name descname">data_share_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.data_share_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Data Share in which this Data Share Blob Storage Dataset should be created. Changing this forces a new Data Share Blob Storage Dataset to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Data Share Dataset.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.file_path">
<code class="sig-name descname">file_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the file in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.folder_path">
<code class="sig-name descname">folder_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.folder_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the folder in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Data Share Blob Storage Dataset. Changing this forces a new Data Share Blob Storage Dataset to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.storage_account">
<code class="sig-name descname">storage_account</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.storage_account" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource group name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subscription id of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetBlobStorage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage account container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>data_share_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Share in which this Data Share Blob Storage Dataset should be created. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Data Share Dataset.</p></li>
<li><p><strong>file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the file in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>folder_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the folder in the storage container to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share Blob Storage Dataset. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><strong>storage_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource group name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subscription id of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.DatasetBlobStorage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.DatasetBlobStorage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.DatasetBlobStorage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetAccountResult.identities">
<code class="sig-name descname">identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetAccountResult.identities" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetAccountResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Data Share Account.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">GetDatasetBlobStorageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_accounts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatasetBlobStorage.</p>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.container_name">
<code class="sig-name descname">container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage account container to be shared with the receiver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Data Share Dataset.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.file_path">
<code class="sig-name descname">file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the file in the storage container to be shared with the receiver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.folder_path">
<code class="sig-name descname">folder_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.folder_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder path of the file in the storage container to be shared with the receiver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage account to be shared with the receiver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetDatasetBlobStorageResult.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetDatasetBlobStorageResult.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.GetShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">GetShareResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getShare.</p>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Data Share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of the Data Share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the snapshot schedule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.snapshot_schedules">
<code class="sig-name descname">snapshot_schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.snapshot_schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">snapshot_schedule</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.GetShareResult.terms">
<code class="sig-name descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.GetShareResult.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>The terms of the Data Share.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.datashare.Share">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">Share</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Share" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Data Share.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">example_share</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">Share</span><span class="p">(</span><span class="s2">&quot;exampleShare&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;CopyBased&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example desc&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="s2">&quot;example terms&quot;</span><span class="p">,</span>
    <span class="n">snapshot_schedule</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example-ss&quot;</span><span class="p">,</span>
        <span class="s2">&quot;recurrence&quot;</span><span class="p">:</span> <span class="s2">&quot;Day&quot;</span><span class="p">,</span>
        <span class="s2">&quot;start_time&quot;</span><span class="p">:</span> <span class="s2">&quot;2020-04-17T04:47:52.9614956Z&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Share account in which the Data Share is created. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Share’s description.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of the Data Share. Possible values are <code class="docutils literal notranslate"><span class="pre">CopyBased</span></code> and <code class="docutils literal notranslate"><span class="pre">InPlace</span></code>. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>snapshot_schedule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">snapshot_schedule</span></code> block as defined below.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The terms of the Data Share.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>snapshot_schedule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the snapshot schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval of the synchronization with the source data. Possible values are <code class="docutils literal notranslate"><span class="pre">Hour</span></code> and <code class="docutils literal notranslate"><span class="pre">Day</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The synchronization with the source data’s start time.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Data Share account in which the Data Share is created. Changing this forces a new Data Share to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Share’s description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of the Data Share. Possible values are <code class="docutils literal notranslate"><span class="pre">CopyBased</span></code> and <code class="docutils literal notranslate"><span class="pre">InPlace</span></code>. Changing this forces a new Data Share to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Data Share. Changing this forces a new Data Share to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.snapshot_schedule">
<code class="sig-name descname">snapshot_schedule</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.snapshot_schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">snapshot_schedule</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the snapshot schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The interval of the synchronization with the source data. Possible values are <code class="docutils literal notranslate"><span class="pre">Hour</span></code> and <code class="docutils literal notranslate"><span class="pre">Day</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The synchronization with the source data’s start time.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.datashare.Share.terms">
<code class="sig-name descname">terms</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datashare.Share.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>The terms of the Data Share.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.Share.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Share.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Share resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Data Share account in which the Data Share is created. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Share’s description.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of the Data Share. Possible values are <code class="docutils literal notranslate"><span class="pre">CopyBased</span></code> and <code class="docutils literal notranslate"><span class="pre">InPlace</span></code>. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Data Share. Changing this forces a new Data Share to be created.</p></li>
<li><p><strong>snapshot_schedule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">snapshot_schedule</span></code> block as defined below.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The terms of the Data Share.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>snapshot_schedule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the snapshot schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval of the synchronization with the source data. Possible values are <code class="docutils literal notranslate"><span class="pre">Hour</span></code> and <code class="docutils literal notranslate"><span class="pre">Day</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The synchronization with the source data’s start time.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.datashare.Share.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Share.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.Share.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.Share.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datashare.get_account">
<code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Data Share Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resource-group&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of this Data Share Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group where the Data Share Account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.datashare.get_dataset_blob_storage">
<code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">get_dataset_blob_storage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data_share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.get_dataset_blob_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Data Share Blob Storage Dataset.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">get_dataset_blob_storage</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-dsbsds&quot;</span><span class="p">,</span>
    <span class="n">data_share_id</span><span class="o">=</span><span class="s2">&quot;example-share-id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data_share_id</strong> (<em>str</em>) – The ID of the Data Share in which this Data Share Blob Storage Dataset should be created.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this Data Share Blob Storage Dataset.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.datashare.get_share">
<code class="sig-prename descclassname">pulumi_azure.datashare.</code><code class="sig-name descname">get_share</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datashare.get_share" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Data Share.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resource-group&quot;</span><span class="p">)</span>
<span class="n">example_share</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">datashare</span><span class="o">.</span><span class="n">get_share</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;existing&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azurerm_data_share_account&quot;</span><span class="p">][</span><span class="s2">&quot;exmaple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">example_share</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_id</strong> (<em>str</em>) – The ID of the Data Share account in which the Data Share is created.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this Data Share.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
