---
title: Module azure
title_tag: Module azure | Package pulumi_signalfx | Python SDK
linktitle: azure
notitle: true
---

<div class="section" id="azure">
<h1>azure<a class="headerlink" href="#azure" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.azure"></span><dl class="class">
<dt id="pulumi_signalfx.azure.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.azure.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx Azure integrations. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Monitoring Microsoft Azure</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
</div></blockquote>
<p>Fields that expect an Azure service will work with one of: “microsoft.sql/servers/elasticpools” “microsoft.storage/storageaccounts” “microsoft.storage/storageaccountsservices/tableservices” “microsoft.storage/storageaccountsservices/blobservices” “microsoft.storage/storageaccounts/queueservices” “microsoft.storage/storageaccounts/fileservices” “microsoft.compute/virtualmachinescalesets” “microsoft.compute/virtualmachinescalesets/virtualmachines” “microsoft.compute/virtualmachines” “microsoft.devices/iothubs” “microsoft.eventHub/namespaces” “microsoft.batch/batchaccounts” “microsoft.sql/servers/databases” “microsoft.cache/redis” “microsoft.logic/workflows”.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/azure_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/azure_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure application ID for the SignalFx app. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/getting-started/send-data.html#connect-to-microsoft-azure">Connect to Microsoft Azure</a> in the product documentation.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What type of Azure integration this is. The allowed values are <code class="docutils literal notranslate"><span class="pre">&quot;azure_us_government&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Microsoft Azure service names for the Azure services you want SignalFx to monitor.</p></li>
<li><p><strong>subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure subscriptions that SignalFx should monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure application ID for the SignalFx app. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/getting-started/send-data.html#connect-to-microsoft-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.environment">
<code class="sig-name descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>What type of Azure integration this is. The allowed values are <code class="docutils literal notranslate"><span class="pre">&quot;azure_us_government&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.poll_rate">
<code class="sig-name descname">poll_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.poll_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.secret_key">
<code class="sig-name descname">secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Microsoft Azure service names for the Azure services you want SignalFx to monitor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.subscriptions">
<code class="sig-name descname">subscriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Azure subscriptions that SignalFx should monitor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.azure.Integration.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.azure.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">secret_key=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure application ID for the SignalFx app. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/getting-started/send-data.html#connect-to-microsoft-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What type of Azure integration this is. The allowed values are <code class="docutils literal notranslate"><span class="pre">&quot;azure_us_government&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Microsoft Azure service names for the Azure services you want SignalFx to monitor.</p></li>
<li><p><strong>subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure subscriptions that SignalFx should monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.azure.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.azure.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
