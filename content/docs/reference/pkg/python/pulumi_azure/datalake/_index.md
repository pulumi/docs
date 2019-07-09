---
---

<div class="section" id="module-pulumi_azure.datalake">
<span id="datalake"></span><h1>datalake<a class="headerlink" href="#module-pulumi_azure.datalake" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.datalake.AnalyticsAccount">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">AnalyticsAccount</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_store_account_name=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Data Lake Analytics Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_store_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data lake store to use by default. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics Account.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Analytics Account. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_50000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_5000AUHours</span></code>, or <code class="docutils literal notranslate"><span class="pre">Commitment_500AUHours</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_account.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.default_store_account_name">
<code class="descname">default_store_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.default_store_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the data lake store to use by default. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Analytics Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsAccount.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The monthly commitment tier for Data Lake Analytics Account. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_50000AUHours</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_5000AUHours</span></code>, or <code class="docutils literal notranslate"><span class="pre">Commitment_500AUHours</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsAccount.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsAccount.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">AnalyticsFirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>start_ip_address=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Azure Data Lake Analytics Firewall Rule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.</li>
<li><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Analytics.</li>
<li><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_analytics_firewall_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.end_ip_address">
<code class="descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The End IP Address for the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Analytics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.start_ip_address">
<code class="descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start IP address for the firewall rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.AnalyticsFirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.AnalyticsFirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.GetStoreResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">GetStoreResult</code><span class="sig-paren">(</span><em>encryption_state=None</em>, <em>encryption_type=None</em>, <em>firewall_allow_azure_ips=None</em>, <em>firewall_state=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStore.</p>
<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.encryption_state">
<code class="descname">encryption_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.encryption_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the Encryption State of this Data Lake Store Account, such as <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.encryption_type">
<code class="descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>the Encryption Type used for this Data Lake Store Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.firewall_allow_azure_ips">
<code class="descname">firewall_allow_azure_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.firewall_allow_azure_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>are Azure Service IP’s allowed through the firewall?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.firewall_state">
<code class="descname">firewall_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.firewall_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the state of the firewall, such as <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Current monthly commitment tier for the account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.GetStoreResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.GetStoreResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.Store">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">Store</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>encryption_state=None</em>, <em>encryption_type=None</em>, <em>firewall_allow_azure_ips=None</em>, <em>firewall_state=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Data Lake Store.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>encryption_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is Encryption enabled on this Data Lake Store Account? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</li>
<li><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Type used for this Data Lake Store Account. Currently can be set to <code class="docutils literal notranslate"><span class="pre">ServiceManaged</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> - and must be a blank string when it’s Disabled.</li>
<li><strong>firewall_allow_azure_ips</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – are Azure Service IP’s allowed through the firewall? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></li>
<li><strong>firewall_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the state of the Firewall. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monthly commitment tier for Data Lake Store. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1PB</span></code> or <code class="docutils literal notranslate"><span class="pre">Commitment_5PB</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.encryption_state">
<code class="descname">encryption_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.encryption_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Encryption enabled on this Data Lake Store Account? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.encryption_type">
<code class="descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Type used for this Data Lake Store Account. Currently can be set to <code class="docutils literal notranslate"><span class="pre">ServiceManaged</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> - and must be a blank string when it’s Disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint for the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.firewall_allow_azure_ips">
<code class="descname">firewall_allow_azure_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.firewall_allow_azure_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>are Azure Service IP’s allowed through the firewall? Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.firewall_state">
<code class="descname">firewall_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.firewall_state" title="Permalink to this definition">¶</a></dt>
<dd><p>the state of the Firewall. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled.</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.Store.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.Store.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The monthly commitment tier for Data Lake Store. Accepted values are <code class="docutils literal notranslate"><span class="pre">Consumption</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_10TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_100TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_500TB</span></code>, <code class="docutils literal notranslate"><span class="pre">Commitment_1PB</span></code> or <code class="docutils literal notranslate"><span class="pre">Commitment_5PB</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.Store.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.Store.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.Store.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.StoreFile">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">StoreFile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>local_file_path=None</em>, <em>remote_file_path=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Azure Data Lake Store File.</p>
<blockquote>
<div><strong>Note:</strong> If you want to change the data in the remote file without changing the <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>, then 
taint the resource so the <code class="docutils literal notranslate"><span class="pre">azurerm_data_lake_store_file</span></code> gets recreated with the new data.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the File should created.</li>
<li><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the local file to be added to the Data Lake Store.</li>
<li><strong>remote_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path created for the file on the Data Lake Store.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_file.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_file.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store for which the File should created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.local_file_path">
<code class="descname">local_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.local_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the local file to be added to the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFile.remote_file_path">
<code class="descname">remote_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.remote_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path created for the file on the Data Lake Store.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFile.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.datalake.StoreFirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.datalake.</code><code class="descname">StoreFirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>start_ip_address=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Azure Data Lake Store Firewall Rule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.</li>
<li><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End IP Address for the firewall rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Data Lake Store.</li>
<li><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Start IP address for the firewall rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_lake_store_firewall_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.end_ip_address">
<code class="descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The End IP Address for the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Data Lake Store.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.datalake.StoreFirewallRule.start_ip_address">
<code class="descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Start IP address for the firewall rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.datalake.StoreFirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.StoreFirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.datalake.get_store">
<code class="descclassname">pulumi_azure.datalake.</code><code class="descname">get_store</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.datalake.get_store" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Data Lake Store.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/data_lake_store.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/data_lake_store.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
