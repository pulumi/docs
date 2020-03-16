---
title: Module datalake
title_tag: Module datalake | Package pulumi_azure | Python SDK
linktitle: datalake
notitle: true
---

<div class="section" id="datalake">
<h1>datalake<a class="headerlink" href="#datalake" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.datalake"></span><dl class="class">
<dt id="pulumi_azure.datalake.AnalyticsAccount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">AnalyticsAccount</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_store_account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Data Lake Analytics Account.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_store_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data lake store to use by default. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics Account.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Analytics Account. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_50000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_5000AUHours</span></code>, or <code class="docutils literal notranslate"><span class="pre">Commitment_500AUHours</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.default_store_account_name">
<code class="sig-name descname">default_store_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.default_store_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the data lake store to use by default. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Analytics Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The monthly commitment tier for Data Lake Analytics Account. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_50000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_5000AUHours</span></code>, or <code class="docutils literal notranslate"><span class="pre">Commitment_500AUHours</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsAccount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_store_account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AnalyticsAccount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_store_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data lake store to use by default. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics Account.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Analytics Account. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_50000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_5000AUHours</span></code>, or <code class="docutils literal notranslate"><span class="pre">Commitment_500AUHours</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsAccount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.AnalyticsAccount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">AnalyticsFirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_ip_address=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Data Lake Analytics Firewall Rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.end_ip_address">
<code class="sig-name descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The End IP Address for the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Analytics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.start_ip_address">
<code class="sig-name descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start IP address for the firewall rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AnalyticsFirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.AwaitableGetStoreResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">AwaitableGetStoreResult</code><span class="sig-paren">(</span><em class="sig-param">encryption_state=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">firewall_allow_azure_ips=None</em>, <em class="sig-param">firewall_state=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AwaitableGetStoreResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.GetStoreResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">GetStoreResult</code><span class="sig-paren">(</span><em class="sig-param">encryption_state=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">firewall_allow_azure_ips=None</em>, <em class="sig-param">firewall_state=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStore.</p>
<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.encryption_state">
<code class="sig-name descname">encryption_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.encryption_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the Encryption State of this Data Lake Store Account, such as <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.encryption_type">
<code class="sig-name descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>the Encryption Type used for this Data Lake Store Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.firewall_allow_azure_ips">
<code class="sig-name descname">firewall_allow_azure_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.firewall_allow_azure_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>are Azure Service IP’s allowed through the firewall?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.firewall_state">
<code class="sig-name descname">firewall_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.firewall_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the state of the firewall, such as <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Current monthly commitment tier for the account.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.Store">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">Store</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encryption_state=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">firewall_allow_azure_ips=None</em>, <em class="sig-param">firewall_state=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Data Lake Store.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encryption_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is Encryption enabled on this Data Lake Store Account? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Type used for this Data Lake Store Account. Currently can be set to <code class="docutils literal notranslate"><span class="pre">ServiceManaged</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> - and must be a blank string when it’s Disabled.</p></li>
<li><p><strong>firewall_allow_azure_ips</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – are Azure Service IP’s allowed through the firewall? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p></li>
<li><p><strong>firewall_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the state of the Firewall. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Store. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1PB</span></code> or <code class="docutils literal notranslate"><span class="pre">Commitment_5PB</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.encryption_state">
<code class="sig-name descname">encryption_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.encryption_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Encryption enabled on this Data Lake Store Account? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.encryption_type">
<code class="sig-name descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Type used for this Data Lake Store Account. Currently can be set to <code class="docutils literal notranslate"><span class="pre">ServiceManaged</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> - and must be a blank string when it’s Disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint for the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.firewall_allow_azure_ips">
<code class="sig-name descname">firewall_allow_azure_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.firewall_allow_azure_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>are Azure Service IP’s allowed through the firewall? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.firewall_state">
<code class="sig-name descname">firewall_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.firewall_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the state of the Firewall. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The monthly commitment tier for Data Lake Store. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1PB</span></code> or <code class="docutils literal notranslate"><span class="pre">Commitment_5PB</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.Store.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">encryption_state=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">firewall_allow_azure_ips=None</em>, <em class="sig-param">firewall_state=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Store resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encryption_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is Encryption enabled on this Data Lake Store Account? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Type used for this Data Lake Store Account. Currently can be set to <code class="docutils literal notranslate"><span class="pre">ServiceManaged</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> - and must be a blank string when it’s Disabled.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint for the Data Lake Store.</p></li>
<li><p><strong>firewall_allow_azure_ips</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – are Azure Service IP’s allowed through the firewall? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p></li>
<li><p><strong>firewall_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the state of the Firewall. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Store. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1PB</span></code> or <code class="docutils literal notranslate"><span class="pre">Commitment_5PB</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.Store.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.Store.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.StoreFile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">StoreFile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">local_file_path=None</em>, <em class="sig-param">remote_file_path=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Data Lake Store File.</p>
<blockquote>
<div><p><strong>Note:</strong> If you want to change the data in the remote file without changing the <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>, then
taint the resource so the <code class="docutils literal notranslate"><span class="pre">datalake.StoreFile</span></code> gets recreated with the new data.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_file.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_file.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the File should created.</p></li>
<li><p><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the local file to be added to the Data Lake Store.</p></li>
<li><p><strong>remote_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path created for the file on the Data Lake Store.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store for which the File should created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.local_file_path">
<code class="sig-name descname">local_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.local_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the local file to be added to the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.remote_file_path">
<code class="sig-name descname">remote_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.remote_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path created for the file on the Data Lake Store.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">local_file_path=None</em>, <em class="sig-param">remote_file_path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StoreFile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the File should created.</p></li>
<li><p><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the local file to be added to the Data Lake Store.</p></li>
<li><p><strong>remote_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path created for the file on the Data Lake Store.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.StoreFile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.StoreFirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">StoreFirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_ip_address=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Data Lake Store Firewall Rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.end_ip_address">
<code class="sig-name descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The End IP Address for the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.start_ip_address">
<code class="sig-name descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start IP address for the firewall rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StoreFirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.datalake.StoreFirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.datalake.get_store">
<code class="sig-prename descclassname">pulumi_azure.datalake.</code><code class="sig-name descname">get_store</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.get_store" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Data Lake Store.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/data_lake_store.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/data_lake_store.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Data Lake Store.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the Data Lake Store exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
