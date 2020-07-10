---
title: Package pulumi_azure
title_tag: Package pulumi_azure | Python SDK
linktitle: pulumi_azure
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="pulumi-azure">
<h1>Pulumi Azure<a class="headerlink" href="#pulumi-azure" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure"></span><dl class="py class">
<dt id="pulumi_azure.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auxiliary_tenant_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_correlation_request_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_terraform_partner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">msi_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_credentials_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_provider_registration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_use_azuread</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_msi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azurerm package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_certificate_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client
Certificate</p></li>
<li><p><strong>client_certificate_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
Principal using a Client Certificate.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID which should be used.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.</p></li>
<li><p><strong>disable_correlation_request_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This will disable the x-ms-correlation-request-id header.</p></li>
<li><p><strong>disable_terraform_partner_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This will disable the Terraform Partner ID which is used if a custom <code class="docutils literal notranslate"><span class="pre">partner_id</span></code> isn’t specified.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to
public.</p></li>
<li><p><strong>metadata_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Metadata URL which will be used to obtain the Cloud Environment.</p></li>
<li><p><strong>msi_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected
automatically.</p></li>
<li><p><strong>partner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.</p></li>
<li><p><strong>skip_credentials_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This will cause the AzureRM Provider to skip verifying the credentials being used are valid.</p></li>
<li><p><strong>skip_provider_registration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the AzureRM Provider skip registering all of the Resource Providers that it supports, if they’re not already
registered?</p></li>
<li><p><strong>storage_use_azuread</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the AzureRM Provider use AzureAD to access the Storage Data Plane API’s?</p></li>
<li><p><strong>subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Subscription ID which should be used.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Tenant ID which should be used.</p></li>
<li><p><strong>use_msi</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allowed Managed Service Identity be used for Authentication.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>features</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">purgeSoftDeleteOnDestroy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoverSoftDeletedKeyVaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOsDiskOnDeletion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_scale_set</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rollInstancesWhenRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="py method">
<dt id="pulumi_azure.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
