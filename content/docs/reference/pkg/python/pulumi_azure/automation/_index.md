---
---

<div class="section" id="module-pulumi_azure.automation">
<span id="automation"></span><h1>automation<a class="headerlink" href="#module-pulumi_azure.automation" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.automation.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>sku_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Automation Account. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</li>
<li><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the account - only <code class="docutils literal notranslate"><span class="pre">Basic</span></code> is supported at this time.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_account.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_primary_access_key">
<code class="descname">dsc_primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the DSC Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_secondary_access_key">
<code class="descname">dsc_secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the DSC Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_server_endpoint">
<code class="descname">dsc_server_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_server_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DSC Server Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Automation Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>) A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.sku_name">
<code class="descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU name of the account - only <code class="docutils literal notranslate"><span class="pre">Basic</span></code> is supported at this time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.BoolVariable">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">BoolVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a boolean variable in Azure Automation</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_bool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_bool.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.BoolVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.BoolVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Credential">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">Credential</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>description=None</em>, <em>name=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Credential.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description associated with this Automation Credential.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Credential. Changing this forces a new resource to be created.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this Automation Credential.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with this Automation Credential.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_credential.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_credential.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description associated with this Automation Credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Credential. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with this Automation Credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username associated with this Automation Credential.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Credential.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Credential.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DateTimeVariable">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">DateTimeVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a date/time variable in Azure Automation</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_datetime.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_datetime.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DateTimeVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DateTimeVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">DscConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>content_embedded=None</em>, <em>description=None</em>, <em>location=None</em>, <em>log_verbose=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation DSC Configuration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.</li>
<li><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Configuration script.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description to go with DSC Configuration.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be the same location as the Automation Account.</li>
<li><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.content_embedded">
<code class="descname">content_embedded</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.content_embedded" title="Permalink to this definition">¶</a></dt>
<dd><p>The PowerShell DSC Configuration script.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description to go with DSC Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be the same location as the Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.log_verbose">
<code class="descname">log_verbose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.log_verbose" title="Permalink to this definition">¶</a></dt>
<dd><p>Verbose log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscNodeConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">DscNodeConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>content_embedded=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation DSC Node Configuration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</li>
<li><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Node Configuration (mof content).</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_nodeconfiguration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_dsc_nodeconfiguration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.content_embedded">
<code class="descname">content_embedded</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.content_embedded" title="Permalink to this definition">¶</a></dt>
<dd><p>The PowerShell DSC Node Configuration (mof content).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscNodeConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscNodeConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.GetBoolVariableResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">GetBoolVariableResult</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBoolVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">GetDateTimeVariableResult</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDateTimeVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetIntVariableResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">GetIntVariableResult</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIntVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetStringVariableResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">GetStringVariableResult</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStringVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.IntVariable">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">IntVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a integer variable in Azure Automation</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_int.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_int.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.IntVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.IntVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Module">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">Module</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>module_link=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Module.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Module is created. Changing this forces a new resource to be created.</li>
<li><strong>module_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published Module link.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Module. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Module is created. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_module.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_module.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.Module.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Module is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.module_link">
<code class="descname">module_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.module_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The published Module link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Module. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Module is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Module.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Module.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.RunBook">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">RunBook</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>content=None</em>, <em>description=None</em>, <em>location=None</em>, <em>log_progress=None</em>, <em>log_verbose=None</em>, <em>name=None</em>, <em>publish_content_link=None</em>, <em>resource_group_name=None</em>, <em>runbook_type=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Runbook.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired content of the runbook.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this credential.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>log_progress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Progress log option.</li>
<li><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Runbook. Changing this forces a new resource to be created.</li>
<li><strong>publish_content_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published runbook content link.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.</li>
<li><strong>runbook_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the runbook - can be either <code class="docutils literal notranslate"><span class="pre">Graph</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShell</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShell</span></code> or <code class="docutils literal notranslate"><span class="pre">Script</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_runbook.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_runbook.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired content of the runbook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.log_progress">
<code class="descname">log_progress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.log_progress" title="Permalink to this definition">¶</a></dt>
<dd><p>Progress log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.log_verbose">
<code class="descname">log_verbose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.log_verbose" title="Permalink to this definition">¶</a></dt>
<dd><p>Verbose log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Runbook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.publish_content_link">
<code class="descname">publish_content_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.publish_content_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The published runbook content link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.runbook_type">
<code class="descname">runbook_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.runbook_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the runbook - can be either <code class="docutils literal notranslate"><span class="pre">Graph</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShell</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShell</span></code> or <code class="docutils literal notranslate"><span class="pre">Script</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.RunBook.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.RunBook.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Schedule">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">Schedule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>automation_account_name=None</em>, <em>description=None</em>, <em>expiry_time=None</em>, <em>frequency=None</em>, <em>interval=None</em>, <em>month_days=None</em>, <em>monthly_occurrences=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>start_time=None</em>, <em>timezone=None</em>, <em>week_days=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Schedule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Schedule.</li>
<li><strong>expiry_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the schedule.</li>
<li><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency of the schedule. - can be either <code class="docutils literal notranslate"><span class="pre">OneTime</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</li>
<li><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of <code class="docutils literal notranslate"><span class="pre">frequency</span></code>s between runs. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>month_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the month that the job should execute on. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">31</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last day of the month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</li>
<li><strong>monthly_occurrences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of occurrences of days within a month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>. The <code class="docutils literal notranslate"><span class="pre">monthly_occurrence</span></code> block supports fields documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Schedule. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.</li>
<li><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.</li>
<li><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone of the start time. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>. For possible values see: <a class="reference external" href="https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx">https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx</a></li>
<li><strong>week_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the week that the job should execute on. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Week</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_schedule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_schedule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.expiry_time">
<code class="descname">expiry_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.expiry_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The end time of the schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.frequency">
<code class="descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency of the schedule. - can be either <code class="docutils literal notranslate"><span class="pre">OneTime</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.interval">
<code class="descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of <code class="docutils literal notranslate"><span class="pre">frequency</span></code>s between runs. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.month_days">
<code class="descname">month_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.month_days" title="Permalink to this definition">¶</a></dt>
<dd><p>List of days of the month that the job should execute on. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">31</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last day of the month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.monthly_occurrences">
<code class="descname">monthly_occurrences</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.monthly_occurrences" title="Permalink to this definition">¶</a></dt>
<dd><p>List of occurrences of days within a month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>. The <code class="docutils literal notranslate"><span class="pre">monthly_occurrence</span></code> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Schedule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.start_time">
<code class="descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.timezone">
<code class="descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone of the start time. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>. For possible values see: <a class="reference external" href="https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx">https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.week_days">
<code class="descname">week_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.week_days" title="Permalink to this definition">¶</a></dt>
<dd><p>List of days of the week that the job should execute on. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Week</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Schedule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Schedule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.StringVariable">
<em class="property">class </em><code class="descclassname">pulumi_azure.automation.</code><code class="descname">StringVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automation_account_name=None</em>, <em>description=None</em>, <em>encrypted=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a string variable in Azure Automation</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</li>
<li><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_string.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/automation_variable_string.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.automation_account_name">
<code class="descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.encrypted">
<code class="descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.StringVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.StringVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.get_bool_variable">
<code class="descclassname">pulumi_azure.automation.</code><code class="descname">get_bool_variable</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_bool_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Bool Variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_bool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_bool.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_date_time_variable">
<code class="descclassname">pulumi_azure.automation.</code><code class="descname">get_date_time_variable</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_date_time_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Datetime Variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_datetime.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_datetime.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_int_variable">
<code class="descclassname">pulumi_azure.automation.</code><code class="descname">get_int_variable</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_int_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Int Variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_int.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_int.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_string_variable">
<code class="descclassname">pulumi_azure.automation.</code><code class="descname">get_string_variable</code><span class="sig-paren">(</span><em>automation_account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_string_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation String Variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_string.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_variable_string.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
