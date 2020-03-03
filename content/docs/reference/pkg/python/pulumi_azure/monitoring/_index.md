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
<span class="target" id="module-pulumi_azure.monitoring"></span><dl class="class">
<dt id="pulumi_azure.monitoring.ActionGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ActionGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arm_role_receivers=None</em>, <em class="sig-param">automation_runbook_receivers=None</em>, <em class="sig-param">azure_app_push_receivers=None</em>, <em class="sig-param">azure_function_receivers=None</em>, <em class="sig-param">email_receivers=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">itsm_receivers=None</em>, <em class="sig-param">logic_app_receivers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">sms_receivers=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">voice_receivers=None</em>, <em class="sig-param">webhook_receivers=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Action Group within Azure Monitor.</p>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>automation_runbook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
<p>The <strong>azure_app_push_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
</ul>
<p>The <strong>azure_function_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>email_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>itsm_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
<p>The <strong>logic_app_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>sms_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>voice_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>webhook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.arm_role_receivers">
<code class="sig-name descname">arm_role_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.arm_role_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.automation_runbook_receivers">
<code class="sig-name descname">automation_runbook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.automation_runbook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.azure_app_push_receivers">
<code class="sig-name descname">azure_app_push_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.azure_app_push_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.azure_function_receivers">
<code class="sig-name descname">azure_function_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.azure_function_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.email_receivers">
<code class="sig-name descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.itsm_receivers">
<code class="sig-name descname">itsm_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.itsm_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.logic_app_receivers">
<code class="sig-name descname">logic_app_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.logic_app_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Action Group instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group. This will be used in SMS messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.sms_receivers">
<code class="sig-name descname">sms_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.voice_receivers">
<code class="sig-name descname">voice_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.voice_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.webhook_receivers">
<code class="sig-name descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.ActionGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arm_role_receivers=None</em>, <em class="sig-param">automation_runbook_receivers=None</em>, <em class="sig-param">azure_app_push_receivers=None</em>, <em class="sig-param">azure_function_receivers=None</em>, <em class="sig-param">email_receivers=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">itsm_receivers=None</em>, <em class="sig-param">logic_app_receivers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">sms_receivers=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">voice_receivers=None</em>, <em class="sig-param">webhook_receivers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roleId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arm role id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>automation_runbook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The automation account ID which holds this runbook and authenticates to Azure resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isGlobalRunbook</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether this instance is global runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runbook_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this runbook.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id for webhook linked to this runbook.</p></li>
</ul>
<p>The <strong>azure_app_push_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
</ul>
<p>The <strong>azure_function_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functionAppResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">functionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The function name in the function app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpTriggerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The http trigger url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>email_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email address of this receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>itsm_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique connection identifier of the ITSM connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ticketConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Log Analytics workspace ID where this connection is defined.</p></li>
</ul>
<p>The <strong>logic_app_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">callbackUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The callback url where http request sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure resource ID of the logic app.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<p>The <strong>sms_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>voice_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">countryCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The country code of the voice receiver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phoneNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The phone number of the voice receiver.</p></li>
</ul>
<p>The <strong>webhook_receivers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI where webhooks should be sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCommonAlertSchema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the common alert schema.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.ActionGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActionGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">ActivityLogAlert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">criteria=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Activity Log Alert within Azure Monitor.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.criteria">
<code class="sig-name descname">criteria</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.criteria" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this activity log alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the activity log alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the activity log alert instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">criteria=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>criteria</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caller</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceProvider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AlertRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AlertRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aggregation=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_action=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">webhook_action=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal">metric-based alert rule</a> in Azure Monitor.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource has been <a class="reference external" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/monitoring-classic-retirement">deprecated</a> in favour of the <code class="docutils literal notranslate"><span class="pre">monitoring.MetricAlert</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</p></li>
<li><p><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</p></li>
<li><p><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>email_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>webhook_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.aggregation">
<code class="sig-name descname">aggregation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.aggregation" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A verbose description of the alert rule that will be included in the alert email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.email_action">
<code class="sig-name descname">email_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.email_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric that defines what the rule monitors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.operator">
<code class="sig-name descname">operator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource monitored by the alert rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.threshold">
<code class="sig-name descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold value that activates the alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.webhook_action">
<code class="sig-name descname">webhook_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.webhook_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AlertRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aggregation=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_action=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">webhook_action=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</p></li>
<li><p><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</p></li>
<li><p><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>email_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>webhook_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AlertRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AlertRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AutoscaleSetting</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification=None</em>, <em class="sig-param">profiles=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AutoScale Setting. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AutoScale Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.notification">
<code class="sig-name descname">notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.profiles">
<code class="sig-name descname">profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the AutoScale Setting. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource ID of the resource that the autoscale setting should be added to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification=None</em>, <em class="sig-param">profiles=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToSubscriptionCoAdministrator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhooks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AutoScale Setting. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricTrigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeAggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeGrain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AwaitableGetActionGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetActionGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arm_role_receivers=None</em>, <em class="sig-param">automation_runbook_receivers=None</em>, <em class="sig-param">azure_app_push_receivers=None</em>, <em class="sig-param">azure_function_receivers=None</em>, <em class="sig-param">email_receivers=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">itsm_receivers=None</em>, <em class="sig-param">logic_app_receivers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">sms_receivers=None</em>, <em class="sig-param">voice_receivers=None</em>, <em class="sig-param">webhook_receivers=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.AwaitableGetDiagnosticCategoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em class="sig-param">logs=None</em>, <em class="sig-param">metrics=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.AwaitableGetLogProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">AwaitableGetLogProfileResult</code><span class="sig-paren">(</span><em class="sig-param">categories=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_policies=None</em>, <em class="sig-param">servicebus_rule_id=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AwaitableGetLogProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.DiagnosticSetting">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">DiagnosticSetting</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_authorization_rule_id=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">log_analytics_destination_type=None</em>, <em class="sig-param">log_analytics_workspace_id=None</em>, <em class="sig-param">metrics=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Diagnostic Setting for an existing Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_authorization_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p></li>
<li><p><strong>log_analytics_destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>metrics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id">
<code class="sig-name descname">eventhub_authorization_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.logs">
<code class="sig-name descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_destination_type">
<code class="sig-name descname">log_analytics_destination_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_destination_type" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id">
<code class="sig-name descname">log_analytics_workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.metrics">
<code class="sig-name descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_authorization_rule_id=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">log_analytics_destination_type=None</em>, <em class="sig-param">log_analytics_workspace_id=None</em>, <em class="sig-param">metrics=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p></li>
<li><p><strong>log_analytics_destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When set to ‘Dedicated’ logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>metrics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.GetActionGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetActionGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arm_role_receivers=None</em>, <em class="sig-param">automation_runbook_receivers=None</em>, <em class="sig-param">azure_app_push_receivers=None</em>, <em class="sig-param">azure_function_receivers=None</em>, <em class="sig-param">email_receivers=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">itsm_receivers=None</em>, <em class="sig-param">logic_app_receivers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">short_name=None</em>, <em class="sig-param">sms_receivers=None</em>, <em class="sig-param">voice_receivers=None</em>, <em class="sig-param">webhook_receivers=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActionGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.arm_role_receivers">
<code class="sig-name descname">arm_role_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.arm_role_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">arm_role_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.automation_runbook_receivers">
<code class="sig-name descname">automation_runbook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.automation_runbook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">automation_runbook_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.azure_app_push_receivers">
<code class="sig-name descname">azure_app_push_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.azure_app_push_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_app_push_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.azure_function_receivers">
<code class="sig-name descname">azure_function_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.azure_function_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">azure_function_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.email_receivers">
<code class="sig-name descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.itsm_receivers">
<code class="sig-name descname">itsm_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.itsm_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">itsm_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.logic_app_receivers">
<code class="sig-name descname">logic_app_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.logic_app_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">logic_app_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook receiver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.short_name">
<code class="sig-name descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.sms_receivers">
<code class="sig-name descname">sms_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.voice_receivers">
<code class="sig-name descname">voice_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.voice_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">voice_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers">
<code class="sig-name descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em class="sig-param">logs=None</em>, <em class="sig-param">metrics=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiagnosticCategories.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs">
<code class="sig-name descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Log Categories supported for this Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics">
<code class="sig-name descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Metric Categories supported for this Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.GetLogProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">GetLogProfileResult</code><span class="sig-paren">(</span><em class="sig-param">categories=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_policies=None</em>, <em class="sig-param">servicebus_rule_id=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLogProfile.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.categories">
<code class="sig-name descname">categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.locations">
<code class="sig-name descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id">
<code class="sig-name descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the storage account in which the Activity Log is stored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.LogProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">LogProfile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">categories=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_policy=None</em>, <em class="sig-param">servicebus_rule_id=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile">Log Profile</a>. A Log Profile configures how Activity Logs are exported.</p>
<blockquote>
<div><p><strong>NOTE:</strong> It’s only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with <code class="docutils literal notranslate"><span class="pre">StatusCode=409</span></code> will occur.</p>
</div></blockquote>
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
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.categories">
<code class="sig-name descname">categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.locations">
<code class="sig-name descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Log Profile. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.retention_policy">
<code class="sig-name descname">retention_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.retention_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.servicebus_rule_id">
<code class="sig-name descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.LogProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">categories=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_policy=None</em>, <em class="sig-param">servicebus_rule_id=None</em>, <em class="sig-param">storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.LogProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.LogProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">MetricAlert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">auto_mitigate=None</em>, <em class="sig-param">criterias=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">severity=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">window_size=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Metric Alert within Azure Monitor.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>auto_mitigate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>criterias</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Metric Alert. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.auto_mitigate">
<code class="sig-name descname">auto_mitigate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.auto_mitigate" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.criterias">
<code class="sig-name descname">criterias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Metric Alert. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Metric Alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.frequency">
<code class="sig-name descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Metric Alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Metric Alert instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of strings of resource IDs at which the metric criteria should be applied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.severity">
<code class="sig-name descname">severity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.window_size">
<code class="sig-name descname">window_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.window_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">auto_mitigate=None</em>, <em class="sig-param">criterias=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">severity=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">window_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MetricAlert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p></li>
<li><p><strong>auto_mitigate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">actionGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webhookProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>criterias</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Metric Alert. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlertRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">MetricAlertRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aggregation=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_action=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">webhook_action=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal">metric-based alert rule</a> in Azure Monitor.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</p></li>
<li><p><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</p></li>
<li><p><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>email_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>webhook_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.aggregation">
<code class="sig-name descname">aggregation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.aggregation" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A verbose description of the alert rule that will be included in the alert email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.email_action">
<code class="sig-name descname">email_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.email_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric that defines what the rule monitors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.operator">
<code class="sig-name descname">operator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource monitored by the alert rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.threshold">
<code class="sig-name descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold value that activates the alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.webhook_action">
<code class="sig-name descname">webhook_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.webhook_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlertRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aggregation=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_action=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">metric_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">webhook_action=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MetricAlertRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</p></li>
<li><p><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</p></li>
<li><p><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>email_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customEmails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses to be notified when the alert is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sendToServiceOwners</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>webhook_action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dictionary of custom properties to include with the webhook POST operation payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service uri of the webhook to POST the notification when the alert is triggered.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlertRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlertRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.get_action_group">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_action_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_action_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of an Action Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Action Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Action Group is located in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_action_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_action_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.monitoring.get_diagnostic_categories">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_diagnostic_categories</code><span class="sig-paren">(</span><em class="sig-param">resource_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_diagnostic_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Monitor Diagnostics Categories supported by an existing Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>resource_id</strong> (<em>str</em>) – The ID of an existing Resource which Monitor Diagnostics Categories should be retrieved for.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_diagnostic_categories.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_diagnostic_categories.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.monitoring.get_log_profile">
<code class="sig-prename descclassname">pulumi_azure.monitoring.</code><code class="sig-name descname">get_log_profile</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_log_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of a Log Profile.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Log Profile.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_log_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_log_profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
