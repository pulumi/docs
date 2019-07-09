---
---

<div class="section" id="securitycenter">
<h1>securitycenter<a class="headerlink" href="#securitycenter" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.securitycenter"></span><dl class="class">
<dt id="pulumi_azure.securitycenter.Contact">
<em class="property">class </em><code class="descclassname">pulumi_azure.securitycenter.</code><code class="descname">Contact</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>alert_notifications=None</em>, <em>alerts_to_admins=None</em>, <em>email=None</em>, <em>phone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the subscription’s Security Center Contact.</p>
<blockquote>
<div><strong>NOTE:</strong> Owner access permission is required.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>alert_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to the security contact.</li>
<li><strong>alerts_to_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to send security alerts notifications to subscription admins.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of the Security Center Contact.</li>
<li><strong>phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The phone number of the Security Center Contact.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_contact.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_contact.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.alert_notifications">
<code class="descname">alert_notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.alert_notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to send security alerts notifications to the security contact.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.alerts_to_admins">
<code class="descname">alerts_to_admins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.alerts_to_admins" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to send security alerts notifications to subscription admins.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of the Security Center Contact.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Contact.phone">
<code class="descname">phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.phone" title="Permalink to this definition">¶</a></dt>
<dd><p>The phone number of the Security Center Contact.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Contact.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Contact.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Contact.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.SubscriptionPricing">
<em class="property">class </em><code class="descclassname">pulumi_azure.securitycenter.</code><code class="descname">SubscriptionPricing</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the Pricing Tier for Azure Security Center in the current subscription.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource requires the <code class="docutils literal notranslate"><span class="pre">Owner</span></code> permission on the Subscription.</p>
<p><strong>NOTE:</strong> Deletion of this resource does not change or reset the pricing tier to <code class="docutils literal notranslate"><span class="pre">Free</span></code></p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing tier to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_subscription_pricing.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_subscription_pricing.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing tier to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.SubscriptionPricing.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.SubscriptionPricing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Workspace">
<em class="property">class </em><code class="descclassname">pulumi_azure.securitycenter.</code><code class="descname">Workspace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>scope=None</em>, <em>workspace_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the subscription’s Security Center Workspace.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Owner access permission is required.</p>
<p><strong>NOTE:</strong> The subscription’s pricing model can not be <code class="docutils literal notranslate"><span class="pre">Free</span></code> for this to have any affect.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.</li>
<li><strong>workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace to save the data in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_workspace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_workspace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Workspace.scope">
<code class="descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.securitycenter.Workspace.workspace_id">
<code class="descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Log Analytics Workspace to save the data in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.securitycenter.Workspace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.securitycenter.Workspace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.securitycenter.Workspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
