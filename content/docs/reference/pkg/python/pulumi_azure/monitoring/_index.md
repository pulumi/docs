---
title: Module monitoring
title_tag: Module monitoring | Package pulumi_azure | Python SDK
linktitle: monitoring
notitle: true
---

<div class="section" id="monitoring">
<h1>monitoring<a class="headerlink" href="#monitoring" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.monitoring"></span><dl class="py class">
<dt id="pulumi_azure.monitoring.ActionGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ActionGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arm_role_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_runbook_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_app_push_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_function_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">itsm_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">voice_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Action Group within Azure Monitor.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_action_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">ActionGroup</span><span class="p">(</span><span class="s2">&quot;exampleActionGroup&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;p0action&quot;</span><span class="p">,</span>
    <span class="n">arm_role_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;armroleaction&quot;</span><span class="p">,</span>
        <span class="s2">&quot;roleId&quot;</span><span class="p">:</span> <span class="s2">&quot;de139f84-1756-47ae-9be6-808fbbe84772&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">automation_runbook_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;action_name_1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;automationAccountId&quot;</span><span class="p">:</span> <span class="s2">&quot;/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg-runbooks/providers/microsoft.automation/automationaccounts/aaa001&quot;</span><span class="p">,</span>
        <span class="s2">&quot;runbookName&quot;</span><span class="p">:</span> <span class="s2">&quot;my runbook&quot;</span><span class="p">,</span>
        <span class="s2">&quot;webhookResourceId&quot;</span><span class="p">:</span> <span class="s2">&quot;/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg-runbooks/providers/microsoft.automation/automationaccounts/aaa001/webhooks/webhook_alert&quot;</span><span class="p">,</span>
        <span class="s2">&quot;isGlobalRunbook&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;serviceUri&quot;</span><span class="p">:</span> <span class="s2">&quot;https://s13events.azure-automation.net/webhooks?token=randomtoken&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">azure_app_push_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;pushtoadmin&quot;</span><span class="p">,</span>
        <span class="s2">&quot;emailAddress&quot;</span><span class="p">:</span> <span class="s2">&quot;admin@contoso.com&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">azure_function_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;funcaction&quot;</span><span class="p">,</span>
        <span class="s2">&quot;functionAppResourceId&quot;</span><span class="p">:</span> <span class="s2">&quot;/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-funcapp/providers/Microsoft.Web/sites/funcapp&quot;</span><span class="p">,</span>
        <span class="s2">&quot;functionName&quot;</span><span class="p">:</span> <span class="s2">&quot;myfunc&quot;</span><span class="p">,</span>
        <span class="s2">&quot;httpTriggerUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;https://example.com/trigger&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">email_receiver</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;sendtoadmin&quot;</span><span class="p">,</span>
            <span class="s2">&quot;emailAddress&quot;</span><span class="p">:</span> <span class="s2">&quot;admin@contoso.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;sendtodevops&quot;</span><span class="p">,</span>
            <span class="s2">&quot;emailAddress&quot;</span><span class="p">:</span> <span class="s2">&quot;devops@contoso.com&quot;</span><span class="p">,</span>
            <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">itsm_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;createorupdateticket&quot;</span><span class="p">,</span>
        <span class="s2">&quot;workspaceId&quot;</span><span class="p">:</span> <span class="s2">&quot;6eee3a18-aac3-40e4-b98e-1f309f329816&quot;</span><span class="p">,</span>
        <span class="s2">&quot;connectionId&quot;</span><span class="p">:</span> <span class="s2">&quot;53de6956-42b4-41ba-be3c-b154cdf17b13&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ticketConfiguration&quot;</span><span class="p">:</span> <span class="s2">&quot;</span><span class="si">{}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="s2">&quot;southcentralus&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">logic_app_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;logicappaction&quot;</span><span class="p">,</span>
        <span class="s2">&quot;resourceId&quot;</span><span class="p">:</span> <span class="s2">&quot;/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-logicapp/providers/Microsoft.Logic/workflows/logicapp&quot;</span><span class="p">,</span>
        <span class="s2">&quot;callbackUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;https://logicapptriggerurl/...&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">sms_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;oncallmsg&quot;</span><span class="p">,</span>
        <span class="s2">&quot;countryCode&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;phoneNumber&quot;</span><span class="p">:</span> <span class="s2">&quot;1231231234&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">voice_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;remotesupport&quot;</span><span class="p">,</span>
        <span class="s2">&quot;countryCode&quot;</span><span class="p">:</span> <span class="s2">&quot;86&quot;</span><span class="p">,</span>
        <span class="s2">&quot;phoneNumber&quot;</span><span class="p">:</span> <span class="s2">&quot;13888888888&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">webhook_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;callmyapiaswell&quot;</span><span class="p">,</span>
        <span class="s2">&quot;serviceUri&quot;</span><span class="p">:</span> <span class="s2">&quot;http://example.com/alert&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useCommonAlertSchema&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arm_role_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>automation_runbook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>azure_app_push_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>azure_function_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>email_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>itsm_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>logic_app_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Action Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Action Group instance.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the action group. This will be used in SMS messages.</p></li>
<li><p><strong>sms_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>voice_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>webhook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>arm_role_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ARM role receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>automation_runbook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the automation runbook receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
<p>The <strong>azure_app_push_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of the user signed into the mobile app who will receive push notifications from this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure app push receiver.</p></li>
</ul>
<p>The <strong>azure_function_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Function receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>email_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the email receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>itsm_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ITSM receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
<p>The <strong>logic_app_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the logic app receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>sms_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the SMS receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the SMS receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the SMS receiver.</p></li>
</ul>
<p>The <strong>voice_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>webhook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.arm_role_receivers">
<code class="sig-name descname">arm_role_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.arm_role_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ARM role receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.automation_runbook_receivers">
<code class="sig-name descname">automation_runbook_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.automation_runbook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the automation runbook receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.azure_app_push_receivers">
<code class="sig-name descname">azure_app_push_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.azure_app_push_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address of the user signed into the mobile app who will receive push notifications from this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure app push receiver.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.azure_function_receivers">
<code class="sig-name descname">azure_function_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.azure_function_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Function receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.email_receivers">
<code class="sig-name descname">email_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the email receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.itsm_receivers">
<code class="sig-name descname">itsm_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.itsm_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ITSM receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.logic_app_receivers">
<code class="sig-name descname">logic_app_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.logic_app_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the logic app receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Action Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Action Group instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.short_name">
<code class="sig-name descname">short_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group. This will be used in SMS messages.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.sms_receivers">
<code class="sig-name descname">sms_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country code of the SMS receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the SMS receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The phone number of the SMS receiver.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.voice_receivers">
<code class="sig-name descname">voice_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.voice_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.webhook_receivers">
<code class="sig-name descname">webhook_receivers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ActionGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arm_role_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_runbook_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_app_push_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_function_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">itsm_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">voice_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_receivers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActionGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arm_role_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>automation_runbook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>azure_app_push_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>azure_function_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>email_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>itsm_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>logic_app_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Action Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Action Group instance.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the action group. This will be used in SMS messages.</p></li>
<li><p><strong>sms_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>voice_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p></li>
<li><p><strong>webhook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>arm_role_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ARM role receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>automation_runbook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the automation runbook receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
<p>The <strong>azure_app_push_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of the user signed into the mobile app who will receive push notifications from this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure app push receiver.</p></li>
</ul>
<p>The <strong>azure_function_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Function receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>email_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the email receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>itsm_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ITSM receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
<p>The <strong>logic_app_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the logic app receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>sms_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the SMS receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the SMS receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the SMS receiver.</p></li>
</ul>
<p>The <strong>voice_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>webhook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ActionGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActionGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ActivityLogAlert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criteria</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Activity Log Alert within Azure Monitor.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">main_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;mainResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">main_action_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">ActionGroup</span><span class="p">(</span><span class="s2">&quot;mainActionGroup&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;p0action&quot;</span><span class="p">,</span>
    <span class="n">webhook_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;callmyapi&quot;</span><span class="p">,</span>
        <span class="s2">&quot;serviceUri&quot;</span><span class="p">:</span> <span class="s2">&quot;http://example.com/alert&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">to_monitor</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;toMonitor&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;GRS&quot;</span><span class="p">)</span>
<span class="n">main_activity_log_alert</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">ActivityLogAlert</span><span class="p">(</span><span class="s2">&quot;mainActivityLogAlert&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This alert will monitor a specific storage account updates.&quot;</span><span class="p">,</span>
    <span class="n">criteria</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;resourceId&quot;</span><span class="p">:</span> <span class="n">to_monitor</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;operationName&quot;</span><span class="p">:</span> <span class="s2">&quot;Microsoft.Storage/storageAccounts/write&quot;</span><span class="p">,</span>
        <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;Recommendation&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">action</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;actionGroupId&quot;</span><span class="p">:</span> <span class="n">main_action_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;webhookProperties&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;from&quot;</span><span class="p">:</span> <span class="s2">&quot;source&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>criteria</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this activity log alert.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the activity log alert. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the activity log alert instance.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address or Azure Active Directory identifier of the user who performed the operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the operation. Possible values are <code class="docutils literal notranslate"><span class="pre">Administrative</span></code>, <code class="docutils literal notranslate"><span class="pre">Autoscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendation</span></code>, <code class="docutils literal notranslate"><span class="pre">ResourceHealth</span></code>, <code class="docutils literal notranslate"><span class="pre">Security</span></code> and <code class="docutils literal notranslate"><span class="pre">ServiceHealth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The severity level of the event. Possible values are <code class="docutils literal notranslate"><span class="pre">Verbose</span></code>, <code class="docutils literal notranslate"><span class="pre">Informational</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Error</span></code>, and <code class="docutils literal notranslate"><span class="pre">Critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Manager Role-Based Access Control operation name. Supported operation should be of the form: <code class="docutils literal notranslate"><span class="pre">&lt;resourceProvider&gt;/&lt;resourceType&gt;/&lt;operation&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of resource group monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific resource monitored by the activity log alert. It should be within one of the <code class="docutils literal notranslate"><span class="pre">scopes</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the resource provider monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the event. For example, <code class="docutils literal notranslate"><span class="pre">Started</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, or <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The sub status of the event.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.actions">
<code class="sig-name descname">actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.criteria">
<code class="sig-name descname">criteria</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.criteria" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address or Azure Active Directory identifier of the user who performed the operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The category of the operation. Possible values are <code class="docutils literal notranslate"><span class="pre">Administrative</span></code>, <code class="docutils literal notranslate"><span class="pre">Autoscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendation</span></code>, <code class="docutils literal notranslate"><span class="pre">ResourceHealth</span></code>, <code class="docutils literal notranslate"><span class="pre">Security</span></code> and <code class="docutils literal notranslate"><span class="pre">ServiceHealth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The severity level of the event. Possible values are <code class="docutils literal notranslate"><span class="pre">Verbose</span></code>, <code class="docutils literal notranslate"><span class="pre">Informational</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Error</span></code>, and <code class="docutils literal notranslate"><span class="pre">Critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Resource Manager Role-Based Access Control operation name. Supported operation should be of the form: <code class="docutils literal notranslate"><span class="pre">&lt;resourceProvider&gt;/&lt;resourceType&gt;/&lt;operation&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of resource group monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The specific resource monitored by the activity log alert. It should be within one of the <code class="docutils literal notranslate"><span class="pre">scopes</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the resource provider monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource type monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the event. For example, <code class="docutils literal notranslate"><span class="pre">Started</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, or <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The sub status of the event.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this activity log alert.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the activity log alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the activity log alert instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.scopes">
<code class="sig-name descname">scopes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criteria</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActivityLogAlert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>criteria</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this activity log alert.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the activity log alert. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the activity log alert instance.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address or Azure Active Directory identifier of the user who performed the operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the operation. Possible values are <code class="docutils literal notranslate"><span class="pre">Administrative</span></code>, <code class="docutils literal notranslate"><span class="pre">Autoscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, <code class="docutils literal notranslate"><span class="pre">Recommendation</span></code>, <code class="docutils literal notranslate"><span class="pre">ResourceHealth</span></code>, <code class="docutils literal notranslate"><span class="pre">Security</span></code> and <code class="docutils literal notranslate"><span class="pre">ServiceHealth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The severity level of the event. Possible values are <code class="docutils literal notranslate"><span class="pre">Verbose</span></code>, <code class="docutils literal notranslate"><span class="pre">Informational</span></code>, <code class="docutils literal notranslate"><span class="pre">Warning</span></code>, <code class="docutils literal notranslate"><span class="pre">Error</span></code>, and <code class="docutils literal notranslate"><span class="pre">Critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Manager Role-Based Access Control operation name. Supported operation should be of the form: <code class="docutils literal notranslate"><span class="pre">&lt;resourceProvider&gt;/&lt;resourceType&gt;/&lt;operation&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of resource group monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The specific resource monitored by the activity log alert. It should be within one of the <code class="docutils literal notranslate"><span class="pre">scopes</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the resource provider monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type monitored by the activity log alert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the event. For example, <code class="docutils literal notranslate"><span class="pre">Started</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, or <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The sub status of the event.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AutoscaleSetting</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_scale_set</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">ScaleSet</span><span class="p">(</span><span class="s2">&quot;exampleScaleSet&quot;</span><span class="p">)</span>
<span class="c1"># ...</span>
<span class="n">example_autoscale_setting</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">AutoscaleSetting</span><span class="p">(</span><span class="s2">&quot;exampleAutoscaleSetting&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">target_resource_id</span><span class="o">=</span><span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">profile</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;defaultProfile&quot;</span><span class="p">,</span>
        <span class="s2">&quot;capacity&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;default&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;minimum&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;maximum&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;rule&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;metric_trigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;GreaterThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">75</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scale_action&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Increase&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;metric_trigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;LessThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scale_action&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Decrease&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">notification</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;sendToSubscriptionAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;sendToSubscriptionCoAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;customEmails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;admin@contoso.com&quot;</span><span class="p">],</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_scale_set</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">ScaleSet</span><span class="p">(</span><span class="s2">&quot;exampleScaleSet&quot;</span><span class="p">)</span>
<span class="n">example_autoscale_setting</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">AutoscaleSetting</span><span class="p">(</span><span class="s2">&quot;exampleAutoscaleSetting&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">notification</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;customEmails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;admin@contoso.com&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sendToSubscriptionAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;sendToSubscriptionCoAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">profiles</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;capacity&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;default&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;maximum&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
            <span class="s2">&quot;minimum&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Weekends&quot;</span><span class="p">,</span>
        <span class="s2">&quot;recurrence&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;days&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;Saturday&quot;</span><span class="p">,</span>
                <span class="s2">&quot;Sunday&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;frequency&quot;</span><span class="p">:</span> <span class="s2">&quot;Week&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hours&quot;</span><span class="p">:</span> <span class="mi">12</span><span class="p">,</span>
            <span class="s2">&quot;minutes&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
            <span class="s2">&quot;timezone&quot;</span><span class="p">:</span> <span class="s2">&quot;Pacific Standard Time&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;rule&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;metricTrigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;GreaterThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scaleAction&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Increase&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;metricTrigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;LessThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scaleAction&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Decrease&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">target_resource_id</span><span class="o">=</span><span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_scale_set</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">ScaleSet</span><span class="p">(</span><span class="s2">&quot;exampleScaleSet&quot;</span><span class="p">)</span>
<span class="c1"># ...</span>
<span class="n">example_autoscale_setting</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">AutoscaleSetting</span><span class="p">(</span><span class="s2">&quot;exampleAutoscaleSetting&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">target_resource_id</span><span class="o">=</span><span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">profile</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;forJuly&quot;</span><span class="p">,</span>
        <span class="s2">&quot;capacity&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;default&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;minimum&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;maximum&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;rule&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;metric_trigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;GreaterThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scale_action&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Increase&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;metric_trigger&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Percentage CPU&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;metricResourceId&quot;</span><span class="p">:</span> <span class="n">example_scale_set</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                    <span class="s2">&quot;timeGrain&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;PT5M&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;timeAggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Average&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;LessThan&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;scale_action&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;direction&quot;</span><span class="p">:</span> <span class="s2">&quot;Decrease&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ChangeCount&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="s2">&quot;PT1M&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
        <span class="p">],</span>
        <span class="s2">&quot;fixed_date&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;timezone&quot;</span><span class="p">:</span> <span class="s2">&quot;Pacific Standard Time&quot;</span><span class="p">,</span>
            <span class="s2">&quot;start&quot;</span><span class="p">:</span> <span class="s2">&quot;2020-07-01T00:00:00Z&quot;</span><span class="p">,</span>
            <span class="s2">&quot;end&quot;</span><span class="p">:</span> <span class="s2">&quot;2020-07-31T23:59:59Z&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="n">notification</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;sendToSubscriptionAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;sendToSubscriptionCoAdministrator&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;customEmails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;admin@contoso.com&quot;</span><span class="p">],</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AutoScale Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p></li>
<li><p><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource ID of the resource that the autoscale setting should be added to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">email</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of custom email addresses to which the email notifications will be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should email notifications be sent to the subscription administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should email notifications be sent to the subscription co-administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">webhook</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTPS URI which should receive scale notifications.</p></li>
</ul>
</li>
</ul>
<p>The <strong>profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">capacity</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the end date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the start date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time Zone of the <code class="docutils literal notranslate"><span class="pre">start</span></code> and <code class="docutils literal notranslate"><span class="pre">end</span></code> times. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the profile.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of days that this profile takes effect on. Possible values include <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code> and <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">23</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time Zone used for the <code class="docutils literal notranslate"><span class="pre">hours</span></code> field. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">metric_trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric that defines what the rule monitors, such as <code class="docutils literal notranslate"><span class="pre">Percentage</span> <span class="pre">CPU</span></code> for <code class="docutils literal notranslate"><span class="pre">Virtual</span> <span class="pre">Machine</span> <span class="pre">Scale</span> <span class="pre">Sets</span></code> and <code class="docutils literal notranslate"><span class="pre">CpuPercentage</span></code> for <code class="docutils literal notranslate"><span class="pre">App</span> <span class="pre">Service</span> <span class="pre">Plan</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Resource which the Rule monitors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the operator used to compare the metric data and threshold. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the metrics from multiple instances are combined. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Min</span></code> and <code class="docutils literal notranslate"><span class="pre">Max</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the threshold of the metric that triggers the scale action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data that’s collected should be combined over time. Possible values include <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Average</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">scale_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scale direction. Possible values are <code class="docutils literal notranslate"><span class="pre">Increase</span></code> and <code class="docutils literal notranslate"><span class="pre">Decrease</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action that should occur. Possible values are <code class="docutils literal notranslate"><span class="pre">ChangeCount</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCount</span></code> and <code class="docutils literal notranslate"><span class="pre">PercentChangeCount</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances involved in the scaling action. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AutoScale Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.notification">
<code class="sig-name descname">notification</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">email</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of custom email addresses to which the email notifications will be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should email notifications be sent to the subscription administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should email notifications be sent to the subscription co-administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">webhook</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTPS URI which should receive scale notifications.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.profiles">
<code class="sig-name descname">profiles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">capacity</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the end date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the start date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Time Zone of the <code class="docutils literal notranslate"><span class="pre">start</span></code> and <code class="docutils literal notranslate"><span class="pre">end</span></code> times. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the profile.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of days that this profile takes effect on. Possible values include <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code> and <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">23</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Time Zone used for the <code class="docutils literal notranslate"><span class="pre">hours</span></code> field. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">metric_trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the metric that defines what the rule monitors, such as <code class="docutils literal notranslate"><span class="pre">Percentage</span> <span class="pre">CPU</span></code> for <code class="docutils literal notranslate"><span class="pre">Virtual</span> <span class="pre">Machine</span> <span class="pre">Scale</span> <span class="pre">Sets</span></code> and <code class="docutils literal notranslate"><span class="pre">CpuPercentage</span></code> for <code class="docutils literal notranslate"><span class="pre">App</span> <span class="pre">Service</span> <span class="pre">Plan</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Resource which the Rule monitors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the operator used to compare the metric data and threshold. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the metrics from multiple instances are combined. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Min</span></code> and <code class="docutils literal notranslate"><span class="pre">Max</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the threshold of the metric that triggers the scale action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the data that’s collected should be combined over time. Possible values include <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Average</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_window</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">scale_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scale direction. Possible values are <code class="docutils literal notranslate"><span class="pre">Increase</span></code> and <code class="docutils literal notranslate"><span class="pre">Decrease</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of action that should occur. Possible values are <code class="docutils literal notranslate"><span class="pre">ChangeCount</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCount</span></code> and <code class="docutils literal notranslate"><span class="pre">PercentChangeCount</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances involved in the scaling action. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource ID of the resource that the autoscale setting should be added to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AutoscaleSetting resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AutoScale Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p></li>
<li><p><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource ID of the resource that the autoscale setting should be added to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">email</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of custom email addresses to which the email notifications will be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should email notifications be sent to the subscription administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should email notifications be sent to the subscription co-administrator? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">webhook</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTPS URI which should receive scale notifications.</p></li>
</ul>
</li>
</ul>
<p>The <strong>profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">capacity</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances for this resource. Valid values are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the end date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the start date for the profile, formatted as an RFC3339 date string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time Zone of the <code class="docutils literal notranslate"><span class="pre">start</span></code> and <code class="docutils literal notranslate"><span class="pre">end</span></code> times. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the profile.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block as defined below. This cannot be specified if a <code class="docutils literal notranslate"><span class="pre">fixed_date</span></code> block is specified.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of days that this profile takes effect on. Possible values include <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code>, <code class="docutils literal notranslate"><span class="pre">Saturday</span></code> and <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">23</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time Zone used for the <code class="docutils literal notranslate"><span class="pre">hours</span></code> field. A list of <a class="reference external" href="https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx">possible values can be found here</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">metric_trigger</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric that defines what the rule monitors, such as <code class="docutils literal notranslate"><span class="pre">Percentage</span> <span class="pre">CPU</span></code> for <code class="docutils literal notranslate"><span class="pre">Virtual</span> <span class="pre">Machine</span> <span class="pre">Scale</span> <span class="pre">Sets</span></code> and <code class="docutils literal notranslate"><span class="pre">CpuPercentage</span></code> for <code class="docutils literal notranslate"><span class="pre">App</span> <span class="pre">Service</span> <span class="pre">Plan</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Resource which the Rule monitors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the operator used to compare the metric data and threshold. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the metrics from multiple instances are combined. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Min</span></code> and <code class="docutils literal notranslate"><span class="pre">Max</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the threshold of the metric that triggers the scale action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data that’s collected should be combined over time. Possible values include <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Average</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">scale_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scale direction. Possible values are <code class="docutils literal notranslate"><span class="pre">Increase</span></code> and <code class="docutils literal notranslate"><span class="pre">Decrease</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action that should occur. Possible values are <code class="docutils literal notranslate"><span class="pre">ChangeCount</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCount</span></code> and <code class="docutils literal notranslate"><span class="pre">PercentChangeCount</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances involved in the scaling action. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AwaitableGetActionGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetActionGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arm_role_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_runbook_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_app_push_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_function_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">itsm_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">voice_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_receivers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.AwaitableGetDiagnosticCategoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.AwaitableGetLogProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetLogProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servicebus_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetLogProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.AwaitableGetScheduledQueryRulesAlertResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetScheduledQueryRulesAlertResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetScheduledQueryRulesAlertResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.AwaitableGetScheduledQueryRulesLogResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetScheduledQueryRulesLogResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetScheduledQueryRulesLogResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.DiagnosticSetting">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">DiagnosticSetting</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_authorization_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_destination_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Diagnostic Setting for an existing Resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;examplestoracc&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">name</span><span class="p">))</span>
<span class="n">example_key_vault</span> <span class="o">=</span> <span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="n">azure</span><span class="o">.</span><span class="n">keyvault</span><span class="o">.</span><span class="n">get_key_vault</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-vault&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">name</span><span class="p">))</span>
<span class="n">example_diagnostic_setting</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">DiagnosticSetting</span><span class="p">(</span><span class="s2">&quot;exampleDiagnosticSetting&quot;</span><span class="p">,</span>
    <span class="n">logs</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;AuditEvent&quot;</span><span class="p">,</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;retentionPolicy&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="n">metrics</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;category&quot;</span><span class="p">:</span> <span class="s2">&quot;AllMetrics&quot;</span><span class="p">,</span>
        <span class="s2">&quot;retentionPolicy&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="n">storage_account_id</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">target_resource_id</span><span class="o">=</span><span class="n">example_key_vault</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_authorization_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>log_analytics_destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p></li>
<li><p><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Diagnostic Log Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Diagnostic Log enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
<p>The <strong>metrics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Diagnostic Metric Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Diagnostic Metric enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id">
<code class="sig-name descname">eventhub_authorization_rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_destination_type">
<code class="sig-name descname">log_analytics_destination_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_destination_type" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id">
<code class="sig-name descname">log_analytics_workspace_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.logs">
<code class="sig-name descname">logs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Diagnostic Log Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Diagnostic Log enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.metrics">
<code class="sig-name descname">metrics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Diagnostic Metric Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Diagnostic Metric enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_authorization_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eventhub_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_destination_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DiagnosticSetting resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_authorization_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>log_analytics_destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p></li>
<li><p><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Diagnostic Log Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Diagnostic Log enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
<p>The <strong>metrics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Diagnostic Metric Category for this Resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Diagnostic Metric enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for which this Retention Policy should apply.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Retention Policy enabled?</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.GetActionGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetActionGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arm_role_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_runbook_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_app_push_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_function_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">itsm_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sms_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">voice_receivers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_receivers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActionGroup.</p>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.arm_role_receivers">
<code class="sig-name descname">arm_role_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.arm_role_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.automation_runbook_receivers">
<code class="sig-name descname">automation_runbook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.automation_runbook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.azure_app_push_receivers">
<code class="sig-name descname">azure_app_push_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.azure_app_push_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.azure_function_receivers">
<code class="sig-name descname">azure_function_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.azure_function_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.email_receivers">
<code class="sig-name descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.itsm_receivers">
<code class="sig-name descname">itsm_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.itsm_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.logic_app_receivers">
<code class="sig-name descname">logic_app_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.logic_app_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook receiver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.sms_receivers">
<code class="sig-name descname">sms_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.voice_receivers">
<code class="sig-name descname">voice_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.voice_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers">
<code class="sig-name descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiagnosticCategories.</p>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs">
<code class="sig-name descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Log Categories supported for this Resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics">
<code class="sig-name descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Metric Categories supported for this Resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.GetLogProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetLogProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servicebus_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLogProfile.</p>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.categories">
<code class="sig-name descname">categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.locations">
<code class="sig-name descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id">
<code class="sig-name descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the storage account in which the Activity Log is stored.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetScheduledQueryRulesAlertResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScheduledQueryRulesAlert.</p>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.authorized_resource_ids">
<code class="sig-name descname">authorized_resource_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.authorized_resource_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Resource IDs referred into query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.data_source_id">
<code class="sig-name descname">data_source_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.data_source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource URI over which log search query is to be run.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the scheduled query rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this scheduled query rule is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.frequency">
<code class="sig-name descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Frequency at which rule condition should be evaluated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.query">
<code class="sig-name descname">query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.query" title="Permalink to this definition">¶</a></dt>
<dd><p>Log search query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.severity">
<code class="sig-name descname">severity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>Severity of the alert.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.throttling">
<code class="sig-name descname">throttling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.throttling" title="Permalink to this definition">¶</a></dt>
<dd><p>Time for which alerts should be throttled or suppressed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.time_window">
<code class="sig-name descname">time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Time window for which data needs to be fetched for query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.triggers">
<code class="sig-name descname">triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesAlertResult.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">trigger</span></code> block as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetScheduledQueryRulesLogResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScheduledQueryRulesLog.</p>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.criterias">
<code class="sig-name descname">criterias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.data_source_id">
<code class="sig-name descname">data_source_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.data_source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource URI over which log search query is to be run.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the scheduled query rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this scheduled query rule is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetScheduledQueryRulesLogResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the dimension.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.monitoring.LogProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">LogProfile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servicebus_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile">Log Profile</a>. A Log Profile configures how Activity Logs are exported.</p>
<blockquote>
<div><p><strong>NOTE:</strong> It’s only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with <code class="docutils literal notranslate"><span class="pre">StatusCode=409</span></code> will occur.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;eastus&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;GRS&quot;</span><span class="p">)</span>
<span class="n">example_event_hub_namespace</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">eventhub</span><span class="o">.</span><span class="n">EventHubNamespace</span><span class="p">(</span><span class="s2">&quot;exampleEventHubNamespace&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">capacity</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">example_log_profile</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">LogProfile</span><span class="p">(</span><span class="s2">&quot;exampleLogProfile&quot;</span><span class="p">,</span>
    <span class="n">categories</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;Action&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Delete&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Write&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;westus&quot;</span><span class="p">,</span>
        <span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">servicebus_rule_id</span><span class="o">=</span><span class="n">example_event_hub_namespace</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="nb">id</span><span class="si">}</span><span class="s2">/authorizationrules/RootManageSharedAccessKey&quot;</span><span class="p">),</span>
    <span class="n">storage_account_id</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">retention_policy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;days&quot;</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of categories of the logs.</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regions for which Activity Log events are stored or streamed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Log Profile. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p></li>
<li><p><strong>servicebus_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>retention_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for the retention policy. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean value to indicate whether the retention policy is enabled.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.categories">
<code class="sig-name descname">categories</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.locations">
<code class="sig-name descname">locations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Log Profile. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.retention_policy">
<code class="sig-name descname">retention_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.retention_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days for the retention policy. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean value to indicate whether the retention policy is enabled.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.servicebus_rule_id">
<code class="sig-name descname">servicebus_rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.LogProfile.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.LogProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servicebus_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of categories of the logs.</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regions for which Activity Log events are stored or streamed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Log Profile. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p></li>
<li><p><strong>servicebus_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>retention_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days for the retention policy. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean value to indicate whether the retention policy is enabled.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.LogProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.LogProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">MetricAlert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_mitigate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Metric Alert within Azure Monitor.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">main_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;mainResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">to_monitor</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;toMonitor&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;LRS&quot;</span><span class="p">)</span>
<span class="n">main_action_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">ActionGroup</span><span class="p">(</span><span class="s2">&quot;mainActionGroup&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;exampleact&quot;</span><span class="p">,</span>
    <span class="n">webhook_receiver</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;callmyapi&quot;</span><span class="p">,</span>
        <span class="s2">&quot;serviceUri&quot;</span><span class="p">:</span> <span class="s2">&quot;http://example.com/alert&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">MetricAlert</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">main_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="n">to_monitor</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Action will be triggered when Transactions count is greater than 50.&quot;</span><span class="p">,</span>
    <span class="n">criteria</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;metricNamespace&quot;</span><span class="p">:</span> <span class="s2">&quot;Microsoft.Storage/storageAccounts&quot;</span><span class="p">,</span>
        <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;Transactions&quot;</span><span class="p">,</span>
        <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;Total&quot;</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;GreaterThan&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
        <span class="s2">&quot;dimension&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;ApiName&quot;</span><span class="p">,</span>
            <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;Include&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;*&quot;</span><span class="p">],</span>
        <span class="p">}],</span>
    <span class="p">}],</span>
    <span class="n">action</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;actionGroupId&quot;</span><span class="p">:</span> <span class="n">main_action_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>auto_mitigate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Metric Alert.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Metric Alert. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Metric Alert instance.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A set of strings of resource IDs at which the metric criteria should be applied.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>window_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
<p>The <strong>criterias</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic that runs over the metric values. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">dimension</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the dimension names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The dimension operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the metric names to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the metric namespaces to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The criteria operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The criteria threshold value that activates the alert.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.actions">
<code class="sig-name descname">actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.auto_mitigate">
<code class="sig-name descname">auto_mitigate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.auto_mitigate" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.criterias">
<code class="sig-name descname">criterias</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The statistic that runs over the metric values. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">dimension</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of the dimension names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The dimension operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of the metric names to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of the metric namespaces to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The criteria operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The criteria threshold value that activates the alert.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Metric Alert.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.frequency">
<code class="sig-name descname">frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Metric Alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Metric Alert instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.scopes">
<code class="sig-name descname">scopes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of strings of resource IDs at which the metric criteria should be applied.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.severity">
<code class="sig-name descname">severity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.window_size">
<code class="sig-name descname">window_size</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.window_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.MetricAlert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_mitigate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MetricAlert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>auto_mitigate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Metric Alert.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Metric Alert. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Metric Alert instance.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A set of strings of resource IDs at which the metric criteria should be applied.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>window_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Action Group can be sourced from the <code class="docutils literal notranslate"><span class="pre">monitoring.ActionGroup</span></code> resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The map of custom string properties to include with the post operation. These data are appended to the webhook payload.</p></li>
</ul>
<p>The <strong>criterias</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic that runs over the metric values. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Count</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code> and <code class="docutils literal notranslate"><span class="pre">Total</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">dimension</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the dimension names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The dimension operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the metric names to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of the metric namespaces to be monitored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The criteria operator. Possible values are <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEquals</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The criteria threshold value that activates the alert.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.MetricAlert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ScheduledQueryRulesAlert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AlertingAction Scheduled Query Rules resource within Azure Monitor.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p></li>
<li><p><strong>authorized_resource_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Resource IDs referred into query.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource URI over which log search query is to be run.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the scheduled query rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Frequency (in minutes) at which rule condition should be evaluated.  Values must be between 5 and 1440 (inclusive).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled query rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log search query.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the scheduled query rule instance.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Severity of the alert. Possible values include: 0, 1, 2, 3, or 4.</p></li>
<li><p><strong>throttling</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in minutes) for which Alerts should be throttled or suppressed.  Values must be between 0 and 10000 (inclusive).</p></li>
<li><p><strong>time_window</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time window for which data needs to be fetched for query (must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">frequency</span></code>).  Values must be between 5 and 2880 (inclusive).</p></li>
<li><p><strong>trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The condition that results in the alert rule being run.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of action group reference resource IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customWebhookPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom payload to be sent for all webhook payloads in alerting action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom subject override for all email ids in Azure action group.</p></li>
</ul>
<p>The <strong>trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTriggerType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The threshold of the metric trigger.    Values must be between 0 and 10000 inclusive.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Result or count threshold based on which rule should be triggered.  Values must be between 0 and 10000 inclusive.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.action" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of action group reference resource IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customWebhookPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom payload to be sent for all webhook payloads in alerting action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom subject override for all email ids in Azure action group.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.authorized_resource_ids">
<code class="sig-name descname">authorized_resource_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.authorized_resource_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Resource IDs referred into query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.data_source_id">
<code class="sig-name descname">data_source_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.data_source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource URI over which log search query is to be run.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the scheduled query rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.frequency">
<code class="sig-name descname">frequency</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Frequency (in minutes) at which rule condition should be evaluated.  Values must be between 5 and 1440 (inclusive).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the scheduled query rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.query">
<code class="sig-name descname">query</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.query" title="Permalink to this definition">¶</a></dt>
<dd><p>Log search query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the scheduled query rule instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.severity">
<code class="sig-name descname">severity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>Severity of the alert. Possible values include: 0, 1, 2, 3, or 4.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.throttling">
<code class="sig-name descname">throttling</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.throttling" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in minutes) for which Alerts should be throttled or suppressed.  Values must be between 0 and 10000 (inclusive).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.time_window">
<code class="sig-name descname">time_window</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Time window for which data needs to be fetched for query (must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">frequency</span></code>).  Values must be between 5 and 2880 (inclusive).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.trigger">
<code class="sig-name descname">trigger</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>The condition that results in the alert rule being run.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTriggerType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The threshold of the metric trigger.    Values must be between 0 and 10000 inclusive.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Result or count threshold based on which rule should be triggered.  Values must be between 0 and 10000 inclusive.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throttling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScheduledQueryRulesAlert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">action</span></code> block as defined below.</p></li>
<li><p><strong>authorized_resource_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Resource IDs referred into query.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource URI over which log search query is to be run.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the scheduled query rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Frequency (in minutes) at which rule condition should be evaluated.  Values must be between 5 and 1440 (inclusive).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled query rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log search query.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the scheduled query rule instance.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Severity of the alert. Possible values include: 0, 1, 2, 3, or 4.</p></li>
<li><p><strong>throttling</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in minutes) for which Alerts should be throttled or suppressed.  Values must be between 0 and 10000 (inclusive).</p></li>
<li><p><strong>time_window</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time window for which data needs to be fetched for query (must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">frequency</span></code>).  Values must be between 5 and 2880 (inclusive).</p></li>
<li><p><strong>trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The condition that results in the alert rule being run.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of action group reference resource IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customWebhookPayload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom payload to be sent for all webhook payloads in alerting action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom subject override for all email ids in Azure action group.</p></li>
</ul>
<p>The <strong>trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricColumn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTriggerType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The threshold of the metric trigger.    Values must be between 0 and 10000 inclusive.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Evaluation operation for rule - ‘Equal’, ‘GreaterThan’ or ‘LessThan’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Result or count threshold based on which rule should be triggered.  Values must be between 0 and 10000 inclusive.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesAlert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ScheduledQueryRulesLog</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criteria</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a LogToMetricAction Scheduled Query Rules resource within Azure Monitor.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>criteria</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource uri over which log search query is to be run.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the scheduled query rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled query rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the scheduled query rule instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">dimension</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator for dimension values, - ‘Include’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the metric.  Supported metrics are listed in the Azure Monitor <a class="reference external" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported#microsoftoperationalinsightsworkspaces">Microsoft.OperationalInsights/workspaces</a> metrics namespace.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.criteria">
<code class="sig-name descname">criteria</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.criteria" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">dimension</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Operator for dimension values, - ‘Include’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the metric.  Supported metrics are listed in the Azure Monitor <a class="reference external" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported#microsoftoperationalinsightsworkspaces">Microsoft.OperationalInsights/workspaces</a> metrics namespace.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.data_source_id">
<code class="sig-name descname">data_source_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.data_source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource uri over which log search query is to be run.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the scheduled query rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the scheduled query rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the scheduled query rule instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_resource_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criteria</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScheduledQueryRulesLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>criteria</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource uri over which log search query is to be run.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the scheduled query rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this scheduled query rule is enabled.  Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled query rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the scheduled query rule instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">dimension</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator for dimension values, - ‘Include’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of dimension values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the metric.  Supported metrics are listed in the Azure Monitor <a class="reference external" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported#microsoftoperationalinsightsworkspaces">Microsoft.OperationalInsights/workspaces</a> metrics namespace.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ScheduledQueryRulesLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ScheduledQueryRulesLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.get_action_group">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_action_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_action_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of an Action Group.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_action_group</span><span class="p">(</span><span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-rg&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-actiongroup&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;actionGroupId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Action Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Action Group is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.monitoring.get_diagnostic_categories">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_diagnostic_categories</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_diagnostic_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Monitor Diagnostics Categories supported by an existing Resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_key_vault</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">keyvault</span><span class="o">.</span><span class="n">get_key_vault</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">azurerm_key_vault</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_key_vault</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;resource_group_name&quot;</span><span class="p">])</span>
<span class="n">example_diagnostic_categories</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_diagnostic_categories</span><span class="p">(</span><span class="n">resource_id</span><span class="o">=</span><span class="n">example_key_vault</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>resource_id</strong> (<em>str</em>) – The ID of an existing Resource which Monitor Diagnostics Categories should be retrieved for.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.monitoring.get_log_profile">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_log_profile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_log_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of a Log Profile.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_log_profile</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;test-logprofile&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;logProfileStorageAccountId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">storage_account_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Log Profile.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.monitoring.get_scheduled_query_rules_alert">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_scheduled_query_rules_alert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_scheduled_query_rules_alert" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of an AlertingAction scheduled query rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_scheduled_query_rules_alert</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-queryrule&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-rg&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;queryRuleId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the scheduled query rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group where the scheduled query rule is located.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.monitoring.get_scheduled_query_rules_log">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_scheduled_query_rules_log</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_scheduled_query_rules_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of a LogToMetricAction scheduled query rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_scheduled_query_rules_log</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-queryrule&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-rg&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;queryRuleId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the scheduled query rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group where the scheduled query rule is located.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
