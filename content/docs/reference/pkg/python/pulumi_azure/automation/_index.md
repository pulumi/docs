---
title: Module automation
title_tag: Module automation | Package pulumi_azure | Python SDK
linktitle: automation
notitle: true
---

<div class="section" id="automation">
<h1>automation<a class="headerlink" href="#automation" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.automation"></span><dl class="class">
<dt id="pulumi_azure.automation.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Automation Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the account - only <code class="docutils literal notranslate"><span class="pre">Basic</span></code> is supported at this time.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_primary_access_key">
<code class="sig-name descname">dsc_primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the DSC Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_secondary_access_key">
<code class="sig-name descname">dsc_secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the DSC Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.dsc_server_endpoint">
<code class="sig-name descname">dsc_server_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.dsc_server_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DSC Server Endpoint associated with this Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Automation Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU name of the account - only <code class="docutils literal notranslate"><span class="pre">Basic</span></code> is supported at this time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dsc_primary_access_key=None</em>, <em class="sig-param">dsc_secondary_access_key=None</em>, <em class="sig-param">dsc_server_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dsc_primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Access Key for the DSC Endpoint associated with this Automation Account.</p></li>
<li><p><strong>dsc_secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Access Key for the DSC Endpoint associated with this Automation Account.</p></li>
<li><p><strong>dsc_server_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DSC Server Endpoint associated with this Automation Account.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Automation Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the account - only <code class="docutils literal notranslate"><span class="pre">Basic</span></code> is supported at this time.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.AwaitableGetBoolVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">AwaitableGetBoolVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.AwaitableGetBoolVariableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.AwaitableGetDateTimeVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">AwaitableGetDateTimeVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.AwaitableGetDateTimeVariableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.AwaitableGetIntVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">AwaitableGetIntVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.AwaitableGetIntVariableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.AwaitableGetStringVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">AwaitableGetStringVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.AwaitableGetStringVariableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.BoolVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">BoolVariable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a boolean variable in Azure Automation</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.BoolVariable.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.BoolVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BoolVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.BoolVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.BoolVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.BoolVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">base64=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Automation Certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Certificate is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded value of the certificate.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Automation Certificate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Certificate is created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Certificate is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.base64">
<code class="sig-name descname">base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded value of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Automation Certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Certificate is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Certificate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint for the certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">base64=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">exportable=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">thumbprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Certificate is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoded value of the certificate.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Automation Certificate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Certificate is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thumbprint for the certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Credential">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">Credential</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Credential.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description associated with this Automation Credential.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Credential. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this Automation Credential.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with this Automation Credential.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description associated with this Automation Credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Credential. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with this Automation Credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Credential.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Credential.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username associated with this Automation Credential.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Credential.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Credential resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description associated with this Automation Credential.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Credential. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this Automation Credential.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with this Automation Credential.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Credential.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Credential.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Credential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DateTimeVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">DateTimeVariable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DateTime variable in Azure Automation</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DateTimeVariable.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DateTimeVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DateTimeVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DateTimeVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DateTimeVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DateTimeVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">DscConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">content_embedded=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">log_verbose=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation DSC Configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Configuration script.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description to go with DSC Configuration.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be the same location as the Automation Account.</p></li>
<li><p><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.content_embedded">
<code class="sig-name descname">content_embedded</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.content_embedded" title="Permalink to this definition">¶</a></dt>
<dd><p>The PowerShell DSC Configuration script.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description to go with DSC Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be the same location as the Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.log_verbose">
<code class="sig-name descname">log_verbose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.log_verbose" title="Permalink to this definition">¶</a></dt>
<dd><p>Verbose log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscConfiguration.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">content_embedded=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">log_verbose=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DscConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Configuration script.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description to go with DSC Configuration.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be the same location as the Automation Account.</p></li>
<li><p><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscNodeConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">DscNodeConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">content_embedded=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation DSC Node Configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Node Configuration (mof content).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.content_embedded">
<code class="sig-name descname">content_embedded</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.content_embedded" title="Permalink to this definition">¶</a></dt>
<dd><p>The PowerShell DSC Node Configuration (mof content).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.DscNodeConfiguration.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscNodeConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">configuration_name=None</em>, <em class="sig-param">content_embedded=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DscNodeConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_embedded</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PowerShell DSC Node Configuration (mof content).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.DscNodeConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.DscNodeConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.DscNodeConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetAccountResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetAccountResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint for this Auomation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetAccountResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetAccountResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the Automation Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetAccountResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetAccountResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the Automation Account.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetBoolVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">GetBoolVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBoolVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetBoolVariableResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetBoolVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">boolean</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">GetDateTimeVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDateTimeVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetDateTimeVariableResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetDateTimeVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable in the <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.6">RFC3339 Section 5.6 Internet Date/Time Format</a>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetIntVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">GetIntVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIntVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetIntVariableResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetIntVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.GetStringVariableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">GetStringVariableResult</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStringVariable.</p>
<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.GetStringVariableResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.GetStringVariableResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.automation.IntVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">IntVariable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a integer variable in Azure Automation</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.IntVariable.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.IntVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.IntVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">integer</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.IntVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.IntVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.IntVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.JobSchedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">JobSchedule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">job_schedule_id=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">run_on=None</em>, <em class="sig-param">runbook_name=None</em>, <em class="sig-param">schedule_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.JobSchedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Links an Automation Runbook and Schedule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Account in which the Job Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>job_schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID identifying the Automation Job Schedule.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs corresponding to the arguments that can be passed to the Runbook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Job Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>run_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of a Hybrid Worker Group the Runbook will be executed on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>runbook_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Runbook to link to a Schedule. It needs to be in the same Automation Account as the Schedule and Job Schedule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Account in which the Job Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.job_schedule_id">
<code class="sig-name descname">job_schedule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.job_schedule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID identifying the Automation Job Schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key/value pairs corresponding to the arguments that can be passed to the Runbook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Job Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.run_on">
<code class="sig-name descname">run_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.run_on" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a Hybrid Worker Group the Runbook will be executed on. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.JobSchedule.runbook_name">
<code class="sig-name descname">runbook_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.runbook_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Runbook to link to a Schedule. It needs to be in the same Automation Account as the Schedule and Job Schedule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.JobSchedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">job_schedule_id=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">run_on=None</em>, <em class="sig-param">runbook_name=None</em>, <em class="sig-param">schedule_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobSchedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Account in which the Job Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>job_schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID identifying the Automation Job Schedule.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs corresponding to the arguments that can be passed to the Runbook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Job Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>run_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of a Hybrid Worker Group the Runbook will be executed on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>runbook_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Runbook to link to a Schedule. It needs to be in the same Automation Account as the Schedule and Job Schedule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.JobSchedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.JobSchedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.JobSchedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Module">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">Module</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">module_link=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Module.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Module is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>module_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published Module link.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Module. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Module is created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>module_link</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The uri of the module content (zip or nupkg).</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.automation.Module.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Module is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.module_link">
<code class="sig-name descname">module_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.module_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The published Module link.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The uri of the module content (zip or nupkg).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Module. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Module.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Module.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Module is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Module.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">module_link=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Module resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Module is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>module_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published Module link.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Module. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Module is created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>module_link</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The uri of the module content (zip or nupkg).</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Module.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Module.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Module.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.RunBook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">RunBook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">log_progress=None</em>, <em class="sig-param">log_verbose=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">publish_content_link=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">runbook_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Runbook.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired content of the runbook.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this credential.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>log_progress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Progress log option.</p></li>
<li><p><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Runbook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>publish_content_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published runbook content link.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>runbook_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the runbook - can be either <code class="docutils literal notranslate"><span class="pre">Graph</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShell</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShell</span></code> or <code class="docutils literal notranslate"><span class="pre">Script</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>publish_content_link</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The uri of the runbook content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired content of the runbook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.log_progress">
<code class="sig-name descname">log_progress</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.log_progress" title="Permalink to this definition">¶</a></dt>
<dd><p>Progress log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.log_verbose">
<code class="sig-name descname">log_verbose</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.log_verbose" title="Permalink to this definition">¶</a></dt>
<dd><p>Verbose log option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Runbook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.publish_content_link">
<code class="sig-name descname">publish_content_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.publish_content_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The published runbook content link.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The uri of the runbook content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.runbook_type">
<code class="sig-name descname">runbook_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.runbook_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the runbook - can be either <code class="docutils literal notranslate"><span class="pre">Graph</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShell</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShell</span></code> or <code class="docutils literal notranslate"><span class="pre">Script</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.RunBook.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.RunBook.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.RunBook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">log_progress=None</em>, <em class="sig-param">log_verbose=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">publish_content_link=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">runbook_type=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RunBook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired content of the runbook.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this credential.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>log_progress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Progress log option.</p></li>
<li><p><strong>log_verbose</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verbose log option.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Runbook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>publish_content_link</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The published runbook content link.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>runbook_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the runbook - can be either <code class="docutils literal notranslate"><span class="pre">Graph</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShell</span></code>, <code class="docutils literal notranslate"><span class="pre">GraphPowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShellWorkflow</span></code>, <code class="docutils literal notranslate"><span class="pre">PowerShell</span></code> or <code class="docutils literal notranslate"><span class="pre">Script</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>publish_content_link</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The uri of the runbook content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.RunBook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.RunBook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.RunBook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Schedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">Schedule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiry_time=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">month_days=None</em>, <em class="sig-param">monthly_occurrences=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">week_days=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Automation Schedule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Schedule.</p></li>
<li><p><strong>expiry_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the schedule.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency of the schedule. - can be either <code class="docutils literal notranslate"><span class="pre">OneTime</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of <code class="docutils literal notranslate"><span class="pre">frequency</span></code>s between runs. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>month_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the month that the job should execute on. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">31</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last day of the month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>monthly_occurrences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of occurrences of days within a month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>. The <code class="docutils literal notranslate"><span class="pre">monthly_occurrence</span></code> block supports fields documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Schedule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone of the start time. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>. For possible values see: <a class="reference external" href="https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx">https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx</a></p></li>
<li><p><strong>week_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the week that the job should execute on. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Week</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>monthly_occurrences</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Day of the occurrence. Must be one of <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>, <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">occurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Occurrence of the week within the month. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">5</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last week within the month.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.expiry_time">
<code class="sig-name descname">expiry_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.expiry_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The end time of the schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.frequency">
<code class="sig-name descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency of the schedule. - can be either <code class="docutils literal notranslate"><span class="pre">OneTime</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.interval">
<code class="sig-name descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of <code class="docutils literal notranslate"><span class="pre">frequency</span></code>s between runs. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.month_days">
<code class="sig-name descname">month_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.month_days" title="Permalink to this definition">¶</a></dt>
<dd><p>List of days of the month that the job should execute on. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">31</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last day of the month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.monthly_occurrences">
<code class="sig-name descname">monthly_occurrences</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.monthly_occurrences" title="Permalink to this definition">¶</a></dt>
<dd><p>List of occurrences of days within a month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>. The <code class="docutils literal notranslate"><span class="pre">monthly_occurrence</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Day of the occurrence. Must be one of <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>, <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">occurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Occurrence of the week within the month. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">5</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last week within the month.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Schedule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.start_time">
<code class="sig-name descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone of the start time. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>. For possible values see: <a class="reference external" href="https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx">https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.Schedule.week_days">
<code class="sig-name descname">week_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.Schedule.week_days" title="Permalink to this definition">¶</a></dt>
<dd><p>List of days of the week that the job should execute on. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Week</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Schedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiry_time=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">month_days=None</em>, <em class="sig-param">monthly_occurrences=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">week_days=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Schedule.</p></li>
<li><p><strong>expiry_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the schedule.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency of the schedule. - can be either <code class="docutils literal notranslate"><span class="pre">OneTime</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of <code class="docutils literal notranslate"><span class="pre">frequency</span></code>s between runs. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, or <code class="docutils literal notranslate"><span class="pre">Month</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>month_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the month that the job should execute on. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">31</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last day of the month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>monthly_occurrences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of occurrences of days within a month. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Month</span></code>. The <code class="docutils literal notranslate"><span class="pre">monthly_occurrence</span></code> block supports fields documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Schedule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone of the start time. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>. For possible values see: <a class="reference external" href="https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx">https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx</a></p></li>
<li><p><strong>week_days</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of days of the week that the job should execute on. Only valid when frequency is <code class="docutils literal notranslate"><span class="pre">Week</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>monthly_occurrences</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Day of the occurrence. Must be one of <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>, <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">occurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Occurrence of the week within the month. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">5</span></code>. <code class="docutils literal notranslate"><span class="pre">-1</span></code> for last week within the month.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.Schedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.Schedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.StringVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">StringVariable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a string variable in Azure Automation</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.automation_account_name">
<code class="sig-name descname">automation_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.automation_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Automation Variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.automation.StringVariable.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.automation.StringVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.StringVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automation_account_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StringVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automation_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the automation account in which the Variable is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Automation Variable.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the Automation Variable is encrypted. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Automation Variable. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Automation Variable as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.automation.StringVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.StringVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.StringVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.automation.get_account">
<code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Automation Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the Automation Account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_bool_variable">
<code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">get_bool_variable</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_bool_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Bool Variable.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>automation_account_name</strong> (<em>str</em>) – The name of the automation account in which the Automation Variable exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Automation Variable.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the automation account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_date_time_variable">
<code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">get_date_time_variable</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_date_time_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Datetime Variable.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>automation_account_name</strong> (<em>str</em>) – The name of the automation account in which the Automation Variable exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Automation Variable.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the automation account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_int_variable">
<code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">get_int_variable</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_int_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation Int Variable.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>automation_account_name</strong> (<em>str</em>) – The name of the automation account in which the Automation Variable exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Automation Variable.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the automation account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.automation.get_string_variable">
<code class="sig-prename descclassname">pulumi_azure.automation.</code><code class="sig-name descname">get_string_variable</code><span class="sig-paren">(</span><em class="sig-param">automation_account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.automation.get_string_variable" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Automation String Variable.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>automation_account_name</strong> (<em>str</em>) – The name of the automation account in which the Automation Variable exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Automation Variable.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the automation account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
