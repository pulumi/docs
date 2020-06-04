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
<span class="target" id="module-pulumi_signalfx.azure"></span><dl class="py class">
<dt id="pulumi_signalfx.azure.AwaitableGetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.azure.</code><code class="sig-name descname">AwaitableGetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.AwaitableGetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.azure.GetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.azure.</code><code class="sig-name descname">GetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.GetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServices.</p>
<dl class="py attribute">
<dt id="pulumi_signalfx.azure.GetServicesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.GetServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.azure.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.azure.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">named_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">poll_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx Azure integrations. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Monitoring Microsoft Azure</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">azure_myteam</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">azure</span><span class="o">.</span><span class="n">Integration</span><span class="p">(</span><span class="s2">&quot;azureMyteam&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">resource</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;signalfxAzureIntegration&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;azureMyteamXX&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;app_id&quot;</span><span class="p">:</span> <span class="s2">&quot;YYY&quot;</span><span class="p">,</span>
                <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
                <span class="s2">&quot;environment&quot;</span><span class="p">:</span> <span class="s2">&quot;azure&quot;</span><span class="p">,</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AzureFoo&quot;</span><span class="p">,</span>
                <span class="s2">&quot;poll_rate&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
                <span class="s2">&quot;secret_key&quot;</span><span class="p">:</span> <span class="s2">&quot;XXX&quot;</span><span class="p">,</span>
                <span class="s2">&quot;services&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;microsoft.sql/servers/elasticpools&quot;</span><span class="p">],</span>
                <span class="s2">&quot;subscriptions&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;sub-guid-here&quot;</span><span class="p">],</span>
                <span class="s2">&quot;tenant_id&quot;</span><span class="p">:</span> <span class="s2">&quot;ZZZ&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
        <span class="p">}],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>NOTE</strong> You can use the data source “azure.getServices” to specify all services.</p>
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
<li><p><strong>named_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A named token to use for ingest</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Microsoft Azure service names for the Azure services you want SignalFx to monitor. See the documentation for <a class="reference external" href="https://developers.signalfx.com/integrations_reference.html#operation/Create%20Integration">Creating Integrations</a> for valida values.</p></li>
<li><p><strong>subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure subscriptions that SignalFx should monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.app_id">
<code class="sig-name descname">app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure application ID for the SignalFx app. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/getting-started/send-data.html#connect-to-microsoft-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.environment">
<code class="sig-name descname">environment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>What type of Azure integration this is. The allowed values are <code class="docutils literal notranslate"><span class="pre">&quot;azure_us_government&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;azure&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.named_token">
<code class="sig-name descname">named_token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.named_token" title="Permalink to this definition">¶</a></dt>
<dd><p>A named token to use for ingest</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.poll_rate">
<code class="sig-name descname">poll_rate</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.poll_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.secret_key">
<code class="sig-name descname">secret_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.services">
<code class="sig-name descname">services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Microsoft Azure service names for the Azure services you want SignalFx to monitor. See the documentation for <a class="reference external" href="https://developers.signalfx.com/integrations_reference.html#operation/Create%20Integration">Creating Integrations</a> for valida values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.subscriptions">
<code class="sig-name descname">subscriptions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Azure subscriptions that SignalFx should monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.azure.Integration.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.azure.Integration.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.azure.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">named_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">poll_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>named_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A named token to use for ingest</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure secret key that associates the SignalFx app in Azure with the Azure tenant ID. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of Microsoft Azure service names for the Azure services you want SignalFx to monitor. See the documentation for <a class="reference external" href="https://developers.signalfx.com/integrations_reference.html#operation/Create%20Integration">Creating Integrations</a> for valida values.</p>
</p></li>
<li><p><strong>subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure subscriptions that SignalFx should monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Azure ID of the Azure tenant. To learn how to get this ID, see the topic <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html#connect-to-azure">Connect to Microsoft Azure</a> in the product documentation.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.azure.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.azure.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.azure.get_services">
<code class="sig-prename descclassname">pulumi_signalfx.azure.</code><code class="sig-name descname">get_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.azure.get_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of Azure service names.</p>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

</div>
